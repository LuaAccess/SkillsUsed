# LLMs & Generative AI

## The AI hierarchy

```
Artificial Intelligence
   └─ Machine Learning (learns patterns from data, not hard-coded)
        └─ Deep Learning (neural nets, complex patterns from large data)
             └─ Generative AI (creates new content: text, image, audio, code)
```

## How an LLM is actually trained (end to end)

**Data phase:** Data Collection → Data Preparation (clean, remove PII) → Data Classification → Tokenization → Vocabulary/Lexicon Creation.

**Training/alignment phase:** Base Training (predict next token) → Model Architecture (Transformer) → Example Outputs (human-labeled ideal responses) → Supervised Fine-Tuning → Feedback/Reward Model → Policy Optimization (RLHF/PPO or DPO) → Model Refinement → Evaluation.

**Deployment phase:** System Deployment → User Input Processing (tokenize the request) → Context Analysis (intent) → Ambiguity Handling → Safety Controls → Answer Generation (token by token).

**Ongoing:** Multilingual Support, User Customization, System/API Integration, Performance Tracking, Continuous Improvement.

Key terms: **Pretraining** (learn general patterns predicting next token) · **Fine-tuning** (adapt for a specific task) · **RLHF** (reinforcement learning from human feedback) · **PPO** (algorithm that optimizes model behavior against a reward model) · **Context window** (how much the model can consider at once) · **Token** (smallest text unit the model processes).

## Fine-tuning & RAG (the two ways to specialize a model)

| Approach | What it does | When to use |
|---|---|---|
| **RAG** (Retrieval-Augmented Generation) | Retrieve relevant docs at query time, inject into the prompt, generate a grounded answer | Knowledge changes often, need citations, don't want to retrain |
| **PEFT** (LoRA / QLoRA / Adapters) | Train small additional parameters on top of a frozen base model | Need the model to *behave* differently (style, task) with limited compute |

RAG pipeline: Document Loading → Chunking → Embeddings → Vector DB → Vector Search → Reranking → Augmented prompt → Generation.

## Building an AI agent

Components: **Planning** (decide actions), **Reasoning** (LLM core), **Memory** (short + long term), **Tools** (API calls, web search, database, code interpreter), **Environment** (external systems), **Human Override** (supervision/control).

## LLM Engineer roadmap (learning path order)

1. Python Programming
2. Git & Linux
3. Mathematics for ML (linear algebra, probability, stats, calculus) → *build: implement gradient descent*
4. Machine Learning (regression, classification, clustering, feature engineering) → *build: house price predictor, text classifier*
5. Deep Learning (NN, backprop, CNNs, attention, PyTorch) → *build: sentiment analyzer*
6. NLP Fundamentals (tokenization, embeddings, NER, BERT) → *build: local chatbot*
7. LLMs (Transformer architecture, self-attention, context window, decoder-only models) → *build: structured output / function calling*
8. Prompt Engineering (zero-shot, few-shot, chain-of-thought) → *build: prompt library*
9. RAG (chunking, embeddings, vector DBs, reranking) → *build: PDF chat assistant*
10. AI Agents (tool calling, memory, multi-agent, MCP, workflows) → *build: research agent*
11. LLM Fine-Tuning (LoRA/QLoRA, PEFT, instruction tuning, preference optimization) → *build: fine-tune a small open LLM*
12. Deployment & Inference (FastAPI, Docker, vLLM/Ollama, GPU inference, monitoring) → *build: deploy an AI API*
13. Portfolio & Career (end-to-end projects, GitHub, technical writing, interviews)

## Foundation model landscape (as of source material)

GPT (OpenAI), Claude (Anthropic), Gemini (Google), Llama (Meta), DeepSeek — treat any specific model comparison as needing a fresh web check since this space moves fast; verify current model names/capabilities before quoting to a client.

## Computer vision GenAI

Diffusion Models (Stable Diffusion), DALL·E, Midjourney, Flux — image generation, editing, inpainting, enhancement.

## Gotcha

Roadmap/tooling content (framework names, model names, "current" capabilities) ages fast — always sanity-check against a web search before presenting to a client as current state of the art, especially for BSP-adjacent proposals where accuracy matters more than recency-of-buzzword.
