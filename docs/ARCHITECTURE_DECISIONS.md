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

**Reason:** Portfolio entities are relational structured data.

---

## ADR-004 — User-Owned Cloud Storage

**Decision:** Professional documents are intended to reside in the tenant's connected Google Drive or OneDrive.

**Reason:** The architecture separates structured application data from user-controlled professional documents.

**Boundary:** Cloud storage integration is a future phase and is not implemented as part of Phase 3 or Phase 4 portfolio CRUD.

---

## ADR-005 — Storage Abstraction

**Decision:** Cloud storage access will use an abstraction layer.

**Reason:** Portfolio features should not be tightly coupled to one cloud provider.

---

## ADR-006 — Supporting Documents Are a Separate Domain

**Decision:** Portfolio records may eventually have multiple associated supporting documents, but Phase 3 and Phase 4 will not implement local file upload or binary document storage.

Examples include:

- Award → Certificate of Award
- Professional Membership → Certificate of Membership
- Research → Research Paper/PDF
- Engagement → Supporting Evidence

**Reason:** Supporting artifacts have their own lifecycle and may support multiple portfolio records.

**Phase boundary:** Document records and upload/management workflows belong to Phase 5. Cloud storage providers belong to Phase 6.

---

## ADR-007 — Engagement and Professional Membership Are Distinct

**Decision:** Professional Memberships must not be treated as Engagement Management records.

A Professional Membership represents a professional affiliation/credential. A Professional Engagement represents meaningful professional involvement undertaken by the portfolio owner.

Mere attendance or passive participation in an event does not constitute a Professional Engagement.

**Reason:** Combining the two concepts would create incorrect domain modeling and would turn Engagement into an activity log.

---

## ADR-008 — Sensitive Identifiers Are Private by Default

**Decision:** Sensitive portfolio identifiers such as `license_number` and `membership_number` are private by default.

**Reason:** Storage in the tenant's private portfolio database does not imply public disclosure.

Future public portfolio and public AI functionality must use explicit public-data/visibility approval.

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

**Decision:** The GitHub repository is the source of truth for committed project code and project documentation.

**Repository:** `fernandlayug/personal-portfolio`

**Reason:** This provides version control, synchronization, rollback, and a stable project baseline.

---

## ADR-013 — Existing UI Architecture

**Decision:** Existing Django templates and CSS conventions will be reused for management interfaces.

**Reason:** Maintain consistency and avoid unnecessary UI framework changes.

---

## ADR-014 — Research Documents Are Deferred

**Decision:** Research CRUD is implemented in Phase 3, but Research PDF/document attachment functionality is deferred to Phase 5.

**Reason:** Document management is a separate roadmap capability and should not be pulled into portfolio CRUD phases.

---

## ADR-015 — Phase 3 Structured Portfolio Scope

**Decision:** Phase 3 includes:

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

**Reason:** These domains constitute the approved structured portfolio-management baseline before Engagement Management.

---

## ADR-016 — Professional Engagement Is a First-Class Portfolio Domain

**Decision:** Professional Engagement is an independent first-class portfolio domain representing meaningful professional involvement.

Engagement does not require a Project, Research record, Membership, Organization, Event, Certificate, Award, or Evidence relationship in order to exist.

**Reason:** Engagement captures professional involvement that has standalone portfolio value and is not adequately represented by an existing domain.

**Boundary:** Website/user engagement analytics remain a separate future Platform Engagement/Analytics concept.

---

## ADR-017 — Engagement Type and Role Are Distinct

**Decision:** Engagement Type describes the nature of the professional involvement, while Role describes the responsibility/capacity of the portfolio owner.

Initial Engagement Types include Speaking & Training, Academic & Research Service, Professional Service & Leadership, Collaboration, Technical Advisory & Evaluation, Professional Representation, Advising & Mentoring, Community & Stakeholder Engagement, and Other Professional Engagement.

An Engagement has one or more Roles with exactly one Primary Role.

**Reason:** This prevents taxonomy explosion and accurately represents multi-role professional activities.

---

## ADR-018 — Shared Portfolio Context for Organizations and Events

**Decision:** Organizations and Events are tenant-owned, reusable portfolio-context entities designed for reuse across Engagements and future portfolio domains.

Organization is a generalized professional/academic/institutional/etc. entity rather than a Company-only or employment-only entity. Event is a reusable occurrence distinct from Engagement.

Organizations may have zero or more classifications. Organization classification describes what the organization is; an Engagement Organization relationship role describes how that organization relates to the Engagement.

An Engagement may relate to zero or one Event. An Event may relate to many Engagements and may exist independently.

