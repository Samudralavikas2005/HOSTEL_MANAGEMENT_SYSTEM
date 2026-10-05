# Phase 5: Threat Modeling

---

## Exercise 6: Asset Identification & CIA Triad Analysis

The Student Hostel Management System (SHMS) processes and manages several high-value information assets. Each asset is evaluated against the **Confidentiality, Integrity, and Availability (CIA)** triad.

### Asset & CIA Matrix

| Asset ID | Asset Name | Description & Data Elements | Confidentiality (C) | Integrity (I) | Availability (A) | CIA Priority & Rationale |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **AST-01** | Student Credentials & Session Tokens | Passwords, bcrypt hashes, MFA secrets, JWT tokens, session IDs. | **HIGH** | **HIGH** | **MEDIUM** | **Critical**: Compromise allows full identity impersonation. |
| **AST-02** | Student Personally Identifiable Info (PII) | Student Full Name, Phone, Email, Guardian info, Home address, Gender. | **HIGH** | **MEDIUM** | **LOW** | **High**: Exposure violates privacy regulations (GDPR/DPDP). |
| **AST-03** | Room Allocation & Occupancy Records | Active room assignments, bed IDs, warden authorization timestamps. | **MEDIUM** | **HIGH** | **HIGH** | **Critical**: Unauthorized modification causes double booking & fraud. |
| **AST-04** | Room Availability & Capacity State | Vacant bed counts per block, room status (maintenance vs active). | **LOW** | **HIGH** | **HIGH** | **High**: Denial of service blocks registration campus-wide. |
| **AST-05** | Student Grievances & Complaint Data | Maintenance issues, security complaints, photo evidence. | **HIGH** | **MEDIUM** | **MEDIUM** | **Medium**: Confidentiality vital for sensitive security grievances. |
| **AST-06** | Security Audit Logs | System logs, allocation overrides, login attempts, IP addresses. | **MEDIUM** | **HIGH** | **HIGH** | **Critical**: Essential for non-repudiation and forensic audit. |

---

## Exercise 7: STRIDE Threat Analysis

We apply the **STRIDE** methodology (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege) across DFD processes, data stores, and data flows.

### STRIDE Threat Table (Minimum 8 Threats)

| Threat ID | DFD Element Affected | Threat Description | STRIDE Category | Risk / Impact |
| :--- | :--- | :--- | :--- | :--- |
| **TRT-01** | P1.0 Authenticate Process | Attacker uses stolen student SSO credentials or weak password spraying to log in as a student. | **Spoofing** | **HIGH**: Impersonation of legitimate student. |
| **TRT-02** | DS4 Allocation Store | Malicious user or rogue internal user manipulates database records directly or via SQL injection to assign rooms without warden approval. | **Tampering** | **CRITICAL**: Unauthorized room allocation and records corruption. |
| **TRT-03** | P3.0 Allocation Process | Rogue Warden allocates room to a preferred student and subsequently deletes allocation logs to deny accountability. | **Repudiation** | **HIGH**: Lack of audit trail for illegal room grants. |
| **TRT-04** | Data Flow: P2.0 → EE_Student | Unencrypted or weakly encrypted HTTP data flow allows eavesdropper on Wi-Fi network to intercept student PII and session JWT tokens. | **Information Disclosure** | **HIGH**: Leakage of student personal data and tokens. |
| **TRT-05** | P2.0 Process Application | Attacker launches automated HTTP flood requests against the room application endpoint during registration start time. | **Denial of Service (DoS)** | **HIGH**: System collapse preventing genuine students from applying. |
| **TRT-06** | P4.0 Manage Complaints | A regular Student modifies the `student_id` in API payload to view and modify another student's private complaint details (IDOR). | **Elevation of Privilege** | **HIGH**: Unauthorized access to private student grievances. |
| **TRT-07** | DS6 Audit Log Store | Malicious administrator alters security audit logs to wipe traces of unauthorized room allocation overrides. | **Tampering / Repudiation** | **CRITICAL**: Destruction of forensic evidence. |
| **TRT-08** | P3.0 Allocation Process | Race condition exploit during room selection allows two concurrent HTTP requests to claim the same bed concurrently (Double Allocation). | **Tampering / DoS** | **HIGH**: Double booking and inconsistent system state. |
| **TRT-09** | Data Flow: P1.0 → DS1 | Attacker performs SQL injection on authentication input field to bypass password validation. | **Elevation of Privilege** | **CRITICAL**: Full admin system compromise. |

