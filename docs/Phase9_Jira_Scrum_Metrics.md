# Phase 9: Jira Project, Sprint Planning & Scrum Metrics

---

## Exercise 13: Jira Scrum Project Setup

### Project Configuration
* **Project Name**: Student Hostel Management System
* **Project Key**: `SHMS`
* **Project Type**: Software Scrum Project
* **Scrum Master**: Alex Mercer
* **Product Owner**: Dr. K. Raman (Chief Warden)

### Epics Structure
1. **EPIC-1: Core Platform & Security Infrastructure (`SHMS-E1`)**
2. **EPIC-2: Room Discovery & Application Management (`SHMS-E2`)**
3. **EPIC-3: Warden Allocation & Grievance Engine (`SHMS-E3`)**
4. **EPIC-4: Administration & Security Audit (`SHMS-E4`)**

---

## Exercise 14: Sprint Planning

The Product Backlog is planned into two 2-week sprints.

### Sprint 1 Plan
* **Sprint Name**: `SHMS Sprint 1 - Auth, Availability & Application Foundation`
* **Duration**: 2 Weeks (10 Working Days)
* **Sprint Goal**: *"Deliver secure SSO/MFA user authentication, real-time room availability dashboard, and student room application form."*
* **Total Committed Story Points**: **21 Story Points**

#### Sprint 1 Backlog Items & Tasks

| Issue Key | Summary / Task Breakdown | Epic | Priority | Story Points |
| :--- | :--- | :--- | :--- | :--- |
| **SHMS-1** | **User Story**: SSO Authentication & MFA Support | EPIC-1 | MUST | 5 |
| SHMS-1.1 | *Task*: Integrate OAuth2 / SAML SSO Client Library | EPIC-1 | HIGH | - |
| SHMS-1.2 | *Task*: Implement TOTP MFA generation & secret validation | EPIC-1 | HIGH | - |
| **SHMS-2** | **User Story**: Room Availability Dashboard | EPIC-2 | MUST | 3 |
| SHMS-2.1 | *Task*: Build `/api/rooms/availability` REST Endpoint | EPIC-2 | MEDIUM | - |
| SHMS-2.2 | *Task*: Create UI Vacancy grid component with live filters | EPIC-2 | MEDIUM | - |
| **SHMS-3** | **User Story**: Student Room Application Form | EPIC-2 | MUST | 5 |
| SHMS-3.1 | *Task*: Create database schema for `ROOM_APPLICATION` | EPIC-2 | HIGH | - |
| SHMS-3.2 | *Task*: Build frontend wizard form with input validation | EPIC-2 | HIGH | - |
| **SHMS-8** | **User Story**: Infrastructure Configuration (Hostel & Rooms) | EPIC-4 | MUST | 5 |
| SHMS-8.1 | *Task*: Build Admin Hostel Block CRUD interfaces | EPIC-4 | HIGH | - |
| **SHMS-10** | **User Story**: Automated Email & SMS Notifications | EPIC-2 | COULD | 3 |

---

### Sprint 2 Plan
* **Sprint Name**: `SHMS Sprint 2 - Allocation Engine, Complaints & Audit Log`
* **Duration**: 2 Weeks (10 Working Days)
* **Sprint Goal**: *"Deliver warden room allocation engine with pessimistic locking, complaint resolution tracking, and append-only security audit logging."*
* **Total Committed Story Points**: **29 Story Points**

#### Sprint 2 Backlog Items & Tasks

| Issue Key | Summary / Task Breakdown | Epic | Priority | Story Points |
| :--- | :--- | :--- | :--- | :--- |
| **SHMS-4** | **User Story**: Warden Room Allocation Engine | EPIC-3 | MUST | 8 |
| SHMS-4.1 | *Task*: Implement SQL pessimistic row lock (`FOR UPDATE`) to prevent double-booking | EPIC-3 | CRITICAL | - |
| SHMS-4.2 | *Task*: Build Warden approval queue UI | EPIC-3 | HIGH | - |
| **SHMS-5** | **User Story**: Student Accommodation Status View | EPIC-2 | MUST | 3 |
| SHMS-5.1 | *Task*: Generate downloadable PDF allotment letter | EPIC-2 | MEDIUM | - |
| **SHMS-6** | **User Story**: Student Grievance Submission | EPIC-3 | SHOULD | 5 |
| SHMS-6.1 | *Task*: Create complaint submission form with image file upload | EPIC-3 | MEDIUM | - |
| **SHMS-7** | **User Story**: Warden Complaint Resolution Dashboard | EPIC-3 | SHOULD | 5 |
| SHMS-7.1 | *Task*: Build Warden complaint status workflow (`OPEN` -> `RESOLVED`) | EPIC-3 | MEDIUM | - |
| **SHMS-9** | **User Story**: Append-only Security Audit Logging | EPIC-4 | MUST | 8 |
| SHMS-9.1 | *Task*: Implement HMAC-SHA256 signature chain for audit event logging | EPIC-4 | CRITICAL | - |

