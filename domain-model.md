# Domain Model: Smart Campus Connect
---
## Overview

This document presents the domain model for Smart Campus Connect, identifying key entities, their attributes, methods, relationships, and business rules. The model aligns with functional requirements from Assignment 4, use cases from Assignment 5, and state/activity diagrams from Assignment 8.

---

## Core Domain Entities

| Entity | Description |
|--------|-------------|
| User | Represents any person using the system (Student, Faculty, Admin) |
| Course | Represents a academic course offered at the university |
| Enrollment | Links a Student to a Course they are registered in |
| Assignment | A task or project created by Faculty for a Course |
| Submission | Student's work submitted for an Assignment |
| Attendance | Record of a Student's presence in a class session |
| StudyRoom | Physical room on campus available for booking |
| Booking | Reservation of a StudyRoom by a Student |
| Event | Campus activity created by Faculty or Admin |
| EventRegistration | Student's registration for an Event |
| StudyGroup | Peer learning group created by Students |
| Message | Communication within a StudyGroup |
| LostItem | Item reported missing by a Student |
| FoundItem | Item reported found by any user |
| MealPlan | Student's dining package with remaining swipes |
| Transaction | Record of a meal swipe or dining dollar usage |
| Shuttle | Campus transportation vehicle |
| ShuttleLocation | Real-time GPS position of a Shuttle |
| Notification | System alert sent to a User |

---

## Entity Details

### 1. User (Abstract)

| Attribute | Type | Description |
|-----------|------|-------------|
| userId | String (PK) | Unique identifier |
| email | String | University email (@mycput.ac.za) |
| passwordHash | String | Bcrypt hashed password |
| firstName | String | User's first name |
| lastName | String | User's last name |
| role | Enum | STUDENT, FACULTY, ADMIN |
| createdAt | DateTime | Account creation timestamp |
| isActive | Boolean | Whether account is active |

| Method | Description |
|--------|-------------|
| register() | Creates new user account |
| login() | Authenticates user |
| updateProfile() | Updates user information |
| deactivate() | Deactivates user account |

### 2. Student (inherits from User)

| Attribute | Type | Description |
|-----------|------|-------------|
| studentId | String | CPUT student number |
| department | String | Academic department |
| graduationYear | Integer | Expected graduation year |

| Method | Description |
|--------|-------------|
| enrollInCourse() | Registers for a course |
| submitAssignment() | Submits assignment work |
| bookStudyRoom() | Reserves a study room |
| registerForEvent() | Signs up for an event |
| createStudyGroup() | Forms a study group |
| reportLostItem() | Reports missing item |
| viewMealPlan() | Checks remaining swipes |

### 3. Faculty (inherits from User)

| Attribute | Type | Description |
|-----------|------|-------------|
| staffId | String | CPUT staff number |
| department | String | Academic department |
| officeLocation | String | Building and room number |

| Method | Description |
|--------|-------------|
| createCourse() | Adds a new course |
| createAssignment() | Creates assignment for course |
| takeAttendance() | Marks student attendance |
| gradeSubmission() | Scores student submission |
| createEvent() | Creates campus event |

### 4. Admin (inherits from User)

| Attribute | Type | Description |
|-----------|------|-------------|
| staffId | String | CPUT staff number |
| role | String | SUPER_ADMIN, EVENT_ADMIN, FACILITY_ADMIN |

| Method | Description |
|--------|-------------|
| approveEvent() | Publishes or rejects event |
| suspendUser() | Temporarily blocks user |
| sendEmergencyAlert() | Broadcasts urgent notification |
| manageResources() | Configures campus facilities |

### 5. Course

| Attribute | Type | Description |
|-----------|------|-------------|
| courseId | String (PK) | Course code (e.g., SE301) |
| courseName | String | Full course title |
| credits | Integer | Credit value (e.g., 15) |
| department | String | Offering department |
| facultyId | String (FK) | Instructor (Faculty) |
| semester | String | e.g., "Semester 1 2026" |
| maxStudents | Integer | Enrollment capacity |

| Method | Description |
|--------|-------------|
| addStudent() | Enrolls a student |
| removeStudent() | Drops a student |
| updateDetails() | Modifies course information |

**Business Rules:**
- A Course must have exactly one Faculty instructor
- A Course can have 0 to maxStudents enrolled
- A Course cannot be deleted if it has active enrollments

### 6. Enrollment

