import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#1F4E78'

# 1. Use Case Diagram
fig, ax = plt.subplots(figsize=(10, 6), dpi=200)
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.axis('off')
ax.set_title("Figure 3.1: Student Hostel Management System - Use Case Diagram", fontsize=12, fontweight='bold', pad=15, color='#1F4E78')

# Box for System Boundary
rect = patches.Rectangle((2.5, 0.5), 5.0, 6.0, linewidth=2, edgecolor='#1F4E78', facecolor='#F8FAFC', linestyle='--')
ax.add_patch(rect)
ax.text(5.0, 6.2, "Student Hostel Management System (SHMS)", fontsize=10, fontweight='bold', ha='center', color='#1F4E78')

# Actors
actors = [
    ("Student", 1.0, 5.0, '#2563EB'),
    ("Warden", 1.0, 2.0, '#D97706'),
    ("Admin", 9.0, 3.5, '#7C3AED')
]

for name, x, y, color in actors:
    ax.add_patch(patches.Circle((x, y+0.4), 0.25, color=color))
    ax.plot([x, x], [y+0.15, y-0.3], color=color, lw=2)
    ax.plot([x-0.2, x+0.2], [y, y], color=color, lw=2)
    ax.plot([x-0.2, x], [y-0.6, y-0.3], color=color, lw=2)
    ax.plot([x+0.2, x], [y-0.6, y-0.3], color=color, lw=2)
    ax.text(x, y-0.8, name, fontsize=9, fontweight='bold', ha='center', color=color)

# Use Cases
use_cases = [
    ("UC-01: Apply for Room", 5.0, 5.2),
    ("UC-02: View Room Availability", 5.0, 4.2),
    ("UC-03: Allocate Hostel Room", 5.0, 3.2),
    ("UC-04: Submit & Resolve Complaints", 5.0, 2.2),
    ("UC-05: Configure Infrastructure & Audit", 5.0, 1.2)
]

for text, x, y in use_cases:
    ellipse = patches.Ellipse((x, y), 3.8, 0.6, edgecolor='#1E293B', facecolor='#E2E8F0', lw=1.5)
    ax.add_patch(ellipse)
    ax.text(x, y, text, fontsize=8, fontweight='bold', ha='center', va='center', color='#0F172A')

# Lines
ax.plot([1.3, 3.1], [5.0, 5.2], 'k-', lw=1)
ax.plot([1.3, 3.1], [4.8, 4.2], 'k-', lw=1)
ax.plot([1.3, 3.1], [4.5, 2.2], 'k-', lw=1)

ax.plot([1.3, 3.1], [2.2, 4.2], 'k-', lw=1)
ax.plot([1.3, 3.1], [2.0, 3.2], 'k-', lw=1)
ax.plot([1.3, 3.1], [1.8, 2.2], 'k-', lw=1)

ax.plot([8.7, 6.9], [3.5, 1.2], 'k-', lw=1)

plt.tight_layout()
plt.savefig('/home/vikas/SSE_LAB_MIDS/use_case_diagram.png', bbox_inches='tight')
plt.close()

# 2. ER Diagram
fig, ax = plt.subplots(figsize=(10, 5), dpi=200)
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')
ax.set_title("Figure 4.1: Entity-Relationship Diagram (ERD)", fontsize=12, fontweight='bold', pad=15, color='#1F4E78')

entities = [
    ("STUDENT", 1.5, 4.5, "#2563EB"),
    ("ROOM_APPLICATION", 5.0, 4.5, "#0D9488"),
    ("HOSTEL_BUILDING", 8.5, 4.5, "#7C3AED"),
    ("ALLOCATION", 5.0, 2.0, "#D97706"),
    ("ROOM", 8.5, 2.0, "#2563EB"),
    ("COMPLAINT", 1.5, 2.0, "#DC2626")
]

for name, x, y, color in entities:
    r = patches.FancyBboxPatch((x-1.1, y-0.4), 2.2, 0.8, boxstyle="round,pad=0.1", edgecolor=color, facecolor='#F1F5F9', lw=2)
    ax.add_patch(r)
    ax.text(x, y, name, fontsize=8, fontweight='bold', ha='center', va='center', color=color)

# Connectors
ax.annotate("", xy=(3.9, 4.5), xytext=(2.6, 4.5), arrowprops=dict(arrowstyle="->", lw=1.5))
ax.text(3.25, 4.7, "1 : N", fontsize=8, fontweight='bold', ha='center')

