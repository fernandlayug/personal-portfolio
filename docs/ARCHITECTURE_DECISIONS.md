# Personal Portfolio Assistant — Architecture Decisions

This document records important architectural decisions that should remain stable unless explicitly changed.

---

## ADR-001 — Multi-Tenant SaaS

**Decision:** The platform will use a multi-tenant architecture.

Each tenant owns isolated portfolio information and settings.

**Reason:** The platform is intended to support multiple independent professional portfolios.

---

## ADR-002 — Tenant Data Isolation

**Decision:** Portfolio management operations must be tenant-scoped.

Views must obtain the current tenant/profile and query records through that tenant relationship.

**Reason:** Prevent unauthorized cross-tenant access.

---

## ADR-003 — MySQL for Structured Information

**Decision:** MySQL is the primary database for structured portfolio information.

**Reason:** Portfolio entities such as education, experience, skills, projects, certificates, research, licenses, awards, and professional memberships are relational structured data.

---

## ADR-004 — User-Owned Cloud Storage

**Decision:** Professional documents are intended to reside in the tenant's connected Google Drive or OneDrive.

**Reason:** The architecture separates structured application data from user-controlled professional documents.

**Boundary:** Cloud storage integration is a future phase and is not implemented as part of Phase 3 portfolio CRUD.

---

## ADR-005 — Storage Abstraction

**Decision:** Cloud storage access will use an abstraction layer.

**Reason:** Portfolio features should not be tightly coupled to one cloud provider.

---

## ADR-006 — Supporting Documents Are a Separate Domain

**Decision:** Portfolio records may eventually have multiple associated supporting documents, but Phase 3 will not implement file upload or binary document storage.

Examples include:

- Award → Certificate of Award
- Professional Membership → Certificate of Membership
- Research → Research Paper/PDF

**Reason:** A portfolio record may require more than one supporting artifact, and document lifecycle management is sufficiently distinct to warrant its own phase.

**Phase boundary:** Document records and upload/management workflows belong to Phase 5. Cloud storage providers belong to Phase 6.

---

## ADR-007 — Engagement and Professional Membership Are Distinct

**Decision:** Professional Memberships must not be treated as Engagement Management records.

A Professional Membership represents a professional affiliation/credential. Engagement Management is a separate domain whose exact model and scope must be established during Phase 4.

**Reason:** Combining the two concepts would create incorrect domain modeling and could cause Phase 4 scope to be inferred from an unrelated portfolio domain.

---

## ADR-008 — Sensitive Identifiers Are Private by Default

**Decision:** Sensitive portfolio identifiers such as `license_number` and `membership_number` are private by default.

**Reason:** Storage in the tenant's private portfolio database does not imply public disclosure.

Future public portfolio and public AI functionality must use explicit public-data/visibility approval rather than automatically exposing all portfolio fields.

---

## ADR-009 — Human Verification of AI Extraction

**Decision:** AI-extracted information requires appropriate human verification before becoming trusted structured portfolio data.

**Reason:** AI extraction may contain errors and should not silently overwrite authoritative information.

---

## ADR-010 — Public AI Is Opt-In

**Decision:** Public AI is disabled by default and must be explicitly enabled by the tenant.

**Reason:** Public access must not expose private portfolio information.

---

## ADR-011 — Phase-Based Development

**Decision:** Development follows the approved 12-phase roadmap.

**Reason:** Prevent scope creep and accidental implementation of future functionality.

---

## ADR-012 — GitHub as Code Source of Truth

**Decision:** The GitHub repository is the source of truth for committed project code.

**Repository:** `fernandlayug/personal-portfolio`

**Reason:** This provides version control, synchronization, rollback, and a stable project baseline.

---

## ADR-013 — Existing UI Architecture

**Decision:** Existing Django templates and CSS conventions will be reused for management interfaces.

**Reason:** Maintain consistency and avoid unnecessary UI framework changes.

---

## ADR-014 — Research Documents Are Deferred

**Decision:** Research CRUD is implemented in Phase 3, but Research PDF/document attachment functionality is deferred to Phase 5.

**Reason:** Document management is a separate roadmap capability and should not be pulled into Phase 3.

---

## ADR-015 — Phase 3 Structured Portfolio Scope

**Decision:** Phase 3 includes the following structured portfolio domains:

- Profile
- Education
- Work Experience
- Skills
- Projects
- Certificates
- Research
- Licenses
- Awards
- Professional Memberships

**Reason:** These domains constitute the approved structured portfolio-management baseline before Engagement Management begins.

---

# Change Control

An architectural decision should only be changed intentionally.

When an architectural decision changes:

1. Update this document.
2. Record the reason.
3. Update affected architecture documentation.
4. Update the roadmap or project status where applicable.
5. Record the change in the changelog.