**Reason:** Reusable context avoids duplicate organization/event records while keeping Engagement activity-centric. This is shared portfolio infrastructure, not CRM or event-management functionality.

**Boundary:** There is no global organization directory, Person/Contact CRM, participant management, event registration, ticketing, attendance management, scheduling engine, or recurring event system in Phase 4.

---

## ADR-019 — Explicit Semantic Engagement Relationships

**Decision:** Engagement relationships are explicit and tenant-scoped rather than represented through a generic relationship mechanism.

Approved relationships:

- Engagement ↔ Organization: M:N, with a semantic Organization Relationship Role
- Engagement → Event: 0..1
- Engagement ↔ Project: M:N
- Engagement ↔ Research: M:N
- Engagement ↔ Professional Membership: M:N
- Engagement ↔ Work Experience: M:N
- Engagement ↔ Skills: M:N
- Engagement ↔ Education: M:N
- Engagement ↔ Certificate: M:N
- Engagement ↔ Award: M:N
- Engagement ↔ Evidence: M:N

All relationships are optional. Only Organization relationships require relationship-specific role semantics initially. Evidence may later receive a simple purpose classification.

**Reason:** Explicit semantics prevent ambiguous generic relationships and preserve domain meaning.

---

## ADR-020 — Evidence Is Reusable Supporting Context

**Decision:** Evidence is information or a resource that substantiates, verifies, or provides supporting context for an Engagement and may eventually support other portfolio domains.

Evidence is broader than a document and may represent certificates, letters, official announcements, email correspondence, photos, external URLs, reviewer records, participant outputs, and other substantiating resources.

Evidence visibility is independent from Engagement visibility.

**Reason:** A single evidence item may substantiate multiple records, and evidence may have different privacy requirements from the portfolio record it supports.

**Boundary:** Phase 4 implements evidence metadata/relationships only. Actual document management is Phase 5 and cloud storage is Phase 6.

---

## ADR-021 — Engagement Lifecycle and Dates

**Decision:** Engagement status is independent from dates.

Initial statuses:

- Draft
- Planned
- Ongoing
- Completed
- Cancelled
- Postponed

Start Date and End Date are independently optional. If both are supplied, End Date must not precede Start Date.

Upcoming/Past are derived presentation states, not stored statuses. Declined is not an Engagement status.

**Reason:** This supports planned, ongoing, completed, cancelled, postponed, single-day, multi-day, and open-ended engagements without conflating scheduling with lifecycle.

---

## ADR-022 — Engagement Visibility and Controlled Public Projection

**Decision:** Engagement visibility is independently tenant-controlled with initial states Private, Public, and Unlisted. New Engagements are private by default.

Visibility does not automatically propagate to related Organizations, Events, Projects, Research, Memberships, Certificates, Awards, or Evidence.

Draft Engagements are never publicly presented regardless of configured visibility. Featured is independent from visibility.

Public presentation must use a controlled public projection rather than unrestricted relationship traversal. The precise direct-access behavior of Unlisted remains a later presentation refinement.

Public Engagement visibility does not imply Public AI eligibility.

**Reason:** Prevent accidental disclosure of private related information while allowing controlled public portfolio presentation.

---

## ADR-023 — Tenant-Aware Configurable Taxonomies

**Decision:** Engagement Type, Engagement Role, Organization Classification, and Tags are tenant-aware configurable taxonomy records rather than permanently hard-coded business choices.

The implementation may provide system-defined defaults while allowing tenant-specific configuration. System defaults and tenant-defined values must remain distinguishable, and configuration must not become an unrestricted generic framework.

Event Type may remain a controlled choice initially because its purpose is simpler and does not require the same taxonomy-management behavior.

**Reason:** A SaaS platform must support extensibility while preserving controlled domain semantics.

---

## ADR-024 — Phase 4 Scope Boundary

**Decision:** Phase 4 covers Professional Engagement Management, reusable Organization/Event context, Evidence metadata/relationships, configurable Engagement taxonomies, portfolio relationships, CRUD workflows, tenant isolation, visibility, and controlled public projection.

Phase 4 does not implement:

- Document Management
- Local file/binary storage
- Google Drive
- OneDrive
- OCR
- Intelligent document extraction
- AI/RAG
- Resume/CV generation
- Public AI
- PWA/Mobile expansion
- Production hardening
- CRM/Contacts
- Event management
- Website/user engagement analytics

**Reason:** Preserve the approved phase boundaries and prevent scope creep.

---

# Change Control

An architectural decision should only be changed intentionally.

When an architectural decision changes:

1. Update this document.
2. Record the reason.
3. Update affected architecture documentation.
4. Update the roadmap or project status where applicable.
5. Record the change in the changelog.
