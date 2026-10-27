---
name: stage2-tech-architecture-risk
description: >-
  Use this skill to audit technical red flags (legacy ERPs, undocumented APIs, data security/LGPD), define the macro architecture topology, and evaluate the necessity of a Phase 0 (Technical Inception).
---

# Stage 2: Technical Architecture & Risk Skill

This skill guides the solutions architecture analysis, evaluation of integration risks, non-functional requirements (NFRs), and the formal gating decision for a **Phase 0 Technical Inception**.

---

## 1. Core Principles

1. **Anti-Corruption Layer (ACL) Isolation**:
   - Never allow legacy ERP models or database schemas to leak into the modern core domain.
   - Always encapsulate external integration points inside dedicated ACL services with asynchronous queues (BullMQ, RabbitMQ, SQS).
2. **Defensive Red Flag Auditing**:
   - Legacy systems are guilty until proven innocent. Absence of staging sandboxes, lack of API documentation, or direct SQL read/writes must be flagged as **High/Critical Red Flags**.
3. **Phase 0 (Technical Inception) Gate**:
   - When integration uncertainty exceeds 30%, committing to a fixed delivery schedule is engineering malpractice. A 2 to 4-week Technical Inception must be mandated.

---

## 2. Execution Runbook

1. **Ingest Handoff 1**: Review the Scope Baseline and identify all external integration touchpoints.
2. **Audit Technical Red Flags**: Evaluate legacy ERPs, APIs, data volume, and regulatory constraints (LGPD/GDPR/PCI).
3. **Formulate Macro Architecture Topology**:
   - Frontend: Framework, rendering strategy (SSR/SPA), state management.
   - Backend: Modular monolith vs microservices, async worker topology.
   - Persistence: Relational DB (PostgreSQL), caching (Redis), search/analytics.
   - DevSecOps: Cloud provider, containerization, IaC, CI/CD, observability.
4. **Issue Phase 0 Verdict**: Evaluate against inception criteria and specify duration, team, and deliverables.
5. **Emit Handoff 2**: Pass `Handoff 2: Tech Foundation & Risks` to Stage 3.