---

## Exercise 8: Information Flow Analysis

### Sensitive Data Flow Matrix

```
[Untrusted Client: Student Browser]
           │
           │ (1. Unauthenticated Login Credentials) [Untrusted Flow] ──► Trust Boundary 1 (WAF / TLS)
           ▼
[Process P1.0: Auth Service]
           │
           │ (2. Query Hash & User Details) [Trusted Flow] ────────────► Trust Boundary 3 (Database Firewall)
           ▼
[Data Store DS1: Student Credentials]
           │
           │ (3. JWT Bearer Token Issued) [Trusted Flow]
           ▼
[Process P2.0 / P3.0: Allocation Engine]
           │
           │ (4. Write Bed Allotment) [Sensitive Flow] ───────────────► Trust Boundary 3
           ▼
[Data Store DS4: Allocation Registry] & [Data Store DS6: Audit Log]
```

### Flow Analysis Table

| Flow ID | Source Element | Target Process / Store | Destination Element | Sensitive Information Carried | Trust Boundary Crossed | Trusted vs Untrusted | Potential Unauthorized Flow Risk |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **FLW-01** | Student Browser | P1.0 Auth Process | DS1 Student Store | Student ID, Password, MFA Code | TB1 (Client/Server) | Untrusted → Trusted | Credential interception via MITM if TLS missing. |
| **FLW-02** | Warden Portal | P3.0 Allocation | DS4 Allocation Store | Student ID, Room ID, Bed ID, Warden Signature | TB1 & TB3 | Untrusted → High Trust | Unauthorized room grant if RBAC missing on API endpoint. |
| **FLW-03** | P4.0 Complaint Engine | DS5 Complaint Store | Student Browser | Grievance notes, room number, personal details | TB1 & TB2 | High Trust → Untrusted | IDOR vulnerability leaking other students' grievances. |
| **FLW-04** | P5.0 Admin Console | DS6 Audit Log Store | System Admin | Audit log entries, IP addresses, system events | TB3 | Internal High Trust | Log wiping by malicious administrator. |

---

## Exercise 9: Vulnerability Analysis

### Vulnerability Analysis Table (6 Critical Vulnerabilities)

| Vuln ID | Affected DFD Element | Related STRIDE Threat | Identified Vulnerability Description | Potential Business Impact | Mitigation & Security Control |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **VUL-01** | P1.0 Auth Process | TRT-01 (Spoofing) | Weak password policy & missing mandatory Multi-Factor Authentication (MFA). | Credential stuffing and account takeover of student/warden accounts. | Enforce Argon2id / Bcrypt password hashing, rate limiting, and mandatory TOTP MFA. |
| **VUL-02** | P4.0 Complaint Process | TRT-06 (Elevation of Privilege) | Insecure Direct Object Reference (IDOR) on `/api/complaints/{id}` endpoint. | Students read or modify complaints filed by other students. | Implement server-side Object-Level Authorization (verify `token.student_id == complaint.student_id`). |
| **VUL-03** | P3.0 Allocation Process | TRT-08 (Tampering) | Absence of database row-level locking during simultaneous room booking requests. | Double booking of hostel beds, leading to student disputes and manual overhead. | Implement database pessimistic locking (`SELECT ... FOR UPDATE`) or serializable isolation level. |
| **VUL-04** | P1.0 & P2.0 Input APIs | TRT-09 (Elevation of Privilege) | Unsanitized SQL input parameters in search/filter endpoints. | Attacker executes arbitrary SQL commands, dumping or wiping data stores. | Use parameterized queries (Prepared Statements) or ORM parameter binding exclusively. |
| **VUL-05** | DS6 Audit Log Store | TRT-07 (Repudiation) | Plaintext database logging without cryptographic integrity checks. | Internal bad actor alters room allocation audit logs without detection. | Implement append-only logs with HMAC-SHA256 hash chains stored in a write-once repository. |
| **VUL-06** | Data Flow TB1 | TRT-04 (Info Disclosure) | Missing HTTP Security Headers (HSTS, Content-Security-Policy, SameSite cookies). | Session hijacking via Cross-Site Scripting (XSS) and Man-In-The-Middle attack. | Enforce Strict HTTPS (TLS 1.3), `HttpOnly`, `Secure`, `SameSite=Strict` cookie flags, and robust CSP. |
