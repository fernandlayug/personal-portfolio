# Personal Portfolio AI Assistant — Architecture

## 1. Architectural Overview

The Personal Portfolio AI Assistant is designed as a multi-tenant SaaS platform.

Each tenant owns and controls an isolated professional portfolio.

The architecture separates:

- Structured portfolio information
- Professional documents and supporting evidence
- Cloud storage
- Document processing
- AI and retrieval
- Public portfolio access

The current implementation is focused on structured portfolio management, tenant isolation, and Phase 4 Engagement Management. Document storage, cloud integration, document intelligence, and AI capabilities remain future phases.

---

# 2. Multi-Tenant Architecture

Each authenticated user operates within a tenant/profile context.

Tenant-owned portfolio information must never be accessible across tenants.

Portfolio records are associated with the tenant's `Profile`, and management operations are tenant-scoped.

Conceptually:

```text
Tenant / User
     |
     v
  Profile
     |
     +-- Education
     +-- Work Experience
     +-- Skills
     +-- Projects
     +-- Certificates
     +-- Research
     +-- Licenses
     +-- Awards
     +-- Professional Memberships
     +-- Engagements
     +-- Organizations
     +-- Events
     +-- Evidence
```

Tenant isolation is a non-negotiable architectural requirement.

---

# 3. Structured Portfolio Data

MySQL stores structured portfolio information.

The structured portfolio domains include:

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
- Professional Engagements

Phase 4 also introduces reusable portfolio context entities:

- Organizations
- Events
- Evidence metadata

These records are tenant-owned and managed through authenticated, tenant-scoped application logic.

Sensitive identifiers such as license numbers and membership numbers remain private by default. Storing a field in MySQL does not imply that it is public.

---

# 4. Professional Engagement Management

## 4.1 Definition

Professional Engagement represents a meaningful professional activity, service, participation, collaboration, leadership, invitation, or other involvement undertaken by the portfolio owner within a defined professional context, where the activity has standalone professional value and is not adequately represented by an existing portfolio domain.

The core principle is:

> Engagement records the portfolio owner's meaningful professional involvement, not merely the existence of an event, organization, or interaction.

Mere attendance or passive participation in a professional event does not constitute a Professional Engagement.

Professional Memberships and Engagements are distinct concepts. A membership represents a professional affiliation/credential; an engagement represents meaningful professional involvement.

## 4.2 Engagement Core Attributes

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

Derived rather than stored:

- Upcoming / Current / Past presentation state
- Duration
- Relationship counts

Description, Purpose, Outcome, and Impact remain distinct narrative fields. Description explains what the engagement was and what the portfolio owner did; Purpose explains why it was undertaken; Outcome explains what resulted; Impact explains why it mattered.

## 4.3 Engagement Lifecycle

Initial statuses:

- Draft
- Planned
- Ongoing
- Completed
- Cancelled
- Postponed

Upcoming and Past are derived presentation states, not stored statuses. Declined is not an Engagement status.

Start and End dates are independently optional. When both are supplied, End Date must not precede Start Date.

## 4.4 Engagement Classification

Engagement Type describes the nature of the professional involvement. Initial types are:

- Speaking & Training
- Academic & Research Service
- Professional Service & Leadership
- Collaboration
- Technical Advisory & Evaluation
- Professional Representation
- Advising & Mentoring
- Community & Stakeholder Engagement
- Other Professional Engagement

Engagement Roles describe the responsibility/capacity of the portfolio owner. Roles are reusable and extensible, with exactly one Primary Role per Engagement.

Engagement Tags provide optional cross-cutting classification such as AI, Research, Educational Technology, Community Outreach, or IT Education.

Engagement Type, Engagement Role, Organization Classification, and Tags are tenant-aware configurable taxonomy records. The implementation may provide system-defined defaults while allowing tenant-specific configuration without creating a generic unrestricted configuration framework.

---

# 5. Organizations as Shared Portfolio Context

## 5.1 Definition

Organization is a tenant-owned, reusable contextual entity representing a professional, academic, institutional, commercial, governmental, nonprofit, community, or other identifiable organization.

Organization is broader than Company or Institution and is not limited to employment.

## 5.2 Organization Attributes

Required:

- Name
- Visibility

Optional:

- Description
- Website
- Location
- One or more Classifications

System-managed:

- Created At
- Updated At

Organization Classification describes what the organization is. It is distinct from an Engagement Organization Relationship Role, which describes how the organization relates to a particular Engagement.

Initial classifications may include:

- Academic Institution
- Educational Institution
- Government Agency
- Professional Association
- Nonprofit Organization
- Private Company
- Research Institution
- Community Organization
- Industry Organization
- Professional Society
- Other

