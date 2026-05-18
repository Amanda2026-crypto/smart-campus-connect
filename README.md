# Smart Campus Connect

A unified student lifecycle management platform for academic tracking, campus navigation, event discovery, and peer connections.

---

## Introduction

Smart Campus Connect is a comprehensive platform that combines academic tracking, campus navigation, event discovery, and social features into one unified application for university students, faculty, and staff.

---

## What It Will Do (Once Completed)

### For Students
- **Academic Dashboard**: View grades, attendance, course materials, and assignment deadlines
- **Campus Navigator**: Interactive map for finding buildings, rooms, and study spaces
- **Event Discovery**: Browse and register for campus events, workshops, and club meetings
- **Study Buddy Finder**: Connect with classmates for group study sessions
- **Shuttle Tracker**: Real-time campus shuttle locations and arrival predictions
- **Lost & Found**: Report and search for lost items
- **Meal Plan Manager**: Track meal swipes and view cafeteria menus

### For Faculty
- **Class Management**: Take attendance, upload materials, post announcements
- **Student Communication**: Send notifications to classes or groups
- **Performance Analytics**: View class performance trends

### For Administration
- **Resource Management**: Track classroom utilization and study spaces
- **Event Approval**: Review and approve student events
- **Emergency Alerts**: Send campus-wide notifications

---

## Technology Stack

| Layer | Technology |
|-------|------------|
| Frontend Web | React.js + Tailwind CSS |
| Mobile App | React Native |
| Backend API | Node.js/Express |
| Database | PostgreSQL |
| Caching | Redis |
| Real-time | Socket.io |
| Maps | Google Maps API |
| Authentication | JWT + OAuth2 |

---

## Documentation

### Assignment 3
- [System Specification](SPECIFICATION.md)
- [C4 Architectural Diagrams](ARCHITECTURE.md)

### Assignment 4
- [Stakeholder Analysis](STAKEHOLDER-ANALYSIS.md)
- [System Requirements Document](SYSTEM-REQUIREMENTS-DOCUMENT.md)
- [Reflection - Assignment 4](REFLECTION.md)

### Assignment 5
- [Use Case Diagram](USE-CASE-DIAGRAM.md)
- [Use Case Specifications](USE-CASE-SPECIFICATIONS.md)
- [Test Cases](TEST-CASES.md)
- [Reflection - Assignment 5](REFLECTION-ASSIGNMENT5.md)

