# Phase 7: User Interface Design

## Exercise 11: UI Wireframe Designs & Golden Rules Analysis

---

### 1. Application of Shneiderman's 8 Golden Rules of UI Design

1. **Strive for Consistency**: Uniform color palette (Slate Blue `#1E293B`, Emerald `#10B981`, Coral `#EF4444`), standardized button styles, consistent navbar layout across Student, Warden, and Admin dashboards.
2. **Enable Frequent Users to Use Shortcuts**: Keyboard shortcuts for Wardens processing bulk approvals (`Alt + A` for Approve, `Alt + R` for Reject), quick search auto-filtering.
3. **Offer Informative Feedback**: Real-time toast notifications upon room application submission, status badge updates (`PENDING` in amber, `ALLOCATED` in green), interactive loading states.
4. **Design Dialogs to Yield Closure**: Multi-step wizard for room applications (Step 1: Select Block → Step 2: Room Type → Step 3: Confirm & Submit) with unambiguous confirmation modal.
5. **Offer Simple Error Handling**: Inline real-time form validation highlighting invalid student IDs or duplicate applications before form submission.
6. **Permit Easy Reversal of Actions**: Warden allocation review window allows undoing room allocation within 10 minutes prior to final commitment.
7. **Support Internal Locus of Control**: Clear navigation breadcrumbs, explicit cancel buttons on modals, non-modal status drawers.
8. **Reduce Short-Term Memory Load**: Auto-filling student details from SSO session, room capacity counters displayed directly beside selection dropdowns.

---

### 2. Major Screen Wireframes Specification

#### Screen 1: Student Portal - Room Application & Availability

* **User Type**: Student
* **User Goal**: View available hostel blocks, check vacant bed count, select preferences, submit room application, view allotment status.
* **Navigation**: Top Bar (`Dashboard` | `Apply for Room` | `My Accommodation` | `Complaints` | `Profile`).
* **Required Information**: Live vacant bed count by block, room fee breakdown, application status timeline.
* **Input Fields**: Hostel Block Select, Room Configuration (Single / Double / AC), Roommate Preference ID, Declaration Checkbox.
* **Error Handling**: Warning message if student has unpaid tuition dues or duplicate active application.

```
+-----------------------------------------------------------------------------------+
|  [SHMS Logo]  Student Portal   Dashboard  Apply Room  Accommodation  Complaints   |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  Welcome back, Rahul Sharma (ID: STU-2024-8841)                                    |
|                                                                                   |
|  +-----------------------------------+  +--------------------------------------+  |
|  | Live Hostel Vacancy               |  | Application Status                   |  |
|  | Block A (Boys): 14 Beds Available |  | Status: [ ALLOCATED ] (Green Badge)  |  |
|  | Block B (Boys): 02 Beds Available |  | Room: Block A - Room 302 (Bed 1)     |  |
|  | Block C (Girls): 28 Beds Available|  | Allotment Date: 01-Oct-2026          |  |
|  +-----------------------------------+  +--------------------------------------+  |
|                                                                                   |
|  Hostel Room Application Form                                                     |
|  -------------------------------------------------------------------------------  |
|  1. Select Preferred Block:  [ Block A - Sunflower Hall (Male)          v ]       |
|  2. Select Room Category:    (o) Double Sharing (Non-AC)   ( ) Single AC          |
|  3. Roommate Preference ID:  [ STU-2024-9912                             ]       |
|                                                                                   |
|  [ Cancel Application ]                     [ SUBMIT APPLICATION -> ]             |
+-----------------------------------------------------------------------------------+
```

---

#### Screen 2: Warden Dashboard - Allocation & Complaint Resolution

* **User Type**: Hostel Warden
* **User Goal**: Review pending room applications, perform room allotment, view block occupancy, assign and resolve student complaints.
* **Navigation**: Sidebar (`Pending Applications` | `Room Allocation Grid` | `Complaints Center` | `Block Analytics`).
* **Required Information**: Pending student application queue, student merit score, room occupancy grid, complaint priority ticket list.
* **Input Fields**: Filter by Department/Merit, Room Allocation Dropdown, Maintenance Staff Assignment Select, Resolution Remarks Textarea.
* **Error Handling**: Alert modal if warden attempts to allocate a student to a room that has reached maximum capacity.

```
+-----------------------------------------------------------------------------------+
| [Warden Portal]  Block A Supervisor Dashboard           Logged in: Warden Prof. V |
+-----------------------------------------------------------------------------------+
| [Applications]  | Pending Student Applications Queue (Total: 12)                  |
| [Room Grid]     | Search: [ STU-2024... ]   Filter: [ Merit Rank High-Low v ]      |
| [Complaints]    | --------------------------------------------------------------- |
| [Analytics]     | Student Name   ID           Merit  Pref. Room  Action           |
|                 | Rahul Sharma   STU-2024-88  94.2%  Double AC   [ ALLOCATE ROOM ] |
|                 | Priya Patel    STU-2024-91  91.8%  Single AC   [ ALLOCATE ROOM ] |
|                 | --------------------------------------------------------------- |
|                 |                                                                 |
|                 | Maintenance Complaints Center                                   |
|                 | Ticket ID  Room  Category    Priority  Status       Action      |
|                 | #CMP-104   A-201 Electrical  HIGH      [IN_PROGRESS] [ RESOLVE ]|
|                 | #CMP-108   A-104 Plumbing    MEDIUM    [OPEN       ] [ ASSIGN  ]|
+-----------------------------------------------------------------------------------+
```

---

#### Screen 3: Admin Dashboard - Infrastructure & Security Audit Log

* **User Type**: System Administrator
* **User Goal**: Manage hostel blocks, set room tariffs, assign wardens, review security audit trails, monitor system threat indicators.
* **Navigation**: Top Navigation (`Hostel Config` | `Warden Assignments` | `Security Audit Logs` | `System Health`).
* **Required Information**: System activity metrics, security threat alert log, audit trails, active sessions.
* **Input Fields**: Hostel Name, Room Count, Fee Rate, Warden Assignment Dropdown, Log Date Range Picker.
* **Error Handling**: Confirmation prompt with administrative password verification before overriding room allocation or wiping old logs.

```
+-----------------------------------------------------------------------------------+
| [SHMS Admin]  System Management Console                      Security: NORMAL     |
+-----------------------------------------------------------------------------------+
| System Summary:  Hostels: 6  | Rooms: 480  | Students: 1,120  | Security Threats: 0|
| --------------------------------------------------------------------------------- |
| [ Create New Hostel Block ]    [ Assign Block Warden ]    [ Export Audit PDF ]    |
|                                                                                   |
| Security & Allocation Audit Log (Append-Only)                                     |
| Timestamp           User        Role    Action Event             IP Address       |
| 05-Oct 13:22:01 UTC warden_v    WARDEN  ROOM_ALLOCATED (A-302)  192.168.1.45     |
| 05-Oct 13:10:14 UTC admin_sys   ADMIN   WARDEN_ASSIGN (Block B)  10.0.4.12        |
| 05-Oct 12:45:00 UTC STU-8841    STUDENT LOGIN_SUCCESS            172.16.8.99      |
+-----------------------------------------------------------------------------------+
```
