---
name: discovery-proposal-orchestrator
description: >-
  Use this skill to orchestrate the end-to-end multi-agent pre-sales engineering pipeline from raw discovery notes, meeting transcripts, or client briefs into a comprehensive technical-commercial pre-proposal dossier (DOSSIE_TECNICO_PRE_PROPOSTA.md). Strictly enforces the 5-stage DAG with contextual handoff, anti-hallucination protocols, and zero slide generation.
---

# Discovery-to-Proposal Orchestrator Skill

This skill orchestrates the end-to-end multi-agent pre-sales engineering pipeline, transforming raw, messy discovery notes and transcripts into an exhaustive, highly structured, analytical technical-commercial pre-proposal dossier (`DOSSIE_TECNICO_PRE_PROPOSTA.md`).

---

## 1. Pipeline Architecture (Directed Acyclic Graph)

The pipeline executes as a deterministic 5-stage DAG with contextual handoff:

```
[Raw Discovery Input]
       │
       ▼
[Stage 1: Problem & Scope Alignment] ──► Handoff 1: Scope Baseline
       │
       ▼
[Stage 2: Tech Architecture & Risk]  ──► Handoff 2: Tech Foundation & Risks
       │
       ▼
[Stage 3: Engineering Estimator]     ──► Handoff 3: Effort Model
       │
       ▼
[Stage 4: Agile Delivery & Staffing] ──► Handoff 4: Delivery Plan
       │
       ▼
[Stage 5: Commercial Governance]     ──► Handoff 5: Commercial Strategy
       │
       ▼
[Lead Orchestrator Synthesizer]      ──► DOSSIE_TECNICO_PRE_PROPOSTA.md
                                        (Validated via validate_dossier.py)
```

---

## 2. Ingestion & Quality Validation Phase

When raw notes or a discovery transcript are provided:

1. **Intake Screening**:
   - Check if the text contains client context, business problems, target features, or technical constraints.
   - If notes are incomplete or ambiguous, **do not halt or hallucinate**. Instead, populate the **Risk & Unknowns Register** and mandate an Inception Spike.

2. **Strict Negative Invariant Check**:
   - Ensure the final output is **NOT** a slide deck, pitch deck, or superficial bullet outline.
   - Enforce dense executive markdown with comprehensive explanations, trade-offs, and technical grounding.

---

## 3. Step-by-Step DAG Execution Procedure

### Stage 1: Problem & Scope Alignment
- Activate `stage1-problem-scope-alignment`.
- Extract core business objectives, quantifiable KPIs, and North Star metrics.
- Build the **Delimitation Matrix: Core In-Scope vs. Explicit Out-of-Scope**.
- Emit `Handoff 1: Scope Baseline`.

### Stage 2: Technical Architecture & Risk Audit
- Activate `stage2-tech-architecture-risk` using `Handoff 1`.
- Audit integration points (legacy ERPs, undocumented APIs, data security/LGPD).
- Recommend macro architecture topology (Frontend, Backend, ACL, DB, Cloud, Observability).
- Evaluate criteria for **Phase 0 (Technical Inception)** and deliver formal verdict.
- Emit `Handoff 2: Tech Foundation & Risks`.

### Stage 3: Engineering Estimation (T-Shirt & Analogy)
- Activate `stage3-macro-engineering-estimator` using `Handoffs 1 & 2`.
- Decompose scope into 5 to 8 functional and technical macro-epics.
- Apply analogy T-shirt sizing (S, M, L, XL) with three-point estimates ($O, M, P$).
- Calculate uncertainty risk buffers (+20% to +40%) based on Stage 2 Red Flags.
- Emit `Handoff 3: Effort Model`.

### Stage 4: Agile Delivery & Staffing
- Activate `stage4-squad-allocation-milestones` using `Handoffs 1, 2 & 3`.
- Size the squad topology (Tech Lead, Senior/Mid Devs, QA/SDET, Designer, PM).
- Apply the mandatory **75% to 80% effective utilization factor** (30-32 productive hours/week/dev).
- Structure the macro calendar schedule around tangible milestones (M0 to M4) with clear exit criteria.
- Emit `Handoff 4: Delivery Plan`.

### Stage 5: Commercial Governance & Risk Mitigation
- Activate `stage5-commercial-governance-risk` using `Handoffs 1 to 4`.
- Recommend the optimal contract engagement model (Dedicated Squad, T&M, Fixed Scope, Paid Inception).
- Draft the Change Request (CR) governance framework and threshold.
- Define client UAT homologation SLAs with an ironclad **Tacit Acceptance Clause** (5 business days).
- Assemble internal pricing support rationale.
- Emit `Handoff 5: Commercial Strategy`.

### Final Synthesis & Verification
- Assemble all chapters into `DOSSIE_TECNICO_PRE_PROPOSTA.md` following `resources/dossier_master_template.md`.
- Run automated audit:
  ```bash
  python3 /Users/danmodan/.gemini/config/plugins/discovery-to-proposal-engine-plugin/skills/discovery-proposal-orchestrator/scripts/validate_dossier.py DOSSIE_TECNICO_PRE_PROPOSTA.md
  ```
- Output the verified dossier to the user.
