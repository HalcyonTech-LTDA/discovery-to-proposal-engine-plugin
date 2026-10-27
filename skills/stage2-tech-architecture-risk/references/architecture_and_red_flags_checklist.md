# Technical Architecture & Red Flags Checklist

## 1. Legacy ERP & Enterprise System Integration Checklist

| Integration Area | Potential Hazard | Recommended Architectural Mitigation |
| :--- | :--- | :--- |
| **Direct Database Reads/Writes** | Schema lock-in, table locks, corrupted ERP state, bypassed business logic. | **STRICT PROHIBITION**: Require vendor-supported APIs or intermediate staging table / CDC pipeline. |
| **Legacy SOAP / XML APIs** | Slow serialization, brittle schema changes, poor error messages, timeout spikes. | Wrap in an asynchronous adapter worker with exponential backoff and BullMQ / Redis queues. |
| **Absence of Staging Sandbox** | Inability to test without mutating live production ERP data. | Mandate Phase 0 spike: client IT must provide mock sandbox or sanitized staging snapshot. |
| **Rate Limiting & Concurrency** | Legacy ERP crashes under high concurrent API calls. | Implement token bucket rate limiter in API Gateway and queue writes asynchronously. |

---

## 2. Security, Compliance & LGPD Checklist

1. **PII Data Isolation**:
   - Ensure personal data (CPF, email, phone, salary) is encrypted at rest using AES-256 via Cloud KMS keys.
   - Implement automated audit logging for all PII access (actor, timestamp, IP, accessed record).
2. **Authentication & Authorization**:
   - Prefer enterprise OpenID Connect / SAML 2.0 (Azure AD, Okta, Google Workspace) over custom auth.
   - Enforce fine-grained Role-Based Access Control (RBAC) at the API Gateway and service layer.
3. **Data Residency & Backup**:
   - Specify cloud region explicitly (e.g. AWS `sa-east-1` São Paulo for Brazilian LGPD compliance).
   - Define backup retention (daily snapshots, 30-day retention, cross-region replication).

---

## 3. Phase 0 (Technical Inception) Decision Matrix

| Condition Present in Discovery | Phase 0 Mandatory? | Key Phase 0 Deliverable |
| :--- | :--- | :--- |
| Legacy ERP integration undocumented or unverified | **YES (MANDATORY)** | Working PoC adapter script connecting to client test environment |
| Client IT has not confirmed cloud accounts or access | **YES (MANDATORY)** | Terraform IaC bootstrap and security sign-off |
| Architecture uses standard modern REST APIs with docs | **NO (STANDARD)** | Proceed directly to Milestone 1 with setup in Milestone 0 |
| Project requires custom distributed streaming or ML | **YES (MANDATORY)** | Performance benchmark and data pipeline PoC |
