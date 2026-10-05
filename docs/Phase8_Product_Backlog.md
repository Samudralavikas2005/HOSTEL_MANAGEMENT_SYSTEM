# Phase 8: Product Backlog

## Exercise 12: Create Product Backlog

---

### Product Backlog Matrix (Minimum 8 User Stories)

| Story ID | Epic | User Story | Priority | Story Points | Derived Requirement / Use Case |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **US-01** | User Auth & Security | **As a** Student / Warden / Admin,<br>**I want to** authenticate via Single Sign-On (SSO) with Multi-Factor Authentication (MFA),<br>**so that** my account and student data are protected from unauthorized access. | **MUST HAVE** | **5** | FR-01, SEC-01, UC-00 |
| **US-02** | Room Availability | **As a** Student,<br>**I want to** view real-time vacant room counts categorized by hostel block and room type,<br>**so that** I can make an informed choice during room application. | **MUST HAVE** | **3** | FR-02, UC-02 |
| **US-03** | Room Application | **As a** Student,<br>**I want to** submit an online hostel room application with my roommate preferences,<br>**so that** I can secure accommodation for the upcoming academic semester. | **MUST HAVE** | **5** | FR-03, UC-01 |
| **US-04** | Room Allocation | **As a** Warden,<br>**I want to** review pending student applications and execute atomic room allocations,<br>**so that** beds are assigned fairly and double-booking is prevented. | **MUST HAVE** | **8** | FR-04, SEC-06, UC-03 |
| **US-05** | Accommodation View | **As a** Student,<br>**I want to** check my allocated room details, bed number, and download my allotment letter,<br>**so that** I have official proof of residence. | **MUST HAVE** | **3** | FR-05, UC-06 |
| **US-06** | Grievance & Complaints | **As a** Student,<br>**I want to** lodge maintenance complaints (electrical, plumbing) with photo attachments,<br>**so that** hostel issues are resolved quickly by maintenance staff. | **SHOULD HAVE** | **5** | FR-06, UC-04 |
| **US-07** | Complaint Resolution | **As a** Warden,<br>**I want to** assign complaints to maintenance staff and update ticket resolution status,<br>**so that** student grievances are tracked and closed efficiently. | **SHOULD HAVE** | **5** | FR-06, UC-04 |
| **US-08** | Infrastructure Admin | **As an** Administrator,<br>**I want to** configure hostel buildings, set room capacities, and assign block wardens,<br>**so that** hostel infrastructure data remains accurate. | **MUST HAVE** | **5** | FR-07, FR-08, UC-05 |
| **US-09** | Security & Audit | **As an** Administrator / Auditor,<br>**I want to** view append-only security logs for all room allocations and administrative overrides,<br>**so that** system security and non-repudiation are maintained. | **MUST HAVE** | **8** | SEC-04, UC-07 |
| **US-10** | Notifications | **As a** Student,<br>**I want to** receive SMS and email notifications upon application status updates or complaint resolution,<br>**so that** I remain informed in real time. | **COULD HAVE** | **3** | FR-09 |
