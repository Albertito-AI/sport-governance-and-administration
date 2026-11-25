"""Reconcile a synthetic event file and draft an advisory brief. No network or writes."""
import argparse
import csv
import json
from pathlib import Path

HEADERS = {
    "cash": ("ref", "kind", "gbp"),
    "policy": ("ref", "rule", "value"),
    "plans": ("ref", "plan", "label", "base_gbp"),
    "scenarios": ("ref", "scenario", "label"),
    "offers": ("ref", "plan", "scenario", "surcharge_gbp", "usable_hours", "accessible_seats"),
    "signoffs": ("ref", "plan", "role", "status"),
}
CASH_KINDS = {"general_cleared", "general_committed", "restricted_cleared", "general_receivable"}
RULES = {"minimum_general_reserve_gbp", "minimum_block_hours", "minimum_accessible_seats"}
REQUIRED_ROLES = ("medical", "technical", "access")


class EvidenceError(ValueError):
    """The records cannot support a comparable result."""


def read_records(directory):
    records = {}
    for table, columns in HEADERS.items():
        with (directory / (table + ".csv")).open(encoding="utf-8", newline="") as stream:
            reader = csv.DictReader(stream)
            if tuple(reader.fieldnames or ()) != columns:
                raise EvidenceError(f"{table}: unexpected columns")
            records[table] = list(reader)
    return records


def index(rows, *fields):
    result = {}
    for row in rows:
        key = tuple(row[field] for field in fields)
        if key in result:
            raise EvidenceError(f"Duplicate {', '.join(fields)}: {', '.join(key)}")
        result[key] = row
    return result


def number(row, key):
    value = row[key]
    if not value.isascii() or not value.isdigit():
        raise EvidenceError(f"{row['ref']}: {key} must be a non-negative whole number")
    return int(value)


