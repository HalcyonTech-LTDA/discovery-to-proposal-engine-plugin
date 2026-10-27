# Anti-Hallucination & Risk Policy in Pre-Sales Engineering

## 1. The Core Hazard: Silent Hallucination in Proposals
In commercial software pre-sales, ungrounded assumptions lead to disastrous fixed-price defaults, project cost overruns, and catastrophic margin collapse. Common client omissions include:
- Unspecified database versions, schemas, or transaction volumes.
- Undocumented legacy ERP protocols (e.g., SOAP XML vs. direct SQL).
- Absence of test or sandbox environments.
- Unspecified authentication mechanisms (e.g., Azure AD vs. Okta vs. custom DB).
- Vague compliance requirements (e.g., "must be secure and compliant").

---

## 2. Mandatory Omission Handling Protocol

When an agent encounters an omitted or ambiguous requirement:

1. **PROHIBITION**:
   - **DO NOT** fabricate a specific technical number, protocol, or timeline as if it were confirmed by the client.
   - **DO NOT** assume optimistic conditions (e.g., "We assume modern REST APIs exist with 100% Swagger coverage").

2. **MANDATORY ACTIONS**:
   - **Log in the Risk & Unknowns Register**: Explicitly flag the omission with a Risk ID, describing what was requested, what was omitted, and the technical impact.
   - **Formulate a Grounded Working Assumption**: Clearly label the assumption:
     > *"Working Assumption for Estimation: Assumed TOTVS SOAP 1.2 interface with staging environment access by Week 2. If direct database query is required, effort will increase by 25%."*
   - **Prescribe a Phase 0 Discovery Spike**: Recommend an architectural spike during Phase 0 Inception to test and validate the item.
   - **Inject Calibrated Uncertainty Buffer**: Scale the epic's uncertainty buffer (+25% to +40%) to ensure commercial safety.

---

## 3. Severity Matrix for Technical Red Flags

| Severity | Definition | Mandatory Pre-Sales Action |
| :--- | :--- | :--- |
| **CRITICAL** | Core blocker (e.g., legacy ERP write-back without API, missing sandbox, conflicting data schemas). | Mandate Phase 0 Paid Inception; reject fixed-price commitment on integration epic. |
| **HIGH** | Major risk (e.g., strict sub-second SLA with unverified distributed queries, PII data residency). | Add +35% uncertainty buffer; require dedicated architecture ADR spike in Milestone 0. |
| **MEDIUM** | Standard third-party dependency (e.g., payment gateway, SMS/email SaaS API). | Add +20% buffer; implement circuit breaker pattern in architecture. |
| **LOW** | Well-established internal feature (e.g., CRUD tables, standard OAuth 2.0). | Standard +10% to +15% sprint contingency. |
