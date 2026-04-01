# Agile Planning Document: Smart Campus Connect

**Assignment 6**
**Amanda**
**April 1, 2026**

---

## Part 1: Product Backlog (Prioritized with MoSCoW)

### MoSCoW Prioritization Legend

| Priority | Meaning |
|----------|---------|
| **Must-have** | Essential for MVP; system cannot function without these |
| **Should-have** | Important but not critical; can be delivered after MVP |
| **Could-have** | Nice to have; adds value but not essential |
| **Won't-have** | Not for this release; future consideration |

---

### Product Backlog Table

| Story ID | User Story | MoSCoW Priority | Story Points | Dependencies | Justification |
|----------|------------|-----------------|--------------|--------------|---------------|
| US-001 | As a **student**, I want to **register using my CPUT email address** so that **I can create an account and access the system**. | Must-have | 3 | None | Without registration, users cannot access the system. This is the foundation. |
| US-002 | As a **student**, I want to **log in with my email and password** so that **I can securely access my student dashboard**. | Must-have | 2 | US-001 | Users need to authenticate after registration. High business value. |
| US-003 | As a **faculty member**, I want to **log in with my staff email and password** so that **I can access my course management dashboard**. | Must-have | 2 | US-001 | Faculty need access to manage courses. Equal priority to student login. |
| US-004 | As a **student**, I want to **view my enrolled courses** so that **I can see my class schedule and academic progress**. | Must-have | 3 | US-002 | Core academic feature. Students need to see their courses first. |
| US-005 | As a **student**, I want to **view my grades for each course** so that **I can track my academic performance**. | Must-have | 3 | US-004 | Students track performance. High demand feature. |
| US-009 | As a **student**, I want to **find available study rooms on campus** so that **I don't waste time walking to rooms that are already full**. | Must-have | 5 | None | High student pain point. Directly addresses stakeholder concern. |
| US-010 | As a **student**, I want to **book a study room for a specific time slot** so that **I can guarantee a space to study**. | Must-have | 3 | US-009 | Natural follow-up to finding rooms. Completes the feature. |
| US-012 | As a **student**, I want to **browse and register for campus events** so that **I don't miss activities I'm interested in**. | Should-have | 3 | US-002 | Students miss events due to poor discovery. High value but not MVP. |
| US-006 | As a **student**, I want to **submit assignments online** so that **I don't have to print and hand in physical papers**. | Should-have | 5 | US-004 | Eliminates paper submissions. Faculty and student benefit. |
| US-007 | As a **faculty member**, I want to **create and publish assignments** so that **students can submit their work digitally**. | Should-have | 5 | US-004 | Faculty need to create assignments before students can submit. |
| US-008 | As a **faculty member**, I want to **take attendance using QR codes** so that **I can save time and avoid manual errors**. | Should-have | 5 | US-003 | Faculty pain point. Manual attendance takes class time. |
| US-011 | As a **student**, I want to **track campus shuttles in real-time** so that **I can plan my commute and avoid waiting**. | Should-have | 5 | None | Students waste time waiting for shuttles. High frustration. |
| US-013 | As a **student**, I want to **create study groups for my courses** so that **I can collaborate with classmates**. | Could-have | 5 | US-004 | Social feature. Helps students collaborate. |
| US-014 | As a **student**, I want to **send messages in my study groups** so that **I can discuss coursework and share resources**. | Could-have | 3 | US-013 | Enables group communication. Follows group creation. |
| US-015 | As a **faculty member**, I want to **create events for my course** so that **I can notify students about guest lectures or deadlines**. | Could-have | 3 | US-003 | Faculty need to create events. |
| US-016 | As an **administrator**, I want to **approve or reject event submissions** so that **only appropriate events are published**. | Could-have | 3 | US-015 | Admin oversight needed for event quality. |
| US-017 | As a **student**, I want to **view my meal plan balance** so that **I know how many swipes I have left**. | Could-have | 2 | US-002 | Useful for students with meal plans. |
| US-018 | As a **student**, I want to **report a lost item** so that **I can increase my chances of getting it back**. | Won't-have | 2 | None | Nice to have. Not critical for MVP or next release. |
| US-019 | As a **system admin**, I want to **send emergency alerts to all users** so that **students and staff receive critical safety information**. | Won't-have | 3 | None | Important but can be added after core features work. |

---

### Product Backlog Summary

| MoSCoW Category | Number of Stories | Total Story Points |
|-----------------|-------------------|-------------------|
| Must-have | 7 | 21 |
| Should-have | 5 | 23 |
| Could-have | 5 | 16 |
| Won't-have | 2 | 5 |
| **Total** | **19** | **65** |

---

### Traceability to Stakeholder Concerns