Organizations are reusable shared portfolio context from the beginning and may eventually be related to Engagements, Work Experience, Projects, Research, Professional Memberships, Certificates, Awards, and other future domains.

There is no global shared organization directory in the initial architecture. The same real-world organization may therefore be represented independently by different tenants.

Contact persons, CRM records, organization registration/tax IDs, and full contact-management functionality are outside Phase 4.

---

# 6. Events as Shared Portfolio Context

## 6.1 Definition

Event is a tenant-owned, reusable contextual entity representing an identifiable professional, academic, institutional, community, or other occurrence.

Event is distinct from Engagement:

- Event = what occurred.
- Engagement = what meaningful professional involvement the portfolio owner undertook.

## 6.2 Event Attributes

Required:

- Event Name/Title
- Visibility

Optional:

- Description
- Event Type
- Start Date
- End Date
- Location
- Mode

System-managed:

- Created At
- Updated At

Initial Event Types may include:

- Conference
- Workshop
- Seminar
- Summit
- Competition
- Symposium
- Training
- Forum
- Other

An Engagement may relate to zero or one Event. An Event may relate to many Engagements and may exist independently of any Engagement.

Event management functionality such as registration, RSVP, ticketing, attendance tracking, participant management, scheduling, recurrence, and capacity management is outside Phase 4.

---

# 7. Engagement Relationships

Relationships are explicit and semantic rather than represented by a generic relationship mechanism.

## 7.1 Relationship Cardinalities

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

All relationships are optional. An Engagement does not require another portfolio record.

## 7.2 Organization Relationship Semantics

Engagement-to-Organization is an explicit relationship because the semantic role of an organization matters.

Initial relationship roles include:

- Partner
- Host
- Organizer
- Appointing Organization
- Collaborating Organization
- Sponsor
- Client
- Beneficiary Organization
- Supporting Organization
- Other

The same organization may legitimately have multiple roles within one Engagement.

## 7.3 Other Portfolio Relationships

Projects: the Engagement materially contributes to, supports, or advances the Project.

Research: the Engagement is materially connected to the Research activity or output.

Professional Memberships: the Engagement occurs through, within, or as part of a membership context; membership remains a distinct credential/affiliation record.

Work Experience: the Engagement occurred within, arose from, or is materially related to a work context.

Skills: the Engagement materially demonstrates, develops, or uses a skill. A relationship does not by itself imply expertise.

Education: the Engagement is connected to an educational context.

Certificates: the certificate documents, recognizes, or supports the Engagement. A Certificate portfolio record remains distinct from Evidence.

Awards: the award recognizes the Engagement, contribution, or outcome. An Award portfolio record remains distinct from the Engagement.

No generic "Related Portfolio Records" relationship is introduced.

---

# 8. Evidence

Evidence is information or a resource that substantiates, verifies, or provides supporting context for a Professional Engagement.

Examples include:

- Certificates
- Letters
- Attendance records
- Evaluation reports
- Official announcements
- Email correspondence
- Meeting records
- Photographs
- Published articles
- Reviewer access/submission records
- External URLs
- Participant outputs

Evidence is a reusable supporting concept and may eventually support Engagements and other portfolio domains.

Engagement ↔ Evidence is M:N. One Evidence item may support multiple records.

Evidence visibility is independent from Engagement visibility. A Public Engagement does not automatically make associated evidence public.

Phase 4 establishes Evidence metadata and relationships only. It does not implement local file storage or cloud storage.

---

# 9. Portfolio Records and Supporting Documents

Portfolio records may eventually have one or more supporting professional documents.

Examples:

```text
Award
  |
  +-- Certificate of Award
  +-- Announcement / Evidence
```

```text
Professional Membership
  |
  +-- Certificate of Membership
  +-- Renewal / Evidence
```

```text
Research
  |
  +-- Research Paper / PDF
  +-- Supporting Evidence
```

The architectural relationship is intentionally recognized now, but document management is a separate roadmap phase.

---

# 10. Document Management Boundary

Actual professional documents such as PDFs, images, certificates, research papers, and supporting evidence are intended to reside in tenant-controlled connected cloud storage rather than becoming permanently coupled to the application database.

Phase 4 does **not** introduce Django `FileField` storage, local binary storage, Google Drive integration, or OneDrive integration.

The roadmap boundary remains:

```text
Phase 4
Evidence metadata + relationships
        |
        v
Phase 5
Document Management
        |
        v
Phase 6
Google Drive / OneDrive
```

---

# 11. Visibility, Privacy, and Public Projection

Engagement, Organization, Event, and Evidence visibility are independently controlled and tenant-scoped.

Initial Engagement visibility states are:

- Private
- Public
- Unlisted

New Engagements are private by default.

Visibility is not publication. Featured is independent of visibility: visibility controls eligibility for presentation, while Featured controls presentation priority.

