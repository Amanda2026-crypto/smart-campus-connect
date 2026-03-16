# Functional Requirements: Smart Campus Connect

## Overview
This document defines 15+ functional requirements for the Smart Campus Connect system, organized by module with acceptance criteria.

---

## Module 1: User Management

### FR-01: User Registration
**Description:** The system shall allow users to register using their university email address.
**Rationale:** Ensures only verified university members can access the system.
**Acceptance Criteria:**
- Registration form accepts email, name, password, and role (student/faculty/admin)
- System sends verification email with unique link
- Account is activated only after email verification
- Duplicate email addresses are rejected with appropriate message
- Password must meet strength requirements (min 8 chars, 1 uppercase, 1 number, 1 special)

### FR-02: User Authentication
**Description:** The system shall authenticate users using email and password with JWT tokens.
**Rationale:** Secure access to system features based on user identity.
**Acceptance Criteria:**
- Login form accepts email and password
- Invalid credentials return appropriate error message
- Successful login returns JWT token valid for 24 hours
- Refresh token mechanism extends session up to 7 days
- "Remember me" option extends session to 30 days

### FR-03: Role-Based Access Control
**Description:** The system shall restrict access to features based on user roles (student, faculty, admin).
**Rationale:** Ensures users only access features appropriate to their role.
**Acceptance Criteria:**
- Students can view courses, grades, events, and campus maps
- Faculty can create assignments, take attendance, post announcements
- Admins can approve events, manage resources, send alerts
- Unauthorized access attempts return 403 error

---

## Module 2: Academic Management

### FR-04: Course Enrollment
**Description:** The system shall allow students to view and enroll in courses for the current semester.
**Rationale:** Students need to manage their course schedule digitally.
**Acceptance Criteria:**
- Students can browse all available courses by department
- Course details include code, name, credits, schedule, and instructor
- Enrollment confirmation is sent via email and in-app notification
- Students cannot enroll in courses with time conflicts
- Maximum enrollment limits are enforced

### FR-05: Grade Viewing
**Description:** The system shall display grades for enrolled courses to students.
**Rationale:** Students need real-time access to academic performance.
**Acceptance Criteria:**
- Grades are displayed by course with assignment breakdown
- Current GPA is calculated automatically
- Grade history is available for previous semesters
- Faculty can release grades individually or by course
- Students receive notification when new grades are posted

### FR-06: Assignment Management
**Description:** The system shall allow faculty to create assignments and students to submit them digitally.
**Rationale:** Streamlines the assignment workflow for both parties.
**Acceptance Criteria:**
- Faculty can create assignments with title, description, due date, and max points
- Students can upload files (PDF, DOC, etc.) up to 50MB
- Late submissions are automatically marked and timestamped
- Faculty can grade submissions and provide feedback
- Students receive notifications for new assignments and grades

### FR-07: Attendance Tracking
**Description:** The system shall allow faculty to take attendance digitally and students to view their attendance records.
**Rationale:** Reduces manual work and provides transparency.
**Acceptance Criteria:**
- Faculty can mark attendance for each class session
- Attendance can be taken via QR code or manual entry
- Students can view their attendance percentage per course
- Automatic alerts sent when attendance falls below 75%
- Attendance reports can be exported as CSV

---

## Module 3: Campus Navigation

### FR-08: Interactive Campus Map
**Description:** The system shall provide an interactive map of campus buildings and facilities.
**Rationale:** Helps students navigate unfamiliar campus areas.
**Acceptance Criteria:**
- Map displays all buildings with labels
- Users can search for buildings by name or code
- Clicking a building shows details and available rooms
- Map supports zoom and pan gestures
- Indoor floor plans available for major buildings

### FR-09: Study Space Finder
**Description:** The system shall show real-time availability of study rooms and empty classrooms.
**Rationale:** Saves students time searching for study spaces.
**Acceptance Criteria:**
- Available rooms are color-coded on the map (green=available, red=occupied)
- Room details include capacity, amenities (projector, whiteboard)
- Users can filter by building, capacity, and amenities
- Rooms can be booked for up to 3 hours at a time
- Booking confirmation sent via notification

### FR-10: Shuttle Tracking
**Description:** The system shall provide real-time location and arrival predictions for campus shuttles.
**Rationale:** Reduces wait time and improves commute planning.
**Acceptance Criteria:**
- Shuttle locations shown on map with vehicle icons
- Estimated arrival times displayed for each stop
- Notifications sent for shuttle delays over 5 minutes
- Route information with all stops displayed
- Historical data for schedule optimization

---

## Module 4: Event Management

