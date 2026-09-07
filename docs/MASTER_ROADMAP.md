# Personal Portfolio AI Assistant — Master Roadmap

## Project Overview

The Personal Portfolio AI Assistant is a multi-tenant SaaS platform for managing professional portfolio information, professional documents, and future AI-assisted portfolio services.

Each tenant owns an isolated portfolio and its settings. Structured portfolio metadata is stored in MySQL. Actual professional documents, PDFs, images, and other supporting files are designed to reside in the tenant's connected Google Drive or Microsoft OneDrive through a storage abstraction layer.

Development is organized into controlled phases so that portfolio management, engagement management, document management, cloud storage, intelligent processing, AI/RAG, public AI, mobile/PWA capabilities, and production SaaS hardening remain clearly separated.

---

## Phase Status

| Phase | Area | Status |
|---|---|---|
| Phase 1 | Foundation | COMPLETE |
| Phase 2 | Professional Portfolio UI | COMPLETE |
| Phase 3 | Multi-Tenant Portfolio Management | COMPLETE |
| Phase 4 | Engagement Management | CURRENT — ARCHITECTURE LOCKED |
| Phase 5 | Document Management | FUTURE |
| Phase 6 | Cloud Storage Integration | FUTURE |
| Phase 7 | Intelligent Document Processing | FUTURE |
| Phase 8 | AI Assistant & RAG | FUTURE |
| Phase 9 | Resume/CV/Portfolio Generator | FUTURE |
| Phase 10 | Public AI | FUTURE |
| Phase 11 | Advanced PWA/Mobile | FUTURE |
| Phase 12 | Production & SaaS Hardening | FUTURE |

---

# Phase 1 — Foundation — COMPLETE

Completed foundation work includes:

- Django project setup
- MySQL database configuration
- Portfolio application
- Initial portfolio models
- Database migrations
- Django Admin registration and customization
- Initial portfolio data
- Dynamic portfolio homepage
- Basic authentication foundation

---

# Phase 2 — Professional Portfolio UI — COMPLETE

Completed interface work includes:

- Responsive portfolio homepage
- Professional navigation
- Portfolio presentation layout
- Dashboard interface
- Consistent management UI
- Reusable CSS classes and templates
- Responsive management pages for portfolio records

---

# Phase 3 — Multi-Tenant Portfolio Management — COMPLETE

Phase 3 established the core private portfolio-management layer and tenant isolation.

## Portfolio Management Domains

The complete Phase 3 structured portfolio domain set is:

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

These are structured portfolio records stored in MySQL and managed through Django.

## Implemented Capabilities

The implemented portfolio management domains support the appropriate:

- List workflows
- Add workflows
- Edit workflows
- Delete workflows
- Form validation
- Success/error messaging
- Dashboard integration
- Tenant-scoped queries
- Authenticated management access

Ownership is assigned server-side from the authenticated tenant/profile context rather than from submitted form data.

## Phase 3 Completion Gate — CLOSED

- [x] Profile management foundation established
- [x] Education CRUD complete
- [x] Work Experience CRUD complete
- [x] Skills CRUD complete
- [x] Projects CRUD complete
- [x] Certificates CRUD complete
- [x] Research CRUD complete
- [x] Licenses CRUD complete
- [x] Awards CRUD complete
- [x] Professional Membership CRUD complete
- [x] Domain validation implemented where required
- [x] Dashboard integration complete
- [x] Authentication protection applied
- [x] Tenant-scoped queries verified
- [x] Cross-tenant access testing completed
- [x] Supporting-document boundary established
- [x] Privacy boundaries for sensitive identifiers established
- [x] Documentation synchronized

**Phase 3 completion date:** 2026-09-06

---

# Phase 4 — Engagement Management — CURRENT

Phase 4 architecture is established and locked. Implementation begins only after the architecture is translated into the existing Django model/view/form/template conventions.

## Purpose and Definition

Professional Engagement is a first-class portfolio domain representing meaningful professional activity, service, participation, collaboration, leadership, invitation, or other involvement undertaken by the portfolio owner within a defined professional context, where the activity has standalone professional value and is not adequately represented by an existing portfolio domain.

Mere attendance or passive participation in a professional event does not constitute a Professional Engagement.

Professional Memberships remain distinct from Engagements.

Website/user engagement analytics are also distinct and remain a future Platform Engagement/Analytics capability.

## Core Engagement Attributes

Required:

- Title
- Description
- Engagement Type
- One or more Roles
- Exactly one Primary Role
- Status
- Visibility

Optional:

- Start Date
- End Date
- Purpose
- Outcome
- Impact
- Location
- Mode
- Tags
- Featured

System-managed:

- Created At
- Updated At

Description, Purpose, Outcome, and Impact remain distinct narrative attributes.

## Lifecycle

Statuses:

- Draft
- Planned
- Ongoing
- Completed
- Cancelled
- Postponed

