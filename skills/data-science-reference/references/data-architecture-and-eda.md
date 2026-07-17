# Data Architecture & Exploratory Data Analysis

## What is data architecture

The blueprint for how data is collected, stored, integrated, and used across an organization — connects business goals to technical implementation. Think "city plan for data": where things live, how they connect, how information moves.

## Key terms

| Term | Meaning |
|---|---|
| Data Architecture | High-level blueprint for data structures & flows |
| Data Model | Representation of entities, attributes, relationships |
| Data Governance | Policies for quality, access, compliance |
| Metadata | Data about data (definitions, formats, lineage) |
| Data Lineage | Where data originates and how it transforms/moves |
| Data Strategy | Plan for how data supports business objectives |

## Architecture types

| Type | Description | Pros | Cons |
|---|---|---|---|
| Centralized | All data flows into one core platform | Strong control, consistency | Can bottleneck |
| Decentralized (domain-based) | Each domain owns/manages its own data | Flexibility, domain expertise | Risk of inconsistency without governance |
| Federated / Hybrid | Central policy hub + local implementation | Balance of control + flexibility | Requires strong governance discipline |

## Three types of data models

1. **Conceptual** — business-level, entities and relationships only (e.g., Customer → Order → Product)
2. **Logical** — adds attributes, keys, cardinality; still platform-agnostic
3. **Physical** — maps to an actual schema (tables, columns, types, indexes)

Flow: Conceptual → Logical → Physical (business view → implementation detail).

## Core components of a data architecture

Data Sources (operational DBs, apps, files, APIs) → Ingestion & Integration (batch/streaming/message queues) → Storage & Processing (data lake, warehouse, marts, NoSQL) → Semantic/Modeling Layer (metrics definitions, semantic views) → Data Access & Consumption (BI dashboards, ML/AI, APIs) — with Governance (access controls, quality rules, lineage) wrapping the whole thing.

## Implementation steps (vision → reality)

1. Understand business strategy
2. Assess current data landscape
3. Define principles & standards
4. Design data models & flows
5. Choose & align technologies
6. Implement iteratively
7. Establish governance & operating model
8. Monitor, evolve, and scale

---

## Exploratory Data Analysis (EDA) checklist

| Step | What to check | Why |
|---|---|---|
| Data distribution | Histograms, density, box plots | Understand shape/skew |
| Missing data | Null counts, missingness patterns | Identify incomplete records |
| Outliers | Box plot, IQR, Z-score | Catch extreme/erroneous values |
| Correlation | Correlation matrix/heatmap | Find related variables |
| Patterns | Trends, clusters, seasonality | Discover hidden structure |
| Data types | Confirm numeric/categorical/datetime/text are stored correctly | Prevent silent type-coercion bugs |
| Summary statistics | Mean, median, std dev, min, max | Quick numeric summary |
| Visualization | Scatter, bar, histogram, pair plots | See what tables hide |
| Data quality | Inconsistencies, invalid entries | Ensure reliability before modeling |
| Class distribution | Target variable balance (e.g., 90/10 split) | Catch class imbalance early |
| Duplicates | Duplicate records | Remove redundant observations |

## Typical EDA workflow order

Load data → Inspect structure (shape, dtypes, columns) → Clean (nulls, dupes) → Compute descriptive stats → Visualize → Identify issues (outliers, imbalance, quality) → Hand off a clean, understood dataset for modeling.

## Gotcha for client work

For BSP-adjacent or Yamaha/UAS data work, the "class distribution" and "data quality" checks aren't optional boilerplate — an undetected 90/10 imbalance or silent type mismatch is exactly the kind of thing that turns into a credibility problem in front of a client audit later. Don't skip straight to modeling.