### Assignment 6
- [Agile Planning Document](AGILE-PLANNING.md)
- [Reflection - Assignment 6](REFLECTION-ASSIGNMENT6.md)
- [Sprint Board](https://github.com/users/Amanda2026-crypto/projects/1)

### Assignment 7
- [Template Analysis](template_analysis.md)
- [Kanban Explanation](kanban_explanation.md)
- [Reflection - Assignment 7](REFLECTION-ASSIGNMENT7.md)
- [Template Comparison Screenshot](template-comparison.png)
- [Kanban Board - Default](kanban-board-default.jpeg)
- [Kanban Board - Custom Columns](kanban-board-custom-columns.jpeg)
- [Kanban Board - Final](kanban-board-final.jpeg)

### Github Tools:
- [Kanban Board](https://github.com/users/Amanda2026-crypto/projects/4)

### Kanban Board Customization
I added two custom columns to the Kanban template:
- **Testing**: Stories need verification before marking Done
- **Blocked**: Stories with dependencies (US-010 depends on US-009)

### Assignment 8
- [State Transition Diagrams](state-transition-diagrams.md)
- [Activity Diagrams](activity-diagrams.md)
- [Reflection - Assignment 8](reflection-assignment8.md)

---
### Assignment 9
- [Domain Model](domain-model.md)
- [Class Diagram](class-diagram.md)
- [Reflection - Assignment 9](reflection-assignment9.md)

## Assignment 10: Creational Design Patterns

- [Source Code](src/)
- [Unit Tests](tests/)
- [CHANGELOG](CHANGELOG.md)
- [GitHub Issues](https://github.com/Amanda2026-crypto/smart-campus-connect/issues)
  
### Language Choice: Python
All code is implemented in Python 3.13.

### Six Creational Patterns Implemented

| Pattern | File Location | Purpose |
|---------|---------------|---------|
| Simple Factory | `src/creational_patterns/simple_factory.py` | Creates User objects (Student, Faculty, Admin) |
| Factory Method | `src/creational_patterns/factory_method.py` | Creates Payment Processors (Credit Card, PayPal) |
| Abstract Factory | `src/creational_patterns/abstract_factory.py` | Creates UI components (Windows/MacOS) |
| Builder | `src/creational_patterns/builder.py` | Builds complex Assignment objects |
| Prototype | `src/creational_patterns/prototype.py` | Clones Notification templates |
| Singleton | `src/creational_patterns/singleton.py` | Single DatabaseConnection instance |

### Running Tests
```bash
python -m unittest discover tests
```

### Test Results
```bash
Ran 25 tests in 0.006s
OK
```

## Assignment 11: Repository Pattern and Storage Abstraction

**Language:** Python

**Repository Pattern Justification:**
- Separates business logic from storage details
- Makes it easy to switch between storage backends
- Simplifies unit testing (use in-memory for tests)

**Storage Abstraction:** Factory Pattern

**Future Storage Backends:**

| Storage Type | Status |
|--------------|--------|
| In-Memory (HashMap) | ✅ Implemented |
| Database (MySQL/PostgreSQL) | 📝 Stub created |
| Filesystem (JSON) | 🔜 Future |

**Deliverables:**

- [Repository Interfaces](src/repositories/)
- [In-Memory Implementations](src/repositories/inmemory/)
- [Factory Pattern](src/factories/repository_factory.py)
- [Future Storage Stub](future_storage/database_repository_stub.py)
- [Unit Tests](tests/test_repositories.py)
- [Updated Class Diagram](class-diagram.md)

**Running Tests:**

```bash
python -m unittest tests.test_repositories
```

## Assignment 12: Service Layer and REST API

**Technology Stack:** FastAPI, Uvicorn, Pydantic

**Service Layer Classes:**
- `UserService` - User registration, login, management
- `CourseService` - Course CRUD, enrollment
- `AssignmentService` - Assignment management, submissions, grading
- `BookingService` - Study room booking

**API Endpoints:**

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/users/register` | Register a new user |
| POST | `/api/users/login` | Authenticate user |
| GET | `/api/users/{user_id}` | Get user by ID |
| GET | `/api/users/` | Get all users |
| DELETE | `/api/users/{user_id}` | Delete user |
| POST | `/api/courses/` | Create a course |
| GET | `/api/courses/` | Get all courses |
| GET | `/api/courses/{course_id}` | Get course by ID |
| PUT | `/api/courses/{course_id}` | Update course |
| DELETE | `/api/courses/{course_id}` | Delete course |
| POST | `/api/courses/{course_id}/enroll/{student_id}` | Enroll student |
| POST | `/api/assignments/` | Create assignment |
| POST | `/api/assignments/{assignment_id}/submit` | Submit assignment |
| POST | `/api/assignments/submissions/{submission_id}/grade` | Grade submission |
| POST | `/api/bookings/rooms` | Create study room |
| GET | `/api/bookings/rooms` | Get all study rooms |
| GET | `/api/bookings/rooms/available` | Get available rooms |
| POST | `/api/bookings/` | Create booking |
| GET | `/api/bookings/{booking_id}` | Get booking by ID |
| DELETE | `/api/bookings/{booking_id}` | Cancel booking |

**Swagger UI Screenshots:**

- [Full Swagger UI Page](swagger-ui-full.png)
- [Expanded Endpoint](swagger-ui-expanded.png)

**Running the API:**

**API Documentation:** http://localhost:8000/docs (Note: Only works when API is running locally)

**Deliverables:**
- [Service Layer](src/services/)
- [API Routes](src/api/routes/)
- [API Models](src/api/models/)
- [Swagger Screenshot 1](swagger-ui-full.png)
- [Swagger Screenshot 2](swagger-ui-expanded.png)
## Author

**Amanda**

" " 