Upcoming/Past are derived presentation states. Declined is not an Engagement status.

Start and End dates are independently optional. If both are supplied, End Date must not precede Start Date.

## Configurable Taxonomies

The following are tenant-aware configurable taxonomy records:

- Engagement Type
- Engagement Role
- Organization Classification
- Tags

System-defined defaults may be provided, while tenant-specific values can be configured. System defaults and tenant-defined values must remain distinguishable. This is not a generic unrestricted configuration framework.

Event Type may remain a controlled choice initially.

## Shared Portfolio Context

Organizations and Events are tenant-owned, reusable portfolio-context entities rather than Engagement-only helper records.

Organization represents a professional, academic, institutional, commercial, governmental, nonprofit, community, or other identifiable organization.

Event represents an identifiable professional, academic, institutional, community, or other occurrence and is distinct from Engagement.

An Engagement may relate to zero or one Event. An Event may relate to many Engagements and may exist independently.

Organizations and Events are designed for future reuse across appropriate portfolio domains while Phase 4 implements only the relationships required now.

There is no global organization directory in the initial architecture.

## Engagement Relationships

| Relationship | Cardinality |
|---|---|
| Engagement ↔ Organization | M:N |
| Engagement → Event | 0..1 |
| Engagement ↔ Project | M:N |
| Engagement ↔ Research | M:N |
| Engagement ↔ Professional Membership | M:N |
| Engagement ↔ Work Experience | M:N |
| Engagement ↔ Skills | M:N |
| Engagement ↔ Education | M:N |
| Engagement ↔ Certificate | M:N |
| Engagement ↔ Award | M:N |
| Engagement ↔ Evidence | M:N |

All relationships are optional.

Organization relationships require semantic roles such as Partner, Host, Organizer, Appointing Organization, Collaborating Organization, Sponsor, Client, Beneficiary Organization, Supporting Organization, and Other.

Other portfolio relationships do not initially require relationship-specific roles.

## Evidence Boundary

Evidence is reusable information or a resource that substantiates, verifies, or provides supporting context for an Engagement.

Evidence may include certificates, letters, official announcements, correspondence, photos, reviewer records, external URLs, participant outputs, and other resources.

Evidence visibility is independent from Engagement visibility.

Phase 4 implements Evidence metadata and relationships only. Document Management is Phase 5 and cloud storage is Phase 6.

## Visibility and Public Projection

Initial Engagement visibility states:

- Private
- Public
- Unlisted

New Engagements are private by default.

Draft Engagements are never publicly presented.

Featured is independent from visibility.

Public visibility does not automatically expose related Organizations, Events, Projects, Research, Memberships, Certificates, Awards, or Evidence.

Public presentation must use a controlled public projection rather than unrestricted relationship traversal.

The exact direct-access behavior of Unlisted remains a later presentation refinement.

Public Engagement visibility does not imply Public AI eligibility.

## CRUD and Security

Phase 4 management will provide tenant-scoped Create, Read, Update, and controlled Delete workflows, plus search/filtering, relationship management, visibility controls, and public-safe presentation.

All submitted related-object IDs must be resolved through the current tenant and authorization context. The client must never select tenant ownership.

The established pattern remains:

```text
Authenticated Request
        |
        v
@login_required
        |
        v
verify_current_tenant(request)
        |
        v
Tenant/Profile-scoped Query
        |
        v
Validate Form and Relationships
        |
        v
Save with Server-side Ownership
```

## Explicit Phase 4 Exclusions

Phase 4 does not implement:

- Document Management
- Local file/binary storage
- Google Drive
- OneDrive
- OCR
- Intelligent document extraction
- AI/RAG
- Resume/CV/Portfolio generation
- Public AI
- Advanced PWA/Mobile expansion
- Production/SaaS hardening
- CRM/Contacts/People management
- Event registration
- RSVP
- Ticketing
- Participant management
- Attendance management
- Event scheduling/recurrence
- Website visitor/page-view analytics

---

# Phase 5 — Document Management — FUTURE

Document Management is the dedicated phase for professional documents and supporting evidence.

Planned scope includes:

- Document records
- Document metadata
- Document categorization
- Relationships between documents and portfolio records
- Multiple supporting documents per portfolio record
- Upload and management workflows
- Document lifecycle management

Examples include research papers/PDFs, certificates of award, certificates of membership, and other professional evidence.

---

# Phase 6 — Cloud Storage Integration — FUTURE

Cloud storage will connect the platform to tenant-owned storage providers.

Planned providers include:

- Google Drive
- Microsoft OneDrive

A storage abstraction layer should prevent portfolio business logic from becoming tightly coupled to a specific provider.

---

# Phase 7 — Intelligent Document Processing — FUTURE

Potential capabilities include:

- Text extraction
- PDF processing
- OCR where necessary
- Metadata extraction
- Structured information extraction
- Document classification
- AI-assisted document analysis
- Human verification workflows

