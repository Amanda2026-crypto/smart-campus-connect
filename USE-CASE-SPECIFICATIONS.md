```markdown
# Use Case Specifications: Smart Campus Connect

## Overview
This document provides detailed specifications for 8 critical use cases identified in the use case diagram.

---

## UC-01: View Grades

| Attribute | Value |
|-----------|-------|
| **Use Case ID** | UC-01 |
| **Use Case Name** | View Grades |
| **Actors** | Student, Faculty |
| **Description** | Allows users to view grades for enrolled courses, including assignment breakdowns and GPA calculation. |
| **Preconditions** | User is logged in; student is enrolled in courses; faculty has assigned courses |
| **Postconditions** | Grades are displayed with course details; system logs the view |

### Basic Flow
1. User logs into the system
2. User navigates to "Academic Dashboard"
3. System displays list of enrolled/assigned courses
4. User selects a course
5. System displays:
   - Current grade percentage
   - Letter grade
   - Assignment breakdown with individual scores
   - Attendance record
6. User can view overall GPA
7. System calculates and displays cumulative GPA

### Alternative Flows
| Flow | Condition | Action |
|------|-----------|--------|
| A-01 | No grades available | System displays "No grades posted yet" message |
| A-02 | Course not found | System displays error message and returns to dashboard |
| A-03 | Network timeout | System shows retry option |

---

## UC-02: Submit Assignment

| Attribute | Value |
|-----------|-------|
| **Use Case ID** | UC-02 |
| **Use Case Name** | Submit Assignment |
| **Actors** | Student |
| **Description** | Allows students to upload and submit assignments for grading. |
| **Preconditions** | Student is logged in; assignment exists and is open for submission; due date has not passed |
| **Postconditions** | Assignment submission is recorded; file is stored; timestamp is logged |

### Basic Flow
1. Student logs into the system
2. Student navigates to "Assignments"
3. System displays list of pending assignments
4. Student selects an assignment
5. System displays assignment details (title, description, due date, points)
6. Student uploads file (max 50MB)
7. Student clicks "Submit"
8. System validates file type and size
9. System saves submission with timestamp
10. System sends confirmation email and in-app notification

### Alternative Flows
| Flow | Condition | Action |
|------|-----------|--------|
| A-01 | Late submission | System marks as "Late" and notifies faculty |
| A-02 | Invalid file type | System rejects and shows allowed formats |
| A-03 | File too large | System rejects and shows size limit |
| A-04 | Assignment closed | System displays "Submission closed" error |
| A-05 | Network failure | System saves draft and offers retry |

---

## UC-03: Take Attendance

| Attribute | Value |
|-----------|-------|
| **Use Case ID** | UC-03 |
| **Use Case Name** | Take Attendance |
| **Actors** | Faculty Member |
| **Description** | Allows faculty to mark student attendance for class sessions. |
| **Preconditions** | Faculty is logged in; course exists; class session is active |
| **Postconditions** | Attendance records are saved; students can view their attendance |

### Basic Flow
1. Faculty logs into the system
2. Faculty selects a course
3. Faculty clicks "Take Attendance"
4. System displays list of enrolled students
5. Faculty selects attendance method:
   - Option A: QR code generation
   - Option B: Manual entry
6. If QR code: System generates unique code; students scan via app; system records attendance
7. If manual: Faculty marks students as Present/Absent/Late
8. Faculty submits attendance
9. System saves records and updates attendance percentages

### Alternative Flows
| Flow | Condition | Action |
|------|-----------|--------|
| A-01 | Student not in list | Faculty can manually add student |
| A-02 | Duplicate QR scan | System rejects second scan |
| A-03 | Network outage | Attendance saved locally, syncs when online |

---

## UC-04: Create Assignment

| Attribute | Value |
|-----------|-------|
| **Use Case ID** | UC-04 |
| **Use Case Name** | Create Assignment |
| **Actors** | Faculty Member |
| **Description** | Allows faculty to create and publish assignments for students. |
| **Preconditions** | Faculty is logged in; course exists |
| **Postconditions** | Assignment is created and visible to students; notifications sent |

### Basic Flow
1. Faculty logs into the system
2. Faculty selects a course
3. Faculty clicks "Create Assignment"
4. System displays assignment creation form
5. Faculty enters:
   - Title
   - Description
   - Due date/time
   - Maximum points
   - Allowed file types
6. Faculty attaches any reference materials
7. Faculty sets submission visibility (individual or group)
8. Faculty clicks "Publish"
9. System validates all fields
10. System saves assignment and sends notifications to enrolled students

### Alternative Flows
| Flow | Condition | Action |
|------|-----------|--------|
| A-01 | Missing required fields | System highlights missing fields and prevents publish |
| A-02 | Due date in past | System displays warning |
| A-03 | Publish later | Faculty can save as draft |

---

## UC-05: Find Study Space

| Attribute | Value |
|-----------|-------|
| **Use Case ID** | UC-05 |
| **Use Case Name** | Find Study Space |
| **Actors** | Student, Administrator |
| **Description** | Allows users to search for and book available study rooms. |
| **Preconditions** | User is logged in; building/room data is loaded |
| **Postconditions** | Available rooms displayed; booking created if confirmed |

### Basic Flow
1. User logs into the system
2. User navigates to "Study Spaces"
3. System displays map with buildings
4. User applies filters:
   - Building
   - Capacity
   - Amenities (whiteboard, projector)
   - Time slot
5. System displays available rooms with status (green=available, red=occupied)
6. User selects a room
7. System shows room details and booking options
8. User selects time slot (max 3 hours)
9. System confirms booking and sends notification
10. User can cancel or modify booking

### Alternative Flows
| Flow | Condition | Action |
|------|-----------|--------|
| A-01 | No rooms available | System displays "No rooms match criteria" and suggests alternatives |
| A-02 | Booking conflict | System shows error and suggests available times |
| A-03 | User cancels | System releases room and sends cancellation confirmation |

---

## UC-06: Register for Event

| Attribute | Value |
|-----------|-------|
| **Use Case ID** | UC-06 |
| **Use Case Name** | Register for Event |
| **Actors** | Student |
| **Description** | Allows students to register for campus events. |
| **Preconditions** | Student is logged in; event exists; event capacity not exceeded |
| **Postconditions** | Registration is recorded; student added to attendee list; confirmation sent |

### Basic Flow
1. Student logs into the system
2. Student navigates to "Events"
3. System displays event list (by date, category, popularity)
4. Student selects an event
5. System displays event details:
   - Title, description, date/time, location
   - Current registrations/capacity
   - Organizer information
6. Student clicks "Register"
7. System checks capacity
8. System adds student to attendee list
9. System sends confirmation email and in-app notification
10. System adds event to student's calendar

### Alternative Flows
| Flow | Condition | Action |
|------|-----------|--------|
| A-01 | Event at capacity | System displays "Event is full" and waitlist option |
| A-02 | Already registered | System displays "Already registered" and offers cancel option |
| A-03 | Cancel registration | System removes student from list and opens spot |

---

## UC-07: Create Study Group

| Attribute | Value |
|-----------|-------|
| **Use Case ID** | UC-07 |
| **Use Case Name** | Create Study Group |
| **Actors** | Student |
| **Description** | Allows students to create and manage study groups for courses. |
| **Preconditions** | Student is logged in; enrolled in at least one course |
| **Postconditions** | Study group created; join requests can be processed |

### Basic Flow
1. Student logs into the system
2. Student selects a course
3. Student clicks "Create Study Group"
4. System displays group creation form
5. Student enters:
   - Group name
   - Description
   - Max members (default: 10)
   - Meeting preferences (optional)
6. Student sets privacy (public/private)
7. Student clicks "Create"
8. System creates group and sets student as admin
9. System displays group page with discussion board
10. Student can invite classmates

### Alternative Flows
| Flow | Condition | Action |
|------|-----------|--------|
| A-01 | Group name exists | System prompts for unique name |
| A-02 | Max members exceeded | System rejects with limit message |
| A-03 | Private group | System requires approval for join requests |

---

## UC-08: Approve Event

| Attribute | Value |
|-----------|-------|
| **Use Case ID** | UC-08 |
| **Use Case Name** | Approve Event |
| **Actors** | Administrator |
| **Description** | Allows administrators to review and approve/reject event submissions. |
| **Preconditions** | Administrator is logged in; event submissions exist in pending queue |
| **Postconditions** | Event status updated; organizer notified |

### Basic Flow
1. Administrator logs into the system
2. Administrator navigates to "Event Approvals"
3. System displays list of pending events
4. Administrator selects an event
5. System displays event details:
   - Title, description, date/time, location
   - Organizer information
   - Expected attendance
   - Resources requested
6. Administrator reviews for:
   - Policy compliance
   - Scheduling conflicts
   - Resource availability
7. Administrator selects:
   - Approve
   - Reject (with reason)
   - Request Changes
8. System updates event status
9. System sends notification to organizer
10. Approved events appear in public listings

### Alternative Flows
| Flow | Condition | Action |
|------|-----------|--------|
| A-01 | Reject with reason | System includes reason in notification |
| A-02 | Request changes | System sends change requests to organizer |
| A-03 | Schedule conflict | System alerts admin to conflict |
