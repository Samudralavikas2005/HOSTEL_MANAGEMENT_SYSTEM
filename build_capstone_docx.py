import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
import os

def set_cell_background(cell, fill_hex):
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def add_callout_box(doc, title, text):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    cell = table.cell(0, 0)
    set_cell_background(cell, "F2F4F7")
    set_cell_margins(cell, top=140, bottom=140, left=200, right=200)
    
    tcPr = cell._element.get_or_add_tcPr()
    borders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:left w:val="single" w:sz="36" w:space="0" w:color="1F4E78"/><w:top w:val="none"/><w:right w:val="none"/><w:bottom w:val="none"/></w:tcBorders>')
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(4)
    run_t = p.add_run(f"ENGINEERING PRINCIPLE: {title}\n")
    run_t.bold = True
    run_t.font.name = 'Arial'
    run_t.font.size = Pt(10)
    run_t.font.color.rgb = RGBColor(0x1F, 0x4E, 0x78)
    
    run_b = p.add_run(text)
    run_b.font.name = 'Arial'
    run_b.font.size = Pt(9.5)
    run_b.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
    
    doc.add_paragraph().paragraph_format.space_after = Pt(6)

def style_table_header(row, col_widths, bg_hex="1F4E78"):
    for idx, cell in enumerate(row.cells):
        set_cell_background(cell, bg_hex)
        set_cell_margins(cell, top=120, bottom=120, left=150, right=150)
        cell.width = col_widths[idx]
        for p in cell.paragraphs:
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            for r in p.runs:
                r.font.name = 'Arial'
                r.font.size = Pt(9.5)
                r.font.bold = True
                r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

def style_table_rows(table, col_widths, alt_shading=True):
    for r_idx, row in enumerate(table.rows[1:]):
        bg = "F9FAFB" if (r_idx % 2 == 1 and alt_shading) else "FFFFFF"
        for c_idx, cell in enumerate(row.cells):
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=100, bottom=100, left=150, right=150)
            cell.width = col_widths[c_idx]
            for p in cell.paragraphs:
                for r in p.runs:
                    r.font.name = 'Arial'
                    r.font.size = Pt(9)
                    r.font.color.rgb = RGBColor(0x22, 0x22, 0x22)

doc = docx.Document()

# Page setup
for section in doc.sections:
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.0)
    section.right_margin = Inches(1.0)

# Title Page Header
p_title = doc.add_paragraph()
p_title.paragraph_format.space_before = Pt(36)
p_title.paragraph_format.space_after = Pt(6)
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
r_t = p_title.add_run("Secure Software Engineering Capstone Report\n")
r_t.bold = True
r_t.font.name = 'Arial'
r_t.font.size = Pt(24)
r_t.font.color.rgb = RGBColor(0x1F, 0x4E, 0x78)

r_sub = p_title.add_run("Student Hostel Management System (SHMS)\n")
r_sub.bold = True
r_sub.font.name = 'Arial'
r_sub.font.size = Pt(16)
r_sub.font.color.rgb = RGBColor(0x2F, 0x55, 0x97)

r_desc = p_title.add_run("Automated Residential Allotment & Security System — A Secure Software Engineering Case Study\n")
r_desc.italic = True
r_desc.font.name = 'Arial'
r_desc.font.size = Pt(11)
r_desc.font.color.rgb = RGBColor(0x55, 0x55, 0x55)

doc.add_paragraph().paragraph_format.space_after = Pt(18)

# Document Control Table
doc_ctrl = doc.add_table(rows=6, cols=2)
doc_ctrl.alignment = WD_TABLE_ALIGNMENT.CENTER
ctrl_widths = [Inches(2.2), Inches(4.3)]

ctrl_data = [
    ("Document Control", "Details"),
    ("Project Title", "Student Hostel Management System (SHMS) Capstone"),
    ("Problem Statement", "Problem 13: Student Hostel Management System"),
    ("Author / Candidate", "Vikas Samudrala (Reg ID: SSE_LAB_MIDS)"),
    ("Course / Scope", "Secure Software Engineering (SSE) — Capstone Report"),
    ("Date & Version", "October 2026 • Version 2.4 Final")
]

