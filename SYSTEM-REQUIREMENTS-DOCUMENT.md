# System Requirements Document
## Smart Campus Connect

**Version:** 1.0
**Date:** March 22, 2026
**Author:** Amanda
**Project:** Smart Campus Connect - Assignment 4

---

## 1. Stakeholder Analysis

| Stakeholder | Role | Key Concerns | Pain Points | Success Metrics |
|-------------|------|--------------|-------------|-----------------|
| **Student** | Primary user who uses the system for academic tracking, campus navigation, event discovery, and social connections | - Easy access to grades and assignments<br>- Finding empty study rooms quickly<br>- Discovering relevant campus events<br>- Connecting with classmates for study groups | - Multiple apps for different functions<br>- Missed events due to poor discovery<br>- Wasted time walking to full study rooms<br>- Difficulty finding study partners | - 30% reduction in time finding study spaces<br>- 50% increase in event attendance<br>- 4.5/5 app store rating<br>- 90% daily active users |
| **Faculty Member** | Professor or instructor who manages courses, takes attendance, and communicates with students | - Efficient attendance tracking<br>- Easy assignment posting and grading<br>- Quick communication with students<br>- Identifying at-risk students early | - Manual attendance taking wastes class time<br>- Students miss important announcements<br>- No centralized way to share course materials<br>- Difficulty tracking student performance | - 50% reduction in time spent on attendance<br>- 80% of students read announcements within 24h<br>- 100% course materials uploaded on time |
| **Administrator** | Staff member who manages campus resources, approves events, and sends alerts | - Optimal utilization of campus spaces<br>- Efficient event approval workflow<br>- Quick emergency communication<br>- Accurate resource allocation data | - No visibility into room utilization<br>- Manual event approval process is slow<br>- Cannot send targeted alerts<br>- Lack of data for planning | - 25% increase in room utilization<br>- Event approvals in <24 hours<br>- Emergency alerts reach 95% within 5 minutes |
| **IT Staff** | Technical team responsible for system maintenance, security, and integration | - System stability and uptime<br>- Easy integration with existing systems<br>- Quick bug fixes and updates<br>- Data security and backup | - Multiple systems to maintain<br>- Complex integrations with legacy systems<br>- Security vulnerabilities<br>- Slow deployment process | - 99.9% system uptime<br>- <1 hour response time for critical issues<br>- Successful integration with LMS<br>- Zero security breaches |
| **Parent** | Guardian who wants to monitor student progress and meal plan usage | - Visibility into student academic performance<br>- Monitoring meal plan balance and usage<br>- Receiving important campus alerts<br>- Communication with advisors | - Limited insight into student life<br>- Unexpected meal plan depletion<br>- Missing emergency notifications<br>- Difficulty reaching faculty | - Monthly academic progress reports<br>- Real-time meal plan alerts at 20% balance<br>- 100% emergency notification receipt |
| **Campus Security** | Staff responsible for campus safety and emergency response | - Real-time campus occupancy data<br>- Quick identification of incidents<br>- Integration with emergency systems<br>- Location tracking during emergencies | - No visibility into building occupancy<br>- Delayed incident reporting<br>- Manual emergency procedures<br>- Difficulty coordinating response | - 50% faster emergency response time<br>- Real-time occupancy data for all buildings<br>- Automated emergency alerts |
| **Event Organizer** | Student clubs or departments hosting campus events | - Easy event creation and promotion<br>- Accurate attendee tracking<br>- Feedback collection from attendees<br>- Budget tracking for events | - Low event attendance<br>- Manual attendee check-in<br>- No feedback from attendees<br>- Difficulty tracking event costs | - 40% increase in event attendance<br>- Digital check-in for all events<br>- 50% attendee feedback rate |
| **Facilities Management** | Staff responsible for building maintenance and cleaning | - Real-time room occupancy data<br>- Maintenance request tracking<br>- Cleaning schedule optimization<br>- Energy usage monitoring | - Cleaning empty rooms wastes resources<br>- Slow maintenance request process<br>- No data for cleaning schedules<br>- High energy costs | - 30% reduction in cleaning costs<br>- Maintenance requests completed in <48h<br>- 20% energy usage reduction |
| **Career Services** | Staff helping students with internships and jobs | - Tracking student skill development<br>- Promoting career events<br>- Connecting students with employers<br>- Monitoring graduate outcomes | - Limited student engagement<br>- Low attendance at career fairs<br>- Difficulty tracking student progress<br>- No alumni employment data | - 50% increase in career event attendance<br>- 80% of students complete skill profiles<br>- 90% graduate employment tracking |
| **Library Staff** | Staff managing library resources and study spaces | - Real-time study room availability<br>- Efficient book checkout system<br>- Tracking resource utilization<br>- Managing fines and fees | - Students frustrated by full study rooms<br>- Manual book checkouts take time<br>- No data on resource usage<br>- Difficulty collecting fines | - 40% increase in study room utilization<br>- Self-service book checkout for 80% of users<br>- 95% fine collection rate |

