# System Requirements Document (SRD)
## Smart Campus Connect

**Version:** 1.0
**Date:** March 17, 2026
**Author:** Amanda
**Project:** Smart Campus Connect - Assignment 4

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-03-17 | Amanda | Initial SRD for Assignment 4 |

---

## 1. Introduction

### 1.1 Purpose
This System Requirements Document (SRD) defines the complete set of requirements for the Smart Campus Connect system. It captures stakeholder needs, functional capabilities, and quality attributes that the system must deliver.

### 1.2 Scope
Smart Campus Connect is a unified student lifecycle management platform that combines academic tracking, campus navigation, event discovery, and social features. This document covers requirements for all modules including user management, academic services, campus services, events, social features, lost and found, and meal planning.

### 1.3 Definitions and Acronyms

| Term | Definition |
|------|------------|
| SRD | System Requirements Document |
| FR | Functional Requirement |
| NFR | Non-Functional Requirement |
| JWT | JSON Web Token |
| WCAG | Web Content Accessibility Guidelines |
| RPO | Recovery Point Objective |
| RTO | Recovery Time Objective |
| MFA | Multi-Factor Authentication |
| CI/CD | Continuous Integration/Continuous Deployment |

---

## 2. Stakeholder Summary

| Stakeholder | Key Concerns | Priority |
|-------------|--------------|----------|
| Student | Easy access to academics, study spaces, events | High |
| Faculty | Efficient class management, communication | High |
| Administrator | Resource optimization, event approval | High |
| IT Staff | System stability, security, integration | Critical |
| Parent | Student progress monitoring | Low |
| Campus Security | Safety, emergency response | Medium |
| Event Organizer | Event promotion, attendance tracking | Medium |
| Facilities Management | Room utilization, maintenance | Medium |

*For detailed stakeholder analysis, see [STAKEHOLDER-ANALYSIS.md](STAKEHOLDER-ANALYSIS.md)*

---

## 3. Functional Requirements

### 3.1 User Management Module

| ID | Requirement | Acceptance Criteria | Priority |
|----|-------------|---------------------|----------|
| FR-01 | User Registration with university email | Email verification required; duplicate prevention | High |
| FR-02 | JWT-based Authentication | 24h token; 7d refresh; remember me option | High |
| FR-03 | Role-Based Access Control | Student/Faculty/Admin roles with appropriate permissions | High |

### 3.2 Academic Management Module

| ID | Requirement | Acceptance Criteria | Priority |
|----|-------------|---------------------|----------|
| FR-04 | Course Enrollment | Browse by department; conflict checking; limits enforced | High |
| FR-05 | Grade Viewing | Per-course breakdown; GPA calculation; history available | High |
| FR-06 | Assignment Management | Create, submit, grade with file uploads up to 50MB | High |
| FR-07 | Attendance Tracking | QR code or manual entry; attendance alerts at 75% | Medium |

### 3.3 Campus Navigation Module

| ID | Requirement | Acceptance Criteria | Priority |
|----|-------------|---------------------|----------|
| FR-08 | Interactive Campus Map | Building search; details view; floor plans | Medium |
| FR-09 | Study Space Finder | Real-time availability; filtering; 3-hour booking | High |
| FR-10 | Shuttle Tracking | Real-time location; arrival predictions; delay alerts | Medium |

### 3.4 Event Management Module

| ID | Requirement | Acceptance Criteria | Priority |
|----|-------------|---------------------|----------|
| FR-11 | Event Creation & Discovery | Browse by category; calendar view; reminders | High |
| FR-12 | Event Approval Workflow | Admin queue; approval/rejection notifications | High |

### 3.5 Social Features Module

| ID | Requirement | Acceptance Criteria | Priority |
|----|-------------|---------------------|----------|
| FR-13 | Study Group Creation | Course-based groups; join requests; file sharing | Medium |
| FR-14 | In-App Messaging | Real-time; read receipts; push notifications | Medium |

### 3.6 Lost and Found Module

| ID | Requirement | Acceptance Criteria | Priority |
|----|-------------|---------------------|----------|
| FR-15 | Lost Item Reporting | Form with photo; matching notifications; 30-day expiry | Low |
| FR-16 | Found Item Reporting | Photo; location; automatic matching; claim process | Low |

### 3.7 Meal Plan Module

