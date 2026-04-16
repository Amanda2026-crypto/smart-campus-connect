
**Click "Commit new file"**

---
```markdown
# Activity Diagrams: Smart Campus Connect

---

## Workflow 1: User Registration

```mermaid
flowchart TD
    A[User opens app] --> B[User enters details]
    B --> C[System validates email]
    C --> D{Email valid?}
    D -->|No| E[Show error message]
    E --> B
    D -->|Yes| F[Create account]
    F --> G[Send verification email]
    G --> H[Complete]
```
Swimlanes: User, System

Steps:

User opens app and enters registration details

System validates email format (@mycput.ac.za)

If invalid, error shown and user re-enters

If valid, account created and verification email sent

FR-01, US-001

Workflow 2: Assignment Submission

```mermaid
flowchart TD
    A[Student selects assignment] --> B[Student uploads file]
    B --> C[System validates file]
    C --> D{File valid?}
    D -->|No| E[Show error]
    E --> B
    D -->|Yes| F[Save submission with timestamp]
    F --> G{Due date passed?}
    G -->|Yes| H[Mark as Late]
    G -->|No| I[Mark as On Time]
    H --> J[Notify faculty]
    I --> J
    J --> K[Show confirmation to student]
    K --> L[Complete]

```
Swimlanes: Student, System

Steps:

Student selects assignment and uploads file

System validates file type and size

If invalid, error shown

If valid, submission saved with timestamp

System checks due date and marks as On Time or Late

Faculty notified, student confirmed

FR-06, UC-02, US-006

Workflow 3: Study Room Booking

```mermaid
flowchart TD
    A[Student opens study spaces] --> B[Student applies filters]
    B --> C[System shows available rooms]
    C --> D[Student selects room and time]
    D --> E[System checks availability]
    E --> F{Room available?}
    F -->|No| G[Show alternatives]
    G --> D
    F -->|Yes| H[Confirm booking]
    H --> I[Send notification]
    I --> J[Add to calendar]
    J --> K[Complete]

```
Swimlanes: Student, System

Steps:

Student applies filters (building, time, capacity)

System displays available rooms (color-coded)

Student selects room and time slot

System checks availability

If unavailable, shows alternatives

If available, confirms booking and sends notification

FR-09, UC-05, US-009, US-010

Workflow 4: Event Registration

```mermaid
flowchart TD
    A[Student browses events] --> B[Student selects event]
    B --> C[System checks capacity]
    C --> D{Spots available?}
    D -->|No| E[Add to waitlist]
    E --> F[Notify when spot opens]
    F --> G[Complete]
    D -->|Yes| H[Register student]
    H --> I[Send confirmation email]
    H --> J[Add to calendar]
    I --> K[Complete]
    J --> K
```
Swimlanes: Student, System

Steps:

Student browses and selects event

System checks capacity

If full, student added to waitlist

If available, student registered

Parallel: Send email + Add to calendar

FR-11, UC-06, US-012

Workflow 5: Attendance via QR Code

```mermaid
flowchart TD
    A[Faculty selects course] --> B[Faculty generates QR code]
    B --> C[Student scans QR code]
    C --> D[System validates QR]
    D --> E{QR valid?}
    E -->|No| F[Show invalid message]
    F --> C
    E -->|Yes| G[Record attendance]
    G --> H[Save timestamp]
    H --> I[Complete]
```
Swimlanes: Faculty, Student, System

Steps:

Faculty generates QR code

Student scans code using app

System validates QR code

If invalid, error shown and student rescans

If valid, attendance recorded with timestamp

FR-07, UC-03, US-008

Workflow 6: Event Approval (Admin)

```mermaid
flowchart TD
    A[Organizer creates event] --> B[Organizer submits for approval]
    B --> C[Admin reviews event]
    C --> D{Approve?}
    D -->|No| E[Reject with reason]
    E --> F[Organizer revises]
    F --> B
    D -->|Yes| G[Publish event]
    G --> H[Notify students]
    H --> I[Complete]
```
Swimlanes: Organizer, Admin, System

Steps:

Organizer creates and submits event

Admin reviews for policy compliance

If rejected, reason sent to organizer for revision

If approved, event published and students notified

FR-12, UC-08, US-016

Workflow 7: Lost Item Claim

```mermaid
flowchart TD
    A[Student reports lost item] --> B[System stores report]
    B --> C[Admin reviews]
    C --> D{Match found?}
    D -->|No| E[Monitor for 30 days]
    E --> C
    D -->|Yes| F[Notify student]
    F --> G[Student confirms ownership]
    G --> H[Arrange return]
    H --> I[Mark as claimed]
    I --> J[Complete]

```
Swimlanes: Student, System, Admin

Steps:

Student reports lost item with photo and location

Admin reviews and searches for matches

If match found, student notified

Student confirms ownership and arranges pickup

Item marked as claimed

FR-15, FR-16, US-018

Workflow 8: Emergency Alert

```mermaid
flowchart TD
    A[Admin composes alert] --> B[Admin selects audience]
    B --> C[System validates content]
    C --> D{Content valid?}
    D -->|No| E[Return for revision]
    E --> A
    D -->|Yes| F[Send push notification]
    D -->|Yes| G[Send email]
    D -->|Yes| H[Send SMS]
    F --> I[Log event]
    G --> I
    H --> I
    I --> J[Complete]
```
Swimlanes: Admin, System

Steps:

Admin composes emergency alert

System validates content

If invalid, returned for revision

If valid, parallel notifications sent (push, email, SMS)

Event logged for audit

US-019, NFR-09

Summary: Workflows and Traceability
Workflow	FR	UC	User Story
User Registration	FR-01	-	US-001
Assignment Submission	FR-06	UC-02	US-006
Study Room Booking	FR-09	UC-05	US-009, US-010
Event Registration	FR-11	UC-06	US-012
Attendance via QR	FR-07	UC-03	US-008
Event Approval	FR-12	UC-08	US-016
Lost Item Claim	FR-15, FR-16	-	US-018
Emergency Alert	NFR-09	-	US-019


