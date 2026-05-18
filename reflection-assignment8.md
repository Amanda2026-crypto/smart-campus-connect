
---

# Reflection: Object State Modeling and Activity Workflow Modeling

---

## Challenge 1: Choosing the Right Number of States

**The Problem:** I didn't know how many states to include. Too few states lose important information. Too many states make the diagram unreadable.

**How I Solved It:** I focused on states that change what the user or system can do. For example, in User Account, "Verified" changes behavior (user can log in). "Email Sent" does not change behavior, so I omitted it.

**Lesson Learned:** Only model states that affect system behavior.

---

## Challenge 2: Adding Guard Conditions

**The Problem:** Some transitions depend on conditions. For example, "Available → Pending" only happens if the time slot is free. I wasn't sure how to show this.

**How I Solved It:** I added guard conditions in the transition tables. For example: "Transition to Confirmed only if no conflicts." This makes the diagram precise.

**Lesson Learned:** Guard conditions make state diagrams executable specifications.

---

## Challenge 3: Activity Diagram Swimlanes

**The Problem:** I initially put all actions in one swimlane. Then I realized activity diagrams should show who does what.

**How I Solved It:** I added swimlanes for User, Student, Faculty, Admin, Organizer, and System. Each workflow now clearly shows responsibilities.

**Lesson Learned:** Swimlanes are essential for understanding handoffs between actors.

---

## Challenge 4: Parallel Actions

**The Problem:** Some workflows have actions that can happen simultaneously (e.g., send email AND add to calendar). I didn't know how to show this.

**How I Solved It:** I used parallel branches in my activity diagrams. For Event Registration, I showed both actions happening at the same time.

**Lesson Learned:** Parallel actions improve efficiency and should be modeled explicitly.

---

## Challenge 5: Mapping to Prior Assignments

**The Problem:** Each diagram had to trace back to functional requirements (Assignment 4), use cases (Assignment 5), and user stories (Assignment 6).

**How I Solved It:** I added traceability tables at the end of each section. For example, "FR-09, UC-05, US-009, US-010" for Study Room Booking.

**Lesson Learned:** Traceability matrices ensure nothing is missed.

---

## State Diagrams vs. Activity Diagrams

| Aspect | State Diagram | Activity Diagram |
|--------|---------------|------------------|
| **Focus** | Object lifecycle | Process flow |
| **Question** | "What states can this object be in?" | "What steps happen to complete this task?" |
| **Example** | Booking: Available → Pending → Confirmed | Study Room Booking: Search → Select → Book → Confirm |

**When to use each:**
- **State diagrams:** Understanding how a specific object changes over time
- **Activity diagrams:** Understanding a process involving multiple actors

---

## What I Learned

1. **State granularity is about behavior, not events.** Only include states that change what the system does.

2. **Guard conditions make diagrams precise.** Without them, transitions are ambiguous.

3. **Swimlanes clarify responsibilities.** They show who does what and where handoffs happen.

4. **Parallel actions save time.** Modeling them explicitly helps identify optimization opportunities.

5. **Traceability is essential.** Without mapping back to requirements, you can't prove completeness.

---

## Conclusion

This assignment taught me how to model dynamic system behavior. The 8 state diagrams and 8 activity diagrams cover all critical objects and workflows in Smart Campus Connect. They trace back to functional requirements (Assignment 4), use cases (Assignment 5), and user stories (Assignment 6). The biggest challenge was choosing the right level of granularity, but the traceability tables kept me focused on what actually matters for my system.
