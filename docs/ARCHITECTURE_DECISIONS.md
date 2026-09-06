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

**Reason:** Portfolio entities such as education, experience, skills, projects, certificates, and research are relational structured data.

---

## ADR-004 — User-Owned Cloud Storage

**Decision:** Professional documents are intended to reside in the tenant's connected Google Drive or OneDrive.

**Reason:** The architecture separates structured application data from user-controlled professional documents.

---

## ADR-005 — Storage Abstraction

**Decision:** Cloud storage access will use an abstraction layer.

**Reason:** Portfolio features should not be tightly coupled to one cloud provider.

---

## ADR-006 — Engagement to Evidence Relationship

**Decision:** Future engagement records may have multiple associated evidence documents.

**Reason:** Professional engagements may require multiple supporting documents.

---

## ADR-007 — Human Verification of AI Extraction

**Decision:** AI-extracted information requires appropriate human verification before becoming trusted structured portfolio data.

**Reason:** AI extraction may contain errors and should not silently overwrite authoritative information.

---

## ADR-008 — Public AI Is Opt-In

**Decision:** Public AI is disabled by default and must be explicitly enabled by the tenant.

**Reason:** Public access must not expose private portfolio information.

---

## ADR-009 — Phase-Based Development

**Decision:** Development follows the approved 12-phase roadmap.

**Reason:** Prevent scope creep and accidental implementation of future functionality.

---

## ADR-010 — GitHub as Code Source of Truth

**Decision:** The GitHub repository is the source of truth for committed project code.

**Repository:** `fernandlayug/personal-portfolio`

**Reason:** This provides version control, synchronization, rollback, and a stable project baseline.

---

## ADR-011 — Existing UI Architecture

**Decision:** Existing Django templates and CSS conventions will be reused for management interfaces.

**Reason:** Maintain consistency and avoid unnecessary UI framework changes.

---

## ADR-012 — Research Documents Are Deferred

**Decision:** Research CRUD is implemented in Phase 3, but Research PDF/document attachment functionality is deferred to Phase 5.

**Reason:** Document management is a separate roadmap capability and should not be pulled into Phase 3.

---

# Change Control

An architectural decision should only be changed intentionally.

When an architectural decision changes:

1. Update this document.
2. Record the reason.
3. Update affected architecture documentation.
4. Update the roadmap or project status where applicable.
5. Record the change in the changelog.