### FR-11: Event Creation and Discovery
**Description:** The system shall allow users to create, browse, and register for campus events.
**Rationale:** Centralizes event information and increases attendance.
**Acceptance Criteria:**
- Events include title, description, date/time, location, and organizer
- Users can browse events by category, date, and popularity
- Calendar view shows events by day/week/month
- Users receive reminders 24h and 1h before events
- Event capacity limits are enforced

### FR-12: Event Approval Workflow
**Description:** The system shall require admin approval for events before they are published.
**Rationale:** Ensures events meet campus guidelines and avoid scheduling conflicts.
**Acceptance Criteria:**
- Submitted events appear in admin approval queue
- Admins can approve, reject, or request changes
- Rejection includes reason for rejection
- Approved events are automatically published
- Organizer notified of approval status via email

---

## Module 5: Social Features

### FR-13: Study Group Creation
**Description:** The system shall allow students to create and join study groups for specific courses.
**Rationale:** Facilitates peer learning and collaboration.
**Acceptance Criteria:**
- Groups can be created with name, description, and max members
- Users can search for groups by course and join if space available
- Group creators can approve or reject join requests
- Each group has a discussion board for messaging
- Files can be shared within the group

### FR-14: In-App Messaging
**Description:** The system shall provide real-time messaging within study groups and between users.
**Rationale:** Enables seamless communication for collaboration.
**Acceptance Criteria:**
- Messages show sender, timestamp, and content
- Read receipts indicate when messages are seen
- Push notifications for new messages
- Users can mute notifications for specific groups
- Message history persists for the duration of the group

---

## Module 6: Lost and Found

### FR-15: Lost Item Reporting
**Description:** The system shall allow users to report lost items with descriptions and locations.
**Rationale:** Centralizes lost and found information to increase recovery chances.
**Acceptance Criteria:**
- Report form includes item name, description, category, date lost, location
- Optional photo upload up to 10MB
- Items appear in searchable lost items database
- User receives notification when matching found item is reported
- Reports expire after 30 days with renewal option

### FR-16: Found Item Reporting
**Description:** The system shall allow users to report found items to help reunite them with owners.
**Rationale:** Encourages community responsibility and item recovery.
**Acceptance Criteria:**
- Report form includes item description, location found, date
- Optional photo upload and storage location
- System automatically checks for matching lost items
- Matches trigger notifications to both parties
- Items marked as claimed when returned

---

## Module 7: Meal Plan Management

### FR-17: Meal Plan Balance Tracking
**Description:** The system shall display current meal plan balance and transaction history.
**Rationale:** Helps students manage dining funds effectively.
**Acceptance Criteria:**
- Dashboard shows remaining swipes and dining dollars
- Transaction history shows date, location, and amount
- Low balance alerts at 20% remaining
- Parents can view balance with student permission
- Automatic notifications for unusual activity

### FR-18: Cafeteria Menu Display
**Description:** The system shall display daily menus for campus dining locations.
**Rationale:** Helps students plan meals and dietary choices.
**Acceptance Criteria:**
- Menus show breakfast, lunch, and dinner options
- Dietary filters (vegetarian, vegan, gluten-free) available
- Nutritional information displayed where available
- Users can favorite dining locations
- Special event menus highlighted

---

## Functional Requirements Traceability Matrix

| Requirement | Student | Faculty | Admin | IT Staff | Priority |
|-------------|---------|---------|-------|----------|----------|
| FR-01: Registration | ✓ | ✓ | ✓ | | High |
| FR-02: Authentication | ✓ | ✓ | ✓ | | High |
| FR-03: Role-Based Access | ✓ | ✓ | ✓ | ✓ | High |
| FR-04: Course Enrollment | ✓ | | | | High |
| FR-05: Grade Viewing | ✓ | ✓ | | | High |
| FR-06: Assignment Management | ✓ | ✓ | | | High |
| FR-07: Attendance Tracking | ✓ | ✓ | | | Medium |
| FR-08: Interactive Map | ✓ | | | | Medium |
| FR-09: Study Space Finder | ✓ | | | | High |
| FR-10: Shuttle Tracking | ✓ | | | | Medium |
| FR-11: Event Creation | ✓ | ✓ | ✓ | | High |
| FR-12: Event Approval | | | ✓ | | High |
| FR-13: Study Groups | ✓ | | | | Medium |
| FR-14: Messaging | ✓ | ✓ | | | Medium |
| FR-15: Lost Items | ✓ | | | | Low |
| FR-16: Found Items | ✓ | | | | Low |
| FR-17: Meal Plan | ✓ | | | ✓ | Medium |
| FR-18: Cafeteria Menu | ✓ | | | | Low |