for r_idx, (k, v) in enumerate(ctrl_data):
    row = doc_ctrl.rows[r_idx]
    c0, c1 = row.cells[0], row.cells[1]
    c0.width, c1.width = ctrl_widths[0], ctrl_widths[1]
    set_cell_margins(c0, 80, 80, 120, 120)
    set_cell_margins(c1, 80, 80, 120, 120)
    
    if r_idx == 0:
        set_cell_background(c0, "1F4E78")
        set_cell_background(c1, "1F4E78")
        p0 = c0.paragraphs[0].add_run(k)
        p1 = c1.paragraphs[0].add_run(v)
        p0.bold = p1.bold = True
        p0.font.color.rgb = p1.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    else:
        set_cell_background(c0, "F2F4F7")
        set_cell_background(c1, "FFFFFF")
        p0 = c0.paragraphs[0].add_run(k)
        p1 = c1.paragraphs[0].add_run(v)
        p0.bold = True
        p0.font.color.rgb = RGBColor(0x1F, 0x4E, 0x78)
        p1.font.color.rgb = RGBColor(0x33, 0x33, 0x33)

doc.add_page_break()

# Function to add heading
def add_sec_heading(doc, text, level=1):
    h = doc.add_paragraph()
    h.paragraph_format.keep_with_next = True
    r = h.add_run(text)
    r.bold = True
    r.font.name = 'Arial'
    if level == 1:
        h.paragraph_format.space_before = Pt(18)
        h.paragraph_format.space_after = Pt(8)
        r.font.size = Pt(16)
        r.font.color.rgb = RGBColor(0x1F, 0x4E, 0x78)
    elif level == 2:
        h.paragraph_format.space_before = Pt(14)
        h.paragraph_format.space_after = Pt(6)
        r.font.size = Pt(13)
        r.font.color.rgb = RGBColor(0x2F, 0x55, 0x97)
    elif level == 3:
        h.paragraph_format.space_before = Pt(10)
        h.paragraph_format.space_after = Pt(4)
        r.font.size = Pt(11)
        r.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
    return h

