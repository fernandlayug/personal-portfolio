# Personal Portfolio Assistant — Development Rules

These rules govern implementation of the Personal Portfolio AI Assistant.

---

# 1. Roadmap First

Before implementing a significant feature:

1. Check `MASTER_ROADMAP.md`.
2. Identify the current phase.
3. Identify the phase assigned to the requested feature.
4. Check `ARCHITECTURE.md`.
5. Check `PROJECT_STATUS.md`.
6. Implement only if the feature belongs to the current phase.

If a requested feature belongs to a future phase, defer it unless the project owner explicitly changes the roadmap.

---

# 2. Architecture First

Before changing core behavior:

- Check existing architecture.
- Preserve tenant isolation.
- Preserve storage abstraction boundaries.
- Avoid introducing future-phase dependencies.
- Avoid silently changing architectural decisions.

If a requested feature exposes an unclear domain concept, establish the domain architecture before writing implementation code.

---

# 3. Feature State

Distinguish clearly between:

- Planned
- Designed
- Implemented
- Tested
- Committed
- Pushed
- Deployed

A feature must not be described as complete when only its code has been written.

---

# 4. Tenant Isolation

Tenant isolation is mandatory.

For tenant-owned CRUD:

- Verify the current tenant/profile.
- Query records through the current tenant relationship.
- Never trust a submitted profile/tenant identifier.
- Assign ownership server-side.
- Prevent access to another tenant's records.
- Test direct/manipulated URLs for edit/delete access where applicable.

---

# 5. Privacy by Default

Portfolio records are private by default.

Sensitive identifiers such as license numbers and membership numbers must not automatically be treated as public data.

Do not add public/visibility behavior merely to support private CRUD. Public exposure must be designed explicitly in the appropriate later phase.

---

# 6. Validation

Validate data before persistence.

Validation should cover:

- Required values
- Date relationships
- Future dates where inappropriate
- URL fields where applicable
- Other domain-specific constraints

Errors should be presented clearly to the user.

---

# 7. UI Consistency

Reuse the existing Django template and CSS architecture.

Do not introduce Bootstrap or another UI framework without an explicit architectural decision.

New management pages should follow existing conventions.

---

# 8. Supporting Documents

Supporting documents are a separate architectural concern from structured portfolio records.

Examples include:

- Award → Certificate of Award
- Professional Membership → Certificate of Membership
- Research → Research Paper/PDF

Phase 3 must not introduce local `FileField` storage solely to attach these files.

Future document management should support multiple supporting documents where appropriate and should follow the approved Document Management and Cloud Storage phases.

---

# 9. Future Feature Boundaries

Do not pull future functionality into the current phase merely because it appears convenient.

Examples:

- Research PDF/document upload → Phase 5
- Award/member supporting-document management → Phase 5
- General document management → Phase 5
- Google Drive → Phase 6
- OneDrive → Phase 6
- Document extraction/OCR → Phase 7
- AI document processing → Phase 7
- RAG → Phase 8
- AI Assistant → Phase 8
- Resume/CV generation → Phase 9
- Public AI → Phase 10
- Advanced PWA/Mobile → Phase 11
- Production/SaaS hardening → Phase 12

---

# 10. Domain Boundary: Professional Membership vs Engagement

Professional Memberships and Engagement Management are separate concepts.

A Professional Membership is a structured portfolio affiliation/credential record.

Engagement Management is a separate domain and must not be inferred or implemented from the membership model. Its purpose, scope, models, relationships, workflows, and completion gate must be established during Phase 4 architecture work.

---

# 11. Testing Before Commit

Before committing a significant feature:

1. Run Django system checks.
2. Run relevant migrations.
3. Test validation.
4. Test CRUD behavior.
5. Test tenant isolation where applicable.
6. Test direct URL access where applicable.
7. Review affected templates.
8. Confirm URLs work.
9. Confirm no unrelated changes are included.

---

# 12. GitHub Synchronization

GitHub is the source of truth for committed code.

Before significant work:

```text
Check branch
Check GitHub synchronization
Check working tree
```

After completing a feature:

```text
Test
Commit
Push
Verify synchronization
```

Preferred commit history should use focused commits where practical.

---

# 13. Documentation

After meaningful milestones:

- Update `PROJECT_STATUS.md`.
- Update `CHANGELOG.md`.
- Update `MASTER_ROADMAP.md` when phase status changes.
- Update `ARCHITECTURE.md` when architecture changes.
- Update `ARCHITECTURE_DECISIONS.md` when a significant architectural decision changes.

Documentation must describe the implementation that actually exists, not planned behavior as though it were already implemented.

---

# 14. Phase Completion

A phase can only be marked COMPLETE when its completion gate has been satisfied.

The completion gate includes:

1. Required features implemented.
2. Tenant isolation considered/tested where applicable.
3. Validation and error handling tested.
4. Documentation updated.
5. Code synchronized with GitHub.
6. Project status explicitly updated.

---

# 15. Roadmap Check Response

When a requested feature may belong to another phase, use this format:

```text
Roadmap Check
Current Phase: [phase]
Requested Feature: [feature]
Assigned Phase: [phase]
Decision: IMPLEMENT / DEFER
```

Do not silently move features between phases.

---

# 16. Project Owner Control

The project owner controls changes to:

- Roadmap
- Architecture
- Scope
- Phase sequencing
- Major technology decisions

Assistant recommendations must not silently become project decisions.
