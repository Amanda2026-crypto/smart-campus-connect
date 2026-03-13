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
C4Context
title System Context diagram for Smart Campus Connect

Person(student, "Student", "University student")
Person(faculty, "Faculty Member", "Professor")
Person(admin, "Administrator", "Staff member")

System(scc, "Smart Campus Connect", "Unified student platform")

System_Ext(lms, "University LMS", "Existing system")
System_Ext(maps, "Maps Service", "Google Maps")
System_Ext(email, "Email Service", "Notifications")

Rel(student, scc, "Uses")
Rel(faculty, scc, "Uses")
Rel(admin, scc, "Manages")
Rel(scc, lms, "Syncs course data")
Rel(scc, maps, "Gets maps")
Rel(scc, email, "Sends emails")
