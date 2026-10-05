# Phase 2: Requirement Analysis

## Exercise 2: Develop Use Cases & UML Use Case Diagram

### 1. Actor Identification
1. **Student**: Regular campus student seeking or managing hostel accommodation.
2. **Warden**: Hostel block supervisor responsible for processing allocations and handling complaints.
3. **Administrator (Admin)**: System administrator responsible for infrastructure, configuration, and security audits.
4. **Authentication System (External)**: Campus SSO / Identity Provider (IdP) service.

---

### 2. Major Use Cases & Relationships

| Use Case ID | Use Case Title | Primary Actor | Included Use Cases (`<<include>>`) | Extended Use Cases (`<<extend>>`) |
| :--- | :--- | :--- | :--- | :--- |
| **UC-01** | Apply for Hostel Room | Student | Login (UC-00), Check Room Availability | Request Roommate Swap (`<<extend>>`) |
| **UC-02** | View Room Availability | Student, Warden | Login (UC-00) | Filter by Amenities / Block |
| **UC-03** | Allocate Hostel Room | Warden | Login (UC-00), Verify Student Details | Manual Allocation Override (`<<extend>>`) |
| **UC-04** | Manage Student Complaints | Student, Warden | Login (UC-00) | Escalate to Admin (`<<extend>>`) |
| **UC-05** | Manage Hostel Information | Admin | Login (UC-00) | Bulk Capacity Import (`<<extend>>`) |
| **UC-06** | View Accommodation Details | Student | Login (UC-00) | Download Allotment Letter (`<<extend>>`) |
| **UC-07** | Review Security Audit Logs | Admin | Login (UC-00) | Export Audit Log PDF (`<<extend>>`) |

---

### 3. UML Use Case Diagram (Mermaid Syntax)

```mermaid
graph TD
    %% Actors
    Student((Student))
    Warden((Hostel Warden))
    Admin((System Admin))
    SSO((Campus SSO IdP))

    %% Use Cases
    UC00[UC-00: Authenticate via SSO]
    UC01[UC-01: Apply for Hostel Room]
    UC02[UC-02: View Room Availability]
    UC03[UC-03: Allocate Hostel Room]
    UC04[UC-04: Submit / Resolve Complaints]
    UC05[UC-05: Manage Hostel Buildings & Rooms]
    UC06[UC-06: View Accommodation & Fee Details]
    UC07[UC-07: Audit Security & Allocation Logs]
    UC08[UC-08: Request Room Swap]

    %% Connections - Student
    Student --> UC00
    Student --> UC01
    Student --> UC02
    Student --> UC06
    Student --> UC04

    %% Connections - Warden
    Warden --> UC00
    Warden --> UC02
    Warden --> UC03
    Warden --> UC04

    %% Connections - Admin
    Admin --> UC00
    Admin --> UC05
    Admin --> UC07

    %% External System
    UC00 -.-> SSO

    %% Include Relationships
    UC01 -.->|include| UC00
    UC01 -.->|include| UC02
    UC03 -.->|include| UC00
    UC04 -.->|include| UC00
    UC05 -.->|include| UC00
    UC06 -.->|include| UC00

    %% Extend Relationships
    UC08 -.->|extend| UC01
```

---

## Exercise 3: Detailed Use Case Specifications

### Use Case Specification 1: UC-01 - Apply for Hostel Room & Allocation

| Section | Description |
| :--- | :--- |
| **Use Case ID & Name** | **UC-01: Apply for Hostel Room & Allocation** |
| **Primary Actor** | Student |
| **Secondary Actor(s)** | Warden, System Database, Notification Service |
| **Description** | Student selects hostel preferences, submits an application for a hostel room, and the system/warden processes allocation based on availability and merit. |
| **Preconditions** | 1. Student must be registered in the university database.<br>2. Student must be authenticated via SSO.<br>3. Room application window must be active. |
| **Postconditions** | 1. Application record is stored with status `PENDING` or `ALLOCATED`.<br>2. Room bed count is reserved atomically.<br>3. Notification email is dispatched to the student and warden. |
| **Main Success Flow (Basic Flow)** | 1. Student navigates to the Hostel Application portal.<br>2. System displays available Hostel Blocks, Room Types, and live vacant bed counts.<br>3. Student selects preferred block, room type, and submits student credentials/academic details.<br>4. System validates eligibility (no outstanding dues, valid active student status).<br>5. System generates a unique Application Reference ID and sets status to `PENDING`.<br>6. Warden reviews application in Warden Portal.<br>7. Warden clicks `Approve & Allocate Room`.<br>8. System assigns Block, Room, and Bed ID, locks the bed record, and updates status to `ALLOCATED`.<br>9. System sends SMS/Email notification with Allotment Summary to the student. |
| **Alternative Flow(s)** | **ALT-1: Preferred Room Full**: If student's top preference is full, system highlights available alternate blocks and permits student to update selection before submission.<br>**ALT-2: Automated Auto-Allocation**: If auto-allocation rule is enabled by Admin, system immediately processes merit rank and allocates room without manual Warden click. |
| **Exception Flow(s)** | **EX-1: Double Allocation Race Condition**: If two students select the last vacant bed simultaneously, database row lock enforces atomic check; second transaction fails with error *"Room bed no longer available, please refresh."*<br>**EX-2: Disciplinary Hold**: If university database flags student with a disciplinary hold, application is blocked with message *"Application denied due to active administrative hold."* |

---

### Use Case Specification 2: UC-04 - Submit and Resolve Maintenance Complaints

| Section | Description |
| :--- | :--- |
| **Use Case ID & Name** | **UC-04: Submit and Resolve Maintenance Complaints** |
| **Primary Actor** | Student |
| **Secondary Actor(s)** | Warden, Maintenance Staff |
| **Description** | Allocated student submits a facility grievance (plumbing, electrical, furniture), warden reviews and assigns maintenance staff, and updates complaint status to resolution. |
| **Preconditions** | 1. Student must have an active allocated room.<br>2. Student must be authenticated. |
| **Postconditions** | 1. Complaint ticket is logged in `ComplaintStore`.<br>2. Maintenance job assigned to staff.<br>3. Ticket status updated to `RESOLVED` with resolution timestamp. |
| **Main Success Flow (Basic Flow)** | 1. Student accesses Complaint Portal and clicks `Lodge New Complaint`.<br>2. Student selects category (Electrical / Plumbing / Furniture / Security), enters description, room number, and optional photo evidence.<br>3. System registers ticket ID, sets status to `SUBMITTED`, and notifies Block Warden.<br>4. Warden opens Warden Complaints Dashboard, views pending tickets.<br>5. Warden assigns maintenance staff and updates status to `IN_PROGRESS`.<br>6. Maintenance staff rectifies physical issue.<br>7. Warden marks ticket as `RESOLVED` with remarks.<br>8. System requests student satisfaction feedback rating. |
| **Alternative Flow(s)** | **ALT-1: Student Re-opens Ticket**: If issue is unresolved, student clicks `Re-open Ticket` within 48 hours, reverting status to `REOPENED` with escalation flag. |
| **Exception Flow(s)** | **EX-1: Invalid Room Details**: If student attempts to submit complaint for a room not assigned to them, system rejects submission with IDOR error. |
