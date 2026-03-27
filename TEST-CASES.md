# Test Cases: Smart Campus Connect

## Functional Test Cases

| Test Case ID | Requirement ID | Description | Steps | Expected Result | Actual Result | Status |
|--------------|----------------|-------------|-------|-----------------|----------------|--------|
| TC-FR-001 | FR-01 - User Registration | Student registration with valid student email | 1. Open app<br>2. Click Register<br>3. Select role: Student<br>4. Enter: Amanda Duma, 123456789@mycput.ac.za, CampusConnect2025!<br>5. Confirm password<br>6. Submit | Account created; verification email sent within 60 seconds | | |
| TC-FR-002 | FR-01 - User Registration | Faculty registration with valid staff email | 1. Open app<br>2. Click Register<br>3. Select role: Faculty<br>4. Enter: Dr John Smith, 987654321@mycput.ac.za, SecurePass2025!<br>5. Confirm password<br>6. Submit | Account created; verification email sent within 60 seconds | | |
| TC-FR-003 | FR-01 - User Registration | Registration with invalid email domain | 1. Open app<br>2. Click Register<br>3. Enter: Amanda Duma, amanda.duma@gmail.com, CampusConnect2025!<br>4. Submit | Error: "Please use your CPUT email address (@mycput.ac.za)" | | |
| TC-FR-004 | FR-01 - User Registration | Registration with existing email | 1. Open app<br>2. Click Register<br>3. Enter: Amanda Duma, 123456789@mycput.ac.za, CampusConnect2025!<br>4. Submit | Error: "Account already exists. Please login or reset password." | | |
| TC-FR-005 | FR-01 - User Registration | Weak password validation | 1. Open app<br>2. Click Register<br>3. Enter: Amanda Duma, 123456789@mycput.ac.za, abc123<br>4. Submit | Error: "Password must contain at least 8 characters, 1 uppercase, 1 number, and 1 special character" | | |
| TC-FR-006 | FR-02 - User Authentication | Student login with valid credentials | 1. Open app<br>2. Enter: 123456789@mycput.ac.za, CampusConnect2025!<br>3. Click Login | Login successful in <3 seconds; student dashboard loads with courses and balance | | |
| TC-FR-007 | FR-02 - User Authentication | Faculty login with valid credentials | 1. Open app<br>2. Enter: 987654321@mycput.ac.za, SecurePass2025!<br>3. Click Login | Login successful in <3 seconds; faculty dashboard loads with courses to manage | | |
| TC-FR-008 | FR-02 - User Authentication | Login with invalid password | 1. Open app<br>2. Enter: 123456789@mycput.ac.za, WrongPass<br>3. Click Login | Error: "Email or password incorrect" | | |
| TC-FR-009 | FR-02 - User Authentication | 5 failed login attempts | 1. Attempt login with wrong password 5 times using same email | Account locked for 15 minutes; error message: "Too many failed attempts. Try again in 15 minutes" | | |
| TC-FR-010 | FR-02 - User Authentication | "Remember Me" functionality | 1. Login with "Remember Me" checked<br>2. Close app<br>3. Reopen app | User remains logged in; dashboard loads directly | | |
| TC-FR-011 | FR-04 - Course Enrollment | Student enroll in available course | 1. Student logs in (123456789@mycput.ac.za)<br>2. Click "Courses" tab<br>3. Select "Software Engineering 301"<br>4. Click "Enroll" | Course added to schedule; confirmation: "You have successfully enrolled in Software Engineering 301" | | |
| TC-FR-012 | FR-04 - Course Enrollment | Student enroll in full course | 1. Student logs in<br>2. Select course at capacity (CS101)<br>3. Click "Enroll" | Error: "CS101 is full. You have been added to the waitlist (position 3)" | | |
| TC-FR-013 | FR-05 - Grade Viewing | Student view grades | 1. Student logs in (123456789@mycput.ac.za)<br>2. Click "Grades"<br>3. Select "Software Engineering 301" | Grades displayed: Assignment 1: 85%, Assignment 2: 92%, Midterm: 78%; Current grade: 84% (B) | | |
| TC-FR-014 | FR-06 - Assignment Submission | Student submit assignment before due date | 1. Student logs in<br>2. Navigate to "Assignments"<br>3. Select "Assignment 3 - System Design"<br>4. Upload "assignment3.pdf"<br>5. Click "Submit" | Submission confirmed; timestamp recorded; notification sent to faculty | | |
| TC-FR-015 | FR-06 - Assignment Submission | Student submit after due date | 1. Student logs in<br>2. Select past-due assignment (due: 2026-03-20)<br>3. Upload file<br>4. Click "Submit" | Warning: "This submission is LATE"; upon confirm, marked "Late" and faculty notified | | |
| TC-FR-016 | FR-07 - Attendance Tracking | Faculty mark attendance via QR code | 1. Faculty logs in (987654321@mycput.ac.za)<br>2. Select "Software Engineering 301"<br>3. Click "Take Attendance"<br>4. Generate QR code<br>5. Student scans code using app | Student marked present; timestamp recorded; attendance updated | | |
| TC-FR-017 | FR-09 - Study Space Finder | Student find available study room | 1. Student logs in (123456789@mycput.ac.za)<br>2. Click "Study Spaces"<br>3. Select building: "Engineering Building"<br>4. Select time: "Today 14:00-16:00"<br>5. Click "Search" | Available rooms displayed: Room E-203 (capacity 6), Room E-305 (capacity 8), both with whiteboard | | |
| TC-FR-018 | FR-09 - Study Space Finder | Student book study room | 1. Student logs in<br>2. Select available room (E-203)<br>3. Choose time slot: 14:00-17:00<br>4. Click "Book" | Booking confirmed; notification: "Room E-203 booked for March 27, 14:00-17:00" | | |
| TC-FR-019 | FR-10 - Shuttle Tracking | Student view shuttle locations | 1. Student logs in (123456789@mycput.ac.za)<br>2. Click "Shuttle Tracker"<br>3. View map | Map displays all active shuttles with vehicle icons; locations update every 5 seconds | | |
| TC-FR-020 | FR-11 - Event Registration | Student register for campus event | 1. Student logs in<br>2. Click "Events"<br>3. Select "Career Fair 2026"<br>4. Click "Register" | Registration confirmed; calendar invite added; confirmation email sent | | |
| TC-FR-021 | FR-13 - Study Group Creation | Student create study group | 1. Student logs in (123456789@mycput.ac.za)<br>2. Select "Software Engineering 301"<br>3. Click "Create Study Group"<br>4. Enter: "SE301 Exam Prep", "Study for final exam, meet Wednesdays 15:00"<br>5. Click "Create" | Group created; student set as admin; discussion board available | | |
| TC-FR-022 | FR-14 - Messaging | Student send message in study group | 1. Join study group<br>2. Navigate to discussion board<br>3. Type: "Does anyone want to meet tomorrow?"<br>4. Click "Send" | Message appears in thread; all members receive push notification | | |
| TC-FR-023 | FR-17 - Meal Plan | Student view meal plan balance | 1. Student logs in (123456789@mycput.ac.za)<br>2. Click "Meal Plan" | Display: Remaining swipes: 32, Dining dollars: R450; transaction history shows last 10 swipes | | |
| TC-FR-024 | FR-17 - Meal Plan | Low balance alert | 1. Student with 5 remaining swipes logs in<br>2. Dashboard loads | Alert: "Low balance: Only 5 meal swipes remaining. Add funds to avoid interruption" | | |
| TC-FR-025 | FR-15 - Lost Item | Student report lost item | 1. Student logs in (123456789@mycput.ac.za)<br>2. Click "Lost & Found"<br>3. Click "Report Lost Item"<br>4. Enter: "Laptop charger", "MacBook USB-C charger, black", lost at "Library 2nd floor"<br>5. Upload photo<br>6. Click "Submit" | Report created; notification if matching found item reported | | |

