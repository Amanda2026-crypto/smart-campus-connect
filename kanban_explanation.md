# Kanban Board Explanation

**Assignment 7**
**Amanda**
**April 10, 2026**

---

## What is a Kanban Board?

A Kanban board is a visual project management tool that helps teams track work as it moves through different stages of completion. It uses columns to represent workflow stages (e.g., "To Do," "In Progress," "Done"), and cards (or issues) move from left to right as work progresses.

The name "Kanban" comes from Japanese, meaning "visual signal" or "card." It was developed by Toyota in the 1940s as a scheduling system for just-in-time manufacturing and has since been adapted for software development by Agile teams.

---

## How My Board Visualizes Workflow

My Kanban board has **7 columns** that represent the complete workflow from idea to completion:

| Column | Purpose | What It Shows |
|--------|---------|---------------|
| **Backlog** | All planned user stories | Stories waiting to be worked on (7 stories) |
| **Ready** | Stories that are ready to be picked up | Stories that have been refined and estimated |
| **In progress** | Stories currently being worked on | Active work (limited to 2 stories) |
| **In review** | Stories completed but awaiting review | Stories that need quality check |
| **Testing** (custom) | Stories being tested | QA verification before final acceptance |
| **Blocked** (custom) | Stories with dependencies | Stories waiting on other work (US-010 depends on US-009) |
| **Done** | Stories fully completed | Finished work that can be demonstrated |

Work flows left to right: **Backlog → Ready → In progress → In review → Testing → Done**

If a story encounters a dependency (e.g., US-010 depends on US-009), it moves to the **Blocked** column. Once the dependency is resolved, it moves back to In progress.

---

## How the Board Limits Work-in-Progress (WIP)

Work-in-Progress limits prevent bottlenecks and context switching. My board has the following self-enforced WIP limits:

| Column | WIP Limit | Why |
|--------|-----------|-----|
| **In progress** | 2 stories | As a solo developer, I can only focus on 2 tasks at once. More than that leads to context switching and half-finished work. |
| **In review** | 1 story | Reviewing requires full attention. Only one story can be reviewed at a time. |
| **Testing** | 1 story | Testing requires focused attention. One story at a time ensures quality. |

### How WIP Limits Are Enforced

The board does not technically block moving cards beyond limits. Instead, I self-enforce:
- If In progress has 2 cards, I finish one before starting another
- If Testing has 1 card, I complete testing before moving another
- This prevents me from starting too many tasks at once

### Why WIP Limits Matter

Without WIP limits, solo developers often:
- Start too many tasks at once (context switching)
- Leave work half-finished
- Feel overwhelmed by too many active tasks
- Delay delivery because nothing gets completed

WIP limits force focus and completion before starting new work.

---

## How the Board Supports Agile Principles

| Agile Principle | How My Kanban Board Supports It |
|----------------|--------------------------------|
| **Continuous delivery** | Work flows continuously through columns. As soon as one story is Done, I pull the next from Backlog. |
| **Adaptability** | Stories can be reprioritized by dragging them up/down in the Backlog column. I can respond to changes quickly. |
| **Transparency** | Anyone looking at the board can see exactly what is in progress, what is blocked, and what is done. No hidden work. |
| **Inspect and adapt** | Daily review of the board shows my progress and identifies blockers. I can adapt my plan based on what I see. |
| **Sustainable pace** | WIP limits prevent me from overloading myself. I work at a sustainable pace without burnout. |
| **Working software** | The Testing column ensures that before a story is marked Done, it has been verified to work. |
| **Respect for people** | The board shows my workload clearly. I can ask for help when blocked. |

---

## Real-Time Visibility and Collaboration

Even as a solo developer, the board provides significant value:

**For myself:**
- **Self-accountability**: I can see what I committed to and what's incomplete
- **Progress tracking**: I know exactly what to work on next
- **Blocked visibility**: Stuck items are clearly marked and cannot be ignored
- **Sprint completion**: The Done column shows what I have achieved

**For stakeholders (professor, future team members):**
- **Transparency**: Anyone can see the exact status of every story
- **Trust**: The board shows real progress, not just claims
- **Communication**: Blocked items explain why work is delayed

---

## Customizations I Made

I added two custom columns to the default Kanban template:

| Custom Column | Reason for Adding |
|---------------|-------------------|
| **Testing** | The default template had no quality assurance stage. Without Testing, stories would move directly from In review to Done without verification, which could lead to bugs. |
| **Blocked** | The default template had no way to handle dependencies. US-010 (Book Study Room) depends on US-009 (Find Study Rooms). Without a Blocked column, US-010 would sit in In progress indefinitely, giving a false sense of progress. |

These customizations make the board more realistic for software development, where testing and dependencies are common.

---

## Comparison to Physical Kanban Boards

| Aspect | Physical Kanban Board | My GitHub Kanban Board |
|--------|----------------------|------------------------|
| **Location** | On a wall | Online (accessible anywhere) |
| **Cards** | Sticky notes | GitHub Issues |
| **Updates** | Manual (move sticky notes) | Manual (drag and drop) |
| **History** | Lost when cards are removed | Preserved in issue history |
| **Collaboration** | Requires being in same room | Anyone can view online |
| **Backup** | None (sticky notes can fall off) | Cloud-backed (GitHub servers) |

My GitHub Kanban board combines the simplicity of a physical board with the power of digital tools (issue tracking, assignments, labels).

---

## Conclusion

A Kanban board is more than columns and cards. It is a tool for visualizing work, limiting waste, and delivering value continuously. My board is customized for Smart Campus Connect's Sprint 1 with:

- **7 columns** representing the complete workflow (including custom Testing and Blocked columns)
- **WIP limits** (2 for In progress, 1 for Testing) that respect solo developer capacity
- **7 user stories** from Assignment 6 populated in the Backlog
- **Assignments** linking each story to me (@Amanda2026-crypto)

This board supports Agile principles of transparency, adaptability, sustainable pace, and continuous delivery. It gives me real-time visibility into my work and helps me focus on completing tasks before starting new ones.
