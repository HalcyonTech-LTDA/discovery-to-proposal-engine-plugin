# Staffing Topology, Utilization Modeling & Milestone Sequencing

## 1. Squad Composition Archetypes

| Project Complexity Profile | Recommended Squad Composition | Total FTE | Ideal For |
| :--- | :--- | :---: | :--- |
| **Standard B2B MVP** | 1.0 Tech Lead + 1.0 Mid Full-Stack + 0.5 QA + 0.5 UX + 0.5 PM | **3.5 FTE** | Green-field web applications with standard SaaS APIs. |
| **Enterprise / Legacy Integration** | 1.0 Tech Lead + 1.0 Senior Backend + 1.0 Mid Full-Stack + 0.5 QA/SDET + 0.5 UX + 0.5 PM | **4.5 FTE** | Projects integrating with ERPs (SAP, TOTVS), complex state machines. |
| **High-Scale Platform** | 1.0 Tech Lead + 2.0 Senior Backend + 1.0 Senior Frontend + 1.0 SDET + 0.5 UX + 0.5 PM | **6.0 FTE** | High throughput (>1,000 req/s), distributed microservices, strict security. |

---

## 2. Productivity & Utilization Math

$$\text{Nominal Hours/Month per Dev} = 40 \text{ hrs/week} \times 4 \text{ weeks} = 160 \text{ hours}$$
$$\text{Effective Productive Hours/Month (80% factor)} = 160 \times 0.80 = \mathbf{128 \text{ hours}}$$

### Why 80% is the Industry Ceiling:
- Scrum Ceremonies (Sprint Planning, Daily Standup, Review, Retrospective): ~4 hrs/week
- Code Review & Pull Request iterations: ~3 hrs/week
- Technical Alignment, Architectural Decision Records (ADRs), Environment Setup: ~1 hr/week
- Total non-coding essential engineering activities: ~8 hrs/week (20% of capacity).

---

## 3. Standard Delivery Milestones Framework

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        DELIVERY MILESTONES (M0 - M4)                   │
├────────────────────────────────────────────────────────────────────────┤
│ M0: Inception & Setup        (Weeks 1 - 3)   IaC, Repos, ERP Spike     │
│ M1: Core MVP                 (Weeks 4 - 7)   Auth, Schema, Core Flow   │
│ M2: Integrations & Logic     (Weeks 8 - 11)  ERP Sync, Dashboards      │
│ M3: Hardening & UAT          (Weeks 12 - 14) k6 Load, Pen-test, UAT    │
│ M4: Cutover & Hypercare      (Weeks 15 - 16) Go-Live, 10-day Assisted  │
└────────────────────────────────────────────────────────────────────────┘
```