---

## 2. Functional Requirements

### Module 1: User Management

#### FR-01: User Registration
**Description:** The system shall allow users to register using their university email address.
**Rationale:** Ensures only verified university members can access the system.
**Acceptance Criteria:**
- Registration form accepts email, name, password, and role (student/faculty/admin)
- System sends verification email with unique link
- Account is activated only after email verification
- Duplicate email addresses are rejected with appropriate message
- Password must meet strength requirements (min 8 chars, 1 uppercase, 1 number, 1 special)

#### FR-02: User Authentication
**Description:** The system shall authenticate users using email and password with JWT tokens.
**Rationale:** Secure access to system features based on user identity.
**Acceptance Criteria:**
- Login form accepts email and password
- Invalid credentials return appropriate error message
- Successful login returns JWT token valid for 24 hours
- Refresh token mechanism extends session up to 7 days
- "Remember me" option extends session to 30 days

#### FR-03: Role-Based Access Control
**Description:** The system shall restrict access to features based on user roles (student, faculty, admin).
**Rationale:** Ensures users only access features appropriate to their role.
**Acceptance Criteria:**
- Students can view courses, grades, events, and campus maps
- Faculty can create assignments, take attendance, post announcements
- Admins can approve events, manage resources, send alerts
- Unauthorized access attempts return 403 error

---

### Module 2: Academic Management

#### FR-04: Course Enrollment
**Description:** The system shall allow students to view and enroll in courses for the current semester.
**Rationale:** Students need to manage their course schedule digitally.
**Acceptance Criteria:**
- Students can browse all available courses by department
- Course details include code, name, credits, schedule, and instructor
- Enrollment confirmation is sent via email and in-app notification
- Students cannot enroll in courses with time conflicts
- Maximum enrollment limits are enforced

#### FR-05: Grade Viewing
**Description:** The system shall display grades for enrolled courses to students.
**Rationale:** Students need real-time access to academic performance.
**Acceptance Criteria:**
- Grades are displayed by course with assignment breakdown
- Current GPA is calculated automatically
- Grade history is available for previous semesters
- Faculty can release grades individually or by course
- Students receive notification when new grades are posted

#### FR-06: Assignment Management
**Description:** The system shall allow faculty to create assignments and students to submit them digitally.
**Rationale:** Streamlines the assignment workflow for both parties.
**Acceptance Criteria:**
- Faculty can create assignments with title, description, due date, and max points
- Students can upload files (PDF, DOC, etc.) up to 50MB
- Late submissions are automatically marked and timestamped
- Faculty can grade submissions and provide feedback
- Students receive notifications for new assignments and grades

#### FR-07: Attendance Tracking
**Description:** The system shall allow faculty to take attendance digitally and students to view their attendance records.
**Rationale:** Reduces manual work and provides transparency.
**Acceptance Criteria:**
- Faculty can mark attendance for each class session
- Attendance can be taken via QR code or manual entry
- Students can view their attendance percentage per course
- Automatic alerts sent when attendance falls below 75%
- Attendance reports can be exported as CSV