ax.annotate("", xy=(7.4, 4.5), xytext=(6.1, 4.5), arrowprops=dict(arrowstyle="->", lw=1.5))
ax.text(6.75, 4.7, "N : 1", fontsize=8, fontweight='bold', ha='center')

ax.annotate("", xy=(5.0, 2.8), xytext=(5.0, 4.1), arrowprops=dict(arrowstyle="->", lw=1.5))
ax.text(5.3, 3.4, "1 : 1", fontsize=8, fontweight='bold')

ax.annotate("", xy=(7.4, 2.0), xytext=(6.1, 2.0), arrowprops=dict(arrowstyle="->", lw=1.5))
ax.text(6.75, 2.2, "1 : N", fontsize=8, fontweight='bold', ha='center')

ax.annotate("", xy=(1.5, 2.8), xytext=(1.5, 4.1), arrowprops=dict(arrowstyle="->", lw=1.5))
ax.text(1.8, 3.4, "1 : N", fontsize=8, fontweight='bold')

plt.tight_layout()
plt.savefig('/home/vikas/SSE_LAB_MIDS/er_diagram.png', bbox_inches='tight')
plt.close()

# 3. DFD Diagram with Trust Boundaries
fig, ax = plt.subplots(figsize=(10, 5.5), dpi=200)
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')
ax.set_title("Figure 5.1: Level 1 Data Flow Diagram with Trust Boundaries (TB1 - TB4)", fontsize=12, fontweight='bold', pad=15, color='#1F4E78')

# Trust Boundary lines
ax.axvline(2.5, color='#DC2626', linestyle='--', linewidth=2)
ax.text(2.5, 5.6, "TB1: Client/WAF Boundary", color='#DC2626', fontsize=8, fontweight='bold', ha='center', backgroundcolor='white')

ax.axvline(7.5, color='#D97706', linestyle='--', linewidth=2)
ax.text(7.5, 5.6, "TB3: High-Trust DB Boundary", color='#D97706', fontsize=8, fontweight='bold', ha='center', backgroundcolor='white')

# Entities
ax.add_patch(patches.Rectangle((0.3, 2.5), 1.8, 1.0, facecolor='#DBEAFE', edgecolor='#2563EB', lw=1.5))
ax.text(1.2, 3.0, "Student / Warden\nBrowsers (Untrusted)", fontsize=7, fontweight='bold', ha='center', va='center')

# App Processes
ax.add_patch(patches.Circle((5.0, 4.2), 0.7, facecolor='#FEF3C7', edgecolor='#D97706', lw=1.5))
ax.text(5.0, 4.2, "P1.0 Auth &\nTokens", fontsize=7, fontweight='bold', ha='center', va='center')

ax.add_patch(patches.Circle((5.0, 1.8), 0.7, facecolor='#FEF3C7', edgecolor='#D97706', lw=1.5))
ax.text(5.0, 1.8, "P3.0 Room\nAllocation Engine", fontsize=7, fontweight='bold', ha='center', va='center')

# Data Stores
ax.add_patch(patches.Rectangle((8.0, 3.7), 1.7, 0.9, facecolor='#E0E7FF', edgecolor='#4338CA', lw=1.5))
ax.text(8.85, 4.15, "DS1: Student DB", fontsize=7, fontweight='bold', ha='center', va='center')

ax.add_patch(patches.Rectangle((8.0, 1.3), 1.7, 0.9, facecolor='#E0E7FF', edgecolor='#4338CA', lw=1.5))
ax.text(8.85, 1.75, "DS4: Allocation &\nAudit Store", fontsize=7, fontweight='bold', ha='center', va='center')

# Data Flows
ax.annotate("", xy=(4.3, 4.2), xytext=(2.1, 3.2), arrowprops=dict(arrowstyle="->", lw=1.5, color='#1E293B'))
ax.annotate("", xy=(4.3, 1.8), xytext=(2.1, 2.8), arrowprops=dict(arrowstyle="->", lw=1.5, color='#1E293B'))

ax.annotate("", xy=(8.0, 4.15), xytext=(5.7, 4.2), arrowprops=dict(arrowstyle="->", lw=1.5, color='#4338CA'))
ax.annotate("", xy=(8.0, 1.75), xytext=(5.7, 1.8), arrowprops=dict(arrowstyle="->", lw=1.5, color='#4338CA'))

