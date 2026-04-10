# Kanban Board Explanation

## What is a Kanban Board?

A Kanban board is a visual project management tool that tracks tasks across stages like "To Do," "In Progress," and "Done." It helps teams visualize workflow, limit work-in-progress, and deliver continuously.

## How My Board Visualizes Workflow

My board has 5 columns:

| Column | Purpose |
|--------|---------|
| Todo | Stories not yet started |
| In Progress | Stories actively being worked on |
| Testing | Stories completed but awaiting verification |
| Blocked | Stories that cannot proceed due to dependencies |
| Done | Stories fully completed |

Work moves left to right: Todo → In Progress → Testing → Done. If a story has a dependency, it moves to Blocked until resolved.

## How It Limits Work-in-Progress (WIP)

I have set self-enforced WIP limits:

| Column | WIP Limit | Reason |
|--------|-----------|--------|
| In Progress | 2 stories | As a solo developer, I can only focus on 2 tasks at once |
| Testing | 1 story | Testing requires full attention; one story at a time |

These limits prevent context switching and ensure tasks are completed before new ones are started.

## How It Supports Agile Principles

| Agile Principle | How My Board Supports It |
|----------------|-------------------------|
| Continuous delivery | Work flows continuously through columns |
| Adaptability | Stories can be reprioritized in Todo column |
| Transparency | Anyone can see the exact status of every story |
| Sustainable pace | WIP limits prevent overload |
| Working software | Testing column ensures verification before Done |
