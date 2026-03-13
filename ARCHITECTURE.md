## Level 1: System Context Diagram

```mermaid
C4Context
  title System Context diagram for Smart Campus Connect
  Person(student, "Student", "A university student who wants to manage academics, find study spaces, and join campus events.")
  Person(faculty, "Faculty Member", "A professor who manages courses, takes attendance, and posts assignments.")
  Person(admin, "Administrator", "A staff member who approves events, manages resources, and sends alerts.")
  System(scc, "Smart Campus Connect", "Unified platform for student lifecycle management.")
  System_Ext(lms, "University LMS", "Existing Learning Management System (Canvas/Blackboard) for course data.")
  System_Ext(maps, "Maps Service", "Google Maps API for campus navigation and shuttle tracking.")
  System_Ext(email, "Email Service", "SendGrid/SMTP for notifications and alerts.")
  System_Ext(payment, "Payment Gateway", "Stripe for meal plan purchases and transactions.")
  Rel(student, scc, "Uses", "Mobile/Web App")
  Rel(faculty, scc, "Uses", "Web App")
  Rel(admin, scc, "Manages", "Admin Dashboard")
  Rel(scc, lms, "Syncs course data", "REST API")
  Rel(scc, maps, "Fetches maps & routes", "REST API")
  Rel(scc, email, "Sends notifications", "SMTP/API")
  Rel(scc, payment, "Processes payments", "REST API")

## Level 2: Container Diagram

```mermaid
C4Container
  title Container diagram for Smart Campus Connect
  Person(student, "Student", "A university student.")
  Person(faculty, "Faculty Member", "A professor.")
  Person(admin, "Administrator", "Staff member.")
  Container_Boundary(c1, "Smart Campus Connect") {
    Container(mobile_app, "Mobile App", "React Native", "Allows students to access all features on iOS and Android.")
    Container(web_app, "Web Dashboard", "React.js", "Allows faculty and admins to manage courses, events, and resources.")
    Container(api_gateway, "API Gateway", "Node.js/Express", "Routes requests to appropriate microservices.")
    Container(auth_svc, "Auth Service", "Node.js", "Manages authentication and authorization using JWT.")
    Container(user_svc, "User Service", "Node.js", "Manages user profiles and roles.")
    Container(academic_svc, "Academic Service", "Node.js", "Handles courses, grades, assignments, attendance.")
    Container(campus_svc, "Campus Service", "Node.js", "Manages buildings, rooms, shuttle tracking.")
    Container(event_svc, "Event Service", "Node.js", "Handles events, registrations, notifications.")
    Container(social_svc, "Social Service", "Node.js + Socket.io", "Manages study groups and messaging.")
    Container(payment_svc, "Payment Service", "Node.js", "Handles meal plans and transactions.")
    ContainerDb(db, "Database", "PostgreSQL", "Stores all user, course, event, and campus data.")
    ContainerDb(redis, "Redis Cache", "Redis", "Caches session data and real-time information.")
  }
  System_Ext(lms, "University LMS", "External system for course data.")
  System_Ext(maps, "Google Maps", "External maps service.")
  System_Ext(email, "Email Service", "External email provider.")
  Rel(student, mobile_app, "Uses")
  Rel(faculty, web_app, "Uses")
  Rel(admin, web_app, "Uses")
  Rel(mobile_app, api_gateway, "Makes API calls", "JSON/HTTPS")
  Rel(web_app, api_gateway, "Makes API calls", "JSON/HTTPS")
  Rel(api_gateway, auth_svc, "Routes auth requests")
  Rel(api_gateway, user_svc, "Routes user requests")
  Rel(api_gateway, academic_svc, "Routes academic requests")
  Rel(api_gateway, campus_svc, "Routes campus requests")
  Rel(api_gateway, event_svc, "Routes event requests")
  Rel(api_gateway, social_svc, "Routes social requests")
  Rel(api_gateway, payment_svc, "Routes payment requests")
  Rel(auth_svc, db, "Read/Write", "SQL")
  Rel(user_svc, db, "Read/Write", "SQL")
  Rel(academic_svc, db, "Read/Write", "SQL")
  Rel(campus_svc, db, "Read/Write", "SQL")
  Rel(event_svc, db, "Read/Write", "SQL")
  Rel(social_svc, db, "Read/Write", "SQL")
  Rel(payment_svc, db, "Read/Write", "SQL")
  Rel(auth_svc, redis, "Store sessions")
  Rel(social_svc, redis, "Cache messages")
  Rel(academic_svc, lms, "Fetches course data", "REST API")
  Rel(campus_svc, maps, "Gets map data", "REST API")
  Rel(event_svc, email, "Sends notifications", "SMTP/API")

## Level 3: Component Diagram (Academic Service)

