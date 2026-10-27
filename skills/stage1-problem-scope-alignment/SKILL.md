---
name: stage1-problem-scope-alignment
description: >-
  Use this skill to extract root business pains, define measurable business KPIs, and establish an ironclad Delimitation Matrix (Core In-Scope vs. Explicit Out-of-Scope) from raw discovery notes or transcripts.
---

# Stage 1: Problem & Scope Alignment Skill

This skill guides the extraction of core business drivers, separates operational pains from superficial feature wishes, defines measurable target metrics, and constructs the non-negotiable **Delimitation Matrix: Core In-Scope vs. Explicit Out-of-Scope**.

---

## 1. Core Principles

1. **Root Cause Analysis (The 5 Whys)**:
   - Never accept client feature requests at face value.
   - Example: If the client requests "AI document OCR", probe the business pain: "Manual invoice entry takes 4 hours per day and causes 6% duplicate payment errors."
2. **Measurable Success Metrics**:
   - Every software project must move at least one commercial or operational metric:
     - Cycle time reduction (e.g. from hours to seconds).
     - Error rate reduction (e.g. from 5% to <0.1%).
     - Cost per transaction reduction.
     - Regulatory compliance guarantee.
3. **Rigorous Scope Boundary**:
   - A proposal with undefined boundaries is a financial catastrophe waiting to happen.
   - For every In-Scope item, identify adjacent features that are explicitly excluded (Out-of-Scope) to prevent scope creep.

---

## 2. Execution Runbook

1. **Ingest Notes**: Read the discovery transcript or unstructured notes.
2. **Synthesize Problem**: Write Section 1.1 and 1.2 of the Dossier.
3. **Map Metrics**: Construct the Business Objectives Table (OBJ-01, OBJ-02, etc.).
4. **Build Delimitation Matrix**: Group features into domains (Auth, Core Workflows, Integrations, Data, Front-end, Back-office) and classify In-Scope vs. Out-of-Scope with justifications.
5. **Log Assumptions & Unknowns**: Record unconfirmed client items in the Risk Register.
6. **Emit Handoff 1**: Pass `Handoff 1: Scope Baseline` to Stage 2.
