
## Challenges Faced in Designing the Domain Model and Class Diagram

### Challenge 1: Identifying the Right Level of Abstraction

The first challenge was determining which entities should be included in the domain model. My system has many potential entities (User, Course, Assignment, Submission, Booking, Event, StudyGroup, Message, LostItem, FoundItem, MealPlan, Transaction, Shuttle, etc.). I had to decide which ones were truly core to the domain.

**How I resolved it:** I referred back to Assignment 4's functional requirements and Assignment 5's use cases. If a requirement referenced an entity, I included it. For example, FR-09 (Study Space Finder) directly references StudyRoom and Booking, so both were included. This gave me 22 entities, which I then organized into a coherent model.

**Lesson learned:** Domain modeling is not about including every possible data point. It is about capturing the essential concepts that stakeholders use to describe the business.

### Challenge 2: Modeling the User Inheritance Hierarchy

Deciding whether to use inheritance or composition for user types was difficult. Students, Faculty, and Admins share common attributes (name, email, password) but have different responsibilities.

**How I resolved it:** I chose inheritance (abstract User class with concrete subclasses) because:
- All user types have the same authentication mechanism
- The "is-a" relationship holds (Student is a User)
- It eliminates code duplication

**Trade-off:** Inheritance creates coupling between classes. If the User class changes, all subclasses are affected. However, for this domain, the stability of user attributes justifies this coupling.

### Challenge 3: Defining Multiplicity Constraints

Determining the correct multiplicity (1..*, 0..1, etc.) for relationships required deep understanding of business rules. For example, can a Course exist without any Enrollments? Yes (new courses). Can an Enrollment exist without a Student? No.

**How I resolved it:** I created business rules (BR-01 to BR-13) in the domain model and used them to derive multiplicity. For example:
- BR-01: "A Course must have exactly one Faculty instructor" → Multiplicity 1 on the Faculty side
- BR-10: "A StudyGroup must have at least 3 members" → Multiplicity * on the Student side

**Lesson learned:** Multiplicity is not arbitrary. It comes directly from business rules.

### Challenge 4: Distinguishing Aggregation vs. Composition

Some relationships could be modeled as either aggregation (weak "has-a") or composition (strong "whole-part"). For example, Shuttle and ShuttleLocation.

**How I resolved it:** I used composition for Shuttle → ShuttleLocation because:
- A ShuttleLocation has no meaning without a Shuttle
- If a Shuttle is deleted, its location history should be deleted
- This follows the "lifecycle dependency" rule

For other relationships like Course → Assignment, I used aggregation because Assignments might be archived or transferred even if a Course is deleted.

**Lesson learned:** Composition implies lifecycle dependency. Aggregation implies independence.

### Challenge 5: Method Signature Design

Deciding what methods each class should have and what parameters they should take required balancing completeness against simplicity.

**How I resolved it:** I focused on methods directly traceable to use cases from Assignment 5. For example:
- UC-002 (Submit Assignment) → `Submission.submit()`
- UC-005 (Find Study Space) → `StudyRoom.checkAvailability()`

I also added parameter types and return types (e.g., `enrollInCourse(courseId: String): Boolean`) to make the signatures actionable for implementation.

**Lesson learned:** Methods should directly support use cases. If a method does not trace to a requirement or use case, it may be unnecessary.

---

## How the Class Diagram Aligns with Previous Assignments

### Alignment with Assignment 4 (Functional Requirements)

Every functional requirement from Assignment 4 is represented in the class diagram:

| FR | Class | Method/Attribute |
|----|-------|------------------|
| FR-01 | User | register() |
| FR-02 | User | login() |
| FR-03 | User | role attribute |
| FR-04 | Enrollment | enrollmentId, studentId, courseId |
| FR-05 | Enrollment | grade attribute |
| FR-06 | Assignment, Submission | publish(), submit() |
| FR-07 | Attendance | markPresent() |
| FR-09 | StudyRoom, Booking | checkAvailability(), confirm() |
| FR-10 | Shuttle, ShuttleLocation | updateLocation() |
| FR-11 | Event, EventRegistration | register() |
| FR-12 | Event | approve(), reject() |
| FR-13 | StudyGroup | addMember() |
| FR-14 | Message | send() |
| FR-15 | LostItem | report() |
| FR-16 | FoundItem | matchWithLost() |
| FR-17 | MealPlan, Transaction | deductSwipe(), record() |

### Alignment with Assignment 5 (Use Cases)

Each use case maps directly to one or more methods:

