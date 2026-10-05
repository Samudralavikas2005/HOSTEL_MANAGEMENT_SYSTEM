# Phase 1: Requirement Engineering
## Software Requirements Specification (SRS) - Student Hostel Management System

---

### 1. Introduction & System Objectives
The **Student Hostel Management System (SHMS)** is an integrated web-based platform designed to automate and streamline hostel administrative operations, room applications, room allocation, fee updates, and grievance management across university residential campuses.

#### 1.1 Objectives
* **Automation**: Eliminate manual paper-based room applications and manual room allotment spreadsheets.
* **Transparency & Real-time Visibility**: Provide students with live updates on hostel room availability, allocation status, and fee breakdown.
* **Role-Based Control**: Enable Wardens to efficiently allocate rooms based on merit/reservation criteria, process room swap requests, and manage complaints.
* **Centralized Administration**: Allow Administrators to manage hostel buildings, room quotas, capacity parameters, and warden assignments.
* **Information Security & Anti-Fraud**: Protect sensitive student Personally Identifiable Information (PII) and safeguard against unauthorized room allocations, privilege escalation, or record tampering.

---

### 2. Stakeholders & User Types

| Stakeholder / User Type | Description & Primary Responsibilities | Access Level |
| :--- | :--- | :--- |
| **Student** | Enrolled university students applying for hostel accommodation, viewing room availability, checking allotment status, submitting maintenance complaints, and viewing fee receipts. | User Level (Restricted to own profile & data) |
| **Warden** | Residential faculty/officers responsible for evaluating student applications, allocating rooms, overseeing hostel block maintenance, and resolving student complaints. | Operational Level (Hostel Block scope) |
| **Administrator (Admin)** | Central IT/Hostel management admins who configure hostels, set room capacities, assign wardens, manage global parameters, and review system logs. | Administrative Level (Global System scope) |
| **System Security Auditor** | Internal/External security reviewers who monitor access logs, audit unauthorized access attempts, and review compliance reports. | Read-Only Audit Level |
| **Maintenance Staff** | Support personnel assigned by wardens to fix reported electrical, plumbing, or structural issues. | Task-Specific Operational Level |

---

### 3. Functional Requirements (FR)

* **FR-01: User Authentication & Role-Based Access Control (RBAC)**
  * The system must authenticate users via Multi-Factor Authentication (MFA) / Single Sign-On (SSO).
  * The system must enforce strict RBAC policies distinguishing Students, Wardens, Admins, and Auditors.

* **FR-02: Room Availability Dashboard**
  * The system shall display real-time hostel room availability categorized by Hostel Block, Gender Quota, Room Type (Single/Double/Triple), and Amenities.

* **FR-03: Student Room Application**
  * Students must be able to fill out an online room application form specifying preferences (Hostel, Room Type, Roommate preference) and uploading necessary verification documents.

* **FR-04: Automated & Manual Room Allocation**
  * Wardens must be able to evaluate pending applications, execute automated merit/lottery allocation rules, or manually assign rooms with mandatory log reasons.

* **FR-05: Accommodation & Fee Status View**
  * Allocated students must be able to view their assigned Hostel Block, Room Number, Bed ID, Allotment Letter, and payment receipt status.

* **FR-06: Complaint Management & Grievance Tracking**
  * Students must be able to lodge complaints under categories (Plumbing, Electrical, Cleanliness, Security) and track status (Open, In Progress, Resolved).
  * Wardens must be able to assign complaints to maintenance staff, update status, and close complaints.

* **FR-07: Hostel & Block Administration**
  * Administrators must be able to create, modify, or decommission Hostel Blocks, set room capacity limits, fee rates, and maintain block configurations.

* **FR-08: User & Warden Management**
  * Administrators shall add/deactivate Warden accounts, assign wardens to specific blocks, and audit user activity.

* **FR-09: Notifications & Alert Service**
  * The system must send automated email/SMS alerts to students upon application approval, room allocation, complaint status change, or fee due dates.

---

### 4. Non-Functional Requirements (NFR)

* **NFR-01: Performance & Response Time**
  * The system must load user dashboards within 1.5 seconds under normal load and maintain a response time under 3 seconds during peak registration periods (up to 5,000 concurrent users).

* **NFR-02: Scalability**
  * The system architecture must scale horizontally using microservices / containerized deployments to handle campus-wide spikes during admission season.

* **NFR-03: Availability & Reliability**
  * The system shall guarantee 99.9% uptime during active academic semesters, supported by automated failover databases and redundant load balancers.

* **NFR-04: Usability & Accessibility**
  * The interface must strictly adhere to WCAG 2.1 AA accessibility guidelines, offering responsive web layout across desktops, tablets, and mobile devices.

* **NFR-05: Data Integrity & Consistency**
  * Database transactions involving room allocations must adhere to ACID (Atomicity, Consistency, Isolation, Durability) properties to prevent double-booking of beds.

---

### 5. Security Requirements (SEC)

* **SEC-01: Authentication & Session Management**
  * Cryptographically secure tokens (JWT / OAuth2 with short lifetime and refresh tokens) must be used for session handling. Sessions automatically expire after 15 minutes of inactivity.

* **SEC-02: Sensitive Data Protection & Encryption**
  * All student PII (Phone, Home Address, Guardian details) and credentials must be encrypted at rest using AES-256 and encrypted in transit using TLS 1.3.

* **SEC-03: Authorization & Prevention of Direct Object References (IDOR)**
  * The API backend must enforce object-level authorization on every request (e.g., verifying that Student A cannot access Student B's accommodation record via URL parameter tampering).

* **SEC-04: Audit Logging & Non-Repudiation**
  * All room allocation actions, privilege changes, and admin overrides must be logged to an append-only, tamper-evident audit log including timestamp, IP address, User ID, and old/new state values.

* **SEC-05: Input Validation & Anti-Exploitation**
  * All incoming input parameters must undergo strict server-side validation and sanitization to protect against SQL Injection (SQLi), Cross-Site Scripting (XSS), and Cross-Site Request Forgery (CSRF).

* **SEC-06: Anti-Tampering & Over-Allocation Prevention**
  * The application logic must perform atomic database level row-locking during room allocation to prevent race conditions and illegal over-allocation by unauthorized parties.
