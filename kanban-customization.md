# Kanban Board Customization

**Assignment 7**
**Amanda**
**April 10, 2026**

---

## Customization Choices

### Selected Template: Kanban

### Added Column 1: Testing

**Reason for adding:** After completing work on a user story, it needs to be tested before being marked as "Done." Without a Testing column, completed work would move directly to Done without verification, which could lead to bugs in the final product.

**How it improves workflow:** The Testing column creates a clear stage for quality assurance. A story moves from In Progress → Testing → Done only after passing tests. If tests fail, it moves back to In Progress.

### Added Column 2: Blocked

**Reason for adding:** Assignment 6 identified dependencies between user stories (e.g., US-010: Book Study Room depends on US-009: Find Study Rooms). Without a Blocked column, dependent stories would sit in In Progress indefinitely, giving a false sense of progress.

**How it improves workflow:** The Blocked column makes dependencies visible. A blocked story is moved to the Blocked column until its dependency is resolved, then moved back to In Progress. This prevents wasted time on stories that cannot proceed.

### Final Column Structure

| Column | Purpose | WIP Limit |
|--------|---------|-----------|
| **Todo** | Stories planned but not started | No limit |
| **In Progress** | Stories actively being worked on | 2 |
| **Testing** | Stories completed but awaiting verification | 1 |
| **Blocked** | Stories that cannot proceed due to dependencies | No limit |
| **Done** | Stories fully completed and verified | No limit |

### WIP Limits Justification

| Column | WIP Limit | Justification |
|--------|-----------|---------------|
| In Progress | 2 | As a solo developer, I can only focus on 2 tasks at once. More leads to context switching. |
| Testing | 1 | Testing requires full attention; one story at a time ensures quality. |

---

## Screenshot of Custom Kanban Board

![Custom Kanban Board](kanban-board-screenshot.png)

*Figure 1: Smart Campus Connect Kanban board with custom columns (Testing, Blocked)*