| Use Case | Class Method |
|----------|--------------|
| UC-001 (Register Account) | `User.register()` |
| UC-002 (Submit Assignment) | `Submission.submit()` |
| UC-003 (Take Attendance) | `Attendance.markPresent()` |
| UC-004 (Create Assignment) | `Faculty.createAssignment()` |
| UC-005 (Find Study Space) | `StudyRoom.checkAvailability()` |
| UC-006 (Register for Event) | `EventRegistration.register()` |
| UC-007 (Create Study Group) | `Student.createStudyGroup()` |
| UC-008 (Approve Event) | `Admin.approveEvent()` |

### Alignment with Assignment 8 (State Diagrams)

Each state diagram corresponds to a class with a status attribute:

| State Diagram | Class | Status Attribute |
|---------------|-------|------------------|
| User Account | User | isActive, role |
| Assignment Submission | Submission | isLate, score |
| Study Room Booking | Booking | status (PENDING, CONFIRMED, CANCELLED) |
| Event | Event | status (DRAFT, SUBMITTED, APPROVED, PUBLISHED) |
| Meal Plan Transaction | Transaction | type (SWIPE, DINING_DOLLAR) |
| Lost Item Report | LostItem | status (REPORTED, INVESTIGATING, FOUND, CLAIMED) |
| Study Group | StudyGroup | isActive |
| Shuttle Location | ShuttleLocation | status (ON_TIME, DELAYED, OFF_ROUTE) |

---

## Trade-offs Made

### Trade-off 1: Inheritance vs. Composition for User Types

**Chosen:** Inheritance (abstract User class)

**Alternative:** Composition (User has a Role attribute with different behaviors injected)

**Why this trade-off:** Inheritance is simpler and more intuitive for this domain. The user types are stable (unlikely to change), and they share significant common behavior (authentication, profile management). Composition would add unnecessary complexity.

### Trade-off 2: Separate Enrollment vs. Direct Many-to-Many

**Chosen:** Separate Enrollment class

**Alternative:** Direct many-to-many between Student and Course with a join table

**Why this trade-off:** The enrollment relationship has its own attributes (grade, status, enrolledAt) and methods (drop, complete). Using a separate class follows UML best practices for association classes and makes the model more expressive.

### Trade-off 3: Method Verbosity

**Chosen:** Included parameter types and return types in all method signatures

**Alternative:** Only method names without signatures

**Why this trade-off:** The assignment requires UML compliance. Including signatures makes the diagram more useful for implementation and demonstrates understanding of method design.

### Trade-off 4: Number of Entities

**Chosen:** 22 entities

**Alternative:** Fewer entities (5-7 as suggested)

**Why this trade-off:** While the assignment suggested 5-7 entities, my system is complex and requires more entities to accurately model the domain. I prioritized completeness over minimalism, ensuring all functional requirements are represented.

---

## Lessons Learned About Object-Oriented Design

### Lesson 1: Domain Models Are Communication Tools

The domain model is not just for developers. It communicates the structure of the system to stakeholders. Using consistent terminology from requirements (e.g., "Enrollment" not "Registration") ensures everyone understands the model.

### Lesson 2: Start with Nouns, Then Add Verbs

I started by listing all nouns from the requirements (User, Course, Assignment, etc.). Then I added relationships. Finally, I added methods (verbs) based on use cases. This systematic approach prevented me from missing entities.

### Lesson 3: Multiplicity Reveals Business Rules

Business rules often hide in multiplicity constraints. For example, "A Course must have exactly one Faculty instructor" is a business rule expressed as multiplicity 1 on the Faculty side. Writing explicit business rules (BR-01 to BR-13) helped me derive correct multiplicity.

### Lesson 4: Traceability Keeps You Honest

Without traceability, it is easy to add unnecessary classes or miss required ones. My traceability tables (mapping to FRs, use cases, and state diagrams) ensured every class had a purpose.

### Lesson 5: Inheritance Requires Careful Consideration

Inheritance is powerful but creates coupling. I used it only where the "is-a" relationship was clear and the subclasses shared significant behavior. For other relationships, I used composition or aggregation.

---

## Conclusion

Designing the domain model and class diagram for Smart Campus Connect required balancing completeness against complexity. I identified 22 core entities, defined their attributes and methods, established relationships with proper multiplicity, and documented 13 business rules. The model traces directly to functional requirements (Assignment 4), use cases (Assignment 5), and state diagrams (Assignment 8).

The biggest challenge was determining the right level of abstraction—knowing when to create a separate class (Enrollment) versus a simple attribute. The trade-offs I made (inheritance vs. composition, separate class vs. direct relationship) were guided by object-oriented principles and the specific needs of this domain.

This assignment reinforced that good domain models are not just technically correct; they are understandable to stakeholders, traceable to requirements, and implementable by developers.
