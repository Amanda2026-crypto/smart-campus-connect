# Reflection: Agile Planning Challenges

**Assignment 6**
**Amanda**
**April 1, 2026**

## Challenge 1: Prioritizing Alone Without Stakeholder Input

As the only person working on this project (playing both product owner and developer), I faced significant internal resistance when prioritizing stories. There was no external stakeholder to push back or validate my decisions. I had to constantly ask myself: "Am I prioritizing what users actually need, or what I want to build?"

I overcame this by returning to Assignment 4's stakeholder analysis. I reminded myself that students' biggest pain point is wasted time (finding study rooms, waiting for shuttles). Faculty's biggest pain point is manual attendance. I prioritized US-009 (Find Study Rooms) high because it directly addresses student frustration, even though it's technically complex (5 story points).

## Challenge 2: Breaking Down Stories to the Right Size

The INVEST principle requires stories to be "Small," but I struggled with sizing. US-006 (Submit assignments) felt too big initially because it involves file uploads, validation, storage, and notifications. I had to resist splitting it further because it would lose its "Valuable" property.

I accepted that some stories are 5 points (2-3 days of work) and that's acceptable. I ensured each story delivers a complete piece of value to the user, not just a technical task.

## Challenge 3: Balancing Technical and User-Centric Stories

I wanted to include technical stories like "Set up database indexing" and "Implement logging framework." But Agile focuses on user value. These technical tasks don't translate to user stories directly.

I kept technical tasks as subtasks within user stories. For example, database indexing is a task under US-004 (View courses) because it enables that feature to perform well. I didn't create separate user stories for infrastructure.

## Challenge 4: Estimating Without Historical Data

With no previous sprints to reference, I had to guess story points. This felt risky because I could underestimate complex features like QR code attendance (US-008).

I used the Fibonacci sequence (1,2,3,5,8) and compared complexity to simpler stories. US-001 (registration) is a 3 because it's standard CRUD. US-008 (QR attendance) is a 5 because it requires camera integration and real-time validation. I added padding for unknowns.

## Challenge 5: Staying True to MVP

The MVP should be the smallest thing that delivers value. I was tempted to add more stories to Sprint 1 (like event registration or study groups). But adding them would delay the core features.

I reminded myself that an MVP that doesn't work is worthless. I kept Sprint 1 focused on registration, login, courses, grades, and study rooms. If these work, users can immediately benefit. Everything else can wait for Sprint 2.

## Lesson Learned

Agile planning alone is difficult because there's no one to challenge your assumptions. But it forced me to think deeply about what "value" means for each user type. The discipline of writing user stories (As a... I want... so that...) kept me focused on outcomes, not outputs.
