---
name: discovery-interview-guide
description: "Create a structured user discovery interview guide with screener questions, a discussion guide, and a synthesis framework. Use when planning user interviews, customer discovery sessions, Jobs-to-be-Done research, or problem validation. Produces a complete guide covering warm-up, problem exploration, and a per-session synthesis template. Do NOT use for sales prospect calls — use discovery-call-prep instead."
---

# Discovery Interview Guide Skill

Design interviews that surface genuine insight — not validation of what you already believe. Every guide follows a story-based, past-behaviour-focused structure.

## Core Principles

1. **Never ask about the future.** "Would you use X?" tells you nothing. "Tell me about the last time you did X" tells you everything.
2. **Interview for behaviour, not opinion.** Opinions are cheap. Behaviour is evidence.
3. **The 5 Whys.** Every surface answer is a door. Keep opening doors.
4. **Confirm the problem before exploring the solution.** Never show a prototype until you've confirmed the pain exists unprompted.

## Interview Structure (60 minutes standard)

### 1. Warm-Up (5 min)
Build rapport. Get them talking. Don't discuss the topic yet.
- "Tell me a bit about your role and what a typical week looks like for you."
- "What tools do you rely on most day-to-day?"

### 2. Context Setting (10 min)
- "Walk me through how you currently [handle the domain area]."
- "What does that process look like from start to finish?"
- "Who else is involved when you do this?"

### 3. Problem Exploration (25 min) — THE CORE
- "Tell me about the last time you had to [relevant task]. What happened?"
- "What was the hardest part of that?"
- "How did you handle it?"
- "What did you try before settling on that approach?"
- "What does it cost you when this goes wrong?" (time, money, stress, reputation)
- "If you could wave a magic wand and change one thing about this process, what would it be?"

⚠️ **Do not mention your product or feature during this phase.**

### 4. Current Solutions (10 min)
- "What tools or workarounds do you use today for this?"
- "What do you like about [current solution]? What frustrates you?"
- "Have you tried other approaches? What happened?"

### 5. Wrap-Up (10 min)
- "Is there anything about this topic we haven't covered that you think I should know?"
- "Is there anyone else you'd recommend I speak to?"
- "Would you be open to a follow-up if I have more questions?"

---

## Output Format

### Discovery Interview Guide — [Topic] — [Date]

**Research Goal:** [One sentence: what decision will this research inform?]
**Target Participant Profile:** [Role, company size, behaviour qualifier]

**Screener Questions** (for recruiting):
1. [Question] → Must answer: [Y/N or specific]
2. [Question] → Must answer: [Y/N or specific]
3. [Disqualifier question] → Disqualify if: [answer]

**Interview Guide:**
[Full structured guide using the format above, customised to the specific research topic]

**Synthesis Template** (fill after each interview):
- Key quote: "[verbatim]"
- Core pain: [1 sentence]
- Current workaround: [what they're doing today]
- Intensity (1–5): [how painful is this?]
- Surprise/unexpected finding: [anything that challenged your assumptions]

**Pattern Detection** (after 5+ interviews):
- Pain mentioned by [X/N] participants: [theme]
- Workaround used by [X/N] participants: [theme]
- Most emotionally charged moment in interviews: [observation]

---

## Required Inputs

Ask the user for these if not provided:
- **Research topic or question** (what decision will this inform?)
- **Target participant profile** (role, behaviour, company type)
- **Session length** (30 / 45 / 60 / 90 minutes)
- **Number of interviews planned**
- **Known hypotheses to test** (optional)

## Quality Checks

- [ ] No future-tense questions ("would you...") — only past-behaviour questions
- [ ] Product or solution not mentioned until after pain is confirmed
- [ ] Questions open-ended (cannot be answered yes/no)
- [ ] Synthesis template included for per-session notes
- [ ] Screener questions identify and disqualify wrong participants

## Anti-Patterns

- [ ] Do not use future-tense questions ("Would you use this?")
- [ ] Do not mention your product or solution before problem exploration is complete
- [ ] Do not synthesise across fewer than 5 interviews
- [ ] Do not write screener questions that are too easy to pass
- [ ] Do not treat participant opinions as evidence of future behaviour

## Gotchas

**Trigger conflicts:**
- This skill and `discovery-call-prep` both involve structured questioning. Use THIS skill for user research and problem validation interviews. Use `discovery-call-prep` for sales calls with new prospects.
- Mutual exclusion: if the goal is to qualify a deal or advance a sale → `discovery-call-prep`. If the goal is to understand user behaviour or validate a problem hypothesis → this skill.

**Known failure modes:**
- Generated interview guides sometimes include future-tense questions despite the instruction. Review every question before use — any "would you," "could you imagine," or "do you think you would" should be rewritten as past-tense.
- Screener questions are sometimes too generic (anyone could pass). Prompt: "Make the screener questions specific enough to filter out people who don't have the exact behaviour we're researching."
- Synthesis template is sometimes omitted from short sessions. Prompt: "Include the synthesis template even for a 30-minute guide."

**Filipino/Asian market specifics:**
- Filipino interview participants tend to give socially desirable answers rather than honest ones, especially early in the interview. The warm-up phase is critical — invest more time than you think you need before moving to problem exploration.
- Switching to Filipino or Taglish mid-interview often signals genuine engagement or emotional relevance. When a participant code-switches, the content of that statement is usually the most honest thing they've said. Note it explicitly.
- Direct questions about pain ("what's your biggest problem with X?") often produce polite deflection. Use storytelling prompts instead: "Tell me about the last time X went wrong" produces richer responses in Philippine cultural contexts.
- Hierarchy affects candour — participants may give more honest answers if the interviewer is a peer rather than someone senior. Consider who conducts the interview.

## Example Trigger Phrases
- "Build a discovery interview guide for [research topic]"
- "I need to run user interviews about [problem area] — help me structure them"
- "Create a Jobs-to-be-Done interview guide for [product/feature]"
