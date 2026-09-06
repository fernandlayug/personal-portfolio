# Personal Portfolio Assistant — Changelog

This changelog records meaningful project milestones and architectural/governance changes.

---

## 2026-09-05 — Project Governance Documentation

### Added

- Master project roadmap.
- Architecture documentation.
- Architecture decision records.
- Project status tracking.
- Development rules.
- Changelog structure.

### Governance

Established:

- Roadmap-first development.
- Architecture-first development.
- Phase gates.
- GitHub as the committed-code source of truth.
- Tenant isolation requirements.
- Future-feature boundaries.

---

## 2026-09-05 — Research Portfolio Management

### Added

- Research model.
- Research migration.
- Research form.
- Research validation.
- Research list.
- Research add.
- Research edit.
- Research delete.
- Tenant-scoped Research access.
- Dashboard integration.
- Research management templates.

### Validation

Implemented validation for:

- Future start dates.
- Future completion dates.
- Completion dates earlier than start dates.

### Testing

Research CRUD was tested for:

- Page loading.
- Creation.
- Validation.
- Editing.
- Cancellation.
- Deletion.
- Tenant-scoped access.

### Deferred

The following were intentionally NOT implemented as part of Research CRUD:

- Research PDF upload.
- Research document management.
- Google Drive integration.
- OneDrive integration.
- Document extraction.
- OCR.
- AI document extraction.
- RAG indexing.

These capabilities remain assigned to their respective future roadmap phases.

---

# Changelog Rules

For meaningful milestones, record:

- Date
- Feature or architectural change
- Added functionality
- Testing where relevant
- Deferred functionality where scope boundaries matter

Do not record a phase as COMPLETE until its phase completion gate has been satisfied.
