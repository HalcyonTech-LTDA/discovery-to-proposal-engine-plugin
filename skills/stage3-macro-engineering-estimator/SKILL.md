---
name: stage3-macro-engineering-estimator
description: >-
  Use this skill to decompose In-Scope requirements into 5 to 8 functional macro-epics, apply analogy and T-shirt sizing (S, M, L, XL), and calculate 3-point PERT effort with explicit uncertainty risk buffers (+20% to +40%).
---

# Stage 3: Engineering Estimator Skill (Analogy & T-Shirt Sizing)

This skill guides the functional decomposition of approved In-Scope requirements into 5 to 8 macro-epics, the application of calibrated T-shirt sizing grounded in industry software benchmarks, and the calculation of statistical three-point effort ranges with explicit risk contingency buffers.

---

## 1. Core Principles

1. **Macro-Epic Granularity (5 to 8 Epics)**:
   - Avoid two extremes: 1 single massive epic (no visibility) or 50 micro-user-stories (false precision in pre-sales).
   - Group the entire delivery into 5 to 8 coherent functional and technical macro-epics.
2. **Analogy-Based T-Shirt Sizing**:
   - Compare requested features against standard industry reference implementations (S, M, L, XL).
3. **Calibrated Uncertainty Buffers**:
   - No engineering estimate is a single deterministic number.
   - Ground estimates in three-point PERT modeling:
     $$E = \frac{O + 4M + P}{6}$$
   - Apply explicit risk multipliers (+15% to +40%) derived from the technical red flags audited in Stage 2.

---

## 2. Execution Runbook

1. **Ingest Handoffs 1 & 2**: Read the Scope Matrix and the Architecture & Red Flags report.
2. **Formulate 5 to 8 Macro-Epics**: Define clear boundaries, drivers, and dependencies for each epic.
3. **Assign T-Shirt Sizes**: Label each epic as S, M, L, or XL with detailed technical justification.
4. **Calculate Three-Point Sprint Ranges**: Establish Optimistic ($O$), Most Likely ($M$), and Pessimistic ($P$) developer-sprint values.
5. **Apply Risk Buffers**: Calculate final buffered developer-sprints and convert to nominal hours.
6. **Identify Critical Path**: Pinpoint the epics with highest variance and dependency concentration.
7. **Emit Handoff 3**: Pass `Handoff 3: Effort Model` to Stage 4.
