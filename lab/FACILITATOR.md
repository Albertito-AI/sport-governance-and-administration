# Facilitator’s notes

Use these notes after the learner has submitted a cash reconciliation, a scenario table and reasons for referring a decision. Keep the handwritten answer. It lets a class distinguish a mathematical mistake from a disagreement over who should decide.

## The opening packet

The treasurer can undertake **£3,900** in new commitments. Cleared general cash is £6,100 (F01). Deduct £1,700 already committed elsewhere (F02) and the £500 minimum reserve (P01). The £4,200 youth grant (F03) cannot pay for these fixtures under the exercise terms. The £1,500 sponsorship receivable (F04) has yet to clear. A bank display combining general and youth cash could show £10,300 and still leave the competition director with precisely £3,900 to work with.

| Plan | On time: price / headroom / usable time / accessible places | Delayed: price / headroom / usable time / accessible places | Sign-off and referral |
| --- | --- | --- | --- |
| A. Early civic hall | £2,550 / £1,350 / 8 h / 8 | £2,900 / £1,000 / 5 h / 4 | All roles signed. The late schedule fails the six-hour requirement and the eight-seat requirement. |
| B. Covered arena | £3,100 / £800 / 8 h / 10 | £3,800 / £100 / 7 h / 8 | All roles signed. Both scenarios satisfy the three constraints. The duty director can now consult and decide. |
| C. Split sessions | £3,450 / £450 / 8 h / 10 | £3,700 / £200 / 7 h / 10 | The technical delegate withheld approval (G08). The booking remains outside the shortlist pending that decision. |

The £100 left in the delayed arena scenario is headroom **above** the protected reserve. After paying £3,800, general cleared cash would be £2,300. Of that, £1,700 must cover the previous commitments and £500 must remain as the reserve. On its own, the size of the bank balance gives supporters no assurance that the league could afford another refund or service commitment.

Formally, take a plan as eligible when all its gates are signed and, in every supplied scenario, its cash cost does not exceed the available sum, its usable hours are at least six and its accessible places at least eight. Among those plans, minimise the maximum scenario cost. A board that wishes to optimise another outcome must say what that outcome is and where its authority to change policy comes from. The athlete representative can reasonably oppose B if travel or caring responsibilities impose an unexamined burden. The director can seek a revised quote, secure another service or postpone. She should record who was heard, who can question the decision, when the revised information is due and which officer can release a public notice.

## What should change the answer?

- With all existing sign-offs held fixed, B remains available at £3,800 of spendable cash. At £3,799 it fails by £1 in the delayed scenario. In the exercise this happens when previous commitments increase from £1,700 to £1,801. Extra money restricted to the youth award gives the director the same answer.
- With the original £3,900 available, a valid technical signature for C makes both B and C eligible. The worst costs are £3,800 and £3,700 respectively. C gains the financial advantage by £100. Its employees and players may still have good reasons to prefer B. The minutes should identify the choice and the actual distribution of inconvenience.
- If C then attracts a £350 late surcharge instead of £250, its worst cost becomes £3,800. The correct financial shortlist contains **B and C**. Printing the first item alphabetically and silently suppressing the second would remove a choice the board retained.
- Remove B’s medical sign-off while G08 remains withheld. No plan qualifies, even if every price can be paid. Remove a scenario quote instead and the worker cannot complete the comparison at all. The first position calls for a new authorised arrangement. The second first calls for the missing quote. Ask the group to draft a different message in each case.
- If the promised £1,500 clears as general money and the gift terms permit spending on the event, move the amount from F04 to F01. The available sum rises to £5,400. If it clears into the restricted programme instead, move it from F04 to F03 and available general money stays at £3,900. Counting both the promise and the receipt would overstate liquidity.

### Mathematics extension

Let $U$ be spendable general cash, $c_{ps}$ the quoted price for plan $p$ in scenario $s$, $h_{ps}$ its available hours and $a_{ps}$ its accessible places. Let $g_p$ equal one when all three responsible officers have signed and zero otherwise. With $S$ the two specified transport scenarios, the feasible set is

$$
E(U)=\{p: g_p=1,\ \max_{s\in S}c_{ps}\le U,\ \min_{s\in S}h_{ps}\ge 6,\ \min_{s\in S}a_{ps}\ge 8\}.
$$

Where this set contains a plan, the financial shortlist comprises all minimisers of $\max_{s\in S}c_{ps}$ over $p\in E(U)$. Give the class £3,900 and a valid technical signature for C. Let C’s late surcharge vary while its other terms stay fixed. For a non-negative surcharge $x$, C costs at most £3,450 + $x$, while B costs at most £3,800. C wins outright for $x<350$, ties at $x=350$ and loses to B for $x>350$. Above £450 its price also takes C outside the feasible set. Ask learners to distinguish that change in rank from the separate loss of feasibility. If a venue offers additional accessible seats at the price of a longer journey, the board must say whether its switching rule captures the outcomes that matter to the players.

## Scoring a 20-mark submission

| Criterion | Marks | Evidence of achievement |
| --- | ---: | --- |
| Trace and classify the cash | 4 | The calculation, grant treatment, outstanding commitments and reserve all reconcile to the records. |
| Assess the six plan-scenario pairs | 4 | Charges and remaining cash are correct, with usable time and access considered separately. |
| Preserve decision authority | 4 | The paper identifies both failed thresholds for A, C’s withheld gate and the director’s outstanding decision. |
| Hear and inform affected people | 4 | The schedule includes a practicable consultation with both squads, an accessible notice and a route for correction or review. |
| Audit the agent’s draft | 4 | The learner tests one marginal case, cites the evidence, identifies one claim the records cannot establish and documents any human amendment. |

For the opening packet, award separate credit for identifying A’s lost operating time under delay, A’s shortage of accessible seats under delay and C’s withheld technical approval. Score numerical accuracy per plan-scenario pair. Keep any false assertion of consent, approval or release of restricted money in a separate column, as a headline agency risk. A time-saving trial needs a comparable manual run and a denominator of completed, reviewed briefs. A passing software test records expected behaviour of software against a fixture. It supplies no estimate of time saved by a federation or of a language model’s reliability.

The duty director can close the exercise by asking each person to name the one field they would remove before running the same workflow at their club. The calculation needs aggregate accessible-seat demand, not passenger names or medical histories. A real competition office also needs current offers, signatures with explicit scope and expiry, authentic source records and an agreed route for late corrections. A completed CSV row on its own cannot confer institutional authority.

[Return to the student exercise](README.md)

© 2026 Albert Tan. All rights reserved. Free to read.
