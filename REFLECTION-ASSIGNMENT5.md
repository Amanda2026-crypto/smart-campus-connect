# Reflection: Translating Requirements to Use Cases and Tests

**Assignment 5**
**Amanda**
**March 27, 2026**

---

## Introduction

This reflection documents the challenges I faced while translating the requirements from Assignment 4 into use case diagrams, use case specifications, and test cases for Smart Campus Connect. As a postgraduate student at CPUT, this project must reflect real university needs.

---

## Key Challenges

### 1. Selecting the Right Use Cases from 18 Functional Requirements

**The Challenge:**
Assignment 4 had 18 functional requirements covering user management, academic features, campus services, events, social features, lost and found, and meal plans. I needed to select 8 critical use cases for specifications while ensuring all major stakeholder groups were represented.

**How I Addressed It:**
I prioritized based on stakeholder impact:
| Priority | Use Cases Selected |
|----------|-------------------|
| Student critical | View Grades, Submit Assignment, Find Study Space, Register for Event |
| Faculty critical | Take Attendance, Create Assignment |
| Admin critical | Approve Event |
| Social features | Create Study Group |

This gave me 8 use cases that cover the most important system functions while balancing stakeholder needs.

---

### 2. Writing Alternative Flows for South African University Context

**The Challenge:**
Many requirements didn't specify what happens when things go wrong. I had to think about real scenarios at CPUT:
- Network outages (load shedding affecting Wi-Fi)
- Late submissions (students with connectivity issues)
- Room booking conflicts (limited study spaces)

**How I Addressed It:**
I added alternative flows for:
| Scenario | Alternative Flow |
|----------|-----------------|
| Network failure | System saves draft locally, syncs when online |
| Late submission | Mark as "Late", notify faculty, deduct points |
| Booking conflict | Show alternative times, suggest other rooms |
| Full course/event | Add to waitlist, notify when spot opens |

---

### 3. Creating Test Cases with Proper CPUT Email Formats

**The Challenge:**
Initially I used generic email formats. My friend pointed out that CPUT uses specific formats:
- Students: `studentnumber@mycput.ac.za`
- Staff: `staffnumber@mycput.ac.za`

**How I Addressed It:**
I updated all test cases to use realistic CPUT email addresses:
- Student: `221350977@mycput.ac.za` (my student number)
- Faculty: `987654321@mycput.ac.za` (generic staff number)

This makes the test cases more realistic for the South African university context.

---

### 4. Ensuring Traceability Back to Assignment 4

**The Challenge:**
Each use case and test case needed to map back to specific requirements from Assignment 4. I had to ensure nothing was missed.

**How I Addressed It:**
I created traceability tables:
| Artifact | Traceability |
|----------|--------------|
| Use Cases | Each maps to 1-3 functional requirements (FR-05, FR-06, etc.) |
| Functional Tests | Each maps to specific FR (TC-FR-001 maps to FR-01) |
| Non-Functional Tests | Each maps to specific NFR (TC-NFR-001 maps to NFR-04) |

This ensures every test case can be traced back to a requirement.

---

### 5. Balancing Test Coverage Against Time Constraints

**The Challenge:**
I needed enough test cases to show thorough testing but not so many that it becomes unmanageable.

**How I Addressed It:**
I created:
- **25 functional tests** covering all major user journeys
- **13 non-functional tests** covering performance, security, usability, scalability, reliability

This gives 38 total tests, which is sufficient for demonstrating test coverage.

---

## Lessons Learned

### 1. Requirements Are Not Complete Without Test Cases
Writing test cases revealed gaps in my requirements. For example, I realized I hadn't specified what happens when a student submits an assignment after the due date. This led me to add alternative flows in the use case specifications.

### 2. Context Matters
The South African university context (load shedding, data costs, CPUT email formats) affects how users interact with the system. I should have considered this earlier.

### 3. Traceability Takes Time
Creating traceability tables was tedious but necessary. Without them, it's easy to miss requirements or create orphaned test cases.

### 4. Alternative Flows Are Essential
The basic flow shows what should happen. Alternative flows show the system is robust. I learned that alternative flows often come from real user experiences, not just requirements documents.

---

## Conclusion

Translating requirements to use cases and test cases requires constant back-and-forth between what stakeholders want and what the system can deliver. The challenges I faced—selecting use cases, writing alternative flows, using correct CPUT formats, ensuring traceability—all taught me that requirements engineering is not a linear process.

The 8 use cases and 38 test cases I produced provide a solid foundation for implementation in future assignments. The traceability matrices ensure that when a test fails, I know exactly which requirement is affected.

If I were to do this again, I would involve stakeholders earlier to validate use cases before writing specifications, and I would create test cases in parallel with requirements rather than after.

---

## Appendix: Traceability Summary

| Assignment 4 | Assignment 5 |
|--------------|--------------|
| 18 Functional Requirements | 25 Functional Test Cases |
| 18 Non-Functional Requirements | 13 Non-Functional Test Cases |
| 10 Stakeholders | 6 Actors in Use Case Diagram |
| 5 Stakeholder Categories | 8 Critical Use Cases |
