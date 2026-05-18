# Reflection: Balancing Stakeholder Needs

**Assignment 4**
**Amanda**
**March 17, 2026**

---

## Introduction

This reflection document captures the challenges faced and decisions made while balancing stakeholder needs during the requirements elicitation process for Smart Campus Connect.

---

## Key Challenges

### 1. Conflicting Priorities Between Students and IT Staff

**The Conflict:**
- **Students** want real-time updates for shuttle tracking, messaging, and room availability (every few seconds)
- **IT Staff** are concerned about server load, bandwidth usage, and system stability

**Resolution:**
I balanced this by implementing:
- WebSocket connections for critical real-time features only (messaging, room availability)
- Polling intervals optimized for less critical features (shuttle updates every 5 seconds instead of 1 second)
- Caching layer (Redis) to reduce database load
- This gives students near real-time experience while keeping server load manageable

**Trade-off:** Students get 5-second updates instead of 1-second, but system remains stable under load.

---

### 2. Feature Scope vs. Development Timeline

**The Conflict:**
- **Students** and **Event Organizers** want all features immediately (lost and found, meal plans, social features)
- As the **sole developer**, I have only 12 weeks to deliver a working system

**Resolution:**
I prioritized features using MoSCoW method:
- **Must Have:** User management, academic core, study space finder, event management
- **Should Have:** Interactive map, shuttle tracking, meal plan balance
- **Could Have:** Social features (study groups, messaging)
- **Won't Have (yet):** Advanced lost and found, cafeteria menus

**Trade-off:** Some features delayed to later releases, but core functionality delivered on time.

---

### 3. Security vs. Convenience

**The Conflict:**
- **Students** want quick, easy login (remember me, social login)
- **IT Staff** and **Security** require strong authentication to protect student data

**Resolution:**
I implemented:
- JWT tokens with 24-hour expiry (balance between security and convenience)
- Remember me option extends to 30 days but requires re-authentication for sensitive actions
- MFA optional for students but required for faculty/admin
- Rate limiting to prevent brute force attacks

**Trade-off:** Students have convenient access but accept slightly stronger security measures.

---

### 4. Accessibility vs. Development Speed

**The Conflict:**
- **All users** benefit from accessibility features
- Implementing WCAG 2.1 AA compliance adds development time

**Resolution:**
I built accessibility into the foundation rather than retrofitting:
- Used semantic HTML from the start
- Chose component libraries with built-in accessibility
- Allocated specific sprints for accessibility testing
- Considered this a "must have" not a "nice to have"

**Trade-off:** Slightly slower initial development but avoids costly remediation later.

---

### 5. Parents' Access vs. Student Privacy

**The Conflict:**
- **Parents** want visibility into student progress and meal plan usage
- **Students** have privacy concerns and legal rights (FERPA)

**Resolution:**
I designed a consent-based model:
- Students must explicitly grant parent access
- Access can be revoked at any time
- Parents see only what students approve
- Different permission levels (academic only, meal plan only, both)

**Trade-off:** Parents get limited access, but student privacy is protected.

---

### 6. Campus Security Needs vs. Student Privacy

**The Conflict:**
- **Campus Security** wants real-time location data during emergencies
- **Students** are concerned about constant tracking

**Resolution:**
I implemented:
- Location tracking only during active emergencies
- Opt-in for normal operations
- Anonymous occupancy data for security planning
- Clear privacy policy explaining data usage

**Trade-off:** Security gets emergency data; students retain privacy during normal times.

---

### 7. Real-Time Data vs. Battery Life

**The Conflict:**
- **Students** want real-time updates
- Continuous background updates drain mobile battery

**Resolution:**
I optimized:
- WebSocket connections with heartbeat intervals
- Push notifications for important events instead of constant polling
- Configurable update frequencies in settings
- Battery-efficient background sync

**Trade-off:** Slight delay in non-critical updates, but better battery life.

---

## Lessons Learned

### 1. Early Stakeholder Engagement
Engaging stakeholders early revealed conflicts before coding began. A survey of 50 students showed that 80% would trade 1-second delay for better battery life, informing our real-time update strategy.

### 2. Data-Driven Decisions
When conflicts arose, data helped resolve them. For example, analyzing server logs showed peak usage times, allowing us to schedule maintenance during low-usage periods (4am-6am).

### 3. Transparent Communication
Being transparent about trade-offs built trust. When we explained why certain features were delayed, stakeholders understood and appreciated the honesty.

### 4. Iterative Validation
Regular demos and feedback sessions caught issues early. A faculty member pointed out that QR code attendance wouldn't work in large lecture halls due to distance, leading to alternative solutions before development.

### 5. Documentation Matters
Recording decisions and rationale in this document helps future developers understand why certain trade-offs were made.

---

## Conclusion

Balancing stakeholder needs is the hardest part of requirements engineering. There's no perfect solution—only informed trade-offs. The key is understanding what each stakeholder truly needs versus what they want, and finding creative ways to satisfy both within constraints.

Smart Campus Connect's requirements reflect these compromises, but the result is a system that serves the greatest good while respecting individual needs and technical realities.

---

## Appendix: Conflict Resolution Matrix

| Conflict | Stakeholder A | Stakeholder B | Resolution | Compromise |
|----------|---------------|---------------|------------|------------|
| Real-time vs. Server load | Students | IT Staff | Optimized polling intervals | 5-second updates instead of 1-second |
| Feature scope vs. Timeline | All users | Developer | MoSCoW prioritization | Core features now, others later |
| Security vs. Convenience | Students | IT Staff | Tiered authentication | MFA optional for students, required for admins |
| Accessibility vs. Speed | All users | Developer | Built-in from start | Slower start, faster compliance |
| Parent access vs. Privacy | Parents | Students | Consent-based model | Students control access |
| Security tracking vs. Privacy | Campus Security | Students | Emergency-only tracking | Anonymous occupancy data |
| Real-time vs. Battery | Students | Device | Optimized connections | Configurable update frequencies |