| Attribute | Type | Description |
|-----------|------|-------------|
| enrollmentId | String (PK) | Unique identifier |
| studentId | String (FK) | Reference to Student |
| courseId | String (FK) | Reference to Course |
| enrolledAt | DateTime | Enrollment date |
| status | Enum | ACTIVE, DROPPED, COMPLETED |
| grade | String | Final grade (A, B, C, etc.) |

| Method | Description |
|--------|-------------|
| drop() | Withdraws from course |
| complete() | Marks course as completed |

**Business Rules:**
- A Student cannot enroll in the same Course twice
- A Student cannot enroll in Courses with time conflicts
- Drop is allowed only within first 2 weeks of semester

### 7. Assignment

| Attribute | Type | Description |
|-----------|------|-------------|
| assignmentId | String (PK) | Unique identifier |
| courseId | String (FK) | Reference to Course |
| title | String | Assignment name |
| description | Text | Instructions |
| dueDate | DateTime | Submission deadline |
| maxPoints | Integer | Maximum possible score |
| allowedFileTypes | String[] | PDF, DOC, DOCX, ZIP |

| Method | Description |
|--------|-------------|
| publish() | Makes assignment visible to students |
| updateDeadline() | Changes due date |
| acceptSubmission() | Receives student work |

**Business Rules:**
- An Assignment belongs to exactly one Course
- Due date cannot be in the past when creating
- Late submissions are automatically marked

### 8. Submission

| Attribute | Type | Description |
|-----------|------|-------------|
| submissionId | String (PK) | Unique identifier |
| assignmentId | String (FK) | Reference to Assignment |
| studentId | String (FK) | Reference to Student |
| fileUrl | String | Link to submitted file |
| submittedAt | DateTime | Submission timestamp |
| isLate | Boolean | Whether after due date |
| score | Integer | Points awarded |
| feedback | Text | Faculty comments |

| Method | Description |
|--------|-------------|
| submit() | Uploads assignment file |
| grade() | Assigns score and feedback |
| resubmit() | Allows new submission |

**Business Rules:**
- A Submission belongs to one Assignment and one Student
- Only one submission per Student per Assignment (override allowed)
- Late submissions trigger faculty notification

### 9. Attendance

| Attribute | Type | Description |
|-----------|------|-------------|
| attendanceId | String (PK) | Unique identifier |
| studentId | String (FK) | Reference to Student |
| courseId | String (FK) | Reference to Course |
| classDate | Date | Session date |
| status | Enum | PRESENT, ABSENT, LATE, EXCUSED |
| recordedAt | DateTime | When attendance was taken |

| Method | Description |
|--------|-------------|
| markPresent() | Records attendance |
| generateReport() | Creates attendance summary |

**Business Rules:**
- A Student can have multiple Attendance records per Course
- Attendance below 75% triggers warning notification

### 10. StudyRoom

| Attribute | Type | Description |
|-----------|------|-------------|
| roomId | String (PK) | Building + room number |
| building | String | Building name |
| capacity | Integer | Maximum occupants |
| amenities | String[] | Whiteboard, projector, etc. |
| isAvailable | Boolean | Current availability |
| hours | String | Operating hours |

| Method | Description |
|--------|-------------|
| checkAvailability() | Verifies time slot |
| releaseRoom() | Frees up room after booking |

**Business Rules:**
- A StudyRoom can be booked for maximum 3 hours per session
- A StudyRoom cannot be double-booked

### 11. Booking

| Attribute | Type | Description |
|-----------|------|-------------|
| bookingId | String (PK) | Unique identifier |
| roomId | String (FK) | Reference to StudyRoom |
| studentId | String (FK) | Reference to Student |
| startTime | DateTime | Booking start |
| endTime | DateTime | Booking end |
| status | Enum | PENDING, CONFIRMED, CANCELLED, COMPLETED |
| qrCode | String | Access verification code |

| Method | Description |
|--------|-------------|
| confirm() | Finalizes booking |
| cancel() | Cancels existing booking |

**Business Rules:**
- A Booking belongs to one StudyRoom and one Student
- Cancellation must be at least 1 hour before start time
- No-shows are recorded after 15 minutes

### 12. Event

| Attribute | Type | Description |
|-----------|------|-------------|
| eventId | String (PK) | Unique identifier |
| title | String | Event name |
| description | Text | Event details |
| startTime | DateTime | Start datetime |
| endTime | DateTime | End datetime |
| location | String | Venue |
| organizerId | String (FK) | Faculty or Student creator |
| maxAttendees | Integer | Capacity limit |
| status | Enum | DRAFT, SUBMITTED, APPROVED, REJECTED, PUBLISHED, COMPLETED |

