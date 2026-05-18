\# Changelog



\## \[1.0.0] - 2026-05-02



\### Added

\- Complete domain model implementation (User, Student, Faculty, Admin, Course, Enrollment, Assignment, Submission, StudyRoom, Booking, Event, EventRegistration)



\### Creational Design Patterns

\- \*\*Simple Factory\*\*: UserFactory for creating Student, Faculty, Admin objects

\- \*\*Factory Method\*\*: PaymentProcessor with CreditCardProcessor and PayPalProcessor

\- \*\*Abstract Factory\*\*: GUIFactory for Windows/MacOS UI components

\- \*\*Builder\*\*: AssignmentBuilder for complex assignment creation

\- \*\*Prototype\*\*: NotificationTemplateCache for cloning notification templates

\- \*\*Singleton\*\*: DatabaseConnection for thread-safe database access



\### Tests

\- Unit tests for all six creational patterns (25 tests total)

\- All tests passing



\### Documentation

\- Updated README.md with language choice and pattern rationales

\- Created CHANGELOG.md

