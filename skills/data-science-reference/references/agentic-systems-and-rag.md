# Agentic Systems, Tool Use & Retrieval Architecture

## The full agentic loop

```
User Task → Planning (LLM reasoning) → Tool Selection → Tool Execution
→ Observation Parsing → Memory Update → Re-Planning Loop → Response Synthesis → Output
```

| Stage | What happens |
|---|---|
| 1. User Task Input | Natural language instruction is received |
| 2. Planning (ReAct loop) | Understand goal → decompose task → identify subtasks → create plan |
| 3. Tool Selection | Rank candidate tools → validate parameters → pick best tool |
| 4. Tool Execution | Call external API/system, with auth, rate limiting, timeout protection |
| 5. Observation Parsing | Validate raw response against a schema (e.g., Pydantic/JSON Schema) before trusting it |
| 6. Memory Update | Short-term (in-context), long-term (vector store), key-value (user/session), episodic log |
| 7. Re-Planning | Is the task complete? If not, loop with updated context |
| 8. Response Synthesis | Combine all observations, format, add citations, run safety checks |
| 9. Output | Streamed tokens or structured response; action taken |

**Key concepts:**
- **Prefill vs decode:** prefill (processing context) is compute-intensive; decode (generating tokens) is memory-bandwidth-intensive.
- **Tool call failure handling:** retry with backoff → fallback tool/model → ask user, in that order.
- **A2A (agent-to-agent):** multi-agent systems call each other via API/MCP/gRPC, not just direct APIs.
- **Latency = sum of** all LLM calls + tool round trips + retrieval + validation retries.
- **Always bound the loop:** max iterations, timeouts, and budget limits — unbounded agentic loops are a real production failure mode.

**Safety/reliability layer (non-negotiable in production agents):** input moderation, prompt-injection defenses, tool permission sandboxing, PII/secret redaction, hallucination/grounding checks, rate limiting, logging/tracing, fallback models.

**Architecture modes:** single-agent (one planner, one tool loop — best for simple tasks) vs multi-agent (orchestrator delegates to specialist agents — best for complex/distributed tasks).

## Vector DB vs Graph DB vs Hybrid (GraphRAG)

| Capability | Vector DB | Graph DB | Hybrid (GraphRAG) |
|---|---|---|---|
| Semantic search | Strong | Moderate | Strong |
| Explicit relationships | Weak | Strong | Strong |
| Multi-hop reasoning | Weak | Strong | Strong |
| Speed & scale | Fast | Moderate | Balanced |
| Context richness | Moderate | Strong | Very strong |
| Explainability | Low | High | High |

**Vector DB** (Pinecone, Weaviate, Qdrant, Milvus, Chroma, Postgres+pgvector): text → embedding → similarity search (cosine/ANN) → top-K results. Best for semantic Q&A, document retrieval, recommendation, image/audio similarity. Weakness: doesn't model explicit relationships.

**Graph DB** (Neo4j, Amazon Neptune, ArangoDB, TigerGraph, Memgraph): entities as nodes, relationships as edges; query → entity extraction → graph traversal → connected results. Best for multi-hop reasoning, fraud detection, compliance, org/supply-chain hierarchies. Weakness: limited native semantic similarity (needs embeddings bolted on).

**Hybrid (GraphRAG):** vector path (semantic) + graph path (structure) → fusion/reranking layer → LLM. This is what production systems increasingly use for complex, relationship-heavy RAG.

## Which one do I use?

| Requirement | Use |
|---|---|
| Simple semantic Q&A / document search | Vector DB |
| Relationship-heavy queries (org charts, fraud rings, compliance chains) | Graph DB |
| Complex multi-hop or relationship-heavy RAG | Hybrid (GraphRAG) |

## Note for BSP/compliance-adjacent work

Graph DBs' explainability advantage (you can literally trace *why* two entities are connected) is worth flagging when the deliverable involves fraud detection or regulatory audit trails — a vector-only system gives you "these look similar" without a traceable reasoning chain, which is a weaker story to a regulator.
