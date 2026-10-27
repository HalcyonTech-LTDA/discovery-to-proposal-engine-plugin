# Scope Delimitation & Anti-Scope Creep Guide

## 1. The Anatomy of Scope Creep
Scope creep in software consulting does not happen suddenly; it occurs through ambiguous pre-sales boundaries. Phrases like *"the system should manage users"*, *"integrate with ERP"*, or *"support notifications"* hide thousands of hours of unbudgeted work.

---

## 2. Standard Exclusions Checklist (Mandatory Out-of-Scope Candidates)

Always audit discovery notes against these classic scope traps and push them to **Explicit Out-of-Scope** unless explicitly budgeted:

1. **Legacy Data Cleansing**:
   - *In-Scope*: Automated migration of active schema-validated records via programmatic script.
   - *Out-of-Scope*: Manual data entry, resolving duplicate records in historical data, migrating unindexed archives older than 12 months.
2. **Third-Party Licensing & Infrastructure Costs**:
   - *In-Scope*: Infrastructure as Code (IaC) templates and configuration.
   - *Out-of-Scope*: Direct cloud provider billing (AWS/Azure/GCP), external API license fees (e.g. OpenAI, Twilio, SendGrid), ERP vendor integration fees.
3. **Multi-Platform Proliferation**:
   - *In-Scope*: Highly responsive, modern Web application (Desktop + Tablet).
   - *Out-of-Scope*: Native iOS and Android app development, App Store submission management, biometric hardware integration.
4. **No-Code / Dynamic Rule Engines**:
   - *In-Scope*: Structured business logic defined in code and configured via database parameters.
   - *Out-of-Scope*: Drag-and-drop workflow visual editors, custom end-user formula builders.
5. **Legacy System Refactoring**:
   - *In-Scope*: Writing Anti-Corruption Layer (ACL) adapters to communicate with legacy APIs.
   - *Out-of-Scope*: Fixing bugs, refactoring stored procedures, or tuning database indexes inside the client's legacy systems.

---

## 3. Delimitation Matrix Format Example

```markdown
| Scope Domain | In-Scope (Mandatory Delivery) | Explicit Out-of-Scope (Excluded) | Business & Engineering Rationale |
| :--- | :--- | :--- | :--- |
| **Identity & IAM** | SSO via SAML 2.0 / Azure AD with 3 predefined roles (Admin, Manager, Operator). | Custom customer registration, social OAuth logins, self-service password reset via SMS. | Corporate enterprise application; identity managed centrally via corporate IdP. |
| **Notification Engine**| Automated transactional email alerts via SendGrid API for 4 critical state events. | Push notifications to mobile, in-app bell notification center, SMS dispatch gateway. | Email covers 100% of regulatory alerting needs for v1; avoids WebSocket overhead. |
```
