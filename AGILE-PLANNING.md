# Agile Planning Document: Smart Campus Connect

**Assignment 6**
**Amanda**
**April 4, 2026**

---

## Part 1: User Stories Table

| Story ID | User Story | Acceptance Criteria | Priority (High/Medium/Low) |
|----------|------------|---------------------|---------------------------|
| US-001 | As a **student**, I want to **register using my CPUT email address** so that **I can create an account and access the system**. | Account created; verification email sent within 60 seconds; error for invalid email | High |
| US-002 | As a **student**, I want to **log in with my email and password** so that **I can securely access my student dashboard**. | Login successful in <3 seconds; JWT token generated; dashboard loads | High |
| US-003 | As a **faculty member**, I want to **log in with my staff email and password** so that **I can access my course management dashboard**. | Login successful; faculty dashboard loads with courses to manage | High |
| US-004 | As a **student**, I want to **view my enrolled courses** so that **I can see my class schedule and academic progress**. | Dashboard shows list of enrolled courses with code, name, credits, instructor | High |
| US-005 | As a **student**, I want to **view my grades for each course** so that **I can track my academic performance**. | Grades displayed with assignment breakdown; GPA calculated | High |
| US-006 | As a **student**, I want to **submit assignments online** so that **I don't have to print and hand in physical papers**. | File upload up to 50MB; submission confirmed; timestamp recorded | Medium |
| US-007 | As a **faculty member**, I want to **create and publish assignments** so that **students can submit their work digitally**. | Assignment created with title, description, due date; notifications sent | Medium |
| US-008 | As a **faculty member**, I want to **take attendance using QR codes** so that **I can save time and avoid manual errors**. | QR code generated; student scan marks attendance; record saved | Medium |
| US-009 | As a **student**, I want to **find available study rooms on campus** so that **I don't waste time walking to rooms that are already full**. | Map shows available rooms color-coded; filters by building, capacity, time | High |
| US-010 | As a **student**, I want to **book a study room for a specific time slot** so that **I can guarantee a space to study**. | Booking confirmed; notification sent; appears in "My Bookings" | High |
| US-011 | As a **student**, I want to **track campus shuttles in real-time** so that **I can plan my commute and avoid waiting**. | Map shows shuttle locations; arrival predictions displayed; updates every 5 seconds | Medium |
| US-012 | As a **student**, I want to **browse and register for campus events** so that **I don't miss activities I'm interested in**. | Events listed by date/category; registration confirmed; calendar invite added | Medium |
| US-013 | As a **student**, I want to **create study groups for my courses** so that **I can collaborate with classmates**. | Group created; student set as admin; discussion board available | Low |
| US-014 | As a **student**, I want to **send messages in my study groups** so that **I can discuss coursework and share resources**. | Message appears in thread; all members receive push notification | Low |
| US-015 | As a **faculty member**, I want to **create events for my course** so that **I can notify students about guest lectures or deadlines**. | Event created; students enrolled in course receive notification | Low |
| US-016 | As an **administrator**, I want to **approve or reject event submissions** so that **only appropriate events are published**. | Pending events appear in queue; approval/rejection sends notification to organizer | Medium |
| US-017 | As a **student**, I want to **view my meal plan balance** so that **I know how many swipes I have left**. | Balance displays remaining swipes and dining dollars; transaction history shown | Low |
| US-018 | As a **student**, I want to **report a lost item** so that **I can increase my chances of getting it back**. | Report created with description, photo, location; notification if matched | Low |
| US-019 | As a **system admin**, I want to **send emergency alerts to all users** so that **students and staff receive critical safety information**. | Alert sent via push notification and email; delivered within 1 minute | Medium |

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

## Part 2: Product Backlog (Prioritized with MoSCoW)

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
| US-001 | Student registration with CPUT email | Must-have | 3 | None | Without registration, users cannot access the system |
| US-002 | Student login with email and password | Must-have | 2 | US-001 | Users need to authenticate after registration |
| US-003 | Faculty login with staff email | Must-have | 2 | US-001 | Faculty need access to manage courses |
| US-004 | View enrolled courses | Must-have | 3 | US-002 | Core academic feature |
| US-005 | View grades for each course | Must-have | 3 | US-004 | Students track performance |
| US-009 | Find available study rooms | Must-have | 5 | None | High student pain point |
| US-010 | Book a study room | Must-have | 3 | US-009 | Completes the study room feature |
| US-012 | Browse and register for campus events | Should-have | 3 | US-002 | High value but not MVP |
| US-006 | Submit assignments online | Should-have | 5 | US-004 | Eliminates paper submissions |
| US-007 | Create and publish assignments | Should-have | 5 | US-004 | Faculty need to create assignments |
| US-008 | Take attendance using QR codes | Should-have | 5 | US-003 | Faculty pain point |
| US-011 | Track campus shuttles in real-time | Should-have | 5 | None | Reduces waiting time |
| US-013 | Create study groups | Could-have | 5 | US-004 | Social feature |
| US-014 | Send messages in study groups | Could-have | 3 | US-013 | Enables group communication |
| US-015 | Create events for course | Could-have | 3 | US-003 | Faculty need to create events |
| US-016 | Approve or reject event submissions | Could-have | 3 | US-015 | Admin oversight needed |
| US-017 | View meal plan balance | Could-have | 2 | US-002 | Useful for students |
| US-018 | Report a lost item | Won't-have | 2 | None | Future consideration |
| US-019 | Send emergency alerts | Won't-have | 3 | None | Future consideration |

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

---

## Part 3: Sprint Plan

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

---

### Sprint 1 Definition of Done

- [ ] Code completed and reviewed
- [ ] Unit tests passing (>80% coverage)
- [ ] Integration tests passing
- [ ] Feature works on mobile and desktop
- [ ] No critical bugs
- [ ] Deployed to staging environment
- [ ] Acceptance criteria met for all stories

---

### Sprint 1 Velocity

| Metric | Value |
|--------|-------|
| Planned story points | 21 |
| Team capacity | 1 developer (you) |
| Estimated completion | 2 weeks |

---

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
| User Stories Table | This document (Part 1) |
| Product Backlog | This document (Part 2) |
| Sprint Plan | This document (Part 3) |
| Reflection | [REFLECTION-ASSIGNMENT6.md](REFLECTION-ASSIGNMENT6.md) |
| GitHub Issues + Project Board | https://github.com/Amanda2026-crypto/smart-campus-connect/issues |

---

## Conclusion

This Agile Planning Document compiles all three required artifacts into one file:
1. User Stories Table (19 stories with acceptance criteria)
2. Product Backlog (MoSCoW prioritization with story points)
3. Sprint Plan (2-week sprint with 7 must-have stories)

The MVP delivers registration, login, course viewing, grade viewing, and study room booking.
