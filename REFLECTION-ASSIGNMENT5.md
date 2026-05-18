# Reflection: Translating Requirements to Use Cases and Tests

**Assignment 5**
**Amanda**
**March 26, 2026**

---

## Introduction

This reflection captures the challenges faced and decisions made while translating requirements from Assignment 4 into use case diagrams, specifications, and test cases for Smart Campus Connect.

---

## Key Challenges

### 1. Identifying the Right Use Cases

**The Challenge:**
Assignment 4 had 18 functional requirements. I needed to select 8 critical use cases that captured the most important system behaviors while ensuring coverage across all stakeholder groups.

**How I Addressed It:**
I prioritized based on:
- **Stakeholder impact:** Use cases that affect the most stakeholders
- **Criticality:** Features that are must-have vs nice-to-have
- **Complexity:** Use cases that demonstrate the system's core value

The selected use cases cover:
| Use Case | Stakeholder Priority |
|----------|---------------------|
| View Grades | Student, Faculty - High |
| Submit Assignment | Student - High |
| Take Attendance | Faculty - Medium |
| Create Assignment | Faculty - High |
| Find Study Space | Student - High |
| Register for Event | Student - Medium |
| Create Study Group | Student - Medium |
| Approve Event | Admin - High |

---

### 2. Writing Clear Alternative Flows

**The Challenge:**
Many requirements didn't specify what happens when things go wrong (e.g., network failure, invalid input). I had to infer error scenarios that real users would encounter.

**How I Addressed It:**
I thought through common failure scenarios:
| Scenario | Alternative Flow |
|----------|-----------------|
| Network timeout | Save draft, offer retry |
| Invalid file upload | Reject with allowed formats |
| Late submission | Mark as late, notify faculty |
| Duplicate QR scan | Reject second scan |
| Room already booked | Show available alternatives |

This approach ensures the system handles real-world edge cases.

---

### 3. Balancing Completeness vs. Clarity in Test Cases

**The Challenge:**
Test cases needed to be detailed enough to be executable but not so detailed they become unreadable. I also needed to cover both functional and non-functional requirements.

**How I Addressed It:**
I created:
- **18 functional tests** covering critical user journeys
- **13 non-functional tests** covering performance, security, usability, scalability, and reliability

The non-functional tests directly address the quality attributes from Assignment 4:

| Attribute | Tested In |
|-----------|----------|
| Performance | NFT-001, NFT-002, NFT-003, NFT-004, NFT-005 |
| Security | NFT-006, NFT-007, NFT-008 |
| Usability | NFT-009, NFT-010 |
| Scalability | NFT-011 |
| Reliability | NFT-012, NFT-013 |

---

### 4. Ensuring Traceability

**The Challenge:**
Each test case needed to map back to a requirement from Assignment 4. Some requirements were broad (e.g., "system shall be secure") and needed multiple test cases.

**How I Addressed It:**
I created a traceability matrix:

| Requirement | Test Cases |
|-------------|------------|
| FR-02 (Authentication) | TC-001, TC-002, NFT-007, NFT-008 |
| FR-06 (Assignment) | TC-007, TC-008, TC-009 |
| FR-09 (Study Space) | TC-011, TC-012 |
| NFR-04 (Performance) | NFT-001, NFT-002, NFT-003 |
| NFR-07 (Security) | NFT-006, NFT-007, NFT-008 |

---

### 5. Consistency Across Assignments

**The Challenge:**
The use case diagram needed to align with the actors from Assignment 4 (stakeholders) and functional requirements. Any mismatch would break traceability.

**How I Addressed It:**
I mapped stakeholders to actors:

| Assignment 4 Stakeholder | Assignment 5 Actor |
|--------------------------|-------------------|
| Student | Student |
| Faculty Member | Faculty Member |
| Administrator | Administrator |
| IT Staff | IT Staff |
| Parent | Parent |
| Campus Security | Campus Security |

All actors from Assignment 4 are represented in the use case diagram.

---

## Lessons Learned

### 1. Use Cases Bridge Requirements and Implementation
Use cases are the natural link between what stakeholders want (requirements) and what developers build (code). Getting this layer right reduces misunderstandings later.

### 2. Alternative Flows Are Essential
The basic flow shows the happy path, but alternative flows show the system is robust. I learned that thinking through failure scenarios early saves development time.

### 3. Test Cases Are Requirements Validation
Writing test cases forces you to ask: "How would I know this requirement is satisfied?" This reveals gaps in requirements before coding starts.

### 4. Traceability is Hard but Necessary
Mapping requirements → use cases → tests ensures nothing is missed. I created a spreadsheet to track this, which helped maintain consistency.

---

## Conclusion

Translating requirements to use cases and test cases is not mechanical—it requires judgment about what to include, how detailed to be, and how to handle edge cases. The decisions I made in this assignment prioritize:

- **Coverage:** Use cases across all stakeholder groups
- **Clarity:** Step-by-step flows with clear conditions
- **Traceability:** Clear links back to Assignment 4 requirements
- **Practicality:** Test cases that are actually executable

The resulting artifacts provide a solid foundation for development and testing in future assignments.