plt.tight_layout()
plt.savefig('/home/vikas/SSE_LAB_MIDS/dfd_diagram.png', bbox_inches='tight')
plt.close()

# 4. Attack Tree
fig, ax = plt.subplots(figsize=(10, 5), dpi=200)
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')
ax.set_title("Figure 7.1: Attack Tree - Unauthorized Room Allocation", fontsize=12, fontweight='bold', pad=15, color='#1F4E78')

# Root Node
ax.add_patch(patches.Rectangle((2.5, 4.8), 5.0, 0.8, facecolor='#FEE2E2', edgecolor='#DC2626', lw=2))
ax.text(5.0, 5.2, "Root Goal: Unauthorized Room Allocation", fontsize=9, fontweight='bold', ha='center', va='center', color='#991B1B')

# Branch Nodes (OR)
branches = [
    ("1. Credential Hijacking", 1.5, 3.2),
    ("2. IDOR / API Privilege Escalation", 4.0, 3.2),
    ("3. SQL Injection", 6.5, 3.2),
    ("4. Race Condition Double Booking", 8.8, 3.2)
]

for text, x, y in branches:
    ax.add_patch(patches.Rectangle((x-1.0, y-0.4), 2.0, 0.8, facecolor='#FEF3C7', edgecolor='#D97706', lw=1.5))
    ax.text(x, y, text, fontsize=7, fontweight='bold', ha='center', va='center', wrap=True)
    ax.plot([5.0, x], [4.8, 3.6], 'k-', lw=1)

# Leaf Conditions (AND)
ax.text(1.5, 1.5, "(AND)\n1.1 XSS Token Theft\n1.2 Missing HttpOnly Cookie", fontsize=6, ha='center', bbox=dict(boxstyle="round", facecolor='#F1F5F9'))
ax.plot([1.5, 1.5], [2.8, 2.0], 'k--', lw=1)

ax.text(4.0, 1.5, "(AND)\n2.1 Intercept HTTP Request\n2.2 Inject admin_override: true", fontsize=6, ha='center', bbox=dict(boxstyle="round", facecolor='#F1F5F9'))
ax.plot([4.0, 4.0], [2.8, 2.0], 'k--', lw=1)

ax.text(6.5, 1.5, "(AND)\n3.1 Unsanitized String Input\n3.2 Direct DB UPDATE SQL", fontsize=6, ha='center', bbox=dict(boxstyle="round", facecolor='#F1F5F9'))
ax.plot([6.5, 6.5], [2.8, 2.0], 'k--', lw=1)

ax.text(8.8, 1.5, "(AND)\n4.1 50 Parallel HTTP Requests\n4.2 Missing DB Row Lock", fontsize=6, ha='center', bbox=dict(boxstyle="round", facecolor='#F1F5F9'))
ax.plot([8.8, 8.8], [2.8, 2.0], 'k--', lw=1)

plt.tight_layout()
plt.savefig('/home/vikas/SSE_LAB_MIDS/attack_tree.png', bbox_inches='tight')
plt.close()

# 5. Burndown Chart
fig, ax = plt.subplots(figsize=(8, 4.5), dpi=200)
days = np.array([0, 2, 4, 6, 8, 10])
ideal = np.array([21, 16.8, 12.6, 8.4, 4.2, 0])
actual = np.array([21, 21, 16, 11, 6, 0])

ax.plot(days, ideal, 'r--', label='Ideal Burndown', lw=2)
ax.plot(days, actual, 'b-o', label='Actual Remaining Story Points', lw=2.5)
ax.fill_between(days, actual, alpha=0.1, color='blue')

ax.set_title("Figure 10.1: Sprint 1 Burndown Chart (21 Story Points)", fontsize=11, fontweight='bold', color='#1F4E78')
ax.set_xlabel("Sprint Timeline (Working Days)", fontsize=9, fontweight='bold')
ax.set_ylabel("Remaining Story Points", fontsize=9, fontweight='bold')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper right')

plt.tight_layout()
plt.savefig('/home/vikas/SSE_LAB_MIDS/burndown_chart.png', bbox_inches='tight')
plt.close()

print("All 5 diagram PNG images successfully generated!")
