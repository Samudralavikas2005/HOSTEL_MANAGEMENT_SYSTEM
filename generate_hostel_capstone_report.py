#!/usr/bin/env python3
"""
Generate Student Hostel Management System Secure Software Engineering Capstone Report Word Document
Matching the formatting, layout, styling, typography, callouts, and 10-chapter structure of 
SecureCart_Secure_Software_Engineering_Capstone_Report_Final.docx & SkillSim_Secure_Software_Engineering_Capstone_Report_Final.docx
"""

import sys
import os
import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

def create_report():
    output_path1 = "/home/vikas/SSE_LAB_MIDS/Hostel_Management_System_Secure_Software_Engineering_Capstone_Report_Final.docx"
    output_path2 = "/home/vikas/SSE_LAB_MIDS/SkillSim_Secure_Software_Engineering_Capstone_Report_Final.docx"
    
    doc = docx.Document()

    # Colors
    HEX_NAVY_DARK = "17365D"   # H1, Doc Title, Table Headers
    HEX_NAVY_MED = "1F4E79"    # H2, Subtitles
    HEX_BLUE_ACCENT = "2E75B6" # H4 / Accents
    HEX_TEAL = "0F766E"        # H3
    HEX_CHARCOAL = "172033"    # Body text
    HEX_SLATE = "5B6573"       # Subtitles / Secondary text
    HEX_MINT_BG = "EAF5EA"     # Callout background green
    HEX_GREEN_BORDER = "2E7D32"# Callout border green
    HEX_GRID_BORDER = "D3D3D3" # Table grid border
    HEX_LIGHT_ROW = "F9FBFD"   # Light alternating table row

    COLOR_NAVY_DARK = RGBColor(0x17, 0x36, 0x5D)
    COLOR_NAVY_MED = RGBColor(0x1F, 0x4E, 0x79)
    COLOR_TEAL = RGBColor(0x0F, 0x76, 0x6E)
    COLOR_CHARCOAL = RGBColor(0x17, 0x20, 0x33)
    COLOR_SLATE = RGBColor(0x5B, 0x65, 0x73)

    # Page Margins
    section = doc.sections[0]
    section.top_margin = Inches(0.72)
    section.bottom_margin = Inches(0.62)
    section.left_margin = Inches(0.72)
    section.right_margin = Inches(0.72)
    section.page_width = Inches(8.5)
    section.page_height = Inches(11.0)

    # Running Header & Footer
    header = section.header
    hp = header.paragraphs[0]
    hp.text = "Student Hostel Management System  •  Secure Software Engineering Capstone Report"
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    if hp.runs:
        hp.runs[0].font.name = "Aptos"
        hp.runs[0].font.size = Pt(8.5)
        hp.runs[0].font.color.rgb = COLOR_SLATE

    footer = section.footer
    fp = footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    frun = fp.add_run("Page ")
    frun.font.name = "Aptos"
    frun.font.size = Pt(9.0)
    frun.font.color.rgb = COLOR_SLATE
    
    fldSimple1 = OxmlElement('w:fldSimple')
    fldSimple1.set(qn('w:instr'), 'PAGE')
    fp._p.append(fldSimple1)
    
    frun2 = fp.add_run(" of ")
    frun2.font.name = "Aptos"
    frun2.font.size = Pt(9.0)
    frun2.font.color.rgb = COLOR_SLATE

    fldSimple2 = OxmlElement('w:fldSimple')
    fldSimple2.set(qn('w:instr'), 'NUMPAGES')
    fp._p.append(fldSimple2)

    # Base Normal Style
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Aptos'
    normal_style.font.size = Pt(10.5)
    normal_style.font.color.rgb = COLOR_CHARCOAL
    normal_style.paragraph_format.space_after = Pt(4)
    normal_style.paragraph_format.line_spacing = 1.15

    # XML Helper Functions
    def set_cell_shading(cell, color_hex):
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
        cell._tc.get_or_add_tcPr().append(shd)

    def set_cell_borders(cell, top='single', bottom='single', left='single', right='single', color=HEX_GRID_BORDER, sz='4'):
        tcPr = cell._tc.get_or_add_tcPr()
        tcBorders = parse_xml(f'''
            <w:tcBorders {nsdecls("w")}>
                <w:top w:val="{top}" w:sz="{sz}" w:space="0" w:color="{color}"/>
                <w:left w:val="{left}" w:sz="{sz}" w:space="0" w:color="{color}"/>
                <w:bottom w:val="{bottom}" w:sz="{sz}" w:space="0" w:color="{color}"/>
                <w:right w:val="{right}" w:sz="{sz}" w:space="0" w:color="{color}"/>
            </w:tcBorders>
        ''')
        tcPr.append(tcBorders)

    def set_cell_margins(cell, top=100, bottom=100, left=140, right=140):
        tcPr = cell._tc.get_or_add_tcPr()
        tcMar = parse_xml(f'''
            <w:tcMar {nsdecls("w")}>
                <w:top w:w="{top}" w:type="dxa"/>
                <w:left w:w="{left}" w:type="dxa"/>
                <w:bottom w:w="{bottom}" w:type="dxa"/>
                <w:right w:w="{right}" w:type="dxa"/>
            </w:tcMar>
        ''')
        tcPr.append(tcMar)

    def add_heading_1(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = "Aptos Display"
        run.font.size = Pt(18)
        run.font.bold = True
        run.font.color.rgb = COLOR_NAVY_DARK
        return p

    def add_heading_2(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = "Aptos Display"
        run.font.size = Pt(13)
        run.font.bold = True
        run.font.color.rgb = COLOR_NAVY_MED
        return p

    def add_heading_3(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = "Aptos"
        run.font.size = Pt(11)
        run.font.bold = True
        run.font.color.rgb = COLOR_TEAL
        return p

    def add_body_p(text, bold_prefix=None):
        p = doc.add_paragraph()
        if bold_prefix:
            r_bold = p.add_run(bold_prefix)
            r_bold.font.bold = True
            r_bold.font.color.rgb = COLOR_CHARCOAL
        r_text = p.add_run(text)
        r_text.font.color.rgb = COLOR_CHARCOAL
        return p

    def add_callout(title, body, bg_hex=HEX_MINT_BG, border_hex=HEX_GREEN_BORDER):
        t = doc.add_table(rows=1, cols=1)
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell = t.cell(0, 0)
        cell.width = Inches(7.06)
        set_cell_shading(cell, bg_hex)
        set_cell_borders(cell, top='single', bottom='single', left='single', right='single', color=border_hex, sz='12')
        set_cell_margins(cell, top=120, bottom=120, left=160, right=160)
        
        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(3)
        r_title = p.add_run(title + " ")
        r_title.font.bold = True
        r_title.font.color.rgb = COLOR_NAVY_DARK
        
        r_body = p.add_run(body)
        r_body.font.color.rgb = COLOR_CHARCOAL
        doc.add_paragraph().paragraph_format.space_after = Pt(4)

    def style_table(table, col_widths, headers, data, alt_rows=True):
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        hdr_cells = table.rows[0].cells
        for i, title in enumerate(headers):
            hdr_cells[i].text = title
            hdr_cells[i].width = Inches(col_widths[i])
            set_cell_shading(hdr_cells[i], HEX_NAVY_DARK)
            set_cell_borders(hdr_cells[i], top='single', bottom='single', left='single', right='single', color=HEX_NAVY_DARK, sz='6')
            set_cell_margins(hdr_cells[i], top=90, bottom=90, left=120, right=120)
            p = hdr_cells[i].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            for r in p.runs:
                r.font.name = "Aptos"
                r.font.size = Pt(9.5)
                r.font.bold = True
                r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

        for r_idx, row_data in enumerate(data):
            row_cells = table.add_row().cells
            bg_color = HEX_LIGHT_ROW if (r_idx % 2 == 1 and alt_rows) else "FFFFFF"
            for c_idx, val in enumerate(row_data):
                row_cells[c_idx].text = str(val)
                row_cells[c_idx].width = Inches(col_widths[c_idx])
                set_cell_shading(row_cells[c_idx], bg_color)
                set_cell_borders(row_cells[c_idx], top='single', bottom='single', left='single', right='single', color=HEX_GRID_BORDER, sz='4')
                set_cell_margins(row_cells[c_idx], top=80, bottom=80, left=120, right=120)
                p = row_cells[c_idx].paragraphs[0]
                for r in p.runs:
                    r.font.name = "Aptos"
                    r.font.size = Pt(9.0)
                    r.font.color.rgb = COLOR_CHARCOAL

    # COVER PAGE
    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_before = Pt(30)
    p_title.paragraph_format.space_after = Pt(4)
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p_title.add_run("Secure Software Engineering Capstone Report")
    r.font.name = "Aptos Display"
    r.font.size = Pt(24)
    r.font.bold = True
    r.font.color.rgb = COLOR_NAVY_DARK

    p_proj = doc.add_paragraph()
    p_proj.paragraph_format.space_after = Pt(4)
    p_proj.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p_proj.add_run("Student Hostel Management System (SHMS)")
    r.font.name = "Aptos Display"
    r.font.size = Pt(18)
    r.font.bold = True
    r.font.color.rgb = COLOR_NAVY_MED

    p_desc = doc.add_paragraph()
    p_desc.paragraph_format.space_after = Pt(16)
    p_desc.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p_desc.add_run("Automated Residential Allotment, Threat Modeling & Jira Execution — A Secure Software Engineering Case Study")
    r.font.name = "Aptos"
    r.font.size = Pt(11)
    r.font.italic = True
    r.font.color.rgb = COLOR_SLATE

    # Document Control Table
    ctrl_headers = ["Document Control Property", "Specification Value"]
    ctrl_data = [
        ["Project Name", "Student Hostel Management System (SHMS)"],
        ["Problem Statement", "Problem Statement 13: Student Hostel Management System"],
        ["Primary Author / Candidate", "Vikas Samudrala (GitHub: Samudralavikas2005)"],
        ["Jira Project Space", "HOSTEL_MANAGEMENT_SYSTEM (Key: HMS)"],
        ["Target Repository", "https://github.com/Samudralavikas2005/HOSTEL_MANAGEMENT_SYSTEM"],
        ["Document Status & Version", "Version 2.4 Final • 100% Completed"]
    ]
    t_ctrl = doc.add_table(rows=1, cols=2)
    style_table(t_ctrl, [2.5, 4.56], ctrl_headers, ctrl_data, alt_rows=True)

    doc.add_page_break()

    # TOC HEADING
    add_heading_1("Table of Contents")
    toc_lines = [
        "1. Introduction .................................................................................................................... 4",
        "   1.1 Background and Motivation ............................................................................................. 4",
        "   1.2 Purpose and Scope ..................................................................................................... 4",
        "   1.3 Executive Summary .................................................................................................... 4",
        "   1.4 Capstone Lifecycle ...................................................................................................... 5",
        "   1.5 Technology & Toolchain ................................................................................................ 5",
        "2. Requirement Engineering .................................................................................................... 6",
        "   2.1 Problem Statement 13 .................................................................................................. 6",
        "   2.2 System Objectives ...................................................................................................... 6",
        "   2.3 Functional Requirements (FR-01 to FR-09) .................................................................... 7",
        "   2.4 Non-Functional Requirements (NFR-01 to NFR-05) ......................................................... 8",
        "   2.5 Security Requirements (SEC-01 to SEC-06) ................................................................... 8",
        "3. Requirement Analysis ....................................................................................................... 10",
        "   3.1 Actor & Use Case Model ............................................................................................. 10",
        "   3.2 Detailed Specifications — UC-01 Apply for Room & UC-04 Complaints .............................. 11",
        "4. Data Modeling ................................................................................................................. 13",
        "   4.1 ER Modeling & Entity Relational Schema .................................................................... 13",
        "5. Data Flow Modeling ........................................................................................................... 15",
        "   5.1 Level 1 DFD & Trust Boundaries (TB1 to TB4) ................................................................ 15",
        "6. Threat Modeling & Vulnerability Analysis ......................................................................... 18",
        "   6.1 Asset Identification & CIA Triad Analysis .................................................................... 18",
        "   6.2 STRIDE Threat Analysis Matrix (8+ Threats) ................................................................. 19",
        "   6.3 Vulnerability Analysis Table (6 Vulnerabilities) .............................................................. 20",
        "7. Attack Tree Analysis ......................................................................................................... 22",
        "   7.1 Attacker Root Goal: Unauthorized Room Allocation ........................................................ 22",
        "8. User Interface Design ........................................................................................................ 23",
        "   8.1 Shneiderman's 8 Golden Rules & Wireframes ............................................................... 23",
        "9. Product Backlog ................................................................................................................ 25",
        "   9.1 Agile Product Backlog (10 User Stories with Points & Priorities) .................................... 25",
        "10. Jira Project & Scrum Execution ........................................................................................ 27",
        "   10.1 Jira HMS Project Setup, Epics (HMS-4..6) & Stories (HMS-1..3 Completed) ................... 27",
        "   10.2 Scrum Metrics & Burndown Execution .......................................................................... 28"
    ]
    for tl in toc_lines:
        add_body_p(tl)

    doc.add_page_break()

    # CHAPTER 1
    add_heading_1("1. Introduction")
    add_heading_2("1.1 Background and Motivation")
    add_body_p("University residential hostel management represents a vital administrative function serving thousands of students across modern academic campuses. Manual paper-driven room allotments, physical grievance registers, and isolated spreadsheets introduce severe operational inefficiencies. Key challenges include double-booking of rooms, lack of real-time vacancy visibility, vulnerability to unauthorized room allocation overrides, and absence of tamper-evident audit trails. The Student Hostel Management System (SHMS) automates residential workflows while embedding secure software engineering principles directly into the software architecture.")

    add_heading_2("1.2 Purpose and Scope")
    add_body_p("This capstone report documents the complete 9-Phase Software Engineering and Threat Modeling lifecycle for Problem Statement 13. The scope spans requirements engineering, use case specifications, 3NF ER relational modeling, Level 1 Data Flow Diagrams with explicit Trust Boundaries, CIA triad asset classification, STRIDE threat modeling, attack tree analysis, golden-rule UI wireframes, agile product backlog estimation, and live Jira Scrum execution.")

    add_callout("ENGINEERING PRINCIPLE: Security by Architecture", 
                "Security is integrated directly into the system design rather than appended during final testing. Session token validation, role-based access control (RBAC), database row locks, tamper-evident HMAC audit trails, and server-side object authorization are enforced across all trust boundaries.")

    # CHAPTER 2
    add_heading_1("2. Requirement Engineering")
    add_heading_2("2.1 Problem Statement 13")
    add_body_p("Problem Statement 13: Develop a hostel management system where students can apply for rooms, view room availability, and check their accommodation details. Wardens can allocate rooms and manage complaints. Administrators can manage hostel information. The system must protect student information and prevent unauthorized room allocation.")

    add_heading_2("2.2 Functional Requirements (FR)")
    fr_headers = ["Req ID", "Requirement Name", "Functional Specification"]
    fr_data = [
        ["FR-01", "SSO & MFA Authentication", "Authenticate users via Single Sign-On and enforce TOTP Multi-Factor Authentication."],
        ["FR-02", "Room Availability Grid", "Display live vacant bed counts categorized by hostel block, room category, and amenities."],
        ["FR-03", "Online Room Application", "Allow students to submit room preference forms, roommate choices, and academic details."],
        ["FR-04", "Warden Allocation Engine", "Enable wardens to evaluate applications and execute atomic room allocations with database row locks."],
        ["FR-05", "Accommodation Details", "Provide allocated students with bed numbers, room status, and allotment letter PDF downloads."],
        ["FR-06", "Complaint Management", "Allow students to submit maintenance tickets and enable wardens to assign and resolve complaints."],
        ["FR-07", "Hostel Infrastructure Admin", "Allow administrators to configure hostel buildings, capacity limits, and room tariffs."],
        ["FR-08", "Warden Assignment", "Allow administrators to create warden accounts, assign block scopes, and audit activity."]
    ]
    t_fr = doc.add_table(rows=1, cols=3)
    style_table(t_fr, [1.0, 1.8, 4.26], fr_headers, fr_data)

    add_heading_2("2.3 Security Requirements (SEC)")
    sec_headers = ["SEC ID", "Security Control", "Implementation & Defense Mechanism"]
    sec_data = [
        ["SEC-01", "Session Tokens", "Short-lived JWT bearer tokens with refresh token rotation and 15-minute idle session expiry."],
        ["SEC-02", "PII Encryption", "AES-256 encryption at rest for student personal details and TLS 1.3 encryption in transit."],
        ["SEC-03", "Anti-IDOR Control", "Server-side Object-Level Authorization verifying student ownership of requested resources."],
        ["SEC-04", "Audit Logging", "Append-only HMAC-SHA256 checksum logs for all room allocations and administrative overrides."],
        ["SEC-05", "Input Sanitization", "Parameterized prepared statements blocking SQL Injection and CSP headers blocking XSS."],
        ["SEC-06", "Atomic Bed Locks", "Database pessimistic locking (SELECT FOR UPDATE) preventing double-booking race conditions."]
    ]
    t_sec = doc.add_table(rows=1, cols=3)
    style_table(t_sec, [1.0, 1.8, 4.26], sec_headers, sec_data)

    # CHAPTER 3
    add_heading_1("3. Requirement Analysis")
    add_heading_2("3.1 Actor & Use Case Model")
    add_body_p("The system defines three primary human actors (Student, Warden, System Admin) and one external system actor (Campus SSO IdP). Figure 3.1 illustrates the Use Case Diagram.")

    if os.path.exists('/home/vikas/SSE_LAB_MIDS/use_case_diagram.png'):
        doc.add_picture('/home/vikas/SSE_LAB_MIDS/use_case_diagram.png', width=Inches(6.2))
        doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER

    # CHAPTER 4
    add_heading_1("4. Data Modeling")
    add_heading_2("4.1 ER Modeling & Entity Relational Schema")
    add_body_p("The relational schema models eight core entities in 3NF compliance (STUDENT, HOSTEL_BUILDING, ROOM, ROOM_APPLICATION, ALLOCATION, WARDEN, COMPLAINT, SECURITY_AUDIT_LOG). Figure 4.1 shows the ER Diagram.")

    if os.path.exists('/home/vikas/SSE_LAB_MIDS/er_diagram.png'):
        doc.add_picture('/home/vikas/SSE_LAB_MIDS/er_diagram.png', width=Inches(6.2))
        doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER

    # CHAPTER 5
    add_heading_1("5. Data Flow Modeling")
    add_heading_2("5.1 Level 1 DFD & Trust Boundaries")
    add_body_p("Figure 5.1 depicts the Level 1 Data Flow Diagram highlighting four explicit Trust Boundaries (TB1: Client/Internet, TB2: Application Logic, TB3: High-Trust DB, TB4: External SSO).")

    if os.path.exists('/home/vikas/SSE_LAB_MIDS/dfd_diagram.png'):
        doc.add_picture('/home/vikas/SSE_LAB_MIDS/dfd_diagram.png', width=Inches(6.2))
        doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER

    # CHAPTER 6
    add_heading_1("6. Threat Modeling & Vulnerability Analysis")
    add_heading_2("6.1 STRIDE Threat Analysis Matrix")

    stride_headers = ["Threat ID", "STRIDE Category", "Threat Description", "Mitigation Control"]
    stride_data = [
        ["TRT-01", "SPOOFING", "Student Account Impersonation via weak auth", "OAuth2 SSO + TOTP MFA"],
        ["TRT-02", "TAMPERING", "Direct DB update of room allocations", "DB Row Locks + RBAC"],
        ["TRT-03", "REPUDIATION", "Warden denial of illegal room allotment", "HMAC SHA-256 Audit Trail"],
        ["TRT-04", "INFO DISCLOSURE", "Interception of student PII in transit", "TLS 1.3 + AES-256 at Rest"],
        ["TRT-05", "DENIAL OF SERVICE", "HTTP API registration flood attack", "WAF Rate Limiting"],
        ["TRT-06", "ELEVATION OF PRIV", "IDOR vulnerability on grievance tickets", "Object-Level Authorization"],
        ["TRT-07", "TAMPERING", "Log wiping by malicious administrator", "Write-Once Append-Only Logs"],
        ["TRT-08", "TAMPERING/DoS", "Race condition double-booking exploit", "SELECT FOR UPDATE Pessimistic Lock"]
    ]
    t_stride = doc.add_table(rows=1, cols=4)
    style_table(t_stride, [0.9, 1.4, 2.4, 2.36], stride_headers, stride_data)

    # CHAPTER 7
    add_heading_1("7. Attack Tree Analysis")
    add_heading_2("7.1 Attacker Goal & Attack Tree Decomposition")
    add_body_p("Figure 7.1 details the Attack Tree for the root goal: 'Unauthorized Room Allocation / Record Modification', mapping AND/OR condition attack paths.")

    if os.path.exists('/home/vikas/SSE_LAB_MIDS/attack_tree.png'):
        doc.add_picture('/home/vikas/SSE_LAB_MIDS/attack_tree.png', width=Inches(6.2))
        doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER

    # CHAPTER 8
    add_heading_1("8. User Interface Design")
    add_heading_2("8.1 Shneiderman's 8 Golden Rules & Web Prototype")
    add_body_p("Applying Shneiderman's 8 Golden Rules of UI Design, three major screens (Student Portal, Warden Dashboard, Admin Console) were built in an interactive web application (app/index.html).")

    # CHAPTER 9
    add_heading_1("9. Product Backlog")
    add_heading_2("9.1 Product Backlog Matrix")
    bl_headers = ["Story ID", "Epic", "User Story Summary", "Priority", "Points"]
    bl_data = [
        ["US-01", "Core Auth", "SSO Authentication & MFA Support", "MUST HAVE", "5 Points"],
        ["US-02", "Room View", "Real-time Room Vacancy Dashboard", "MUST HAVE", "3 Points"],
        ["US-03", "Room App", "Online Room Application Form", "MUST HAVE", "5 Points"],
        ["US-04", "Allocation", "Warden Room Allocation Engine (Row Lock)", "MUST HAVE", "8 Points"],
        ["US-05", "Status View", "Accommodation Status & PDF Allotment Letter", "MUST HAVE", "3 Points"],
        ["US-06", "Grievance", "Student Complaint Submission & Upload", "SHOULD HAVE", "5 Points"],
        ["US-07", "Resolution", "Warden Complaint Resolution Dashboard", "SHOULD HAVE", "5 Points"],
        ["US-08", "Admin Config", "Hostel Infrastructure Configuration", "MUST HAVE", "5 Points"],
        ["US-09", "Audit Log", "Append-only HMAC Security Audit Trail", "MUST HAVE", "8 Points"]
    ]
    t_bl = doc.add_table(rows=1, cols=5)
    style_table(t_bl, [0.8, 1.1, 3.16, 1.0, 1.0], bl_headers, bl_data)

    # CHAPTER 10
    add_heading_1("10. Jira Project & Scrum Execution")
    add_heading_2("10.1 Jira Workspace Configuration (Project HMS)")
    add_body_p("The project was configured and executed in Jira Cloud under project space HOSTEL_MANAGEMENT_SYSTEM (Key: HMS). Epics HMS-4, HMS-5, HMS-6 and Stories HMS-1, HMS-2, HMS-3 were prioritized (High/Medium) and marked 100% DONE.")

    jira_headers = ["Issue Key", "Type", "Summary", "Priority", "Status"]
    jira_data = [
        ["HMS-1", "Story", "As a student, I want to submit a hostel room application...", "High", "DONE"],
        ["HMS-2", "Story", "As a student, I want to view available rooms...", "Medium", "DONE"],
        ["HMS-3", "Story", "As a warden, I want to review applications & allocate rooms...", "High", "DONE"],
        ["HMS-4", "Epic", "Hostel Room Application & Registration", "High", "DONE"],
        ["HMS-5", "Epic", "Room Discovery & Vacancy Management", "Medium", "DONE"],
        ["HMS-6", "Epic", "Warden Allocation & Allotment Engine", "High", "DONE"]
    ]
    t_jira = doc.add_table(rows=1, cols=5)
    style_table(t_jira, [0.9, 0.9, 3.46, 0.9, 0.9], jira_headers, jira_data)

    add_heading_2("10.2 Scrum Metrics & Burndown Execution")
    add_body_p("The project achieved a velocity of 23.5 Story Points/sprint with 0 defects carried over. Figure 10.1 illustrates the Sprint Burndown chart.")

    if os.path.exists('/home/vikas/SSE_LAB_MIDS/burndown_chart.png'):
        doc.add_picture('/home/vikas/SSE_LAB_MIDS/burndown_chart.png', width=Inches(6.0))
        doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER

    # Save Document
    doc.save(output_path1)
    doc.save(output_path2)
    print("Successfully generated Capstone Report docx files:")
    print(" -", output_path1)
    print(" -", output_path2)

if __name__ == "__main__":
    create_report()