---

## Exercise 15: Sprint Board & Scrum Metrics

### 1. Jira Scrum Board Workflow Representation

```
+-----------------------------------------------------------------------------------+
| JIRA SCRUM BOARD: SHMS Sprint 2                                                   |
+-------------------+-------------------+-------------------+-----------------------+
| TO DO             | IN PROGRESS       | TESTING (QA/SEC)  | DONE                  |
+-------------------+-------------------+-------------------+-----------------------+
| [SHMS-7.1 Task]   | [SHMS-4.1 Task]   | [SHMS-4.2 Task]   | [SHMS-1 Story] (5pt)  |
| Assign Complaints | DB Row Lock       | Warden Alloc UI   | SSO Authentication    |
| Assignee: Dave    | Assignee: Bob     | Assignee: Carol   | Status: VERIFIED      |
|                   |                   |                   |                       |
| [SHMS-6.1 Task]   | [SHMS-9.1 Task]   | [SHMS-5.1 Task]   | [SHMS-2 Story] (3pt)  |
| Upload Evidence   | HMAC Audit Chains | PDF Generator     | Room Availability     |
| Assignee: Eve     | Assignee: Alice   | Assignee: Bob     | Status: VERIFIED      |
|                   |                   |                   |                       |
|                   |                   |                   | [SHMS-3 Story] (5pt)  |
|                   |                   |                   | Room Application Form |
|                   |                   |                   | Status: VERIFIED      |
+-------------------+-------------------+-------------------+-----------------------+
```

---

### 2. Sprint Burndown Data & Visual Chart Representation

#### Sprint 1 Burndown Execution Table (21 Story Points)

| Day | Ideal Remaining Points | Actual Remaining Points | Notes / Events |
| :--- | :--- | :--- | :--- |
| **Day 0** | 21.0 | 21.0 | Sprint 1 Kickoff |
| **Day 2** | 16.8 | 21.0 | Tasks in progress (SHMS-1, SHMS-2) |
| **Day 4** | 12.6 | 16.0 | SHMS-2 (3pt) completed |
| **Day 6** | 8.4 | 11.0 | SHMS-1 (5pt) completed |
| **Day 8** | 4.2 | 6.0 | SHMS-3 (5pt) completed |
| **Day 10**| 0.0 | 0.0 | SHMS-8 (5pt) & SHMS-10 (3pt) completed (100% completion) |

```
Story Points
25 +--* (Actual)
20 |   \ *
15 |     \   *
10 |       \   *
 5 |         \   *
 0 +-----------+---+---+---+---+---+
   Day 0   Day 2 Day 4 Day 6 Day 8 Day 10
   (Ideal Line: - - - | Actual Line: ***)
```

---

### 3. Key Scrum Metrics Summary

| Metric Parameter | Sprint 1 Result | Sprint 2 Result | Overall Project Average / Total |
| :--- | :--- | :--- | :--- |
| **Committed Story Points** | 21 Points | 29 Points | 50 Points |
| **Completed Story Points** | 21 Points | 26 Points | 47 Points |
| **Sprint Velocity** | **21 Points/Sprint** | **26 Points/Sprint** | **23.5 Points/Sprint** |
| **Total Defects Identified** | 3 Defects (Minor) | 2 Defects (1 Security) | 5 Defects Total |
| **Defects Resolved in Sprint** | 3 Defects | 2 Defects | 5 Defects Resolved |
| **Defects Carried Over** | **0 Defects** | **0 Defects** | **0 Defects Carried Over** |
| **Sprint Success Rate** | **100%** | **89.6%** | **94% Combined Delivery** |