---

### Module 3: Campus Navigation

#### FR-08: Interactive Campus Map
**Description:** The system shall provide an interactive map of campus buildings and facilities.
**Rationale:** Helps students navigate unfamiliar campus areas.
**Acceptance Criteria:**
- Map displays all buildings with labels
- Users can search for buildings by name or code
- Clicking a building shows details and available rooms
- Map supports zoom and pan gestures
- Indoor floor plans available for major buildings

#### FR-09: Study Space Finder
**Description:** The system shall show real-time availability of study rooms and empty classrooms.
**Rationale:** Saves students time searching for study spaces.
**Acceptance Criteria:**
- Available rooms are color-coded on the map (green=available, red=occupied)
- Room details include capacity, amenities (projector, whiteboard)
- Users can filter by building, capacity, and amenities
- Rooms can be booked for up to 3 hours at a time
- Booking confirmation sent via notification

#### FR-10: Shuttle Tracking
**Description:** The system shall provide real-time location and arrival predictions for campus shuttles.
**Rationale:** Reduces wait time and improves commute planning.
**Acceptance Criteria:**
- Shuttle locations shown on map with vehicle icons
- Estimated arrival times displayed for each stop
- Notifications sent for shuttle delays over 5 minutes
- Route information with all stops displayed
- Historical data for schedule optimization

---

### Module 4: Event Management

#### FR-11: Event Creation and Discovery
**Description:** The system shall allow users to create, browse, and register for campus events.
**Rationale:** Centralizes event information and increases attendance.
**Acceptance Criteria:**
- Events include title, description, date/time, location, and organizer
- Users can browse events by category, date, and popularity
- Calendar view shows events by day/week/month
- Users receive reminders 24h and 1h before events
- Event capacity limits are enforced

#### FR-12: Event Approval Workflow
**Description:** The system shall require admin approval for events before they are published.
**Rationale:** Ensures events meet campus guidelines and avoid scheduling conflicts.
**Acceptance Criteria:**
- Submitted events appear in admin approval queue
- Admins can approve, reject, or request changes
- Rejection includes reason for rejection
- Approved events are automatically published
- Organizer notified of approval status via email

---

### Module 5: Social Features

#### FR-13: Study Group Creation
**Description:** The system shall allow students to create and join study groups for specific courses.
**Rationale:** Facilitates peer learning and collaboration.
**Acceptance Criteria:**
- Groups can be created with name, description, and max members
- Users can search for groups by course and join if space available
- Group creators can approve or reject join requests
- Each group has a discussion board for messaging
- Files can be shared within the group

#### FR-14: In-App Messaging
**Description:** The system shall provide real-time messaging within study groups and between users.
**Rationale:** Enables seamless communication for collaboration.
**Acceptance Criteria:**
- Messages show sender, timestamp, and content
- Read receipts indicate when messages are seen
- Push notifications for new messages
- Users can mute notifications for specific groups
- Message history persists for the duration of the group

---

### Module 6: Lost and Found

#### FR-15: Lost Item Reporting
**Description:** The system shall allow users to report lost items with descriptions and locations.
**Rationale:** Centralizes lost and found information to increase recovery chances.
**Acceptance Criteria:**
- Report form includes item name, description, category, date lost, location
- Optional photo upload up to 10MB
- Items appear in searchable lost items database
- User receives notification when matching found item is reported
- Reports expire after 30 days with renewal option

#### FR-16: Found Item Reporting
**Description:** The system shall allow users to report found items to help reunite them with owners.
**Rationale:** Encourages community responsibility and item recovery.
**Acceptance Criteria:**
- Report form includes item description, location found, date
- Optional photo upload and storage location
- System automatically checks for matching lost items
- Matches trigger notifications to both parties
- Items marked as claimed when returned

---

### Module 7: Meal Plan Management

