import unittest
from pathlib import Path

from reference_agent import EvidenceError, read_records, reconcile


class DisruptedFixtureTests(unittest.TestCase):
    def setUp(self):
        self.records = read_records(Path(__file__).parent / "fixtures")

    def amend(self, table, ref, field, value):
        row = next(row for row in self.records[table] if row["ref"] == ref)
        row[field] = value

    def test_hand_calculation_and_provenance(self):
        report = reconcile(self.records)
        self.assertEqual(report["spendable_general_gbp"], 3900)
        self.assertEqual(report["lowest_worst_cost_eligible_plans"], ["B"])
        by_plan = {row["plan"]: row for row in report["plans"]}
        self.assertEqual([by_plan[k]["worst_cost_gbp"] for k in "ABC"], [2900, 3800, 3700])
        late_b = next(row for row in by_plan["B"]["scenarios"] if row["scenario"] == "late")
        self.assertEqual((late_b["total_gbp"], late_b["spendable_balance_gbp"]), (3800, 100))
        self.assertEqual(late_b["evidence"], ["S02", "Q02", "O04"])
        self.assertEqual(by_plan["A"]["exceptions"], ["late: usable block 5 h", "late: accessible seats 4"])
        self.assertEqual(by_plan["C"]["exceptions"], ["technical sign-off withheld"])

    def test_restricted_cash_and_promised_money_cannot_rescue_a_shortfall(self):
        self.amend("cash", "F02", "gbp", "1801")
        self.amend("cash", "F03", "gbp", "14200")
        self.amend("cash", "F04", "gbp", "20000")
        report = reconcile(self.records)
        self.assertEqual(report["spendable_general_gbp"], 3799)
        self.assertEqual(report["lowest_worst_cost_eligible_plans"], [])

    def test_equality_at_cash_boundary(self):
        self.amend("cash", "F02", "gbp", "1800")
        self.assertEqual(reconcile(self.records)["lowest_worst_cost_eligible_plans"], ["B"])

    def test_signed_amendment_exposes_lower_cost_alternative(self):
        self.amend("signoffs", "G08", "status", "signed")
        self.assertEqual(reconcile(self.records)["lowest_worst_cost_eligible_plans"], ["C"])

    def test_tied_plans_are_referred_together(self):
        self.amend("signoffs", "G08", "status", "signed")
        self.amend("offers", "O06", "surcharge_gbp", "350")
        self.assertEqual(reconcile(self.records)["lowest_worst_cost_eligible_plans"], ["B", "C"])

    def test_missing_sign_off_cannot_be_treated_as_favourable(self):
        self.records["signoffs"] = [row for row in self.records["signoffs"] if row["ref"] != "G04"]
        report = reconcile(self.records)
        self.assertEqual(report["lowest_worst_cost_eligible_plans"], [])
        self.assertIn("medical sign-off missing", report["plans"][1]["exceptions"])

    def test_unpriced_scenario_stops_the_comparison(self):
        self.records["offers"].pop()
        with self.assertRaisesRegex(EvidenceError, "every specified scenario"):
            reconcile(self.records)

    def test_duplicate_source_references_stop_the_comparison(self):
        self.records["offers"][1]["ref"] = "F01"
        with self.assertRaisesRegex(EvidenceError, "Duplicate evidence"):
            reconcile(self.records)

    def test_negative_cost_is_escalated(self):
        self.amend("offers", "O03", "surcharge_gbp", "-15")
        with self.assertRaisesRegex(EvidenceError, "non-negative"):
            reconcile(self.records)

    def test_inputs_are_unchanged_after_run(self):
        import copy
        snapshot = copy.deepcopy(self.records)
        self.assertEqual(reconcile(self.records), reconcile(self.records))
        self.assertEqual(self.records, snapshot)


if __name__ == "__main__":
    unittest.main()
