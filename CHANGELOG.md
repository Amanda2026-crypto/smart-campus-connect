\# Changelog


## [1.4.0] - 2026-05-19

### Added - Assignment 13: CI/CD with GitHub Actions

**Branch Protection:**
- Main branch protected with PR review requirement
- Status checks required before merging
- Direct pushes disabled

**CI Pipeline:**
- GitHub Actions workflow runs tests on every push/PR
- Python 3.13 environment setup

**CD Pipeline:**
- Artifacts uploaded on successful workflow runs

**Documentation:**
- PROTECTION.md with branch protection justification
- Updated README with CI/CD instructions
  

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