#### FR-17: Meal Plan Balance Tracking
**Description:** The system shall display current meal plan balance and transaction history.
**Rationale:** Helps students manage dining funds effectively.
**Acceptance Criteria:**
- Dashboard shows remaining swipes and dining dollars
- Transaction history shows date, location, and amount
- Low balance alerts at 20% remaining
- Parents can view balance with student permission
- Automatic notifications for unusual activity

#### FR-18: Cafeteria Menu Display
**Description:** The system shall display daily menus for campus dining locations.
**Rationale:** Helps students plan meals and dietary choices.
**Acceptance Criteria:**
- Menus show breakfast, lunch, and dinner options
- Dietary filters (vegetarian, vegan, gluten-free) available
- Nutritional information displayed where available
- Users can favorite dining locations
- Special event menus highlighted

---

## 3. Non-Functional Requirements

### 3.1 Usability

#### NFR-01: Mobile-First Design
**Description:** The system shall provide a responsive interface optimized for mobile devices.
**Target Metric:** ≤ 3s load on 4G; 44px touch targets
**Priority:** High

#### NFR-02: Accessibility Compliance
**Description:** The system shall comply with WCAG 2.1 AA accessibility standards.
**Target Metric:** Alt text for images; color contrast ratio 4.5:1; keyboard navigation
**Priority:** High

#### NFR-03: Intuitive Navigation
**Description:** The system shall provide clear, consistent navigation with minimal learning curve.
**Target Metric:** New users complete core tasks within 5 minutes without training
**Priority:** Medium

---

### 3.2 Performance

#### NFR-04: Page Load Time
**Description:** The system shall load pages within 2 seconds under normal conditions.
**Target Metric:** Homepage ≤ 2 seconds; API responses ≤ 500ms (95th percentile)
**Priority:** High

#### NFR-05: Concurrent User Support
**Description:** The system shall support 5,000 concurrent users during peak periods.
**Target Metric:** Response time degradation ≤ 50% under peak load; zero crashes
**Priority:** High

#### NFR-06: Real-Time Updates
**Description:** The system shall provide real-time updates for critical features.
**Target Metric:** Message delivery ≤ 1 second; shuttle updates every 5 seconds
**Priority:** Medium

---

### 3.3 Security

#### NFR-07: Data Encryption
**Description:** All sensitive user data shall be encrypted at rest and in transit.
**Target Metric:** AES-256 at rest; TLS 1.3 in transit; passwords hashed with bcrypt
**Priority:** Critical

#### NFR-08: Authentication Security
**Description:** The system shall implement secure authentication mechanisms.
**Target Metric:** Rate limiting (5 failed attempts before CAPTCHA); MFA option; 30m session timeout
**Priority:** Critical

#### NFR-09: Data Privacy
**Description:** The system shall protect user privacy and allow users to control their data.
**Target Metric:** Users can view/export/delete data; audit logs track sensitive access
**Priority:** High

---

### 3.4 Scalability

#### NFR-10: Horizontal Scaling
**Description:** The system shall scale horizontally by adding more instances without downtime.
**Target Metric:** Zero downtime scaling; stateless design; load balancer distribution
**Priority:** High

#### NFR-11: Database Scalability
**Description:** The database shall handle growing data volumes without performance degradation.
**Target Metric:** Stable performance with 1M+ records; partitioning strategy for large tables
**Priority:** Medium

---

### 3.5 Maintainability

#### NFR-12: Code Documentation
**Description:** The system shall include comprehensive documentation for developers.
**Target Metric:** Swagger/OpenAPI docs; README with setup instructions; ADRs
**Priority:** Medium

#### NFR-13: Modular Architecture
**Description:** The system shall follow a modular architecture with clear separation of concerns.
**Target Metric:** Independent modules; API versioning; dependency injection
**Priority:** Medium

#### NFR-14: Automated Testing
**Description:** The system shall maintain high test coverage to ensure reliability.
**Target Metric:** Unit test coverage ≥ 80%; integration tests for all endpoints; CI/CD integration
**Priority:** High

---

### 3.6 Deployability