| Method | Description |
|--------|-------------|
| submitForApproval() | Sends to admin queue |
| approve() | Admin publishes event |
| reject() | Admin denies with reason |

**Business Rules:**
- An Event must be approved by Admin before publication
- An Event cannot exceed venue capacity
- Approval required at least 48 hours before start

### 13. EventRegistration

| Attribute | Type | Description |
|-----------|------|-------------|
| registrationId | String (PK) | Unique identifier |
| eventId | String (FK) | Reference to Event |
| studentId | String (FK) | Reference to Student |
| registeredAt | DateTime | Registration timestamp |
| attended | Boolean | Whether student checked in |

| Method | Description |
|--------|-------------|
| register() | Adds student to event |
| cancel() | Removes registration |
| checkIn() | Marks attendance |

**Business Rules:**
- A Student can register for an Event only once
- Waitlist is created when Event reaches capacity

### 14. StudyGroup

| Attribute | Type | Description |
|-----------|------|-------------|
| groupId | String (PK) | Unique identifier |
| name | String | Group name |
| courseId | String (FK) | Associated course |
| createdBy | String (FK) | Student creator |
| maxMembers | Integer | Capacity (default 10) |
| isActive | Boolean | Whether group is active |
| createdAt | DateTime | Creation timestamp |

| Method | Description |
|--------|-------------|
| addMember() | Adds student to group |
| removeMember() | Removes student |
| disband() | Deactivates group |

**Business Rules:**
- A StudyGroup must have at least 3 members to be active
- A Student can create multiple StudyGroups
- StudyGroup auto-archives at semester end

### 15. Message

| Attribute | Type | Description |
|-----------|------|-------------|
| messageId | String (PK) | Unique identifier |
| groupId | String (FK) | Reference to StudyGroup |
| senderId | String (FK) | Reference to User |
| content | Text | Message body |
| sentAt | DateTime | Timestamp |
| isEdited | Boolean | Whether modified |

| Method | Description |
|--------|-------------|
| send() | Delivers message to group |
| edit() | Modifies message content |
| delete() | Removes message |

**Business Rules:**
- A Message belongs to one StudyGroup
- Only group members can send messages
- Messages cannot be deleted after 1 hour

### 16. LostItem

| Attribute | Type | Description |
|-----------|------|-------------|
| itemId | String (PK) | Unique identifier |
| reporterId | String (FK) | Reference to Student |
| title | String | Item description |
| description | Text | Detailed description |
| category | String | e.g., Electronics, Books, etc. |
| locationLost | String | Where item was lost |
| dateLost | Date | When lost |
| photoUrl | String | Image reference |
| status | Enum | REPORTED, INVESTIGATING, FOUND, CLAIMED, CLOSED |

| Method | Description |
|--------|-------------|
| report() | Submits lost item |
| markFound() | Updates when matched |
| claim() | Owner retrieves item |

**Business Rules:**
- A LostItem automatically closes after 30 days
- Match confidence > 80% required for Found status

### 17. FoundItem

| Attribute | Type | Description |
|-----------|------|-------------|
| foundId | String (PK) | Unique identifier |
| reporterId | String (FK) | Reference to User |
| title | String | Item description |
| description | Text | Detailed description |
| category | String | Item type |
| locationFound | String | Where found |
| dateFound | Date | When found |
| photoUrl | String | Image reference |
| storageLocation | String | Where kept |
| status | Enum | UNCLAIMED, CLAIMED, RETURNED |

| Method | Description |
|--------|-------------|
| report() | Submits found item |
| matchWithLost() | Finds potential owner |
| markClaimed() | Records return |

**Business Rules:**
- FoundItem triggers automatic matching with LostItems
- Claimed requires proof of ownership

### 18. MealPlan

| Attribute | Type | Description |
|-----------|------|-------------|
| planId | String (PK) | Unique identifier |
| studentId | String (FK) | Reference to Student |
| totalSwipes | Integer | Swipes per semester |
| remainingSwipes | Integer | Available swipes |
| diningDollars | Decimal | Additional balance (Rands) |
| startDate | Date | Plan start |
| endDate | Date | Plan expiration |
| isActive | Boolean | Plan status |

| Method | Description |
|--------|-------------|
| deductSwipe() | Uses one meal swipe |
| addFunds() | Adds dining dollars |
| checkBalance() | Returns remaining swipes |

