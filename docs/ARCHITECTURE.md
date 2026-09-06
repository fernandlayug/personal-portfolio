# Personal Portfolio Assistant — Architecture

## 1. Architectural Overview

The Personal Portfolio Assistant is designed as a multi-tenant SaaS platform.

Each tenant owns and controls an isolated professional portfolio.

The architecture separates:

- Structured portfolio information
- Professional documents
- Cloud storage
- Document processing
- AI and retrieval
- Public portfolio access

---

# 2. Multi-Tenant Architecture

Each authenticated user operates within a tenant context.

Tenant-owned portfolio information must never be accessible across tenants.

Portfolio records are associated with the tenant's Profile and management operations are tenant-scoped.

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
```

Tenant isolation is a non-negotiable architectural requirement.

---

# 3. Structured Data

MySQL stores structured portfolio information.

Examples include:

- Profile
- Education
- Work Experience
- Skills
- Projects
- Certificates
- Research

Structured records are managed through Django models and tenant-scoped application logic.

---

# 4. Professional Documents

Actual professional documents such as:

- PDFs
- Images
- Supporting documents
- Professional evidence

are intended to reside in the tenant's connected cloud storage rather than becoming permanently coupled to the application database.

Cloud storage is a future implementation area.

---

# 5. Cloud Storage Abstraction

The platform is designed around a storage abstraction layer.

Future providers include:

- Google Drive
- OneDrive

Portfolio features should communicate with the storage abstraction rather than directly depending on provider-specific implementation details.

This allows additional storage providers to be introduced later without redesigning portfolio features.

---

# 6. Engagement and Evidence Relationship

Future engagement management may associate professional engagements with multiple evidence documents.

Conceptually:

```text
Engagement
    |
    +-- Evidence Document
    +-- Evidence Document
    +-- Evidence Document
```

Document management is intentionally deferred to the appropriate roadmap phase.

---

# 7. Document Intelligence

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

---

# 8. AI and RAG

The future AI layer will use tenant-scoped retrieval.

The conceptual flow is:

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

---

# 9. Public AI

Public AI must:

- Be explicitly enabled by the tenant.
- Use only approved public information.
- Respect tenant boundaries.
- Never expose private portfolio information.

---

# 10. UI Architecture

The current project uses Django templates with an existing CSS architecture.

New management features should reuse the established template and CSS conventions.

Do not introduce Bootstrap or a separate UI framework unless the architecture is explicitly changed.

---

# 11. Architectural Principles

The following principles are non-negotiable:

1. Tenant isolation.
2. Server-side ownership assignment.
3. Tenant-scoped CRUD.
4. Validation before persistence.
5. Structured data in MySQL.
6. Cloud storage abstraction.
7. Human verification for AI-extracted data.
8. Public AI is opt-in.
9. Private information must not leak into public AI.
10. Development follows the approved roadmap.