| Stakeholder | Must-have Story | Justification |
|-------------|-----------------|---------------|
| Student | US-009 (Find Study Rooms) | Directly addresses pain point: wasted time finding spaces |
| Student | US-005 (View Grades) | Directly addresses need: tracking academic performance |
| Faculty | US-003 (Faculty Login) | Directly addresses need: access to course management |
| Faculty | US-007 (Create Assignment) | Directly addresses need: easy assignment posting |
| Admin | US-016 (Approve Event) | Directly addresses need: efficient event approval workflow |

---

## Part 2: Sprint Plan

### Sprint 1 Goal

**"Deliver a functional MVP that allows students to register, log in, view courses and grades, and find and book study rooms."**

### Sprint Duration: 2 weeks

### Selected Stories for Sprint 1 (Must-have)

| Story ID | User Story | MoSCoW Priority | Story Points | Acceptance Criteria |
|----------|------------|-----------------|--------------|---------------------|
| US-001 | Student registration with CPUT email | Must-have | 3 | User can register with valid CPUT email; verification email sent |
| US-002 | Student login with email and password | Must-have | 2 | User can log in; JWT token generated; dashboard loads |
| US-003 | Faculty login with staff email | Must-have | 2 | Faculty can log in; faculty dashboard loads |
| US-004 | View enrolled courses | Must-have | 3 | Student dashboard shows list of enrolled courses |
| US-005 | View grades for each course | Must-have | 3 | Grades displayed with assignment breakdown |
| US-009 | Find available study rooms | Must-have | 5 | Map shows available rooms; filters work |
| US-010 | Book a study room | Must-have | 3 | User can select time slot and confirm booking |

### Sprint 1 Total Story Points: 21

---

### Sprint Tasks Breakdown

| Story ID | Task | Effort (Hours) | Dependencies |
|----------|------|----------------|--------------|
| US-001 | Create registration API endpoint | 4 | Database setup |
| US-001 | Create registration UI screen | 3 | API endpoint |
| US-001 | Add email verification | 2 | Email service |
| US-002 | Create login API endpoint | 2 | User database |
| US-002 | Create login UI screen | 2 | API endpoint |
| US-002 | Implement JWT token generation | 2 | - |
| US-003 | Add role-based dashboard routing | 3 | Login functionality |
| US-004 | Create course enrollment table | 3 | Database schema |
| US-004 | Display courses on student dashboard | 2 | Course table |
| US-005 | Create grades table | 2 | Course enrollment |
| US-005 | Display grades with calculation | 2 | Grades data |
| US-009 | Integrate campus map API | 4 | Map service account |
| US-009 | Implement room availability query | 3 | Database |
| US-009 | Create filter UI | 2 | Map integration |
| US-010 | Create booking API endpoint | 3 | Room data |
| US-010 | Create booking confirmation UI | 2 | Booking API |
| Testing | Unit and integration tests | 5 | All features |
| Documentation | Update README and API docs | 3 | - |

### Sprint 1 Definition of Done

- [ ] Code completed and reviewed
- [ ] Unit tests passing (>80% coverage)
- [ ] Integration tests passing
- [ ] Feature works on mobile and desktop
- [ ] No critical bugs
- [ ] Deployed to staging environment
- [ ] Acceptance criteria met for all stories

### Sprint 1 Velocity

| Metric | Value |
|--------|-------|
| Planned story points | 21 |
| Team capacity | 1 developer (you) |
| Estimated completion | 2 weeks |

### Potential Risks and Mitigation

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Map API integration delays | Medium | High | Start map integration early in sprint |
| Email verification service issues | Low | Medium | Have fallback: show verification code in app |
| Database performance | Low | Medium | Use indexing from the start |
| Scope creep | High | High | Strictly follow selected stories; defer others |

---

## Summary of Artifacts

| Artifact | Location |
|----------|----------|
| Product Backlog | This document (Part 1) |
| Sprint Plan | This document (Part 2) |
| User Stories Table | GitHub Issues + Project Board |
| Reflection | [REFLECTION-ASSIGNMENT6.md](REFLECTION-ASSIGNMENT6.md) |
| GitHub Milestones | https://github.com/Amanda2026-crypto/smart-campus-connect/milestones |
| GitHub Project Board | https://github.com/Amanda2026-crypto/smart-campus-connect/projects |

---

## Traceability to Prior Assignments

| Assignment | Artifact | Location in This Document |
|------------|----------|---------------------------|
| Assignment 4 | Functional Requirements | Product Backlog justification column |
| Assignment 4 | Stakeholder Concerns | Traceability to stakeholder concerns table |
| Assignment 5 | Use Cases | Selected Sprint 1 stories map to UC-01, UC-05 |
| Assignment 5 | Use Case Specifications | Acceptance criteria align with use case flows |

---

## Conclusion

This Agile Planning Document compiles the Product Backlog (Part 1) and Sprint Plan (Part 2) into one file. The MVP (Sprint 1) delivers 7 must-have stories totaling 21 story points. This gives students immediate value while keeping the scope manageable for a single developer. The remaining stories are prioritized using MoSCoW for future sprints.