def add_body_p(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.line_spacing = 1.15
    r = p.add_run(text)
    r.font.name = 'Arial'
    r.font.size = Pt(10)
    r.font.color.rgb = RGBColor(0x22, 0x22, 0x22)
    return p

# SECTION 1: Introduction
add_sec_heading(doc, "1. Introduction", level=1)

add_sec_heading(doc, "1.1 Background and Motivation", level=2)
add_body_p(doc, "University hostel accommodations represent critical campus infrastructure requiring transparent, equitable, and secure administrative workflows. Traditional manual spreadsheet-based room allotment systems suffer from data redundancy, vulnerability to unauthorized room overrides, lack of real-time vacancy visibility, and audit trail gaps. The Student Hostel Management System (SHMS) automates residential operations while enforcing stringent secure software engineering practices.")

add_sec_heading(doc, "1.2 Purpose and Scope", level=2)
add_body_p(doc, "This capstone report documents the complete 9-Phase Software Engineering and Security lifecycle of SHMS. The scope encompasses requirements engineering, use case modeling, ER data modeling, Level 1 DFD with trust boundaries, CIA triad asset analysis, STRIDE threat modeling, attack tree decomposition, golden-rule UI wireframes, product backlog management, and Jira Scrum sprint execution metrics.")

add_callout_box(doc, "Security Architecture First", "Security is designed directly into the architectural model rather than added during post-development testing. Authentication, role-based access control (RBAC), database pessimistic row locks, tamper-evident HMAC audit logging, and input sanitization are enforced across all application boundaries.")

# SECTION 2: Requirement Engineering
add_sec_heading(doc, "2. Requirement Engineering", level=1)

add_sec_heading(doc, "2.1 Problem Statement", level=2)
add_body_p(doc, "Problem 13: Develop a hostel management system where students can apply for rooms, view room availability, and check their accommodation details. Wardens can allocate rooms and manage complaints. Administrators can manage hostel information. The system must protect student information and prevent unauthorized room allocation.")

add_sec_heading(doc, "2.2 Functional Requirements", level=2)
fr_widths = [Inches(1.2), Inches(2.3), Inches(3.0)]
t_fr = doc.add_table(rows=6, cols=3)
t_fr.alignment = WD_TABLE_ALIGNMENT.CENTER
t_fr.rows[0].cells[0].paragraphs[0].add_run("Req ID")
t_fr.rows[0].cells[1].paragraphs[0].add_run("Requirement Name")
t_fr.rows[0].cells[2].paragraphs[0].add_run("Detailed Functional Specification")

fr_data = [
    ("FR-01", "SSO & MFA Auth", "Authenticate users via Single Sign-On and enforce TOTP Multi-Factor Authentication."),
    ("FR-02", "Vacancy Dashboard", "Display real-time vacant room counts categorized by block, gender quota, and amenities."),
    ("FR-03", "Room Application", "Allow students to select preferences, roommate preferences, and submit online applications."),
    ("FR-04", "Warden Allotment", "Enable wardens to evaluate applications and execute atomic room allocations with row-level locks."),
    ("FR-05", "Grievance Engine", "Allow students to submit maintenance tickets and enable wardens to resolve grievances.")
]
for idx, (rid, rname, rdesc) in enumerate(fr_data):
    row = t_fr.rows[idx+1]
    row.cells[0].paragraphs[0].add_run(rid)
    row.cells[1].paragraphs[0].add_run(rname)
    row.cells[2].paragraphs[0].add_run(rdesc)

style_table_header(t_fr.rows[0], fr_widths)
style_table_rows(t_fr, fr_widths)
doc.add_paragraph().paragraph_format.space_after = Pt(6)

add_sec_heading(doc, "2.3 Security Requirements", level=2)
sec_widths = [Inches(1.2), Inches(2.0), Inches(3.3)]
t_sec = doc.add_table(rows=5, cols=3)
t_sec.alignment = WD_TABLE_ALIGNMENT.CENTER
t_sec.rows[0].cells[0].paragraphs[0].add_run("SEC ID")
t_sec.rows[0].cells[1].paragraphs[0].add_run("Security Control")
t_sec.rows[0].cells[2].paragraphs[0].add_run("Implementation & Defense Mechanism")

sec_data = [
    ("SEC-01", "Session Tokens", "Short-lived JWT bearer tokens with refresh token rotation and 15-min idle timeout."),
    ("SEC-02", "PII Protection", "AES-256 encryption at rest for student personal details and TLS 1.3 in transit."),
    ("SEC-03", "Anti-IDOR Control", "Server-side Object-Level Authorization verifying student ownership of requested resources."),
    ("SEC-04", "Audit Trails", "Append-only HMAC-SHA256 checksum logs for all room allocations and admin actions.")
]
for idx, (sid, sctrl, sdesc) in enumerate(sec_data):
    row = t_sec.rows[idx+1]
    row.cells[0].paragraphs[0].add_run(sid)
    row.cells[1].paragraphs[0].add_run(sctrl)
    row.cells[2].paragraphs[0].add_run(sdesc)

style_table_header(t_sec.rows[0], sec_widths)
style_table_rows(t_sec, sec_widths)
doc.add_paragraph().paragraph_format.space_after = Pt(6)

# SECTION 3: Requirement Analysis
add_sec_heading(doc, "3. Requirement Analysis", level=1)
add_sec_heading(doc, "3.1 Actor & Use Case Model", level=2)
add_body_p(doc, "The system defines three primary human actors (Student, Warden, System Admin) and one external system actor (Campus SSO Identity Provider). Figure 3.1 illustrates the Use Case model and include/extend relationships.")

if os.path.exists('/home/vikas/SSE_LAB_MIDS/use_case_diagram.png'):
    doc.add_picture('/home/vikas/SSE_LAB_MIDS/use_case_diagram.png', width=Inches(6.2))
    p_img = doc.paragraphs[-1]
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_after = Pt(12)

# SECTION 4: Data Modeling
add_sec_heading(doc, "4. Data Modeling", level=1)
add_sec_heading(doc, "4.1 ER Diagram & Relational Schema", level=2)
add_body_p(doc, "The relational schema models eight core entities ensuring strict normal form compliance (3NF) and ACID transactional integrity. Figure 4.1 outlines the Entity-Relationship Diagram.")

if os.path.exists('/home/vikas/SSE_LAB_MIDS/er_diagram.png'):
    doc.add_picture('/home/vikas/SSE_LAB_MIDS/er_diagram.png', width=Inches(6.2))
    p_img = doc.paragraphs[-1]
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_after = Pt(12)

# SECTION 5: Data Flow Modeling
add_sec_heading(doc, "5. Data Flow Modeling", level=1)
add_sec_heading(doc, "5.1 Level 1 DFD and Trust Boundaries", level=2)
add_body_p(doc, "Figure 5.1 depicts the Level 1 Data Flow Diagram highlighting four explicit Trust Boundaries (TB1 to TB4) protecting application processes and backend data stores.")

if os.path.exists('/home/vikas/SSE_LAB_MIDS/dfd_diagram.png'):
    doc.add_picture('/home/vikas/SSE_LAB_MIDS/dfd_diagram.png', width=Inches(6.2))
    p_img = doc.paragraphs[-1]
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_after = Pt(12)

# SECTION 6: Threat Modeling
add_sec_heading(doc, "6. Threat Modeling & Vulnerability Analysis", level=1)
add_sec_heading(doc, "6.1 STRIDE Threat Analysis Matrix", level=2)

stride_widths = [Inches(1.0), Inches(1.5), Inches(2.2), Inches(1.8)]
t_stride = doc.add_table(rows=7, cols=4)
t_stride.alignment = WD_TABLE_ALIGNMENT.CENTER
t_stride.rows[0].cells[0].paragraphs[0].add_run("Threat ID")
t_stride.rows[0].cells[1].paragraphs[0].add_run("STRIDE Category")
t_stride.rows[0].cells[2].paragraphs[0].add_run("Threat Description")
t_stride.rows[0].cells[3].paragraphs[0].add_run("Mitigation Control")

stride_data = [
    ("TRT-01", "SPOOFING", "Student Account Impersonation via weak auth", "OAuth2 SSO + TOTP MFA"),
    ("TRT-02", "TAMPERING", "Direct DB update of room allocations", "DB Row Locks + RBAC"),
    ("TRT-03", "REPUDIATION", "Warden denial of illegal room allotment", "HMAC SHA-256 Audit Trail"),
    ("TRT-04", "INFO DISCLOSURE", "Interception of student PII in transit", "TLS 1.3 + AES-256 at Rest"),
    ("TRT-05", "DENIAL OF SERVICE", "HTTP API registration flood attack", "WAF Rate Limiting"),
    ("TRT-06", "ELEVATION OF PRIV", "IDOR vulnerability on grievance tickets", "Object-Level Authorization")
]
for idx, (tid, tcat, tdesc, tmit) in enumerate(stride_data):
    row = t_stride.rows[idx+1]
    row.cells[0].paragraphs[0].add_run(tid)
    row.cells[1].paragraphs[0].add_run(tcat)
    row.cells[2].paragraphs[0].add_run(tdesc)
    row.cells[3].paragraphs[0].add_run(tmit)

style_table_header(t_stride.rows[0], stride_widths)
style_table_rows(t_stride, stride_widths)
doc.add_paragraph().paragraph_format.space_after = Pt(6)

# SECTION 7: Attack Tree Analysis
add_sec_heading(doc, "7. Attack Tree Analysis", level=1)
add_sec_heading(doc, "7.1 Attacker Goal & Tree Decomposition", level=2)
add_body_p(doc, "Figure 7.1 details the Attack Tree for the root attacker goal: 'Unauthorized Room Allocation / Record Modification', mapping AND/OR condition paths.")

if os.path.exists('/home/vikas/SSE_LAB_MIDS/attack_tree.png'):
    doc.add_picture('/home/vikas/SSE_LAB_MIDS/attack_tree.png', width=Inches(6.2))
    p_img = doc.paragraphs[-1]
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_after = Pt(12)

# SECTION 8: User Interface Design
add_sec_heading(doc, "8. User Interface Design", level=1)
add_sec_heading(doc, "8.1 Wireframe Screens & Interactive Prototype", level=2)
add_body_p(doc, "Applying Shneiderman's 8 Golden Rules of UI Design, three major screens were designed and implemented in an interactive web application (app/index.html): Student Portal, Warden Dashboard, and System Admin Console.")

# SECTION 9: Product Backlog
add_sec_heading(doc, "9. Product Backlog", level=1)
add_sec_heading(doc, "9.1 User Stories & Story Point Estimation", level=2)

bl_widths = [Inches(0.9), Inches(1.2), Inches(3.2), Inches(1.2)]
t_bl = doc.add_table(rows=6, cols=4)
t_bl.alignment = WD_TABLE_ALIGNMENT.CENTER
t_bl.rows[0].cells[0].paragraphs[0].add_run("Story ID")
t_bl.rows[0].cells[1].paragraphs[0].add_run("Epic")
t_bl.rows[0].cells[2].paragraphs[0].add_run("User Story Summary")
t_bl.rows[0].cells[3].paragraphs[0].add_run("Story Points")

bl_data = [
    ("US-01", "Core Auth", "SSO Authentication & MFA Support", "5 Points"),
    ("US-02", "Room View", "Real-time Room Vacancy Dashboard", "3 Points"),
    ("US-03", "Room App", "Online Room Application Form", "5 Points"),
    ("US-04", "Allocation", "Warden Room Allocation Engine (Row Lock)", "8 Points"),
    ("US-09", "Security Log", "Append-only HMAC Security Audit Log", "8 Points")
]
for idx, (sid, sepic, ssum, spt) in enumerate(bl_data):
    row = t_bl.rows[idx+1]
    row.cells[0].paragraphs[0].add_run(sid)
    row.cells[1].paragraphs[0].add_run(sepic)
    row.cells[2].paragraphs[0].add_run(ssum)
    row.cells[3].paragraphs[0].add_run(spt)

style_table_header(t_bl.rows[0], bl_widths)
style_table_rows(t_bl, bl_widths)
doc.add_paragraph().paragraph_format.space_after = Pt(6)

# SECTION 10: Jira Project & Scrum Metrics
add_sec_heading(doc, "10. Jira Project & Scrum Execution", level=1)
add_sec_heading(doc, "10.1 Sprint Execution & Burndown Metrics", level=2)
add_body_p(doc, "The project was executed across two 2-week sprints achieving a velocity of 23.5 story points/sprint with 0 defects carried over. Figure 10.1 illustrates the Sprint 1 Burndown execution.")

if os.path.exists('/home/vikas/SSE_LAB_MIDS/burndown_chart.png'):
    doc.add_picture('/home/vikas/SSE_LAB_MIDS/burndown_chart.png', width=Inches(6.0))
    p_img = doc.paragraphs[-1]
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_after = Pt(12)

# Save files
path1 = '/home/vikas/SSE_LAB_MIDS/SkillSim_Hostel_Management_System_Capstone_Report.docx'
path2 = '/home/vikas/SSE_LAB_MIDS/Student_Hostel_Management_System_Lab_Report.docx'

doc.save(path1)
doc.save(path2)
print("Successfully generated Capstone Report docx files:")
print(" -", path1)
print(" -", path2)
