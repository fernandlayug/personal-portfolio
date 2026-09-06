# Personal Portfolio AI Assistant — Master Roadmap

**Project:** Personal Portfolio AI Assistant  
**Architecture:** Multi-tenant SaaS  
**Current Date:** 2026-09-06  
**Current Phase:** Phase 3 — Multi-Tenant Portfolio Management

---

## 1. Project Vision

The Personal Portfolio AI Assistant is a multi-tenant professional portfolio platform that allows each user/tenant to maintain structured professional information, manage supporting documents, connect cloud storage, and eventually use AI to search, analyze, generate, and present portfolio information.

Each tenant has isolated portfolio data and settings.

### Core architecture principles

- Structured portfolio metadata is stored in MySQL.
- Professional documents, PDFs, and images are stored through a storage abstraction layer.
- Tenant-owned Google Drive or OneDrive storage will be integrated in a later phase.
- Tenant data must remain isolated.
- Owner/private AI capabilities will be separated from public AI capabilities.
- Public AI is opt-in and must only use tenant-approved public information.
- Document processing, OCR, extraction, RAG, and AI capabilities are deliberately deferred to later phases.

---

# 2. Phase Roadmap

| Phase | Area | Status |
|---|---|---|
| Phase 1 | Foundation | COMPLETE |
| Phase 2 | Professional Portfolio UI | COMPLETE |
| Phase 3 | Multi-Tenant Portfolio Management | CURRENT |
| Phase 4 | Engagement Management | FUTURE |
| Phase 5 | Document Management | FUTURE |
| Phase 6 | Cloud Storage Integration | FUTURE |
| Phase 7 | Intelligent Document Processing | FUTURE |
| Phase 8 | AI Assistant & RAG | FUTURE |
| Phase 9 | Resume/CV/Portfolio Generator | FUTURE |
| Phase 10 | Public AI | FUTURE |
| Phase 11 | Advanced PWA/Mobile | FUTURE |
| Phase 12 | Production & SaaS Hardening | FUTURE |

---

# 3. Phase 1 — Foundation

**Status: COMPLETE**

Completed foundation work includes:

- Django project setup
- MySQL database configuration
- Portfolio application
- Initial portfolio data models
- Django migrations
- Django Admin configuration
- Initial portfolio records
- Dynamic portfolio homepage
- Basic authentication foundation

---

# 4. Phase 2 — Professional Portfolio UI

**Status: COMPLETE**

Completed UI work includes:

- Professional portfolio homepage
- Responsive navigation
- Portfolio presentation sections
- Dashboard foundation
- Login interface
- Management interfaces
- Consistent CSS design system
- Responsive desktop/mobile presentation

---

# 5. Phase 3 — Multi-Tenant Portfolio Management

**Status: CURRENT**

The objective of Phase 3 is to establish reliable tenant-scoped CRUD management for the professional portfolio.

## 5.1 Portfolio domains

The current portfolio management structure is:

```text
Profile
   |
   +-- Education
   +-- Work Experience
   +-- Skills
   +-- Projects
   +-- Certificates
   +-- Licenses
   +-- Research
```

## 5.2 Implemented portfolio management

The following are implemented and tested:

- Profile
- Education
- Work Experience
- Skills
- Projects
- Certificates
- Research

### Research status

Research CRUD is implemented and browser-tested:

- Research list
- Add Research
- Edit Research
- Delete Research
- Date validation
- Tenant-scoped access
- Dashboard integration

**Important boundary:** Research PDF/document upload is NOT part of Research CRUD. It belongs to Phase 5 — Document Management.

---

## 5.3 Licenses — NEXT PHASE 3 FEATURE

Professional and academic licenses will be added as a Phase 3 portfolio-management feature.

Planned capabilities:

- License list
- Add License
- Edit License
- Delete License
- License type
- Issuing organization
- License number
- Issue date
- Expiration date
- Status
- Verification/license URL
- Description
- Tenant-scoped access
- Dashboard integration

### Planned License structure

```text
Profile
   |
   +-- Licenses
          |
          +-- Name
          +-- Issuing Organization
          +-- License Type
          +-- License Number
          +-- Issue Date
          +-- Expiration Date
          +-- Status
          +-- License URL
          +-- Description
```

### Planned validation

- Issue date cannot be in the future.
- Expiration date cannot be earlier than the issue date.
- Status is stored as portfolio information and is not automatically inferred solely from the expiration date.

---

## 5.4 Phase 3 security requirements

All management functionality must preserve tenant isolation.

Required pattern:

```text
@login_required
        |
        v
verify_current_tenant(request)
        |
        v
Current Profile
        |
        v
Profile-scoped QuerySet
        |
        v
CRUD operation
```

Rules:

- Never trust a profile ID supplied by the browser for ownership.
- Do not expose a `profile` field in tenant-facing ModelForms.
- Assign the current profile server-side when creating records.
- Retrieve existing records through the current profile relationship.
- Use Django authentication for protected management views.
- Use POST + CSRF protection for destructive operations.
- Preserve existing CSS and template conventions.

---

# 6. Phase 3 Completion Gate

Phase 3 must NOT be marked complete until the following are verified:

