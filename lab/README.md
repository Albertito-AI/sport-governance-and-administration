# Can the fixture go ahead?

A practical laboratory for *Sport Governance and Administration* by Albert Tan. Allow 60 to 75 minutes. Work in pairs, with one person acting as the duty director and the other as the evidence officer. A third participant can represent the players. Bring in the treasurer, venue manager and league secretary for a board exercise.

At 03.30 on 30 July 2024, organisers and public authorities met with World Triathlon and other bodies to consider water quality in the Seine. The men’s Olympic triathlon scheduled for 08.00 that morning was postponed. Someone had to reconcile distinct bodies of evidence quickly enough for people to act. The transfer exercise below moves that difficulty to a much smaller competition. Its people, records, prices and options are fictional. [World Triathlon, ‘Men’s Paris 2024 Olympic Triathlon postponed’, 30 July 2024](https://triathlon.org/news/mens-paris-2024-olympic-triathlon-postponed)

## The duty director’s file

A six-club women’s league has lost its usual venue for two Saturday fixtures. At 09.00 on Friday the duty director needs comparable terms before she can consult both home and visiting squads. Three venues offer alternative arrangements. A late vehicle would shorten some operating windows, increase some charges and change the number of accessible passenger places. The teams need six usable hours altogether and eight accessible passenger places in each scenario. Six hours cover two fixtures of two hours each and a total of two hours for set-up and changeover. Each offer already accounts for any transfer between its venues.

The league has cash in one bank account. Part belongs to a youth coaching award whose terms restrict it to that programme. A sponsor has promised a further payment. The treasurer must honour existing general commitments and the minimum reserve before the league can undertake fresh expenditure. Grounds, medical and access arrangements have their own responsible people. Technical, medical and access sign-offs must all cover the proposed plan. A commercial deadline confers no authority over any of those decisions.

All monetary amounts are whole pounds sterling including applicable charges. Each price is an **incremental** commitment payable on choosing that option. The existing commitments in the ledger cover other obligations. The two transport scenarios are alternatives for the same day. The file contains neither an estimated probability for either scenario nor evidence that the players have accepted a changed itinerary.

| Record | What the evidence officer receives |
| --- | --- |
| [Cash reconciliation](fixtures/cash.csv) | Cleared general and restricted cash, existing general commitments, and the amount still receivable. |
| [Board and competition policy](fixtures/policy.csv) | The minimum reserve, usable hours and accessible places. |
| [Venue quotations](fixtures/plans.csv) | A unique plan reference and its base price. |
| [Transport scenarios](fixtures/scenarios.csv) | The two conditions the duty director asked every bidder to price. |
| [Conditional offers](fixtures/offers.csv) | Surcharge, remaining usable hours and accessible places for each plan under each condition. |
| [Sign-off register](fixtures/signoffs.csv) | Written status from each accountable role. A withheld sign-off remains with its issuer. |

### First, make a decision by hand

1. Reconcile the amount the treasurer can commit. On one sheet record each source reference and explain the treatment of the grant, prior obligations, reserve and expected sponsor payment.
2. Draw a three-by-two table, one row per plan and one column per transport scenario. Enter the price, remaining spendable cash, usable hours and accessible places. Add each outstanding signature beside the plan, together with the person who can resolve it.
3. Present an admissible shortlist and the least expensive admissible plan under the more costly scenario for each. State who bears any extra journey, who still needs to be heard and what would trigger postponement. Retain a reasoned minority view if the players and venue operator differ.

Calculate spendable cash as cleared general funds less existing general commitments and the reserve. Add the relevant transport surcharge to each base price. A plan qualifies for referral only if **every** transport scenario clears the cash, time and access constraints and all three roles have signed. For each qualifying plan, take its highest scenario cost. The smallest of those maxima determines the financial shortlist. Equal maxima leave the choice with the duty director. This objective puts a price on quoted expenditure. Additional journeys, effects on caring responsibilities and fairness to travelling players enter her written reasons.

### Run an evidence-checking agent

From the directory containing this page, run the following commands with Python 3.8 or later. The reference worker uses Python’s standard library, reads six local CSV files and prints its evidence and draft to the terminal. It requires no account, model subscription or network access.

```sh
python3 -B reference_agent.py
python3 -B -m unittest discover -v
```

Compare the cash calculation, each scenario and every sign-off in the JSON output with your handwritten record. Follow one conclusion back through its reference numbers. Read the proposed `draft_board_brief` aloud to the player representative. Which consequence would she need the director to spell out before she could seek the views of both squads?

For a second sitting, use a **copy** of `fixtures/` and change one item at a time. The command `python3 -B reference_agent.py --fixtures path/to/copy` reads your revised packet. Run one round in which the sponsor pays into the restricted fund, one in which a new general liability becomes due and one in which a technical delegate supplies written approval for the split sessions. For the first, record receipt correctly by reducing the receivable and increasing restricted cleared cash. For the third, change the sign-off only after the delegate has supplied it. At what cash figure does the director lose the last viable option? Record the first change that affects the shortlist. An exit code of 0 means at least one plan qualified for human review, 1 means none did, and 2 means the evidence could not support a comparison.

### Put a language agent to work

Give the reconciled JSON and the role instruction below to a locally approved language agent. The Python worker supplies a reproducible comparison and a rule-based draft. An optional language model can prepare a more readable brief from those same results. Store only synthetic inputs when using this public exercise.

> Act as the competition secretary’s drafting assistant. Prepare a 150-word paper for the duty director from the supplied report. Quote the spendable balance and the maximum exposure of every quoted plan. Cite the evidence references beside each figure or sign-off. Name any missing voice and say which record would change the advice. Send the draft for review. Leave approvals, bookings, payment and communication with athletes to the officers named in the exercise.

Give the reviewing officer the draft **and** the structured result. Ask them to underline every assertion, trace its evidence and circle anything the source cannot establish. A statement that the route is “fully accessible” would go beyond a transport seat count. A statement that the players agreed to the time is equally serious when the packet contains no consultation record. Record each correction before the director makes her own decision.

## From the classroom to a federation

Start with a weekly task for which someone already checks a record against an independent source. Give the agent a defined reading permission, a named reviewer and a draft destination. Athlete or staff members need a human contact who can correct an error and explain the underlying decision. Retain the version of the relevant policy, the identifiers of evidence relied upon, the correction and the officer’s signed decision in the organisation’s usual records system.

| Proposed deployment | What an agent can deliver | Who closes the decision and what remains on the record |
| --- | --- | --- |
| Grants and treasury | Reconcile cleared receipts to the approved spending categories and flag unmatched commitments before the payment run. | The treasurer verifies restrictions and the delegated signatories authorise payment. The chief executive takes a projected breach to the finance committee. |
| Fixtures and supporter services | Compare published fixture changes with venue holds, ticket allocations, accessible transport capacity and proposed refund batches. | The competition director owns the fixture. Club liaison records player feedback, and ticketing obtains finance approval before refunding a batch. |
| Selection and appeals | Cross-reference the published policy version, the panel’s recorded reasons and the date by which another athlete may need notice. | Selectors decide merit. The appeal secretary protects the independence of the reviewing body and records any correction or notification. |
| Athlete welfare and safeguarding | Check whether a case reference was acknowledged by the appointed officer within the agreed time. Limit the input to reference, time and routing status. | The safeguarding lead handles the report and decides its route under the applicable policy. Preserve a direct human reporting route outside the agent. |
| Facilities and insurance | Match each venue hold to a dated technical sign-off and the insurer’s stated coverage conditions. Route gaps to the responsible officer. | The medical and technical leads retain their remits. The director obtains any necessary insurer confirmation before opening. |
| Evaluation and public reporting | Flag changed denominators, missing clubs and duplicated attendance totals in the season return. | The evaluation officer checks contested records with clubs, explains changes in coverage and signs the corrected report. |

### Does deployment earn its place?

Run the same packet manually and with assistance in separate groups, or reverse the order across groups using a new packet of similar difficulty. The director times the work from receipt of the packet to a **reviewed, releasable** paper, including time spent checking and correcting it. Each group reports the number of exact scenario calculations out of six, the number of material exceptions found out of those in its packet, any inaccurate assertions about authority or consent, and whether the appropriate person received the escalation. Use the same scoring key for both methods. Never describe a discarded, unreviewed draft as time saved.

Before piloting on real records, specify a review period and an officer with authority to pause the pilot. A draft that spends restricted money, treats a withheld signature as approval or invents player consent is a critical error. Record whether the human reviewer caught it as well as whether the agent produced it. Compare medians across comparable packets, report the number assessed and preserve dissent from the people whose work changed. Publish only aggregate timings and error counts. Real case identifiers, contact details and health information belong in access-controlled systems under the organisation’s retention rules.

**For instructors.** Keep the reasoning and boundary tests until groups have delivered their first paper. [Facilitator’s notes](FACILITATOR.md)

This exercise extends the Atlas Agent School’s work on evidence, testing and delegation and offers the Atlas Open Mathematics project a finite problem with constraints, ties and a verifiable optimum. [Atlas Agent School](https://github.com/Albertito-AI/atlas-agent-school-public) · [Atlas Open Mathematics](https://github.com/Albertito-AI/atlas-open-mathematics)

© 2026 Albert Tan. All rights reserved. Free to read. Third-party materials retain their respective rights.