def reconcile(records):
    """A fixed policy compares complete packets and never grants approval."""
    refs = set()
    for table, columns in HEADERS.items():
        for row in records[table]:
            if set(row) != set(columns) or any(not value or not value.strip() for value in row.values()):
                raise EvidenceError(f"{table}: incomplete record")
            if row["ref"] in refs:
                raise EvidenceError(f"Duplicate evidence reference: {row['ref']}")
            refs.add(row["ref"])

    cash_totals = {kind: 0 for kind in CASH_KINDS}
    cash_rows = records["cash"]
    if {row["kind"] for row in cash_rows} != CASH_KINDS:
        raise EvidenceError("The cash snapshot requires all four categories, including explicit zeros")
    for row in cash_rows:
        cash_totals[row["kind"]] += number(row, "gbp")

    policy_rows = index(records["policy"], "rule")
    if {key[0] for key in policy_rows} != RULES:
        raise EvidenceError("The policy packet is incomplete or contains an unknown rule")
    policy = {rule: number(row, "value") for (rule,), row in policy_rows.items()}
    spendable = (cash_totals["general_cleared"] - cash_totals["general_committed"]
                 - policy["minimum_general_reserve_gbp"])

    plans = index(records["plans"], "plan")
    scenarios = index(records["scenarios"], "scenario")
    offers = index(records["offers"], "plan", "scenario")
    signoffs = index(records["signoffs"], "plan", "role")
    if not plans or not scenarios:
        raise EvidenceError("At least one plan and one disruption scenario are required")
    expected_offers = {(p, s) for (p,) in plans for (s,) in scenarios}
    if set(offers) != expected_offers:
        raise EvidenceError("Each plan needs an offer for every specified scenario")
    valid_gate_keys = {(p, role) for (p,) in plans for role in REQUIRED_ROLES}
    if not set(signoffs) <= valid_gate_keys:
        raise EvidenceError("The sign-off register contains an unrecognised plan or role")
    if any(row["status"] not in {"signed", "withheld", "pending"} for row in signoffs.values()):
        raise EvidenceError("Unrecognised sign-off status")

    results = []
    for (plan,), terms in sorted(plans.items()):
        gates = {}
        blockers = []
        for role in REQUIRED_ROLES:
            gate = signoffs.get((plan, role))
            status = gate["status"] if gate else "missing"
            gates[role] = {"status": status, "ref": gate["ref"] if gate else None}
            if status != "signed":
                blockers.append(f"{role} sign-off {status}")
        scenarios_for_plan = []
        for (scenario,), scenario_record in sorted(scenarios.items()):
            offer = offers[plan, scenario]
            total = number(terms, "base_gbp") + number(offer, "surcharge_gbp")
            available_hours = number(offer, "usable_hours")
            seats = number(offer, "accessible_seats")
            reasons = []
            if total > spendable:
                reasons.append(f"cash shortfall GBP {total - spendable}")
            if available_hours < policy["minimum_block_hours"]:
                reasons.append(f"usable block {available_hours} h")
            if seats < policy["minimum_accessible_seats"]:
                reasons.append(f"accessible seats {seats}")
            blockers.extend(f"{scenario}: {reason}" for reason in reasons)
            scenarios_for_plan.append({"scenario": scenario, "total_gbp": total,
                                       "spendable_balance_gbp": spendable - total,
                                       "usable_hours": available_hours, "accessible_seats": seats,
                                       "evidence": [scenario_record["ref"], terms["ref"], offer["ref"]],
                                       "exceptions": reasons})
        results.append({"plan": plan, "label": terms["label"], "gates": gates,
                        "scenarios": scenarios_for_plan, "exceptions": blockers,
                        "eligible_for_human_review": not blockers,
                        "worst_cost_gbp": max(entry["total_gbp"] for entry in scenarios_for_plan)})
    eligible = [row for row in results if row["eligible_for_human_review"]]
    least_cost = min((row["worst_cost_gbp"] for row in eligible), default=None)
    shortlist = [row["plan"] for row in eligible if row["worst_cost_gbp"] == least_cost]
    cash_refs = [row["ref"] for row in cash_rows + records["policy"]]
    finance_refs = [row["ref"] for row in cash_rows] + [policy_rows[("minimum_general_reserve_gbp",)]["ref"]]
    draft = [f"General funds available for this decision total GBP {spendable:,} "
             f"after commitments and the standing reserve ({', '.join(finance_refs)})."]
    for row in results:
        cited = sorted({ref for item in row["scenarios"] for ref in item["evidence"]}
                       | {gate["ref"] for gate in row["gates"].values() if gate["ref"]})
        finding = ", ".join(row["exceptions"]) or "all three sign-offs and the quoted resource constraints are satisfied"
        draft.append(f"{row['label']} has a maximum cost of GBP {row['worst_cost_gbp']:,}. The review records "
                     f"{finding} ({', '.join(cited)}).")
    if shortlist:
        draft.append(f"Refer {', '.join(shortlist)} to the duty director for consultation and decision.")
    else:
        draft.append("Refer the failed conditions to the duty director for a fresh offer or postponement.")
    return {
        "status": "brief for duty director" if shortlist else "escalate: no feasible plan",
        "authorisation": "No spending, entry or participant decision has been authorised.",
        "cash_gbp": dict(sorted(cash_totals.items())), "spendable_general_gbp": spendable,
        "policy": dict(sorted(policy.items())),
        "cash_and_policy_evidence": cash_refs,
        "plans": results, "lowest_worst_cost_eligible_plans": shortlist,
        "draft_board_brief": draft,
        "next_decision": "Duty director records consultation, reasons, dissent and the review route.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixtures", type=Path, default=Path(__file__).parent / "fixtures")
    args = parser.parse_args()
    try:
        result = reconcile(read_records(args.fixtures))
    except (EvidenceError, OSError, csv.Error) as exc:
        print(json.dumps({"status": "escalate: evidence incomplete", "detail": str(exc)}, indent=2))
        return 2
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["lowest_worst_cost_eligible_plans"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