Draft Engagements are never publicly presented, regardless of configured visibility.

A Public Engagement does not automatically expose related Organizations, Events, Projects, Research, Professional Memberships, Certificates, Awards, or Evidence. Related records retain their own visibility rules.

Public presentation must use a controlled public projection rather than unrestricted relationship traversal.

The precise direct-access behavior of Unlisted remains a later presentation refinement.

Public Engagement visibility does not imply eligibility for future Public AI.

Sensitive identifiers remain private by default.

---

# 12. Engagement CRUD and Management Workflow

The management workflow is:

```text
Engagement List
      |
      +-- Create
      |
      v
Engagement Form
      |
      +-- Basic Information
      +-- Timing & Context
      +-- Narrative
      +-- Organizations
      +-- Event
      +-- Portfolio Relationships
      +-- Evidence
      +-- Visibility & Presentation
      |
      v
Save
      |
      v
Engagement Detail
      |
      +-- Edit
      +-- Change Visibility
      +-- Feature / Unfeature
      +-- Manage Relationships
      +-- Controlled Delete
```

Management supports tenant-scoped search and filtering by appropriate Engagement attributes such as Type, Status, Visibility, and date/year. Related-object lookup must also remain tenant-scoped.

Create, update, and relationship assignment must validate submitted objects against the current tenant. The client must never be trusted to select tenant ownership.

---

# 13. Management and Security Pattern

Tenant-owned CRUD follows the established pattern:

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

Edit and delete operations must retrieve the target record through the current tenant relationship so manipulated IDs/URLs cannot cross tenant boundaries.

Every Phase 4 entity and relationship must remain tenant-scoped. Cross-tenant relationship assignment is prohibited.

---

# 14. Shared Portfolio Context Principle

Organizations and Events are shared portfolio-context infrastructure rather than Engagement-only helper records.

They are designed for reuse across current and future portfolio domains while implementation remains limited to relationships required by the current phase.

This does not create a generic entity-management or CRM platform.

People, contacts, departments, committees, divisions, boards, audiences, beneficiaries, and other participants may be described contextually in Engagement narratives or fields but are not reusable Person/Contact entities in Phase 4.

---

# 15. Document Intelligence

Future document processing will support extraction and intelligent processing.

The intended sequence is:

```text
Document
   |
   v
Storage
   |
   v
Extraction / OCR
   |
   v
AI-assisted Processing
   |
   v
Human Verification
   |
   v
Structured Portfolio Data
```

AI extraction must not silently become authoritative portfolio data without appropriate human verification.

Document intelligence belongs to Phase 7.

---

# 16. AI and RAG

The future AI layer will use tenant-scoped retrieval.

Conceptually:

```text
Tenant Portfolio
      |
      v
Authorized Knowledge
      |
      v
Retrieval
      |
      v
AI Assistant
      |
      v
Grounded Response
```

Owner AI is authenticated and private.

Public AI is opt-in and restricted to tenant-approved public information.

The AI layer must never bypass tenant isolation or data/document permissions.

---

# 17. Public AI

Public AI must:

- Be explicitly enabled by the tenant.
- Use only tenant-approved public information.
- Respect tenant boundaries.
- Never expose private portfolio information.
- Never assume that all structured portfolio fields are public.

Public AI is a later roadmap capability and is not introduced by Phase 4 Engagement visibility.

---

# 18. Future Platform Engagement / Analytics

Website/user engagement and analytics remain a separate future capability and are not Professional Engagement records.

Future platform analytics may cover concepts such as:

- Visitors
- Page views
- Portfolio interactions
- Downloads
- Referrals
- AI conversation analytics

These must not be modeled as Professional Engagements.

---

# 19. UI Architecture

The current project uses Django templates with an established CSS architecture.

New management features should reuse the established template and CSS conventions.

Do not introduce Bootstrap or a separate UI framework unless the architecture is explicitly changed.

---

# 20. Architectural Principles

The following principles are non-negotiable:

1. Tenant isolation.
2. Server-side ownership assignment.
3. Tenant-scoped CRUD and relationship assignment.
4. Validation before persistence.
5. Structured portfolio data in MySQL.
6. Professional documents separated from structured database data.
7. Supporting documents are separate reusable evidence/document concepts, not Phase 4 local file fields.
8. Cloud storage abstraction.
9. Human verification for AI-extracted data.
10. Public AI is opt-in.
11. Private information must not leak into public AI or public portfolio projections.
12. Professional Memberships and Engagements are distinct concepts.
13. Organizations and Events are tenant-owned reusable portfolio context.
14. People/Contacts are not a Phase 4 CRM domain.
15. Public projection must be controlled rather than unrestricted relationship traversal.
16. Development follows the approved roadmap.
17. Future-phase capabilities must not be silently pulled into the current phase.