**Business Rules:**
- A MealPlan belongs to exactly one Student
- Remaining swipes cannot go negative
- Low balance alert at 20% remaining

### 19. Transaction

| Attribute | Type | Description |
|-----------|------|-------------|
| transactionId | String (PK) | Unique identifier |
| planId | String (FK) | Reference to MealPlan |
| amount | Decimal | Swipe or Rand value |
| type | Enum | SWIPE, DINING_DOLLAR, REFUND |
| description | String | e.g., "Cafeteria Lunch" |
| location | String | Dining venue |
| timestamp | DateTime | Transaction time |

| Method | Description |
|--------|-------------|
| record() | Logs transaction |
| refund() | Reverses transaction |

**Business Rules:**
- A Transaction belongs to one MealPlan
- Refund only allowed within 24 hours

### 20. Shuttle

| Attribute | Type | Description |
|-----------|------|-------------|
| shuttleId | String (PK) | Vehicle identifier |
| route | String | Route name |
| capacity | Integer | Passenger limit |
| isActive | Boolean | Whether in service |

| Method | Description |
|--------|-------------|
| updateLocation() | Sends GPS position |
| reportDelay() | Notifies schedule change |

### 21. ShuttleLocation

| Attribute | Type | Description |
|-----------|------|-------------|
| locationId | String (PK) | Unique identifier |
| shuttleId | String (FK) | Reference to Shuttle |
| latitude | Double | GPS coordinate |
| longitude | Double | GPS coordinate |
| speed | Integer | Current speed (km/h) |
| heading | Integer | Direction in degrees |
| timestamp | DateTime | Location time |
| status | Enum | ON_TIME, DELAYED, OFF_ROUTE |

| Method | Description |
|--------|-------------|
| update() | Records new position |

**Business Rules:**
- Location updates every 5 seconds
- Location history retained for 7 days

### 22. Notification

| Attribute | Type | Description |
|-----------|------|-------------|
| notificationId | String (PK) | Unique identifier |
| userId | String (FK) | Recipient |
| title | String | Notification title |
| body | Text | Message content |
| type | Enum | INFO, WARNING, SUCCESS, EMERGENCY |
| isRead | Boolean | Read status |
| createdAt | DateTime | Creation time |
| data | JSON | Additional payload |

| Method | Description |
|--------|-------------|
| send() | Delivers notification |
| markAsRead() | Updates status |

---

## Relationship Summary

| Entity A | Relationship | Entity B | Multiplicity |
|----------|--------------|----------|--------------|
| User | abstract parent | Student | - |
| User | abstract parent | Faculty | - |
| User | abstract parent | Admin | - |
| Student | enrolls in | Course | * : * (via Enrollment) |
| Faculty | teaches | Course | 1 : * |
| Course | has | Assignment | 1 : * |
| Assignment | receives | Submission | 1 : * |
| Student | submits | Submission | 1 : * |
| Student | has | Attendance | 1 : * |
| Course | records | Attendance | 1 : * |
| Student | books | Booking | 1 : * |
| StudyRoom | has | Booking | 1 : * |
| Faculty | creates | Event | 1 : * |
| Student | registers for | Event | * : * (via EventRegistration) |
| Student | creates | StudyGroup | 1 : * |
| StudyGroup | has | Message | 1 : * |
| Student | reports | LostItem | 1 : * |
| User | reports | FoundItem | 1 : * |
| Student | has | MealPlan | 1 : 1 |
| MealPlan | has | Transaction | 1 : * |
| User | receives | Notification | 1 : * |

---

## Business Rules Summary

| Rule ID | Rule |
|---------|------|
| BR-01 | A Course must have exactly one Faculty instructor |
| BR-02 | A Student cannot enroll in the same Course twice |
| BR-03 | Drop is allowed only within first 2 weeks of semester |
| BR-04 | An Assignment due date cannot be in the past when creating |
| BR-05 | Only one submission per Student per Assignment |
| BR-06 | Attendance below 75% triggers warning notification |
| BR-07 | A StudyRoom can be booked for maximum 3 hours per session |
| BR-08 | A StudyRoom cannot be double-booked |
| BR-09 | An Event must be approved by Admin before publication |
| BR-10 | A StudyGroup must have at least 3 members to be active |
| BR-11 | A LostItem automatically closes after 30 days |
| BR-12 | Remaining swipes cannot go negative |
| BR-13 | Location updates every 5 seconds |
