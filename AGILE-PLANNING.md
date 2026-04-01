# Agile Planning Document: Smart Campus Connect

**Assignment 6**
**Amanda**
**April 1, 2026**

---

## Part 1: User Stories

### User Stories Table

| Story ID | User Story (As a... I want... so that...) | INVEST Check | Story Points | Source (FR/UC) |
|----------|-------------------------------------------|--------------|--------------|----------------|
| US-001 | As a **student**, I want to **register using my CPUT email address** so that **I can create an account and access the system** | Independent, Valuable, Testable | 3 | FR-01 |
| US-002 | As a **student**, I want to **log in with my email and password** so that **I can securely access my dashboard** | Independent, Valuable, Estimable, Testable | 2 | FR-02 |
| US-003 | As a **faculty member**, I want to **log in with my staff email and password** so that **I can access my course management dashboard** | Independent, Valuable, Testable | 2 | FR-02 |
| US-004 | As a **student**, I want to **view my enrolled courses** so that **I can see my class schedule and academic progress** | Valuable, Small, Testable | 3 | FR-04, UC-01 |
| US-005 | As a **student**, I want to **view my grades for each course** so that **I can track my academic performance** | Valuable, Estimable, Testable | 3 | FR-05, UC-01 |
| US-006 | As a **student**, I want to **submit assignments online** so that **I don't have to print and hand in physical papers** | Independent, Valuable, Testable | 5 | FR-06, UC-02 |
| US-007 | As a **faculty member**, I want to **create and publish assignments** so that **students can submit their work digitally** | Independent, Valuable, Testable | 5 | FR-06, UC-04 |
| US-008 | As a **faculty member**, I want to **take attendance using QR codes** so that **I can save time and avoid manual errors** | Valuable, Estimable, Testable | 5 | FR-07, UC-03 |
| US-009 | As a **student**, I want to **find available study rooms on campus** so that **I don't waste time walking to full rooms** | Independent, Valuable, Testable | 5 | FR-09, UC-05 |
| US-010 | As a **student**, I want to **book a study room for a specific time slot** so that **I can guarantee a space to study** | Valuable, Small, Testable | 3 | FR-09, UC-05 |
| US-011 | As a **student**, I want to **track campus shuttles in real-time** so that **I can plan my commute and avoid waiting** | Independent, Valuable, Testable | 5 | FR-10 |
| US-012 | As a **student**, I want to **browse and register for campus events** so that **I don't miss activities I'm interested in** | Independent, Valuable, Testable | 3 | FR-11, UC-06 |
| US-013 | As a **student**, I want to **create study groups for my courses** so that **I can collaborate with classmates** | Independent, Valuable, Testable | 5 | FR-13, UC-07 |
| US-014 | As a **student**, I want to **send messages in my study groups** so that **I can discuss coursework and share resources** | Valuable, Small, Testable | 3 | FR-14 |
| US-015 | As a **faculty member**, I want to **create events for my course** so that **I can notify students about guest lectures or deadlines** | Independent, Valuable, Testable | 3 | FR-11 |
| US-016 | As an **administrator**, I want to **approve or reject event submissions** so that **only appropriate events are published** | Independent, Valuable, Testable | 3 | FR-12, UC-08 |
| US-017 | As a **student**, I want to **view my meal plan balance** so that **I know how many swipes I have left** | Independent, Valuable, Testable | 2 | FR-17 |
| US-018 | As a **student**, I want to **report a lost item** so that **I can increase my chances of getting it back** | Independent, Small, Testable | 2 | FR-15 |
| US-019 | As a **system admin**, I want to **send emergency alerts to all users** so that **students and staff receive critical safety information** | Independent, Valuable, Testable | 3 | FR-12, NFR-09 |

---

### INVEST Criteria Validation

