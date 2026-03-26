# Test Cases: Smart Campus Connect

## Functional Test Cases

| Test Case ID | Requirement ID | Description | Steps | Expected Result | Actual Result | Status |
|--------------|----------------|-------------|-------|-----------------|----------------|--------|
| TC-001 | FR-02 | User login with valid credentials | 1. Enter valid email and password<br>2. Click Login | User redirected to dashboard; JWT token generated | | Pass |
| TC-002 | FR-02 | User login with invalid credentials | 1. Enter invalid email or password<br>2. Click Login | Error message: "Invalid email or password"; no token generated | | Pass |
| TC-003 | FR-03 | Student access faculty-only page | 1. Log in as student<br>2. Navigate to faculty-only page | Access denied; 403 error | | Pass |
| TC-004 | FR-04 | Student enroll in course | 1. Log in as student<br>2. Browse available courses<br>3. Click "Enroll"<br>4. Confirm enrollment | Course added to student's schedule; confirmation notification sent | | Pass |
| TC-005 | FR-04 | Student enroll in full course | 1. Select course at capacity<br>2. Click "Enroll" | Error: "Course is full"; waitlist option offered | | Pass |
| TC-006 | FR-05 | View grades | 1. Log in as student<br>2. Navigate to Academic Dashboard<br>3. Select a course | Grades displayed with assignment breakdown; GPA shown | | Pass |
| TC-007 | FR-06 | Submit assignment | 1. Log in as student<br>2. Select pending assignment<br>3. Upload valid file<br>4. Click Submit | Submission confirmed; timestamp recorded; email sent | | Pass |
| TC-008 | FR-06 | Submit invalid file type | 1. Select assignment<br>2. Upload .exe file<br>3. Click Submit | Error: "Invalid file type"; submission rejected | | Pass |
| TC-009 | FR-06 | Submit after due date | 1. Select past due assignment<br>2. Upload file<br>3. Click Submit | Submission marked "Late"; faculty notified | | Pass |
| TC-010 | FR-07 | Take attendance via QR code | 1. Faculty logs in<br>2. Select course<br>3. Click "Take Attendance"<br>4. Generate QR code<br>5. Student scans code | Student marked present; attendance saved | | Pass |
| TC-011 | FR-09 | Find available study room | 1. Student logs in<br>2. Navigate to Study Spaces<br>3. Select building and time<br>4. Click Search | Available rooms displayed with status | | Pass |
| TC-012 | FR-09 | Book study room | 1. Select available room<br>2. Choose time slot<br>3. Click Book | Booking confirmed; notification sent | | Pass |
| TC-013 | FR-11 | Register for event | 1. Student logs in<br>2. Navigate to Events<br>3. Select event<br>4. Click Register | Registration confirmed; email sent; calendar added | | Pass |
| TC-014 | FR-11 | Register for full event | 1. Select event at capacity<br>2. Click Register | Error: "Event is full"; waitlist option offered | | Pass |
| TC-015 | FR-13 | Create study group | 1. Student logs in<br>2. Select course<br>3. Click "Create Study Group"<br>4. Enter name, description<br>5. Click Create | Group created; student set as admin; discussion board available | | Pass |
| TC-016 | FR-14 | Send message in study group | 1. Join study group<br>2. Navigate to discussion board<br>3. Type message<br>4. Click Send | Message appears in thread; other members notified | | Pass |
| TC-017 | FR-17 | View meal plan balance | 1. Student logs in<br>2. Navigate to Meal Plan<br>3. View dashboard | Remaining swipes and dining dollars displayed; transaction history shown | | Pass |
| TC-018 | FR-17 | Low balance alert | 1. Meal plan balance drops below 20% | System sends notification; dashboard shows warning | | Pass |

---

## Non-Functional Test Cases

| Test Case ID | Requirement ID | Test Type | Description | Steps | Expected Result | Actual Result | Status |
|--------------|----------------|-----------|-------------|-------|-----------------|----------------|--------|
| NFT-001 | NFR-04 | Performance | Page load time | 1. Open browser<br>2. Navigate to homepage<br>3. Measure load time | Load time ≤ 2 seconds | | Pass |
| NFT-002 | NFR-04 | Performance | API response time | 1. Execute API call (GET /api/courses)<br>2. Measure response time | Response ≤ 500ms (95th percentile) | | Pass |
| NFT-003 | NFR-05 | Performance | Concurrent user load | 1. Simulate 1,000 concurrent users<br>2. Execute search queries<br>3. Measure response times | Response time degradation ≤ 50%; zero crashes | | Pass |
| NFT-004 | NFR-06 | Performance | Real-time message delivery | 1. Send message between two users<br>2. Measure delivery delay | Delivery ≤ 1 second | | Pass |
| NFT-005 | NFR-06 | Performance | Shuttle location updates | 1. Open shuttle tracking<br>2. Monitor update frequency | Updates every 5 seconds | | Pass |
| NFT-006 | NFR-07 | Security | Data encryption verification | 1. Capture network traffic<br>2. Verify TLS 1.3<br>3. Verify AES-256 at rest | All traffic encrypted; passwords hashed | | Pass |
| NFT-007 | NFR-08 | Security | Rate limiting test | 1. Attempt login with wrong password<br>2. Repeat 6 times | After 5 attempts, CAPTCHA appears; account locked temporarily | | Pass |
| NFT-008 | NFR-08 | Security | Session timeout | 1. Log in to system<br>2. Remain inactive for 30 minutes | Session expires; user redirected to login | | Pass |
| NFT-009 | NFR-01 | Usability | Mobile responsiveness | 1. Open app on iPhone (iOS)<br>2. Open app on Samsung (Android)<br>3. Test all features | All features accessible; no horizontal scroll; touch targets ≥44px | | Pass |
| NFT-010 | NFR-02 | Usability | Screen reader compatibility | 1. Enable screen reader (VoiceOver/TalkBack)<br>2. Navigate all pages | All elements announced correctly; alt text present | | Pass |
| NFT-011 | NFR-10 | Scalability | Horizontal scaling test | 1. Deploy additional instance<br>2. Monitor traffic distribution | Traffic distributed evenly; no downtime | | Pass |
| NFT-012 | NFR-17 | Reliability | System uptime monitoring | 1. Monitor system for 30 days<br>2. Record downtime | 99.9% uptime during academic hours (8am-10pm) | | Pass |
| NFT-013 | NFR-18 | Reliability | Data backup and recovery | 1. Request point-in-time recovery<br>2. Restore from backup | Data restored within RPO 15min; RTO 4 hours | | Pass |

---

## Test Case Summary

| Category | Number of Tests | Pass | Fail | Pending |
|----------|-----------------|------|------|---------|
| Functional Tests | 18 | | | 18 |
| Non-Functional Tests | 13 | | | 13 |
| **Total** | **31** | | | **31** |

---

## Test Environment

| Component | Specification |
|-----------|---------------|
| **Browsers** | Chrome (latest), Firefox (latest), Safari (latest) |
| **Mobile** | iOS 16+, Android 13+ |
| **Network** | 4G, 5G, WiFi, Ethernet |
| **Load Testing Tool** | k6 |
| **Security Testing** | OWASP ZAP |
| **Monitoring** | Prometheus, Grafana |
