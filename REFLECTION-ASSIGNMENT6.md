# Reflection: Agile Planning Challenges

**Assignment 6**
**Amanda**
**April 1, 2026**

---

## Introduction

As the sole stakeholder, product owner, and developer for Smart Campus Connect, I faced unique challenges in translating requirements into Agile artifacts. This reflection documents the internal resistance and difficult decisions I encountered during prioritization, estimation, and alignment of Agile practices with stakeholder needs.

---

## Challenge 1: Prioritizing Alone Without External Stakeholders

**The Problem:**
In real Agile teams, product owners negotiate priorities with stakeholders who have competing interests. Here, I had to play both roles. I found myself constantly arguing internally: "Should I prioritize what users actually need, or what I find technically interesting to build?"

I was tempted to prioritize US-011 (Shuttle Tracking) because it's technically interesting with real-time maps. But Assignment 4's stakeholder analysis clearly showed students' biggest pain point is wasted time finding study spaces, not waiting for shuttles.

**How I Overcame It:**
I physically printed the stakeholder analysis table from Assignment 4 and kept it on my desk. Every time I felt tempted to prioritize a "cool" feature, I asked: "Does this address a stated pain point from Assignment 4?"

The answer for US-009 (Find Study Rooms) was YES — students explicitly said they waste time walking to full rooms. For US-011 (Shuttle Tracking), the pain point existed but was less urgent. I forced myself to prioritize based on documented stakeholder needs, not my technical curiosity.

---

## Challenge 2: Breaking Down Stories to the Right Size

**The Problem:**
The INVEST principle requires stories to be "Small," but I struggled with sizing. US-006 (Submit Assignments) initially felt too big — it involves file uploads, virus scanning, storage, notifications, and late submission handling. I was tempted to split it into "Upload file" and "Submit assignment" but that would lose user value.

**How I Overcame It:**
I applied the "vertical slice" principle. Each story must deliver end-to-end value. US-006 as one story means a student can upload AND submit AND get confirmation. Splitting it would mean the student can upload but not submit — that's not valuable.

I accepted that some stories are 5 points (2-3 days) and that's acceptable for a solo developer. The key is ensuring each story is independently valuable.

---

## Challenge 3: Technical Debt vs. User Value

**The Problem:**
I wanted to include technical stories like "Set up database indexing," "Implement logging framework," and "Add monitoring dashboards." But Agile user stories must deliver user value. These don't translate to "As a user, I want database indexing."

**How I Overcame It:**
I kept technical tasks as subtasks within user stories. For example:
- US-004 (View Courses): Includes database indexing task
- US-009 (Find Study Rooms): Includes map API optimization task
- All stories: Include logging task for that feature

This ensures technical work is done but not presented as separate "user stories" that would clutter the backlog with non-user-facing items.

---

## Challenge 4: Estimating Without Historical Data

**The Problem:**
Agile teams use velocity from previous sprints to estimate. As a first-time solo Agile planner, I had no historical data. I was guessing.

US-009 (Find Study Rooms) felt like a 5 because it requires map integration, real-time availability queries, and filters. But was that realistic? I had no way to know.

**How I Overcame It:**
I used the Fibonacci sequence (1,2,3,5,8) and compared complexity to simpler stories:
- US-001 (Registration): 3 points (standard CRUD)
- US-008 (QR Attendance): 5 points (camera integration, real-time validation)
- US-009 (Study Rooms): 5 points (map API, real-time availability, filters)

I added 20% padding for unknowns. If I finish early, I pull the next story from the backlog. If I'm late, the padding absorbs the delay.

---

## Challenge 5: MVP vs. Perfectionism

**The Problem:**
My perfectionist voice kept saying: "But you can't release without event registration! Or study groups! Or lost and found!" I was tempted to add more stories to Sprint 1, which would have made it 8+ weeks instead of 2 weeks.

**How I Overcame It:**
I reminded myself of the Agile Manifesto principle: "Deliver working software frequently." The MVP must be the smallest thing that delivers value. Sprint 1's 7 stories deliver:
- Students can register and log in ✅
- Students can see their courses and grades ✅
- Students can find and book study rooms ✅

That's actual value delivered in 2 weeks. Everything else can wait for Sprint 2, 3, and 4. If I delayed to add more, students would have nothing for weeks.

---

## Challenge 6: Mapping User Stories to Requirements

**The Problem:**
Assignment 4 had 18 functional requirements. Assignment 5 had 8 use cases. I needed to ensure all were covered by user stories without creating redundant stories.

**How I Overcame It:**
I created a traceability matrix:
- FR-01 → US-001
- FR-02 → US-002, US-003
- FR-04 → US-004
- FR-05 → US-005
- FR-06 → US-006, US-007
- FR-07 → US-008
- FR-09 → US-009, US-010
- FR-11 → US-012, US-015
- FR-12 → US-016
- FR-13 → US-013
- FR-14 → US-014
- FR-17 → US-017
- FR-15 → US-018
- NFR-09 → US-019

This ensured complete coverage. I added the traceability column in my user stories table to prove each story maps to a requirement.

---

## Lesson Learned

Agile planning alone is harder than with a real team. There's no one to challenge your assumptions, push back on estimates, or advocate for different stakeholders. I had to be brutally honest with myself about what truly delivers value versus what I simply wanted to build.

The discipline of writing user stories in the "As a... I want... so that..." format forced me to justify every story. If I couldn't articulate the "so that" benefit clearly, I removed the story from the backlog.

I also learned that technical work can be hidden in subtasks. Users don't care about database indexing — they care that grades load quickly. My job is to deliver that experience, not to show off technical complexity in the backlog.

---

## Conclusion

This exercise taught me that Agile is not about following rituals. It's about delivering value early and often. Sprint 1's MVP of 7 stories delivers tangible value to students and faculty. The remaining stories are prioritized in the backlog for future sprints.

The hardest part was resisting my own perfectionism and technical curiosity. But if I had added all 19 stories to Sprint 1, I would have nothing to show for weeks. Instead, in 2 weeks, I have a working registration, login, course view, grade view, and study room finder.

That's real value. That's Agile.