| Story ID | Independent | Negotiable | Valuable | Estimable | Small | Testable | Status |
|----------|-------------|------------|----------|-----------|-------|----------|--------|
| US-001 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Pass |
| US-002 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Pass |
| US-003 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Pass |
| US-004 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Pass |
| US-005 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Pass |
| US-006 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Pass |
| US-007 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Pass |
| US-008 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Pass |
| US-009 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Pass |
| US-010 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Pass |
| US-011 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Pass |
| US-012 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Pass |
| US-013 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Pass |
| US-014 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Pass |
| US-015 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Pass |
| US-016 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Pass |
| US-017 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Pass |
| US-018 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Pass |
| US-019 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | Pass |

---

### Traceability to Assignments 4 and 5

| User Story | Functional Requirement (Assignment 4) | Use Case (Assignment 5) |
|------------|---------------------------------------|------------------------|
| US-001 | FR-01 (User Registration) | - |
| US-002 | FR-02 (User Authentication) | - |
| US-003 | FR-02 (User Authentication) | - |
| US-004 | FR-04 (Course Enrollment) | UC-01 (View Grades) |
| US-005 | FR-05 (Grade Viewing) | UC-01 (View Grades) |
| US-006 | FR-06 (Assignment Management) | UC-02 (Submit Assignment) |
| US-007 | FR-06 (Assignment Management) | UC-04 (Create Assignment) |
| US-008 | FR-07 (Attendance Tracking) | UC-03 (Take Attendance) |
| US-009 | FR-09 (Study Space Finder) | UC-05 (Find Study Space) |
| US-010 | FR-09 (Study Space Finder) | UC-05 (Find Study Space) |
| US-011 | FR-10 (Shuttle Tracking) | - |
| US-012 | FR-11 (Event Creation and Discovery) | UC-06 (Register for Event) |
| US-013 | FR-13 (Study Group Creation) | UC-07 (Create Study Group) |
| US-014 | FR-14 (In-App Messaging) | - |
| US-015 | FR-11 (Event Creation and Discovery) | - |
| US-016 | FR-12 (Event Approval Workflow) | UC-08 (Approve Event) |
| US-017 | FR-17 (Meal Plan Balance Tracking) | - |
| US-018 | FR-15 (Lost Item Reporting) | - |
| US-019 | NFR-09 (Security) | - |

---

## Part 2: Sprint Plan

### Sprint 1 Goal

**"Deliver a functional MVP that allows students to register, log in, view courses and grades, and find study rooms."**

### Sprint Duration: 2 weeks

### Selected Stories for Sprint 1

| Story ID | User Story | Story Points | Acceptance Criteria |
|----------|------------|--------------|---------------------|
| US-001 | Student registration with CPUT email | 3 | User can register with valid CPUT email; verification email sent |
| US-002 | Student login with email and password | 2 | User can log in; JWT token generated; dashboard loads |
| US-003 | Faculty login with staff email | 2 | Faculty can log in; faculty dashboard loads |
| US-004 | View enrolled courses | 3 | Student dashboard shows list of enrolled courses |
| US-005 | View grades for each course | 3 | Grades displayed with assignment breakdown |
| US-009 | Find available study rooms | 5 | Map shows available rooms; filters work |
| US-010 | Book a study room | 3 | User can select time slot and confirm booking |

### Sprint 1 Total Story Points: 21

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

## Summary of Deliverables

| Deliverable | Location |
|-------------|----------|
| User Stories Table | This document (Part 1) |
| Sprint Plan | This document (Part 2) |
| Product Backlog | [PRODUCT-BACKLOG.md](PRODUCT-BACKLOG.md) |
| Reflection | [REFLECTION-ASSIGNMENT6.md](REFLECTION-ASSIGNMENT6.md) |
| GitHub Issues | https://github.com/Amanda2026-crypto/smart-campus-connect/issues |
| GitHub Milestones | https://github.com/Amanda2026-crypto/smart-campus-connect/milestones |
| GitHub Project Board | https://github.com/Amanda2026-crypto/smart-campus-connect/projects |

---

## Conclusion

This Agile planning document translates 19 user stories from Assignments 4 and 5 into a prioritized backlog and a focused 2-week sprint. The MVP (Sprint 1) delivers registration, login, course viewing, grade viewing, and study room booking. This gives students immediate value while keeping the scope manageable for a single developer.
