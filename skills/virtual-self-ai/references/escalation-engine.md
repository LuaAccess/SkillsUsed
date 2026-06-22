[Uploading escalation-engine.md…]()
# Escalation Engine — Difficulty Calibration Rules

Used by virtual-self-ai to calibrate challenge level in real time based on Luther's responses.


## Core Escalation Logic

| Luther's Response Quality | Your Response |
|--------------------------|---------------|
| Strong — addresses system, leverage, and cultural layer | Increase complexity: add hidden actors, time pressure, or a new cultural variable |
| Adequate — correct but effort-based or incomplete | Reject the effort-based component. Demand the leverage version. |
| Weak — linear, surface-level, or obvious | Simplify the surface of the scenario but increase the depth of reasoning required |
| Repeats a pattern used earlier this session | Name the pattern explicitly. Block him from using it again this session. |
| Gives a generic answer | Demand specificity. "What does this look like for a mid-size PH bank, specifically?" |
| Avoids emotional or cultural dimension | Reframe the entire problem around the dimension he avoided |


## Escalation Layers (in order)

When Luther is succeeding, escalate by adding from this list:

1. **Hidden actor** — introduce a stakeholder he hasn't accounted for (a silent CFO, a political blocker, a competitor's internal champion)
2. **Time pressure** — compress the decision window ("the client moves to contract next week")
3. **Resource constraint** — remove a resource he assumed was available
4. **Cultural variable** — introduce a cultural dynamic that makes his current approach backfire
5. **Relationship risk** — reveal that a key contact in the account is leaving or changing roles
6. **Competitor move** — the competitor just made a move that changes the frame
7. **Internal political shift** — the champion who was supporting him just lost influence internally
8. **Scope ambiguity** — the client's stated requirement turns out to conflict with their actual business need
9. **Ethical edge** — introduce a situation where the highest-leverage move conflicts with a relationship or integrity constraint
10. **Meta-challenge** — ask him to explain the system he just navigated, from the outside


## Pattern Library — Name These When You See Them

When Luther repeats a pattern, name it explicitly so he can recognise it next time.

| Pattern Name | What It Looks Like | Why It's a Trap |
|-------------|-------------------|-----------------|
| **Effort Substitution** | "I'll work harder / prepare more / follow up more" | Effort is not leverage. It scales linearly and doesn't fix the system. |
| **Solution Jump** | Moves directly to a fix without diagnosing the real problem | The real problem is usually one layer deeper than the stated one |
| **Assumption Lock** | Treats an unverified belief as a confirmed fact | Decisions built on assumptions collapse when the assumption is wrong |
| **Title Bias** | Focuses on the most senior title in the room as the decision-maker | In PH business culture, real power and title often diverge |
| **Logic Override** | Leads with data/logic when the client is in an emotional or relational mode | Logic doesn't land until trust is established. Relationship before transaction. |
| **Symmetry Error** | Assumes the client interprets the situation the same way he does | His frame and the client's frame are almost always different. Map both. |
| **Visibility Trap** | Assumes what was said out loud is what the client actually believes | The real conversation in PH business often happens after the meeting |
| **Lone Wolf** | Plans a solution that depends entirely on his own execution | Leverage requires other people. Who else moves this forward? |
| **Timeline Compression** | Assumes the decision will happen faster than it will in PH enterprise | Relationships and hierarchy extend timelines. Build for the real clock. |


## Mental Models Bank

Offer one of these at the end of every session as the "mental model you should have used."

| Mental Model | When to Apply |
|-------------|---------------|
| **Second-order thinking** | When his solution solves the problem but creates a worse downstream problem |
| **Inversion** | When he is stuck — ask what would guarantee failure, then avoid it |
| **Incentive mapping** | When people are not doing what he expects — find what they're actually rewarded for |
| **Power law thinking** | When he is spreading effort evenly — 20% of the moves produce 80% of the outcomes |
| **Systems map** | When he is optimising one part of a system while ignoring the whole |
| **Pre-mortem** | Before a major client move — imagine it failed. What caused it? |
| **OODA loop** | In fast-moving competitive situations — observe, orient, decide, act faster than the competitor |
| **Contrast effect** | In pricing and positioning — what he is compared against determines how he is perceived |
| **Status quo bias** | When a client won't move — what is the cost of staying still vs. the cost of change? |
| **Narrative framing** | When logic isn't landing — what story does the client need to tell themselves to say yes? |
| **Commitment and consistency** | Get small yeses before the big ask — people align their behaviour with prior commitments |
| **Social proof in hierarchy** | In PH enterprise, "who else has done this" often matters more than "how good is this" |


## Session Tracking Template

At the end of each session, log:

```
Session date: [Date]
Mode: [MODE 1 / MODE 2]
Skills exercised: [List]
Luther's self-ratings: [Skill: rating]
Observed performance vs. self-rating: [Gap notes]
Linear pattern repeated: [Pattern name]
Mental model offered: [Model name]
Escalation level reached: [1–10]
Cultural dynamics engaged: [Yes/No — which ones]
```
