---
description: >-
  Enforces Discovery-to-Proposal Pre-Sales Engineering standards, anti-slide constraints, anti-hallucination protocols, and staged multi-agent DAG handoffs across Problem & Scope Alignment, Solutions Architecture & Risk, Engineering Estimation, Agile Staffing & Milestones, and Commercial Governance.
trigger: model_decision
---

# Discovery-to-Proposal Engineering Guardrails & DAG Protocol

When ingesting raw discovery notes, meeting transcripts, or client project briefings to produce the unified pre-sales engineering dossier (`DOSSIE_TECNICO_PRE_PROPOSTA.md`), all agents and execution stages MUST strictly comply with these non-negotiable architectural guardrails.

---

## 1. Critical Negative Constraint: Absolute Prohibition of Slides & Presentation Summaries

- **Zero Slides Tolerance**: The plugin and all constituent agents are **STRICTLY FORBIDDEN** from generating slide decks, slide outlines, presentation pitch formats, or summarized bullet decks (e.g., "Slide 1: Problem", "Slide 2: Solution", "Deck Outline", bullet points formatted for PowerPoint/Keynote).
- **Format Invariant**: The sole authorized primary artifact is a dense, analytical, technical-commercial Markdown dossier titled `DOSSIE_TECNICO_PRE_PROPOSTA.md`.
- **Analytical Density**: Text must be executive yet technically exhaustive. Every claim, architecture recommendation, epic estimate, and commercial clause must be fully articulated with context, rationale, trade-offs, and risk analysis.

---

## 2. Anti-Hallucination & Risk Assumption Protocol

- **Never Fabricate Omitted Details**: In real-world discovery meetings, clients frequently omit technical specs (e.g., legacy ERP version, database throughput, authentication protocol, exact concurrent users, data volume). Agents MUST NOT invent or assume these facts silently.
- **Explicit Risk & Assumption Register**: Whenever critical information is missing from the discovery inputs:
  1. Record the omission explicitly in the **Assumptions & Open Technical Questions** register.
  2. Document the potential architectural and cost impacts of varying outcomes.
  3. Prescribe an explicit **Discovery Spike / Inception Spike** task to validate the item before coding starts.
  4. Apply an explicit **Uncertainty Risk Buffer (+20% to +40%)** to affected epic estimations.

---

## 3. Strict Boundary Matrix: In-Scope vs. Explicit Out-of-Scope

- **Scope Creep Prevention**: No proposal is valid without an explicit, unambiguous Out-of-Scope delimitation.
- **Mutual Exclusivity**:
  - **In-Scope (Core)**: Concrete capabilities, journeys, and integrations agreed upon for this engagement.
  - **Explicit Out-of-Scope**: Adjacent features mentioned as future desires, legacy data cleansing, third-party licensing fees, infrastructure cloud spend, legacy hardware maintenance, mobile responsiveness if web-only, etc.
- **Traceability**: Every In-Scope item must link directly to an addressed business pain and a measured success metric.

---

## 4. Realistic Engineering Estimation & 75-80% Utilization Factor

- **Analogy & T-Shirt Sizing Grounding**:
  - Small (S): 1-2 developer-sprints (low complexity, standard CRUD, established patterns).
  - Medium (M): 3-5 developer-sprints (moderate complexity, 1 standard external integration, custom business rules).
  - Large (L): 6-8 developer-sprints (high complexity, legacy integrations, non-standard state machines, high concurrency).
  - Extra Large (XL): 9+ developer-sprints (critical architectural risk, legacy ERP write-backs, distributed consensus, heavy regulatory compliance).
- **Buffer Calibration**: High-risk epics (legacy ERP sync, undocumented APIs) must carry a mandatory +25% to +35% risk contingency buffer.
- **Utilization Factor**: When converting epic effort into calendar duration, **never assume 100% capacity**. Staffing must calculate throughput at **75% to 80% effective utilization** (30-32 productive engineering hours/week per developer) to account for agile ceremonies, code reviews, staging deployments, team cross-training, and context switching.

---

## 5. Commercial Governance & Tacit Acceptance Protection

- **Defensive Commercial Framing**: Pre-sales engineering must protect delivery margin and cash flow.
- **Mandatory Change Request (CR) Protocol**: Any requirement alteration exceeding 10% of sprint capacity or deviating from the In-Scope baseline requires formal written CR with impact analysis on cost and timeline before execution.
- **UAT & Tacit Acceptance Clause**:
  - Maximum client homologation window of **5 business days** per milestone delivery.
  - If the client fails to report Severity 1 (Blocker) defects within this window, the milestone is deemed **tacitly approved and accepted** for invoicing and progression.
- **Phase 0 (Technical Inception) Gate**: If architectural uncertainty exceeds 30%, recommend a dedicated 2-to-4 week Paid Technical Inception before committing to fixed delivery dates.

---

## 6. Staged Multi-Agent DAG Execution Protocol

The pipeline must execute strictly as a Directed Acyclic Graph (DAG) with contextual handoffs:

```
[Input: Raw Discovery Notes]
       │
       ▼
[Stage 1: Problem & Scope Alignment Analyst] ──► Handoff 1: Scope Baseline
       │
       ▼
[Stage 2: Principal Solutions Architect & Risk Auditor] ──► Handoff 2: Tech Foundation & Risks
       │
       ▼
[Stage 3: Engineering Estimator (Analogy & T-Shirt)] ──► Handoff 3: Effort Model
       │
       ▼
[Stage 4: Agile Delivery & Staffing Specialist] ──► Handoff 4: Delivery Plan
       │
       ▼
[Stage 5: Commercial Governance & Risk Mitigator] ──► Handoff 5: Commercial Strategy
       │
       ▼
[Lead Pre-Sales Orchestrator & Synthesizer] ──► DOSSIE_TECNICO_PRE_PROPOSTA.md
```

- Each stage ingests the cumulative output of previous stages.
- No downstream stage may contradict an upstream decision without explicit architectural notation.
- If run in an environment without dynamic subagent spawning, the root agent adopts each persona sequentially in strict DAG order.