#### NFR-15: Multi-Platform Deployment
**Description:** The system shall be deployable on Linux and Windows servers.
**Target Metric:** Docker containers; configuration via environment variables; database migrations automated
**Priority:** Medium

#### NFR-16: CI/CD Pipeline
**Description:** The system shall use automated CI/CD for reliable releases.
**Target Metric:** GitHub Actions; automated deployment to staging; manual approval for production
**Priority:** High

---

### 3.7 Reliability

#### NFR-17: System Availability
**Description:** The system shall achieve 99.9% uptime during academic hours (8am-10pm).
**Target Metric:** Maximum 45 minutes downtime per month; monitoring alerts within 1 minute
**Priority:** Critical

#### NFR-18: Data Backup and Recovery
**Description:** The system shall back up data daily and support point-in-time recovery.
**Target Metric:** RPO 15 minutes; RTO 4 hours; backup restoration tested quarterly
**Priority:** Critical

---

## 4. Requirements Traceability Matrix

| Requirement | Student | Faculty | Admin | IT Staff | Priority |
|-------------|---------|---------|-------|----------|----------|
| FR-01: Registration | ✓ | ✓ | ✓ | | High |
| FR-02: Authentication | ✓ | ✓ | ✓ | ✓ | High |
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
| FR-17: Meal Plan | ✓ | | | | Medium |
| FR-18: Cafeteria Menu | ✓ | | | | Low |
| NFR-01: Mobile-First | ✓ | ✓ | | | High |
| NFR-02: Accessibility | ✓ | ✓ | ✓ | | High |
| NFR-03: Intuitive Nav | ✓ | ✓ | ✓ | | Medium |
| NFR-04: Page Load | ✓ | ✓ | ✓ | | High |
| NFR-05: Concurrent Users | ✓ | ✓ | ✓ | ✓ | High |
| NFR-06: Real-Time | ✓ | | | | Medium |
| NFR-07: Encryption | ✓ | ✓ | ✓ | ✓ | Critical |
| NFR-08: Auth Security | ✓ | ✓ | ✓ | ✓ | Critical |
| NFR-09: Data Privacy | ✓ | ✓ | ✓ | ✓ | High |
| NFR-10: Horizontal Scale | | | | ✓ | High |
| NFR-11: DB Scale | | | | ✓ | Medium |
| NFR-12: Documentation | | | | ✓ | Medium |
| NFR-13: Modular | | | | ✓ | Medium |
| NFR-14: Testing | | | | ✓ | High |
| NFR-15: Multi-Platform | | | | ✓ | Medium |
| NFR-16: CI/CD | | | | ✓ | High |
| NFR-17: Availability | ✓ | ✓ | ✓ | ✓ | Critical |
| NFR-18: Backup | ✓ | ✓ | ✓ | ✓ | Critical |

---

## 5. Requirements Prioritization Summary

| Priority | Functional Requirements | Non-Functional Requirements |
|----------|------------------------|----------------------------|
| **Critical** | FR-01, FR-02, FR-03, FR-04, FR-05, FR-06 | NFR-07, NFR-08, NFR-17, NFR-18 |
| **High** | FR-09, FR-11, FR-12 | NFR-01, NFR-02, NFR-04, NFR-05, NFR-09, NFR-10, NFR-14, NFR-16 |
| **Medium** | FR-07, FR-08, FR-10, FR-13, FR-14, FR-17 | NFR-03, NFR-06, NFR-11, NFR-12, NFR-13, NFR-15 |
| **Low** | FR-15, FR-16, FR-18 | - |

---

## 6. Assumptions and Constraints

### Assumptions
1. Users have access to smartphones or computers with internet connectivity
2. University provides API access to existing LMS for course data
3. Campus maps and building data are available in digital format
4. Students have valid university email addresses
5. IT staff will maintain the production infrastructure

### Constraints
1. Budget: $0 (open-source technologies only)
2. Timeline: 15 assignments across the semester
3. Team size: 1 developer
4. Must integrate with existing university systems where possible
5. Must comply with FERPA/GDPR privacy regulations
