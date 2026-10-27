# Analogy & T-Shirt Sizing Models in Pre-Sales Engineering

## 1. T-Shirt Size Benchmark Reference Table

*(Calibrated for a pair of mid/senior engineers working in standard 2-week sprints)*

| T-Shirt Size | Developer-Sprints | Gross Dev-Hours | Typical Functional Complexity | Real-World Software Analogies |
| :---: | :---: | :---: | :--- | :--- |
| **S** (Small) | 1 - 2 sprints | 80 - 160 hrs | Low complexity, standard CRUD, zero external blockers, standard UI components. | User profile settings, standard email dispatch, static configuration tables, read-only audit log viewer. |
| **M** (Medium) | 3 - 5 sprints | 240 - 400 hrs | Moderate complexity, custom business rules, 1 standard 3rd-party SaaS API, intermediate data transforms. | Customer onboarding checkout flow, Stripe webhook integration, operational dashboard with charts, CSV import parser. |
| **L** (Large) | 6 - 8 sprints | 480 - 640 hrs | High complexity, state machine transitions, asynchronous task pipelines, non-standard enterprise security. | Multi-level order approval workflow, real-time telemetry stream, complex pricing calculator, federated SAML/Azure AD setup. |
| **XL** (Extra-Large)| 9 - 12 sprints| 720 - 960 hrs | Critical architectural risk, legacy ERP synchronization, distributed transactions, zero docs. | Bi-directional SAP/TOTVS order & inventory sync, legacy data migration with reconciliation, custom billing engine. |

---

## 2. Risk Buffer Calibration Matrix

| Technical Risk Factor Identified | Uncertainty Multiplier | Justification |
| :--- | :---: | :--- |
| **Modern REST API with Sandbox** | **+10% to +15%** | Minor schema shifts, standard bug remediation cycles. |
| **New Domain / Complex Logic** | **+20% to +25%** | Edge cases discovered during edge-testing and demo iterations. |
| **Legacy ERP / SOAP Integration** | **+30% to +35%** | Network latency, schema mismatches, vendor API downtime. |
| **Undocumented API / No Sandbox** | **+35% to +45%** | Severe reverse-engineering friction, mock building required. |

---

## 3. Mathematical Conversion Formula

$$\text{PERT Expected Effort } (E) = \frac{O + 4M + P}{6}$$
$$\text{Buffered Effort } (E_{\text{buffered}}) = E \times (1 + \text{Risk Buffer})$$
$$\text{Nominal Gross Hours} = E_{\text{buffered}} \times 80 \text{ hours/sprint}$$
