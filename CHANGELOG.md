# Changelog

## [1.0.0] - 2026-05-02

### Added

- Complete domain model implementation (User, Student, Faculty, Admin, Course, Enrollment, Assignment, Submission, StudyRoom, Booking, Event, EventRegistration)

### Creational Design Patterns

- **Simple Factory**: UserFactory for creating Student, Faculty, Admin objects
- **Factory Method**: PaymentProcessor with CreditCardProcessor and PayPalProcessor
- **Abstract Factory**: GUIFactory for Windows/MacOS UI components
- **Builder**: AssignmentBuilder for complex assignment creation
- **Prototype**: NotificationTemplateCache for cloning notification templates
- **Singleton**: DatabaseConnection for thread-safe database access

### Tests

- Unit tests for all six creational patterns (25 tests total)
- All tests passing

### Documentation

- Updated README.md with language choice and pattern rationales
- Created CHANGELOG.md


---

## [1.2.0] - 2026-05-04

### Added - Assignment 11: Repository Pattern

**Repository Interfaces:**
- Generic `Repository[T, ID]` interface with CRUD operations
- Entity-specific interfaces for User, Course, Assignment, Booking, Event
- 20+ custom query methods (find_by_email, find_by_department, etc.)

**In-Memory Implementations:**
- HashMap-based storage using Python dict
- Complete CRUD operations for all entities
- All custom query methods implemented

**Factory Pattern:**
- `RepositoryFactory` class for storage abstraction
- Switch storage via `storage_type` parameter
- Currently supports "MEMORY" storage

**Future-Proofing:**
- `DatabaseUserRepository` stub for future database integration

**Unit Tests:**
- 10+ test cases covering all CRUD operations
- Factory pattern tests
- All tests passing

**Documentation:**
- Updated class diagram with repository layer
- README justification for design decisions


---

### Added - Assignment 12: Service Layer and REST API

**Service Layer:**
- `UserService` - Registration, login, user management
- `CourseService` - Course CRUD, enrollment
- `AssignmentService` - Assignment management, submissions, grading
- `BookingService` - Study room booking

**REST API (FastAPI):**
- 15+ endpoints for users, courses, assignments, bookings
- OpenAPI/Swagger documentation auto-generated
- Request/response validation using Pydantic schemas

**Testing:**
- Unit tests for service layer
- Integration tests for API endpoints

**Business Rules Implemented:**
- Email must be @mycput.ac.za
- Booking duration ≤ 3 hours
- Cancellation ≥ 1 hour before start
- Course capacity limits
- Assignment due date validation