- [x] Profile management foundation
- [x] Education CRUD
- [x] Work Experience CRUD
- [x] Skills CRUD
- [x] Projects CRUD
- [x] Certificates CRUD
- [x] Research CRUD
- [ ] Licenses CRUD
- [ ] Dashboard integration for Licenses
- [ ] Tenant isolation verification
- [ ] Final browser testing
- [ ] Final Django checks
- [ ] Documentation update
- [ ] Git commit and push
- [ ] Phase 3 completion review

Only after this gate is satisfied should the project proceed to Phase 4.

---

# 7. Phase 4 — Engagement Management

**Status: FUTURE**

Phase 4 will introduce professional engagement and relationship-oriented portfolio capabilities.

Potential areas include:

- Professional contacts
- Organizations
- Clients
- Professional relationships
- Engagement records
- Collaboration history
- Other approved engagement-management features

Phase 4 must not absorb document management or cloud-storage responsibilities.

---

# 8. Phase 5 — Document Management

**Status: FUTURE**

This phase is responsible for managing professional documents associated with portfolio records.

Potential capabilities:

- Document records
- Document metadata
- Document categories
- Document-to-portfolio-record relationships
- Upload workflows
- Document listing
- Document replacement/deletion
- Document access rules
- Document versioning where appropriate

### Important boundary

Research documents belong here.

For example:

```text
Research
   |
   +-- Research metadata
   |
   +-- Research document(s)
```

Do not implement Research PDF upload during Phase 3.

---

# 9. Phase 6 — Cloud Storage Integration

**Status: FUTURE**

This phase will implement the storage abstraction layer and tenant-owned cloud storage connections.

Target providers:

- Google Drive
- Microsoft OneDrive

Conceptually:

```text
Django Application
        |
        v
Storage Abstraction Layer
        |
        +---- Google Drive
        |
        +---- OneDrive
```

The application should avoid coupling portfolio logic directly to one storage provider.

---

# 10. Phase 7 — Intelligent Document Processing

**Status: FUTURE**

Potential capabilities:

- PDF text extraction
- OCR
- Metadata extraction
- Structured information extraction
- Document classification
- Document summarization
- Validation of extracted information
- Human review workflows

This phase depends on the document-management and storage foundations.

---

# 11. Phase 8 — AI Assistant & RAG

**Status: FUTURE**

Potential capabilities:

- Portfolio question answering
- Semantic search
- Retrieval-Augmented Generation
- Personal professional assistant
- Context-aware portfolio queries
- Source-grounded answers
- Document-aware responses

The AI layer must respect tenant boundaries and document permissions.

---

# 12. Phase 9 — Resume/CV/Portfolio Generator

**Status: FUTURE**

Potential capabilities:

- Resume generation
- CV generation
- Portfolio document generation
- Job-specific customization
- Professional profile summaries
- Export workflows

Generated outputs should be based on tenant-approved portfolio information.

---

# 13. Phase 10 — Public AI

**Status: FUTURE**

Public AI is opt-in.

The public assistant must:

- Be disabled by default.
- Use only tenant-approved public information.
- Never expose private portfolio information.
- Respect tenant configuration.
- Preserve tenant isolation.

Conceptually:

```text
Private Portfolio Data
        |
        +---- Owner AI
        |
        +---- Restricted / approved public data
                         |
                         v
                    Public AI
```

---

# 14. Phase 11 — Advanced PWA/Mobile

**Status: FUTURE**

Potential capabilities:

- Progressive Web App enhancements
- Mobile-first workflows
- Offline support where appropriate
- Installable application experience
- Mobile portfolio management
- Mobile document workflows

---

# 15. Phase 12 — Production & SaaS Hardening

**Status: FUTURE**

Potential capabilities:

- Production deployment
- Security hardening
- Monitoring
- Logging
- Backups
- Rate limiting
- SaaS subscription architecture
- Tenant administration
- Operational controls
- Performance optimization
- Production database/storage strategy

---

# 16. Feature Boundary

The following boundaries are locked:

| Feature | Phase |
|---|---|
| Portfolio metadata CRUD | Phase 3 |
| Certificates CRUD | Phase 3 |
| Research CRUD | Phase 3 |
| Licenses CRUD | Phase 3 |
| Research PDF/document upload | Phase 5 |
| Document management | Phase 5 |
| Google Drive integration | Phase 6 |
| OneDrive integration | Phase 6 |
| Document extraction/OCR | Phase 7 |
| Intelligent document processing | Phase 7 |
| AI Assistant | Phase 8 |
| RAG | Phase 8 |
| Resume/CV generation | Phase 9 |
| Public AI | Phase 10 |
| Advanced PWA/Mobile | Phase 11 |
| Production SaaS hardening | Phase 12 |

These boundaries prevent later-phase functionality from being prematurely introduced into the current CRUD implementation.

---

# 17. Current Development Direction

The immediate development sequence is:

```text
Phase 3
   |
   +-- Research CRUD [COMPLETE]
   |
   +-- Licenses CRUD [NEXT]
   |
   +-- Phase 3 security/testing gate
   |
   v
Phase 4 — Engagement Management
```

After Phase 3 is formally closed, the project may proceed to Phase 4.