```mermaid
C4Component
  title Component diagram for Academic Service
  Container(api_gateway, "API Gateway", "Routes requests to academic service")
  Container_Boundary(academic, "Academic Service") {
    Component(course_ctrl, "Course Controller", "Route Handler", "Handles course-related requests (GET/POST /api/courses)")
    Component(grade_ctrl, "Grade Controller", "Route Handler", "Handles grade-related requests (GET /api/grades)")
    Component(assignment_ctrl, "Assignment Controller", "Route Handler", "Handles assignment requests (GET/POST /api/assignments)")
    Component(attendance_ctrl, "Attendance Controller", "Route Handler", "Handles attendance tracking (POST /api/attendance)")
    Component(course_svc, "Course Service", "Business Logic", "Manages course operations: create, read, update, delete")
    Component(grade_svc, "Grade Service", "Business Logic", "Calculates and stores grades")
    Component(assignment_svc, "Assignment Service", "Business Logic", "Manages assignment workflow and submissions")
    Component(attendance_svc, "Attendance Service", "Business Logic", "Processes attendance records")
    Component(course_repo, "Course Repository", "Data Access", "Database operations for courses")
    Component(enrollment_repo, "Enrollment Repository", "Data Access", "Database operations for enrollments")
    Component(assignment_repo, "Assignment Repository", "Data Access", "Database operations for assignments")
    Component(submission_repo, "Submission Repository", "Data Access", "Database operations for submissions")
    Component(attendance_repo, "Attendance Repository", "Data Access", "Database operations for attendance")
  }
  ContainerDb(db, "PostgreSQL", "Academic database schema")
  Rel(api_gateway, course_ctrl, "GET/POST /api/courses")
  Rel(api_gateway, grade_ctrl, "GET /api/grades")
  Rel(api_gateway, assignment_ctrl, "GET/POST /api/assignments")
  Rel(api_gateway, attendance_ctrl, "POST /api/attendance")
  Rel(course_ctrl, course_svc, "Uses")
  Rel(grade_ctrl, grade_svc, "Uses")
  Rel(assignment_ctrl, assignment_svc, "Uses")
  Rel(attendance_ctrl, attendance_svc, "Uses")
  Rel(course_svc, course_repo, "Uses")
  Rel(course_svc, enrollment_repo, "Uses")
  Rel(grade_svc, submission_repo, "Uses")
  Rel(assignment_svc, assignment_repo, "Uses")
  Rel(assignment_svc, submission_repo, "Uses")
  Rel(attendance_svc, attendance_repo, "Uses")
  Rel(course_repo, db, "SQL")
  Rel(enrollment_repo, db, "SQL")
  Rel(assignment_repo, db, "SQL")
  Rel(submission_repo, db, "SQL")
  Rel(attendance_repo, db, "SQL")

## Level 4: Code Diagram (Authentication Flow)

```mermaid
sequenceDiagram
    participant Student
    participant MobileApp
    participant APIGateway
    participant AuthService
    participant UserService
    participant Database
    participant Redis
    
    Student->>MobileApp: Enter email and password
    MobileApp->>APIGateway: POST /api/auth/login
    APIGateway->>AuthService: Forward login request
    
    AuthService->>UserService: validateCredentials(email, password)
    UserService->>Database: SELECT * FROM users WHERE email = ?
    Database-->>UserService: User record with password_hash
    
    UserService->>UserService: Compare password with hash
    
    alt Valid credentials
        UserService-->>AuthService: User validated (id, role)
        AuthService->>AuthService: Generate JWT token
        AuthService->>AuthService: Generate refresh token
        AuthService->>Redis: Store refresh token
        AuthService-->>APIGateway: 200 OK + tokens
        APIGateway-->>MobileApp: 200 OK + tokens
        MobileApp-->>Student: Login successful
        
    else Invalid credentials
        UserService-->>AuthService: Authentication failed
        AuthService-->>APIGateway: 401 Unauthorized
        APIGateway-->>MobileApp: 401 Unauthorized
        MobileApp-->>Student: Invalid email/password
    end

## Entity Relationship Diagram

```mermaid
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
        string password_hash
        string first_name
        string last_name
        string role
        string student_id
        string department
        datetime created_at
    }
    
    COURSES {
        int id PK
        string course_code
        string course_name
        int credits
        string department
        int faculty_id FK
        string semester
        int year
    }
    
    ENROLLMENTS {
        int id PK
        int student_id FK
        int course_id FK
        string grade
        datetime enrolled_at
    }
    
    ASSIGNMENTS {
        int id PK
        int course_id FK
        string title
        text description
        datetime due_date
        int max_points
    }
    
    SUBMISSIONS {
        int id PK
        int assignment_id FK
        int student_id FK
        string file_url
        int score
        text feedback
        datetime submitted_at
    }
    
    ATTENDANCE {
        int id PK
        int student_id FK
        int course_id FK
        date class_date
        string status
        datetime recorded_at
    }
    
    EVENTS {
        int id PK
        string title
        text description
        datetime start_time
        datetime end_time
        string location
        int organizer_id FK
        int max_attendees
    }
    
    BUILDINGS {
        int id PK
        string name
        string code
        double latitude
        double longitude
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
        datetime created_at
    }
