# Personal Portfolio Assistant — Development Rules

These rules govern implementation of the Personal Portfolio Assistant.

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

---

# 5. Validation

Validate data before persistence.

Validation should cover:

- Required values
- Date relationships
- Future dates where inappropriate
- URL fields where applicable
- Other domain-specific constraints

Errors should be presented clearly to the user.

---

# 6. UI Consistency

Reuse the existing Django template and CSS architecture.

Do not introduce Bootstrap or another UI framework without an explicit architectural decision.

New management pages should follow existing conventions.

---

# 7. Future Feature Boundaries

Do not pull future functionality into the current phase merely because it appears convenient.

Examples:

- Research PDF upload -> Phase 5
- Google Drive -> Phase 6
- OneDrive -> Phase 6
- Document extraction -> Phase 7
- AI extraction -> Phase 7
- RAG -> Phase 8
- AI Assistant -> Phase 8
- Resume/CV generation -> Phase 9
- Public AI -> Phase 10

---

# 8. Testing Before Commit

Before committing a significant feature:

1. Run Django system checks.
2. Run relevant migrations.
3. Test validation.
4. Test CRUD behavior.
5. Test tenant isolation where applicable.
6. Review affected templates.
7. Confirm URLs work.
8. Confirm no unrelated changes are included.

---

# 9. GitHub Synchronization

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

# 10. Documentation

After meaningful milestones:

- Update `PROJECT_STATUS.md`.
- Update `CHANGELOG.md`.
- Update `MASTER_ROADMAP.md` when phase status changes.
- Update `ARCHITECTURE.md` when architecture changes.
- Update `ARCHITECTURE_DECISIONS.md` when a significant architectural decision changes.

---

# 11. Phase Completion

A phase can only be marked COMPLETE when its completion gate has been satisfied.

The completion gate includes:

1. Required features implemented.
2. Tenant isolation considered/tested where applicable.
3. Validation and error handling tested.
4. Documentation updated.
5. Code synchronized with GitHub.
6. Project status explicitly updated.

---

# 12. Roadmap Check Response

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

# 13. Project Owner Control

The project owner controls changes to:

- Roadmap
- Architecture
- Scope
- Phase sequencing
- Major technology decisions

Assistant recommendations must not silently become project decisions.