---

# Phase 8 — AI Assistant & RAG — FUTURE

Potential capabilities include:

- Portfolio question answering
- Retrieval-Augmented Generation
- Semantic search
- Portfolio-grounded responses
- Owner-only AI access
- Context-aware professional assistance

The AI layer must respect tenant isolation and data/document permissions.

---

# Phase 9 — Resume/CV/Portfolio Generator — FUTURE

Potential capabilities include:

- Resume generation
- CV generation
- Portfolio content generation
- Job-targeted versions
- Structured professional summaries
- Export workflows

---

# Phase 10 — Public AI — FUTURE

Public AI is opt-in.

Public AI must operate only on tenant-approved public information. Private portfolio data must not automatically become available to public users.

---

# Phase 11 — Advanced PWA/Mobile & UI Enhancement — FUTURE

### Objective

Transform the application into a polished, consistent, responsive, accessible, and progressively web-app-oriented SaaS experience while completing the migration of the earlier standalone UI architecture.

### Workstream 11A — UI Architecture Enhancement

The UI Enhancement workstream will modernize and unify the application's presentation architecture.

#### Major Activities

- Complete adoption of `base.html`
- Migrate Phase 1–3 standalone templates
- Standardize dashboard layouts
- Standardize page structures
- Standardize navigation
- Standardize forms
- Standardize validation and error presentation
- Standardize buttons and action patterns
- Standardize cards and list views
- Standardize empty states
- Standardize messages and notifications
- Improve responsive behavior
- Improve accessibility
- Establish reusable template/UI patterns
- Review visual consistency across portfolio domains
- Review UI consistency across tenant-facing SaaS workflows
- Regression test migrated functionality

### Workstream 11B — Advanced PWA/Mobile

The PWA/mobile workstream will build on the unified UI architecture.

#### Major Activities

- Progressive Web App architecture
- Web app manifest
- Service worker
- Installability
- Offline-capable functionality where appropriate
- Mobile-first workflow refinement
- Responsive optimization
- Touch-friendly interactions
- Mobile dashboard experience
- Mobile portfolio management
- Performance optimization
- Appropriate device capabilities where supported

### Phase 11 UI Migration Principle

Phase 11 is the planned application-wide UI enhancement point.

The objective is not simply to convert templates to `base.html`, but to establish a consistent, maintainable, responsive, accessible, and reusable presentation architecture across the entire SaaS platform.

### Phase 11 Boundary

Phase 4 introduces `base.html` for newly developed functionality.

Phase 1–3 templates remain operational until Phase 11.

No broad Phase 1–3 UI migration is required during Phase 4 unless necessary for functionality or security.

### Expected Outcome

By completion of Phase 11:

```text
All major application interfaces
        │
        ▼
Shared template architecture
        │
        ├── Consistent navigation
        ├── Consistent layouts
        ├── Consistent forms
        ├── Consistent components
        ├── Responsive design
        ├── Accessibility
        └── PWA/mobile readiness

---

# Phase 12 — Production & SaaS Hardening — FUTURE

Production hardening will address:

- Deployment
- Environment configuration
- Secrets management
- Security hardening
- Logging
- Monitoring
- Backups
- Tenant-isolation auditing
- Performance
- Reliability
- SaaS operational concerns

---

# Feature Boundary Rules

| Feature | Phase |
|---|---|
| Profile, Education, Work Experience, Skills, Projects | Phase 3 |
| Certificates | Phase 3 |
| Research CRUD | Phase 3 |
| Licenses | Phase 3 |
| Awards | Phase 3 |
| Professional Memberships | Phase 3 |
| Professional Engagement Management | Phase 4 |
| Organizations and Events as reusable portfolio context | Phase 4 |
| Evidence metadata and relationships | Phase 4 |
| Supporting-document relationship concept | Phase 3 / Phase 4 as applicable |
| Research PDF/document upload | Phase 5 |
| Award/member supporting-document management | Phase 5 |
| General document management | Phase 5 |
| Google Drive | Phase 6 |
| OneDrive | Phase 6 |
| OCR/document extraction | Phase 7 |
| AI/RAG | Phase 8 |
| Resume/CV generator | Phase 9 |
| Public AI | Phase 10 |
| Advanced PWA/Mobile | Phase 11 |
| Production SaaS hardening | Phase 12 |
| Platform Engagement / Website Analytics | Future separate capability |

---

# Current Development Direction

**Phase 3 — Multi-Tenant Portfolio Management is complete. Phase 4 — Engagement Management architecture is locked and ready for technical model design.**

The next step is Step 5.15 — Django Model Architecture. Do not implement Phase 4 models until the architecture is translated into the existing Django conventions and tenant-isolation patterns.

Do not pull Phase 5–12 implementation into Phase 4 unless the roadmap is deliberately revised and documented.
