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
graph TD
    Student["Student"] -->|Uses| SCC["Smart Campus Connect"]
    Faculty["Faculty Member"] -->|Uses| SCC
    Admin["Administrator"] -->|Manages| SCC
    SCC -->|Syncs with| LMS["University LMS"]
    SCC -->|Gets maps from| Maps["Google Maps"]
    SCC -->|Sends| Email["Email Service"]
