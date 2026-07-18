---
name: data-science-reference
description: Quick-reference lookup for data science, statistics, machine learning, deep learning, LLM/GenAI, and data architecture concepts — formulas, definitions, decision guides, and comparison tables. Use whenever brainstorming a model choice, explaining a formula, picking a statistical test, comparing algorithms/architectures, sanity-checking a technical claim in a proposal, or prepping client-facing material (e.g., UAS/Yamaha/BSP) that touches ML, statistics, or AI system design. Trigger on mentions of regression, classification, clustering, loss function, probability distribution, neural network architecture, LLM, RAG, vector database, graph database, backpropagation, gradient descent, EDA, hypothesis testing, or "which algorithm/test/model should I use." Not for running code or analyzing an actual dataset — for that, use the data:* or engineering:* skills instead; this skill is the concept/formula layer they can cite.
---

# Data Science & ML Reference

A structured formula/decision-support library. It does not execute analysis — it supplies the concepts, formulas, and selection logic so you (or another skill) can apply them correctly. Built from a curated set of ML/stats cheat sheets, cleaned of duplicates and formatting artifacts.

## Gotchas

- **This is reference, not computation.** If the user wants an actual regression run, a chart built from real data, or a model trained, hand off to `data:analyze`, `data:statistical-analysis`, or `data:data-visualization` — don't try to compute results from memory using these formulas.
- **Don't dump a whole reference file into chat.** Read only the section needed to answer the question; summarize, don't paste full tables unless asked for the full sheet.
- **Formula notation varies by source.** Where two source sheets defined the same term differently (e.g., MSE vs MSE regularized, or Gamma distribution parameterized by rate vs scale), the reference notes both conventions — check which one the user's downstream tool (sklearn, a specific textbook) expects before applying.
- **Mutual exclusion with other reference skills:** if the request is really about *writing SQL* → `data:sql-queries`/`data:write-query`. If it's about *building a dashboard* → `data:build-dashboard`. If it's about *architecture decisions for a client system* → `engineering:architecture`. This skill is the pure-concept layer underneath those.
- **Client-facing use (Filipino/Asian market context):** when this reference is used to prep material for UAS, Yamaha, or BSP-adjacent conversations, keep the explanation at decision-maker level (mechanism + when-to-use + trade-off) rather than raw formula dumps — save the math for the technical annex.

## Routing table

| If the question is about... | Read |
|---|---|
| Core math notation (gradient descent, MLE, OLS, eigenvectors, entropy, SVD, Lagrange, cosine similarity, sigmoid, softmax, ReLU, z-score, correlation) | `references/math-foundations.md` |
| Which probability distribution to use / how they relate to each other | `references/probability-distributions.md` |
| Which statistical test to run / hypothesis testing / confidence intervals / CLT | `references/statistical-tests-and-inference.md` |
| Which ML algorithm fits a problem (regression, classification, clustering, ensembles, RL) | `references/ml-algorithms.md` |
| Neural network architecture selection, backpropagation mechanics | `references/neural-networks-and-backprop.md` |
| Which loss function to use for a model | `references/loss-functions.md` |
| How LLMs are trained/work, LLM engineer learning path, prompt/RAG/fine-tuning concepts | `references/llm-and-genai.md` |
| AI agent execution loop, tool calling, vector DB vs graph DB vs hybrid RAG | `references/agentic-systems-and-rag.md` |
| Data architecture patterns, EDA checklist | `references/data-architecture-and-eda.md` |

## How to use this in a session

1. Identify which reference file(s) the question touches (can be more than one — e.g., "what loss function for an imbalanced classifier" touches both `ml-algorithms.md` and `loss-functions.md`).
2. Read only that file (or the relevant section via view_range if it's long).
3. Answer using its **Quick Selection Guide** table first — those are decision shortcuts. Pull the formula/detail table only if the user needs the mechanism.
4. If the user is brainstorming a client-facing solution (BSP, UAS, Yamaha), translate the selected concept into plain business language before presenting — this skill's tables are intentionally terse/technical.
5. If the concept feeds into an actual build (e.g., "let's actually run this regression on our churn data"), hand off to `data:analyze` or `data:statistical-analysis` rather than continuing in reference mode.

## File index (line counts, for planning reads)

- `math-foundations.md` — 24 core formulas (gradient descent → eigenvectors)
- `probability-distributions.md` — 10+ distributions, relationships, interview favorites
- `statistical-tests-and-inference.md` — test selection guide + inferential stats (CLT, CI, hypothesis testing)
- `ml-algorithms.md` — regression/classification/clustering/ensemble/RL algorithm map + selection guide
- `neural-networks-and-backprop.md` — 25 architectures + backprop equations/code
- `loss-functions.md` — regression + classification loss functions, selection guide
- `llm-and-genai.md` — how LLMs train, LLM engineer roadmap, GenAI roadmap, PEFT/RAG basics
- `agentic-systems-and-rag.md` — agentic loop stages, vector vs graph vs hybrid DB selection
- `data-architecture-and-eda.md` — data architecture types/components, EDA checklist