---

## Non-Functional Test Cases

| Test Case ID | NFR ID | Description | Test Setup | Expected Result | Actual Result | Status |
|--------------|--------|-------------|------------|-----------------|----------------|--------|
| TC-NFR-001 | NFR-04 - Performance | API response time under load | Simulate 100 concurrent users making 10 requests each (1,000 total requests) using k6 load testing tool | 95% of requests complete in <500ms; 0% error rate | | |
| TC-NFR-002 | NFR-04 - Performance | Page load time | Use Lighthouse to measure homepage load on 4G connection | Load time ≤ 2 seconds; Lighthouse score >90 | | |
| TC-NFR-003 | NFR-04 - Performance | Real-time message delivery | Send message between two users; measure delivery delay using timestamp logs | Delivery ≤ 1 second (95th percentile) | | |
| TC-NFR-004 | NFR-05 - Scalability | Concurrent user support | Ramp up users from 100 to 1,200 over 5 minutes using JMeter; measure error rates | System maintains <5% error rate at 1,000 concurrent users | | |
| TC-NFR-005 | NFR-07 - Security | Data encryption at rest | Query database directly for user password fields | Passwords stored as bcrypt hash (not plaintext); no sensitive data unencrypted | | |
| TC-NFR-006 | NFR-07 - Security | TLS encryption verification | Use SSL Labs test tool to scan API endpoint | TLS 1.3 enforced; SSL Labs rating A or higher | | |
| TC-NFR-007 | NFR-08 - Security | Rate limiting enforcement | Send 150 API requests from same IP within 1 minute | Requests 101-150 return HTTP 429 (Too Many Requests) | | |
| TC-NFR-008 | NFR-08 - Security | Session timeout | Log in; remain inactive for 30 minutes; attempt to access protected page | Session expires; user redirected to login page | | |
| TC-NFR-009 | NFR-01 - Usability | New user onboarding time | Give new user (no training) tasks: register, enroll in course, find study room | User completes all tasks in <5 minutes | | |
| TC-NFR-010 | NFR-01 - Usability | Mobile responsiveness | Open app on iPhone 14 (iOS) and Samsung S23 (Android); test all features | All features accessible; no horizontal scroll; touch targets ≥44px | | |
| TC-NFR-011 | NFR-02 - Accessibility | Screen reader compatibility | Enable VoiceOver/TalkBack; navigate all pages | All elements announced correctly; alt text present; focus order logical | | |
| TC-NFR-012 | NFR-17 - Reliability | System uptime monitoring | Monitor system for 30 days; record any downtime | 99.9% uptime during academic hours (8am-10pm) | | |
| TC-NFR-013 | NFR-18 - Reliability | Data backup and recovery | Request point-in-time recovery from 15 minutes ago | Data restored within RPO 15min; RTO 4 hours | | |

---

## Test Execution Summary

| Category | Total Tests | Passed | Failed | Pending |
|----------|-------------|--------|--------|---------|
| Functional Tests | 25 | | | 25 |
| Non-Functional Tests | 13 | | | 13 |
| **Total** | **38** | | | **38** |
