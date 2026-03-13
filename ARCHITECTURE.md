# 🏗️ Architectural Documentation

## Smart Campus Connect - C4 Model Diagrams

---

## Project Overview

| Aspect | Description |
|--------|-------------|
| **Title** | Smart Campus Connect |
| **Domain** | Education Technology |
| **Problem Statement** | Fragmented student experience across multiple platforms |
| **Individual Scope** | Modular development over 12 weeks |

---

## Level 1: System Context Diagram

```mermaid
graph TD
    Student["Student"] -->|Uses| SCC["Smart Campus Connect"]
    Faculty["Faculty Member"] -->|Uses| SCC
    Admin["Administrator"] -->|Manages| SCC
    SCC -->|Syncs with| LMS["University LMS"]
    SCC -->|Gets maps from| Maps["Google Maps"]
    SCC -->|Sends| Email["Email Service"]

graph TD
    Student["Student"] -->|Uses| Mobile["Mobile App (React Native)"]
    Faculty["Faculty"] -->|Uses| Web["Web Dashboard (React.js)"]
    Admin["Admin"] -->|Uses| Web
    
    Mobile -->|API Calls| API["API Gateway (Node.js)"]
    Web -->|API Calls| API
    
    API -->|Routes to| Auth["Auth Service"]
    API -->|Routes to| User["User Service"]
    API -->|Routes to| Academic["Academic Service"]
    API -->|Routes to| Campus["Campus Service"]
    API -->|Routes to| Event["Event Service"]
    
    Auth -->|Stores sessions| Redis[(Redis Cache)]
    User -->|Read/Write| Postgres[(PostgreSQL)]
    Academic -->|Read/Write| Postgres
    Campus -->|Read/Write| Postgres
    Event -->|Read/Write| Postgres

graph TD
    API["API Gateway"] --> CourseCtrl["Course Controller"]
    API --> GradeCtrl["Grade Controller"]
    API --> AssignCtrl["Assignment Controller"]
    
    CourseCtrl --> CourseSvc["Course Service"]
    GradeCtrl --> GradeSvc["Grade Service"]
    AssignCtrl --> AssignSvc["Assignment Service"]
    
    CourseSvc --> CourseRepo["Course Repository"]
    CourseSvc --> EnrollRepo["Enrollment Repository"]
    GradeSvc --> SubRepo["Submission Repository"]
    AssignSvc --> AssignRepo["Assignment Repository"]
    
    CourseRepo --> DB[(PostgreSQL)]
    EnrollRepo --> DB
    SubRepo --> DB
    AssignRepo --> DB

sequenceDiagram
    participant Student
    participant MobileApp
    participant API
    participant Auth
    participant DB
    
    Student->>MobileApp: Enter email & password
    MobileApp->>API: POST /api/auth/login
    API->>Auth: forward request
    Auth->>DB: SELECT user WHERE email = ?
    DB-->>Auth: user record
    Auth->>Auth: verify password
    Auth->>Auth: generate JWT token
    Auth-->>API: 200 OK + token
    API-->>MobileApp: login success
    MobileApp-->>Student: show dashboard

erDiagram
    USERS ||--o{ ENROLLMENTS : has
    USERS ||--o{ ATTENDANCE : records
    USERS ||--o{ SUBMISSIONS : submits
    USERS ||--o{ EVENT_REGISTRATIONS : registers
    USERS ||--o{ ROOM_BOOKINGS : books
    USERS ||--o{ STUDY_GROUPS : creates
    USERS ||--o{ MESSAGES : sends
    USERS ||--o{ LOST_ITEMS : reports
    USERS ||--o{ FOUND_ITEMS : reports
    USERS ||--o{ TRANSACTIONS : makes
    
    COURSES ||--o{ ENROLLMENTS : has
    COURSES ||--o{ ASSIGNMENTS : includes
    COURSES ||--o{ ATTENDANCE : tracks
    
    ASSIGNMENTS ||--o{ SUBMISSIONS : receives
    EVENTS ||--o{ EVENT_REGISTRATIONS : has
    BUILDINGS ||--o{ ROOMS : contains
    ROOMS ||--o{ ROOM_BOOKINGS : scheduled for
    STUDY_GROUPS ||--o{ STUDY_GROUP_MEMBERS : has
    
    USERS {
        int id PK
        string email
        string name
        string role
    }
    
    COURSES {
        int id PK
        string code
        string name
        int credits
    }
    
    ENROLLMENTS {
        int id PK
        int student_id FK
        int course_id FK
        string grade
    }
    
    ASSIGNMENTS {
        int id PK
        int course_id FK
        string title
        date due_date
        int points
    }
    
    SUBMISSIONS {
        int id PK
        int assignment_id FK
        int student_id FK
        int score
        date submitted_at
    }
    
    ATTENDANCE {
        int id PK
        int student_id FK
        int course_id FK
        date class_date
        string status
    }
    
    EVENTS {
        int id PK
        string title
        datetime start_time
        datetime end_time
        string location
    }
    
    BUILDINGS {
        int id PK
        string name
        string code
        string address
    }
    
    ROOMS {
        int id PK
        int building_id FK
        string room_number
        int capacity
        string type
    }
    
    STUDY_GROUPS {
        int id PK
        string name
        int course_id FK
        int created_by FK
        int max_members
    }