| ID | Requirement | Acceptance Criteria | Priority |
|----|-------------|---------------------|----------|
| FR-17 | Meal Plan Balance Tracking | Remaining swipes; transaction history; low balance alerts | Medium |
| FR-18 | Cafeteria Menu Display | Daily menus; dietary filters; nutritional info | Low |

*For complete functional requirements, see [FUNCTIONAL-REQUIREMENTS.md](FUNCTIONAL-REQUIREMENTS.md)*

---

## 4. Non-Functional Requirements

### 4.1 Usability

| ID | Requirement | Target Metric | Priority |
|----|-------------|---------------|----------|
| NFR-01 | Mobile-First Design | ≤ 3s load on 4G; 44px touch targets | High |
| NFR-02 | WCAG 2.1 AA Accessibility | Alt text; color contrast 4.5:1; keyboard navigation | High |
| NFR-03 | Intuitive Navigation | 5-minute task completion for new users | Medium |

### 4.2 Performance

| ID | Requirement | Target Metric | Priority |
|----|-------------|---------------|----------|
| NFR-04 | Page Load Time | ≤ 2 seconds | High |
| NFR-05 | Concurrent User Support | 5,000 concurrent users | High |
| NFR-06 | Real-Time Updates | ≤ 1s message delay; 5s shuttle updates | Medium |

### 4.3 Security

| ID | Requirement | Target Metric | Priority |
|----|-------------|---------------|----------|
| NFR-07 | Data Encryption | AES-256 at rest; TLS 1.3 in transit | Critical |
| NFR-08 | Authentication Security | Rate limiting; MFA option; 30m session timeout | Critical |
| NFR-09 | Data Privacy | User data export; deletion; audit logs | High |

### 4.4 Scalability

| ID | Requirement | Target Metric | Priority |
|----|-------------|---------------|----------|
| NFR-10 | Horizontal Scaling | Zero downtime scaling; stateless design | High |
| NFR-11 | Database Scalability | Stable performance with 1M+ records | Medium |

### 4.5 Maintainability

| ID | Requirement | Target Metric | Priority |
|----|-------------|---------------|----------|
| NFR-12 | Code Documentation | Swagger API docs; README; ADRs | Medium |
| NFR-13 | Modular Architecture | Independent modules; API versioning | Medium |
| NFR-14 | Automated Testing | ≥80% coverage; CI/CD integration | High |

### 4.6 Deployability

| ID | Requirement | Target Metric | Priority |
|----|-------------|---------------|----------|
| NFR-15 | Multi-Platform Deployment | Linux and Windows support; Docker | Medium |
| NFR-16 | CI/CD Pipeline | Automated builds; staging; rollback capability | High |

### 4.7 Reliability

| ID | Requirement | Target Metric | Priority |
|----|-------------|---------------|----------|
| NFR-17 | System Availability | 99.9% uptime during academic hours | Critical |
| NFR-18 | Data Backup & Recovery | RPO 15min; RTO 4h; quarterly restore tests | Critical |

*For complete non-functional requirements, see [NON-FUNCTIONAL-REQUIREMENTS.md](NON-FUNCTIONAL-REQUIREMENTS.md)*

---

## 5. Requirements Traceability Matrix

