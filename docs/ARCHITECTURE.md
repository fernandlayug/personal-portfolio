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

The current implementation is focused on structured portfolio management and tenant isolation. Document storage, cloud integration, document intelligence, and AI capabilities remain future phases.

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
```

Tenant isolation is a non-negotiable architectural requirement.

---

# 3. Structured Portfolio Data

MySQL stores structured portfolio information.

The Phase 3 structured portfolio domains are:

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

These records are represented by Django models and managed through authenticated, tenant-scoped application logic.

Sensitive identifiers such as license numbers and membership numbers remain private by default. Storing a field in MySQL does not imply that it is public.

---

# 4. Portfolio Records and Supporting Documents

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

The architectural relationship is intentionally recognized now, but Phase 3 does not implement document uploads or binary storage.

A record should not be limited architecturally to a single future file. The document-management design should support multiple supporting documents where appropriate.

---

# 5. Professional Documents

Actual professional documents such as:

- PDFs
- Images
- Certificates
- Supporting evidence
- Research papers
- Membership documents

are intended to reside in tenant-controlled connected cloud storage rather than becoming permanently coupled to the application database.

Document Management is a future phase.

Phase 3 therefore does **not** introduce Django `FileField` storage or local document storage for these records.

---

# 6. Cloud Storage Abstraction

The platform is designed around a storage abstraction layer.

Future providers include:

- Google Drive
- Microsoft OneDrive

Portfolio features should communicate with the storage abstraction rather than directly depending on provider-specific implementation details.

This allows additional storage providers to be introduced later without redesigning portfolio features.

Cloud provider integration belongs to Phase 6, after Document Management has been established in Phase 5.

---

# 7. Engagement and Evidence Boundary

Engagement Management is a separate future portfolio domain and must not be conflated with Professional Memberships.

A Professional Membership represents a professional affiliation/credential record. An Engagement represents a separate concept whose exact meaning and scope must be established during Phase 4 architecture work.

Future engagement records may associate with multiple evidence documents, for example:

```text
Engagement
    |
    +-- Evidence Document
    +-- Evidence Document
    +-- Evidence Document
```

This is an architectural relationship concept only. It does not define the Phase 4 Engagement Management model before that phase is formally designed.

---

# 8. Document Intelligence

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

# 9. AI and RAG

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

# 10. Public AI

Public AI must:

- Be explicitly enabled by the tenant.
- Use only tenant-approved public information.
- Respect tenant boundaries.
- Never expose private portfolio information.
- Never assume that all structured portfolio fields are public.

Public visibility controls belong to the appropriate later public-functionality phase and are not added merely to support Phase 3 CRUD.

---

# 11. UI Architecture

The current project uses Django templates with an established CSS architecture.

New management features should reuse the established template and CSS conventions.

Do not introduce Bootstrap or a separate UI framework unless the architecture is explicitly changed.

---

# 12. Management and Security Pattern

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
Validate Form
        |
        v
Save with Server-side Ownership
```

The client must not be trusted to choose the tenant/profile ownership of a record.

Edit and delete operations must retrieve the target record through the current tenant relationship so that manipulated IDs/URLs cannot cross tenant boundaries.

---

# 13. Architectural Principles

The following principles are non-negotiable:

1. Tenant isolation.
2. Server-side ownership assignment.
3. Tenant-scoped CRUD.
4. Validation before persistence.
5. Structured portfolio data in MySQL.
6. Professional documents separated from structured database data.
7. Supporting documents are a future multi-document relationship, not a Phase 3 local file field.
8. Cloud storage abstraction.
9. Human verification for AI-extracted data.
10. Public AI is opt-in.
11. Private information must not leak into public AI.
12. Professional Memberships and Engagement Management are distinct concepts.
13. Development follows the approved roadmap.
14. Future-phase capabilities must not be silently pulled into the current phase.