| Requirement | Student | Faculty | Admin | IT Staff | Security | Performance |
|-------------|---------|---------|-------|----------|----------|-------------|
| FR-01: Registration | ✓ | ✓ | ✓ | | | |
| FR-02: Authentication | ✓ | ✓ | ✓ | ✓ | ✓ | |
| FR-03: Role-Based Access | ✓ | ✓ | ✓ | ✓ | ✓ | |
| FR-04: Course Enrollment | ✓ | | | | | |
| FR-05: Grade Viewing | ✓ | ✓ | | | | |
| FR-06: Assignment Management | ✓ | ✓ | | | | |
| FR-07: Attendance Tracking | ✓ | ✓ | | | | |
| FR-08: Interactive Map | ✓ | | | | | ✓ |
| FR-09: Study Space Finder | ✓ | | | | | ✓ |
| FR-10: Shuttle Tracking | ✓ | | | | | ✓ |
| FR-11: Event Creation | ✓ | ✓ | ✓ | | | |
| FR-12: Event Approval | | | ✓ | | | |
| FR-13: Study Groups | ✓ | | | | | |
| FR-14: Messaging | ✓ | ✓ | | | ✓ | ✓ |
| FR-15: Lost Items | ✓ | | | | | |
| FR-16: Found Items | ✓ | | | | | |
| FR-17: Meal Plan | ✓ | | | | ✓ | |
| FR-18: Cafeteria Menu | ✓ | | | | | |
| NFR-01: Mobile-First | ✓ | ✓ | | | | ✓ |
| NFR-02: Accessibility | ✓ | ✓ | ✓ | | | |
| NFR-03: Intuitive Nav | ✓ | ✓ | ✓ | | | |
| NFR-04: Page Load | ✓ | ✓ | ✓ | | | ✓ |
| NFR-05: Concurrent Users | ✓ | ✓ | ✓ | ✓ | | ✓ |
| NFR-06: Real-Time | ✓ | | | | | ✓ |
| NFR-07: Encryption | ✓ | ✓ | ✓ | ✓ | ✓ | |
| NFR-08: Auth Security | ✓ | ✓ | ✓ | ✓ | ✓ | |
| NFR-09: Data Privacy | ✓ | ✓ | ✓ | ✓ | ✓ | |
| NFR-10: Horizontal Scale | | | | ✓ | | ✓ |
| NFR-11: DB Scale | | | | ✓ | | ✓ |
| NFR-12: Documentation | | | | ✓ | | |
| NFR-13: Modular | | | | ✓ | | |
| NFR-14: Testing | | | | ✓ | | |
| NFR-15: Multi-Platform | | | | ✓ | | |
| NFR-16: CI/CD | | | | ✓ | | |
| NFR-17: Availability | ✓ | ✓ | ✓ | ✓ | | ✓ |
| NFR-18: Backup | ✓ | ✓ | ✓ | ✓ | ✓ | |

---

## 6. Requirements Prioritization

### Critical (Must Have)
- FR-01, FR-02, FR-03 (User Management)
- FR-04, FR-05, FR-06 (Academic Core)
- NFR-07, NFR-08 (Security)
- NFR-17, NFR-18 (Reliability)

### High Priority (Should Have)
- FR-09 (Study Space Finder)
- FR-11, FR-12 (Event Management)
- NFR-01, NFR-02 (Usability)
- NFR-04, NFR-05 (Performance)
- NFR-09 (Data Privacy)
- NFR-10 (Scalability)
- NFR-14 (Testing)
- NFR-16 (CI/CD)

### Medium Priority (Could Have)
- FR-07 (Attendance Tracking)
- FR-08 (Interactive Map)
- FR-10 (Shuttle Tracking)
- FR-13, FR-14 (Social Features)
- FR-17 (Meal Plan)
- NFR-03, NFR-06, NFR-11, NFR-12, NFR-13, NFR-15

### Low Priority (Nice to Have)
- FR-15, FR-16 (Lost and Found)
- FR-18 (Cafeteria Menu)

---

## 7. Assumptions and Constraints

### Assumptions
1. Users have access to smartphones or computers with internet connectivity
2. University provides API access to existing LMS for course data
3. Campus maps and building data are available in digital format
4. Students have valid university email addresses
5. IT staff will maintain the production infrastructure

### Constraints
1. Budget: $0 (open-source technologies only)
2. Timeline: 12 weeks for initial release
3. Team size: 1 developer
4. Must integrate with existing university systems where possible
5. Must comply with FERPA/GDPR privacy regulations
6. Mobile apps must be approved by Apple and Google stores

---

## 8. Appendix

### 8.1 References
- [STAKEHOLDER-ANALYSIS.md](STAKEHOLDER-ANALYSIS.md)
- [FUNCTIONAL-REQUIREMENTS.md](FUNCTIONAL-REQUIREMENTS.md)
- [NON-FUNCTIONAL-REQUIREMENTS.md](NON-FUNCTIONAL-REQUIREMENTS.md)
- Assignment 3: C4 Architecture Diagrams
- WCAG 2.1 Guidelines: https://www.w3.org/TR/WCAG21/
- FERPA Regulations: https://studentprivacy.ed.gov/

### 8.2 Review History
| Reviewer | Role | Date | Comments |
|----------|------|------|----------|
| TBD | Instructor | | |
| TBD | Peer | | |
