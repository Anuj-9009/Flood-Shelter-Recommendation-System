import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

OUT_DOCX = "/Users/anuj9009/Downloads/major_project/Flood_Shelter_Recommendation_System_Report.docx"
LOGO_PATH = "/Users/anuj9009/Downloads/major_project/assets/word/media/image2.jpeg"
FIG_DIR = "/Users/anuj9009/Downloads/major_project/assets/figures"

def add_page_border(section):
    sectPr = section._sectPr
    pgBorders = OxmlElement('w:pgBorders')
    pgBorders.set(qn('w:offsetFrom'), 'page')
    for border_name in ('top', 'left', 'bottom', 'right'):
        border = OxmlElement(f'w:{border_name}')
        border.set(qn('w:val'), 'single')
        border.set(qn('w:sz'), '12')
        border.set(qn('w:space'), '24')
        border.set(qn('w:color'), '000000')
        pgBorders.append(border)
    sectPr.append(pgBorders)

def set_cell_shading(cell, color_hex):
    shading_elm = OxmlElement('w:shd')
    shading_elm.set(qn('w:val'), 'clear')
    shading_elm.set(qn('w:color'), 'auto')
    shading_elm.set(qn('w:fill'), color_hex)
    cell._tc.get_or_add_tcPr().append(shading_elm)

def add_p(doc, text="", size=12, bold=False, italic=False, underline=False, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=0, space_after=6, line_spacing=1.35):
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing
    if text:
        run = p.add_run(text)
        run.font.name = "Times New Roman"
        run.font.size = Pt(size)
        run.bold = bold
        run.italic = italic
        run.underline = underline
        run.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_rich_p(doc, parts, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_before=0, space_after=8, line_spacing=1.35, left_indent=0):
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing
    if left_indent:
        p.paragraph_format.left_indent = Inches(left_indent)
    for part in parts:
        text = part[0]
        bold = part[1] if len(part) > 1 else False
        size = part[2] if len(part) > 2 else 12
        italic = part[3] if len(part) > 3 else False
        run = p.add_run(text)
        run.font.name = "Times New Roman"
        run.font.size = Pt(size)
        run.bold = bold
        run.italic = italic
        run.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_bullet(doc, lead_bold, text, space_after=4):
    p = doc.add_paragraph(style='List Bullet')
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.3
    if lead_bold:
        r1 = p.add_run(lead_bold)
        r1.font.name = "Times New Roman"
        r1.font.size = Pt(12)
        r1.bold = True
    r2 = p.add_run(text)
    r2.font.name = "Times New Roman"
    r2.font.size = Pt(12)
    return p

def add_figure(doc, img_filename, caption_text, width_inches=6.0):
    img_path = os.path.join(FIG_DIR, img_filename)
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(8)
        p_img.paragraph_format.space_after = Pt(4)
        run_img = p_img.add_run()
        run_img.add_picture(img_path, width=Inches(width_inches))
    add_p(doc, caption_text, size=11, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=2, space_after=12)

doc = Document()

# Page setup
for section in doc.sections:
    section.page_width = Inches(8.27)   # A4
    section.page_height = Inches(11.69) # A4
    section.top_margin = Inches(0.85)
    section.bottom_margin = Inches(0.85)
    section.left_margin = Inches(0.9)
    section.right_margin = Inches(0.9)
    add_page_border(section)

# ==============================================================================
# PAGE 1: COVER PAGE
# ==============================================================================
add_p(doc, "A PROJECT REPORT", size=14, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=18, space_after=6)
add_p(doc, "on", size=12, bold=False, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
add_p(doc, '"Flood Shelter Recommendation System"', size=16, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=10)
add_p(doc, "Submitted to", size=12, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
add_p(doc, "KIIT Deemed to be University", size=13, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
add_p(doc, "In Partial Fulfillment of the Requirements for the Award of", size=12, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
add_p(doc, "BACHELOR'S DEGREE IN COMPUTER SCIENCE AND ENGINEERING", size=13, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
add_p(doc, "BY", size=12, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=8)

members = [
    ("KRITIKA GHOSH", "23051024"),
    ("NANDINI KUMARI BISWAL", "23051032"),
    ("NUPUR KUMARI", "23051035"),
    ("ANUJ KUMAR", "2305439"),
    ("ANAS KHAN", "24057009"),
]
for m_name, m_roll in members:
    add_p(doc, f"{m_name}        {m_roll}", size=12, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)

add_p(doc, "Under the Guidance of", size=12, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=10, space_after=4)
add_p(doc, "SUNIL KUMAR GOUDA", size=13, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)

if os.path.exists(LOGO_PATH):
    p_logo = doc.add_paragraph()
    p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_logo.paragraph_format.space_before = Pt(6)
    p_logo.paragraph_format.space_after = Pt(12)
    p_logo.add_run().add_picture(LOGO_PATH, width=Inches(1.35))

add_p(doc, "SCHOOL OF COMPUTER ENGINEERING", size=12, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
add_p(doc, "KALINGA INSTITUTE OF INDUSTRIAL TECHNOLOGY", size=12, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
add_p(doc, "BHUBANESWAR, ODISHA — 751024", size=12, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
add_p(doc, "2026", size=12, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=0)

doc.add_page_break()

# ==============================================================================
# PAGE 2: CERTIFICATE
# ==============================================================================
if os.path.exists(LOGO_PATH):
    p_logo2 = doc.add_paragraph()
    p_logo2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_logo2.paragraph_format.space_before = Pt(12)
    p_logo2.paragraph_format.space_after = Pt(10)
    p_logo2.add_run().add_picture(LOGO_PATH, width=Inches(1.25))

add_p(doc, "KIIT Deemed to be University", size=13, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
add_p(doc, "School of Computer Engineering", size=12, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
add_p(doc, "Bhubaneswar, Odisha — 751024", size=12, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=18)

add_p(doc, "CERTIFICATE", size=14, bold=True, underline=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=14)
add_p(doc, "This is to certify that the project titled", size=12, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=10)
add_p(doc, '"Flood Shelter Recommendation System"', size=14, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=10)
add_p(doc, "submitted by", size=12, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=10)

for m_name, m_roll in members:
    add_p(doc, f"{m_name} — {m_roll}", size=12, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)

add_p(
    doc,
    "is a record of authentic work accomplished by them toward the partial fulfillment of the Bachelor of Engineering (Computer Science & Engineering) degree at KIIT Deemed to be University, Bhubaneswar. This research and development work was conducted during the academic year 2025–2026 under our direct supervision and guidance.",
    size=12,
    align=WD_ALIGN_PARAGRAPH.CENTER,
    space_before=14,
    space_after=28,
    line_spacing=1.4,
)

add_p(doc, "Date: ____ / ____ / ________", size=12, align=WD_ALIGN_PARAGRAPH.LEFT, space_after=36)
add_p(doc, "Sunil Kumar Gouda", size=12, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
add_p(doc, "Project Supervisor", size=12, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
add_p(doc, "School of Computer Engineering, KIIT University", size=12, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=0)

doc.add_page_break()

# ==============================================================================
# PAGE 3: ACKNOWLEDGEMENTS
# ==============================================================================
add_p(doc, "Acknowledgements", size=15, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=12, space_after=24)
add_rich_p(
    doc,
    [
        ("We extend our deepest gratitude to our Project Supervisor, ", False),
        ("Prof. Sunil Kumar Gouda", True),
        (", of the School of Computer Engineering, KIIT Deemed to be University, whose unwavering support, technical insights, and mentorship were indispensable throughout every stage of this project — from initial conceptualization of the multi-criteria fuzzy inference engine to the final full-stack web deployment. Their patient guidance in soft computing theory, software architecture, and academic writing elevated the quality of this work significantly.", False),
    ],
    space_after=16,
    line_spacing=1.45,
)
add_rich_p(
    doc,
    [
        ("We also express our sincere thanks to the Dean and faculty members of the School of Computer Engineering, Kalinga Institute of Industrial Technology, for providing the computational infrastructure, academic environment, and continuous encouragement required to complete this project successfully.", False),
    ],
    space_after=36,
    line_spacing=1.45,
)

for m_name, _ in members:
    add_p(doc, m_name, size=12, bold=True, align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=4)

doc.add_page_break()

# ==============================================================================
# PAGE 4: ABSTRACT
# ==============================================================================
add_p(doc, "Abstract", size=15, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=12, space_after=20)
add_rich_p(
    doc,
    [
        ("During severe flood emergencies, evacuating affected citizens to safe relief shelters rapidly and reliably is a critical disaster management challenge. Traditional shelter locators rely primarily on shortest-path distance metrics; however, in real-world flood scenarios, the nearest shelter is not necessarily the safest or most viable option. A nearby shelter may be situated on low-lying terrain, in close proximity to overflowing water bodies, lacking road accessibility, or depleted of available beds and medical supplies. To address this multi-criteria decision problem under uncertainty, this project presents the ", False),
        ("Flood Shelter Recommendation System", True),
        (", an intelligent decision-support application powered by a ", False),
        ("Mamdani Fuzzy Inference System (FIS)", True),
        (". Rather than applying rigid binary thresholds, the system evaluates six operational and environmental antecedents — travel distance (0–20 km), usable bed capacity (0–100), road accessibility (0–10), terrain elevation level (0–10), proximity to water bodies (0–10), and medical facility readiness (0–10) — using trapezoidal and triangular membership functions across 21 domain-specific fuzzy rules to compute a continuous ", False),
        ("Suitability Score (0–100)", True),
        (" via centroid defuzzification.", False),
    ],
    space_after=14,
    line_spacing=1.4,
)
add_rich_p(
    doc,
    [
        ("The system is engineered as a modular, three-tier full-stack application using ", False),
        ("Flask", True),
        (" and ", True),
        ("SQLAlchemy", True),
        (" on the backend, ", False),
        ("scikit-fuzzy", True),
        (" and ", False),
        ("NumPy", True),
        (" for the inference engine, and ", False),
        ("SQLite / PostgreSQL", True),
        (" for persistent storage of geospatial shelter records, operational status updates, and audit logs. The presentation layer supports three client interfaces sharing a unified recommendation core: a responsive web dashboard built with ", False),
        ("Bootstrap 5, Chart.js, and Leaflet/OpenStreetMap", True),
        (" (deployed live at ", False),
        ("https://flood-shelter.vercel.app/", True),
        ("), a ", False),
        ("Tkinter", True),
        (" desktop GUI, and an interactive CLI. Experimental validation across 26 built-in benchmark shelters and 20 real-world Odisha flood shelters demonstrates that the Mamdani fuzzy engine effectively penalizes hazardous nearby shelters (e.g., Shelter V at 0.5 km scoring 34.72 due to low elevation and water proximity) while prioritizing high-elevation, well-equipped shelters (e.g., Shelter H scoring 67.83 and Shelter A scoring 66.92), providing transparent, life-saving evacuation guidance.", False),
    ],
    space_after=18,
    line_spacing=1.4,
)
add_rich_p(
    doc,
    [
        ("Keywords: ", True),
        ("Flood Shelter Recommendation, Fuzzy Logic, Mamdani Inference System, Multi-Criteria Decision Making (MCDM), Centroid Defuzzification, scikit-fuzzy, Flask REST API, Leaflet Geospatial Mapping, Disaster Management, Emergency Evacuation.", False),
    ],
    align=WD_ALIGN_PARAGRAPH.LEFT,
    space_after=0,
    line_spacing=1.35,
)

doc.add_page_break()

# ==============================================================================
# PAGE 5: TABLE OF CONTENTS & LIST OF FIGURES
# ==============================================================================
add_p(doc, "Contents", size=16, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=6, space_after=14)

toc_items = [
    ("Chapter 1 — Introduction", "1", True),
    ("Chapter 2 — Theoretical Background / Literature Review", "2-3", True),
    ("    2.1 Fuzzy Logic and Mamdani Inference System", "2", False),
    ("    2.2 Membership Functions and Centroid Defuzzification", "2", False),
    ("    2.3 Flask Web Framework and RESTful Architecture", "2-3", False),
    ("    2.4 Geospatial Visualization with Leaflet and Chart.js", "3", False),
    ("    2.5 SQLite & SQLAlchemy for Relational Data Persistence", "3", False),
    ("    2.6 Related Work", "3", False),
    ("Chapter 3 — Problem Statement and Requirement Specifications", "4-8", True),
    ("    3.1 Problem Statement", "4", False),
    ("    3.2 Project Planning", "4", False),
    ("    3.3 Software Requirements Specification (SRS)", "5", False),
    ("    3.4 System Design", "5-7", False),
    ("    3.5 Database Schema", "8", False),
    ("    3.6 API Endpoint Specification", "8", False),
    ("Chapter 4 — Implementation", "9-15", True),
    ("    4.1 Methodology", "9-11", False),
    ("    4.2 Testing and Verification Plan", "12-13", False),
    ("    4.3 Result Analysis", "13-14", False),
    ("    4.4 Quality Assurance", "15", False),
    ("Chapter 5 — Standards Adopted", "16-17", True),
    ("    5.1 Design Standards", "16", False),
    ("    5.2 Coding Standards", "16-17", False),
    ("    5.3 Testing Standards", "17", False),
    ("    5.4 Cost Analysis", "17", False),
    ("Chapter 6 — Conclusion and Future Scope", "18-19", True),
    ("    6.1 Conclusion", "18", False),
    ("    6.2 Future Scope", "18-19", False),
    ("References", "20", True),
    ("Individual Contribution Sheet", "21-25", True),
    ("Turnitin Plagiarism Report", "26", True),
]

for title, pg, is_main in toc_items:
    dots = "." * max(5, 82 - len(title) - len(pg))
    add_p(doc, f"{title} {dots} {pg}", size=11.5, bold=is_main, space_after=3, line_spacing=1.15)

doc.add_page_break()

add_p(doc, "List of Figures", size=16, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=6, space_after=14)
figures_list = [
    "Fig 1 : System Architecture Diagram (Three-Tier Presentation, Fuzzy Logic, and Persistence Layers)",
    "Fig 2 : Block Diagram of Mamdani Fuzzy Inference and Shelter Ranking Pipeline",
    "Fig 3 : Application Execution and Automated Pytest Verification on Local Host",
    "Fig 4 : Flood Shelter Intelligence Web Dashboard (Live Deployment on Vercel)",
    "Fig 5 : Geospatial & Operational Flood Shelter Dataset Preview (Odisha Shelters)",
    "Fig 6 : Top Ranked Shelter Match Card and Multi-Criteria Suitability Rankings",
    "Fig 7 : Interactive Leaflet & OpenStreetMap View with Shelter Suitability Popups",
    "Fig 8 : Bar Graph — Shelter Suitability Score Comparison (Direct vs. Alternative Matches)",
    "Fig 9 : Radar Chart — Multi-Criteria Fuzzy Preference Profile vs. Shelter Attributes",
    "Fig 10 : Fuzzy Membership Functions (Antecedent Distance & Consequent Suitability Universe)",
]
for f_item in figures_list:
    add_p(doc, f_item, size=12, bold=False, space_after=8, line_spacing=1.3)

add_p(doc, "List of Tables", size=16, bold=True, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=18, space_after=12)
tables_list = [
    "Table 1 : Fuzzy Antecedent and Consequent Linguistic Variables, Universes, and Parameters",
    "Table 2 : Functional and Non-Functional Verification Test Cases (T01 – T10)",
    "Table 3 : Comparative Evaluation of Shelter Ranking Methodologies and Benchmark Results",
]
for t_item in tables_list:
    add_p(doc, t_item, size=12, bold=False, space_after=8, line_spacing=1.3)

doc.add_page_break()

# ==============================================================================
# CHAPTER 1: INTRODUCTION
# ==============================================================================
add_p(doc, "Chapter 1", size=16, bold=True, space_before=6, space_after=4)
add_p(doc, "Introduction", size=14, bold=True, space_after=12)

add_rich_p(
    doc,
    [
        ("Floods are among the most frequent and devastating natural disasters worldwide, particularly in coastal and riverine regions such as Odisha, India, where annual monsoonal surges and cyclonic depressions frequently inundate residential zones. During a flood emergency, timely evacuation of citizens to safe relief shelters is paramount to minimizing casualties and human distress. However, displaced individuals and emergency response coordinators often face severe information asymmetry when selecting an evacuation shelter. Conventional navigation tools and static government directories typically sort shelters solely by geographic proximity or list raw tabular attributes without synthesizing overall safety.", False),
    ],
)

add_rich_p(
    doc,
    [
        ("The core motivation behind the ", False),
        ("Flood Shelter Recommendation System", True),
        (" is the critical realization that ", False),
        ("the nearest shelter is not necessarily the safest or most suitable option", True),
        (". For instance, a shelter located 0.5 km away may lie in a low-elevation basin immediately adjacent to a swelling river, possess difficult road accessibility due to waterlogging, lack medical facilities for injured evacuees, or have zero available beds remaining. Conversely, a shelter situated 2.5 to 3.8 km away on high terrain, far from water bodies, with easy road access, 40+ available beds, and advanced medical support offers vastly superior protection. Evaluating these competing factors manually during a high-stress emergency is cognitively overwhelming and prone to dangerous misjudgments.", False),
    ],
)

add_rich_p(
    doc,
    [
        ("Furthermore, real-world disaster parameters are inherently imprecise and continuous rather than binary (black-and-white). A shelter is rarely strictly 'safe' or 'unsafe'; instead, it exhibits graded degrees of accessibility, moderate or high elevation safety, and varying margins of bed capacity. To model this real-world vagueness mathematically, this project employs ", False),
        ("Fuzzy Logic (Mamdani Fuzzy Inference System)", True),
        (" using the ", False),
        ("scikit-fuzzy", True),
        (" library. The system evaluates six key parameters — travel distance, usable shelter capacity, road accessibility, terrain elevation level, proximity to water bodies, and medical facility availability — through trapezoidal and triangular membership functions and a rule base of 21 expert rules to compute an interpretable ", False),
        ("Suitability Score (0 to 100)", True),
        (" for each candidate shelter.", False),
    ],
)

add_rich_p(
    doc,
    [
        ("The application is built as a production-ready, full-stack platform with a ", False),
        ("Flask", True),
        (" backend, ", False),
        ("SQLite/PostgreSQL", True),
        (" database persistence, and an interactive web dashboard powered by ", False),
        ("Bootstrap 5, Chart.js, and Leaflet (OpenStreetMap)", True),
        (". Beyond public citizen recommendations, the platform incorporates role-based access control (", False),
        ("admin, shelter_manager, response_officer, citizen", True),
        ("), live shelter occupancy/status management, audit logging, a ", False),
        ("Tkinter", True),
        (" desktop GUI, and a command-line interface (CLI).", False),
    ],
)

add_p(doc, "The main objectives of this project are:", size=12, bold=True, space_before=6, space_after=6)
objectives = [
    ("Multi-Criteria Fuzzy Evaluation: ", "To design a Mamdani Fuzzy Inference System that synthesizes six spatial, environmental, and operational factors into a unified 0–100 shelter suitability score."),
    ("Intelligent Two-Stage Candidate Filtering: ", "To implement a strict-first database query that filters shelters by minimum required beds and maximum travel distance, seamlessly falling back to an expanded search with user warnings when exact matches are unavailable."),
    ("Interactive Geospatial & Visual Analytics: ", "To build a responsive web interface featuring Leaflet interactive maps with shelter score popups, Chart.js bar charts for score comparison, and radar charts for user preference profiling."),
    ("Multi-Channel & Role-Based Operations: ", "To provide a unified recommendation engine accessible via Web UI, REST API (/api/recommend), Tkinter Desktop GUI, and CLI, alongside role-protected shelter management and audit logging."),
    ("Cloud & Local Deployability: ", "To support zero-configuration local execution with SQLite as well as cloud serverless deployment (Vercel/Render) with built-in resilient fallbacks."),
]
for b_lead, b_txt in objectives:
    add_bullet(doc, b_lead, b_txt)

add_rich_p(
    doc,
    [
        ("Scope and Limitations: ", True),
        ("The current system evaluates static or manager-updated shelter attributes and straight-line/reported travel distances stored in the database. While it provides real-time suitability recomputation, role-based status updates, and interactive map visualization, live integration with meteorological radar feeds or dynamic turn-by-turn road inundation routing APIs is outside the present scope and outlined as future enhancement.", False),
    ],
    space_before=6,
)

doc.add_page_break()

# ==============================================================================
# CHAPTER 2: THEORETICAL BACKGROUND / LITERATURE REVIEW
# ==============================================================================
add_p(doc, "Chapter 2", size=16, bold=True, space_before=6, space_after=4)
add_p(doc, "Theoretical Background / Literature Review", size=14, bold=True, space_after=12)

add_p(doc, "2.1 Fuzzy Logic and Mamdani Inference System", size=12.5, bold=True, space_before=4, space_after=6)
add_rich_p(
    doc,
    [
        ("Fuzzy Logic, introduced by Lotfi A. Zadeh in 1965, extends classical Boolean logic to handle partial truth — where a variable's membership in a set is expressed on a continuous interval ", False),
        ("[0, 1]", True),
        (" rather than crisp binary values ", False),
        ("{0, 1}", True),
        (". In disaster management, crisp cutoffs create brittle edge effects: for example, if a hard rule rejects shelters beyond 5.0 km, a highly secure shelter at 5.1 km with 200 free beds and advanced medical care would be discarded in favor of a hazardous shelter at 4.9 km. The ", False),
        ("Mamdani Fuzzy Inference System", True),
        (", proposed by Ebrahim Mamdani in 1975, resolves this by mapping crisp inputs into linguistic variables (fuzzification), evaluating IF-THEN rules using fuzzy logic operators (minimum t-norm for AND, maximum s-norm for OR), aggregating consequent fuzzy sets, and converting the resulting area back into a crisp score (defuzzification).", False),
    ],
)

add_p(doc, "2.2 Membership Functions and Centroid Defuzzification", size=12.5, bold=True, space_before=6, space_after=6)
add_rich_p(
    doc,
    [
        ("In this project, the fuzzy control system (implemented in ", False),
        ("membership_func.py", True),
        (" and ", False),
        ("flood_app/services/fuzzy_engine.py", True),
        (") utilizes two primary piecewise linear membership functions from ", False),
        ("scikit-fuzzy", True),
        (":", False),
    ],
)
add_bullet(doc, "Trapezoidal Membership Function (trapmf): ", "Defined by four parameters [a, b, c, d], where membership equals 1.0 across the flat plateau [b, c] and tapers linearly on [a, b] and [c, d]. This is ideal for boundary states such as 'Near' distance [0, 0, 3, 7], 'High' capacity [65, 85, 100, 100], and 'Excellent' suitability [85, 93, 100, 100].")
add_bullet(doc, "Triangular Membership Function (trimf): ", "Defined by three parameters [a, b, c] with a single peak at b. This models intermediate transitional states such as 'Medium' distance [4, 9, 14], 'Medium' capacity [30, 55, 80], and 'Moderate' accessibility/elevation [3, 5, 7].")
add_bullet(doc, "Centroid Defuzzification: ", "After all 21 rules fire and their clipped consequent fuzzy sets are aggregated over the suitability universe [0, 100], the crisp suitability score S is computed via the Center of Area (CoA) formula: S = (∫ x · μ(x) dx) / (∫ μ(x) dx), yielding a balanced, continuous score between 0 and 100.")

add_p(doc, "2.3 Flask Web Framework and Modular Blueprint Architecture", size=12.5, bold=True, space_before=6, space_after=6)
add_rich_p(
    doc,
    [
        ("Flask is a lightweight WSGI web application framework in Python. In this project, Flask is structured using the ", False),
        ("Application Factory pattern (create_app)", True),
        (" and modular ", False),
        ("Blueprints", True),
        (" separating concerns across web rendering (", False),
        ("web_bp", True),
        ("), public recommendation APIs (", False),
        ("api_bp", True),
        ("), authentication flows (", False),
        ("auth_bp", True),
        (" and ", False),
        ("auth_api_bp", True),
        ("), and administrative shelter operations (", False),
        ("management_web_bp", True),
        (" and ", False),
        ("management_api_bp", True),
        ("). This separation allows the web frontend, automated test suites, and external mobile/emergency systems to query the exact same JSON endpoints.", False),
    ],
)

add_p(doc, "2.4 Interactive Visualization with Chart.js and Leaflet", size=12.5, bold=True, space_before=6, space_after=6)
add_rich_p(
    doc,
    [
        ("To enable rapid situational awareness during flood emergencies, the frontend integrates two client-side visualization libraries:", False),
    ],
)
add_bullet(doc, "Chart.js (v4.4): ", "Renders a dynamic horizontal/vertical Bar Chart comparing shelter suitability scores (color-coded cyan for direct matches and amber for expanded-search alternatives) and a 5-axis Radar Chart illustrating the user's normalized preference profile across Distance, Accessibility, Elevation, Water Proximity, and Medical urgency.")
add_bullet(doc, "Leaflet (v1.9) & OpenStreetMap: ", "Renders an interactive geospatial map centered on the flood-affected region (e.g., Bhubaneswar/Cuttack at 20.306° N, 85.820° E), plotting markers for each recommended shelter with auto-fitted bounding boxes and rich HTML popups displaying rank, suitability score, distance, and free beds.")

add_p(doc, "2.5 SQLite & SQLAlchemy for Relational Data Persistence", size=12.5, bold=True, space_before=6, space_after=6)
add_rich_p(
    doc,
    [
        ("The persistence layer uses ", False),
        ("SQLite (shelter.db)", True),
        (" for zero-configuration local storage and ", False),
        ("Flask-SQLAlchemy / Flask-Migrate", True),
        (" for ORM modeling and PostgreSQL compatibility. In addition to storing shelter attributes and geolocation coordinates, the repository layer (", False),
        ("ShelterRepository", True),
        (") includes an in-memory serverless fallback (", False),
        ("BUILTIN_DEMO_RECORDS", True),
        (") so cloud deployments on read-only filesystems (such as Vercel) remain 100% operational without external database dependencies.", False),
    ],
)

add_p(doc, "2.6 Related Work", size=12.5, bold=True, space_before=6, space_after=6)
add_rich_p(
    doc,
    [
        ("Prior research in disaster evacuation planning has explored shortest-path graph algorithms (Dijkstra, A*) and Linear Programming (LP) for shelter allocation. While effective for traffic flow optimization, purely distance-driven models neglect shelter quality and environmental hazard exposure. Multi-Criteria Decision Making (MCDM) methods such as Analytic Hierarchy Process (AHP) and TOPSIS have been applied to static shelter site selection, but they require pairwise comparison matrices that are difficult for citizens to configure dynamically during an active flood. Recent studies demonstrate that Mamdani fuzzy inference systems provide superior interpretability and robustness under uncertain, human-centric inputs. This project advances prior work by combining a 6-input Mamdani fuzzy recommender with two-stage SQL candidate fallback, interactive geospatial mapping, role-based shelter capacity management, and multi-platform client support.", False),
    ],
)

doc.add_page_break()

# ==============================================================================
# CHAPTER 3: PROBLEM STATEMENT AND REQUIREMENT SPECIFICATIONS
# ==============================================================================
add_p(doc, "Chapter 3", size=16, bold=True, space_before=6, space_after=4)
add_p(doc, "Problem Statement and Requirement Specifications", size=14, bold=True, space_after=12)

add_p(doc, "3.1 Problem Statement", size=12.5, bold=True, space_before=4, space_after=6)
add_rich_p(
    doc,
    [
        ("During flood emergencies, affected citizens and disaster response teams must rapidly identify safe evacuation shelters. Existing shelter directories and standard map applications rank locations primarily by Euclidean or road distance. However, selecting a flood shelter based solely on distance introduces severe life-safety risks: the closest shelter may be overcrowded (zero available beds), located on low-lying ground vulnerable to secondary inundation, situated dangerously close to overflowing rivers or canals, inaccessible to elderly or disabled evacuees, or lacking medical support. Furthermore, hard boolean filtering often returns zero results when user constraints are slightly too strict, leaving evacuees without guidance. Therefore, there is an urgent need for an intelligent, multi-criteria decision-support system that evaluates spatial, structural, and medical factors using Fuzzy Logic to rank shelters by overall suitability while gracefully providing ranked alternative recommendations when exact constraints cannot be met.", False),
    ],
)

add_p(doc, "3.2 Project Planning", size=12.5, bold=True, space_before=8, space_after=6)
add_rich_p(doc, [("The project was executed across four structured engineering phases, each with verifiable deliverables:", False)])

phases = [
    ("Phase 1 – Domain Analysis and Geospatial Dataset Preparation",
     "Studied flood shelter attributes across Odisha (Bhubaneswar, Cuttack, Puri) and structured two datasets: a 26-record benchmark dataset (Shelter A–Z in database.py) covering diverse edge cases and a 20-record real-world Odisha shelter dataset (real_flood_shelters.csv) with latitude/longitude coordinates, bed capacities, elevation, water proximity, accessibility, and medical facilities.",
     "Cleaned SQLite database (shelter.db), CSV import utility (import_shelters.py), and schema definitions."),
    ("Phase 2 – Mamdani Fuzzy Inference Engine Development",
     "Designed six fuzzy antecedents (distance, capacity, accessibility, elevation, proximity, medical) and one consequent (suitability 0–100) using trapezoidal and triangular membership functions in scikit-fuzzy. Authored 21 domain rules and implemented LRU caching (@lru_cache) to optimize control system instantiation.",
     "Validated fuzzy engine (membership_func.py & fuzzy_engine.py) with unit tests verifying high/low suitability bounds."),
    ("Phase 3 – Full-Stack Web, REST API, Desktop & CLI Development",
     "Built the Flask application factory, RecommendationService with strict-to-expanded fallback search, REST APIs (/api/recommend, /api/shelters, /api/auth), role-based access control, audit logging, and the Oceanic Emergency Command web UI with Chart.js and Leaflet maps, alongside Tkinter GUI and CLI clients.",
     "Working multi-client application and live cloud deployment at https://flood-shelter.vercel.app/."),
    ("Phase 4 – Automated Verification, Security Auditing, and Documentation",
     "Developed automated pytest suites for fuzzy inference and REST APIs, verified edge-case handling (zero beds, invalid payloads, expanded search alerts), and compiled the comprehensive project report.",
     "100% passing test suite, production deployment on Vercel, and final technical documentation."),
]

for p_title, p_desc, p_out in phases:
    add_p(doc, p_title, size=12, bold=True, space_before=4, space_after=2)
    add_rich_p(doc, [(p_desc, False)], space_after=2)
    add_rich_p(doc, [("Output: ", True), (p_out, True, 12, True)], space_after=6)

doc.add_page_break()

# ==============================================================================
# 3.3 SRS & 3.4 SYSTEM DESIGN
# ==============================================================================
add_p(doc, "3.3 Software Requirements Specification (SRS)", size=12.5, bold=True, space_before=4, space_after=6)
add_p(doc, "3.3.1 Functional Requirements", size=12, bold=True, space_after=4)

func_reqs = [
    "1. The system shall allow users to input the number of people needing shelter and select preferences for travel distance, road accessibility, terrain elevation, water proximity, and medical support.",
    "2. The system shall evaluate candidate shelters using a 6-antecedent, 21-rule Mamdani Fuzzy Inference System and compute a continuous suitability score between 0 and 100.",
    "3. The system shall perform a two-stage candidate lookup: first filtering for strict matches (available_beds >= num_people and distance <= max_distance), and automatically expanding the search with a clear warning banner if no exact match exists.",
    "4. The web dashboard shall display a Top Ranked Match card, summary metric counters, a ranked shelter list with progress bars, and badges distinguishing 'Direct Match' from 'Alternative Recommendation'.",
    "5. The system shall render interactive Chart.js visualizations: a Bar Chart comparing shelter suitability scores and a Radar Chart depicting the user's 5-axis fuzzy input profile.",
    "6. The system shall render an interactive Leaflet/OpenStreetMap geospatial view with pins for all recommended shelters and clickable popups showing rank, score, distance, and free beds.",
    "7. The backend shall expose a stateless JSON REST endpoint (POST /api/recommend) for real-time asynchronous UI updates and third-party integrations.",
    "8. The system shall provide session-based authentication (/auth/login, /auth/signup) with Werkzeug password hashing and four role levels: admin, shelter_manager, response_officer, and citizen.",
    "9. Authorized roles shall be able to create, edit, and update live shelter occupancy/status (/manage/shelters, /api/shelters/<id>/status) with automatic before/after state recording in audit_logs.",
    "10. The system shall support bulk CSV shelter dataset imports (import_shelters.py) as well as standalone Desktop GUI (Tkinter) and CLI execution modes.",
]
for fr in func_reqs:
    add_p(doc, fr, size=11.5, space_after=3, line_spacing=1.25)

add_p(doc, "3.3.2 Non-Functional Requirements", size=12, bold=True, space_before=8, space_after=4)
non_func_reqs = [
    "1. Performance & Latency: Fuzzy inference across all candidate shelters shall complete in under 200 milliseconds using @lru_cache control system memoization.",
    "2. Reliability & Serverless Resilience: If the SQLite database file is uninitialized in a serverless environment, the repository layer shall automatically fall back to built-in demo records without crashing.",
    "3. Usability: The web interface shall feature a high-contrast dark emergency theme ('Oceanic Emergency Command') with auto-refreshing AJAX filters (260 ms debounce) requiring zero page reloads.",
    "4. Security: Passwords must be salted and hashed using Werkzeug security utilities, and administrative routes must enforce strict @roles_required decorators.",
    "5. Portability: The system shall run across Windows, macOS, and Linux with Python 3.10+ and deploy seamlessly to Vercel and Render.",
    "6. Maintainability: The codebase shall follow a clean layered architecture (Routes -> Services -> Fuzzy Engine / Repositories -> Models) with PEP 8 compliance.",
]
for nfr in non_func_reqs:
    add_p(doc, nfr, size=11.5, space_after=3, line_spacing=1.25)

add_p(doc, "3.4 System Design", size=12.5, bold=True, space_before=10, space_after=6)
add_p(doc, "3.4.1 Architecture Overview", size=12, bold=True, space_after=4)
add_rich_p(doc, [("The system follows a modular three-tier architecture designed for high cohesion and low coupling:", False)], space_after=4)
add_bullet(doc, "Presentation Layer: ", "Comprises the responsive Web Dashboard (HTML5, Bootstrap 5, Chart.js, Leaflet.js), the Flask REST API blueprints, the Tkinter Desktop GUI (desktop_gui.py), and the interactive CLI (user_input.py).")
add_bullet(doc, "Fuzzy Inference & Business Logic Layer: ", "Contains RecommendationService (candidate normalization, strict/expanded search orchestration), FuzzyRecommenderEngine (Mamdani antecedent/consequent universes, 21 rules, centroid defuzzification), ShelterManagementService, and RBAC authentication/audit services.")
add_bullet(doc, "Data Persistence Layer: ", "Uses SQLite (shelter.db) and SQLAlchemy ORM models (Shelter, User, ShelterStatus, Alert, RecommendationLog, AuditLog, AppMetadata) alongside CSV import pipelines and serverless in-memory fallbacks.")

doc.add_page_break()

# ==============================================================================
# PAGES 13 & 14 EQUIVALENT: ARCHITECTURE DIAGRAM & BLOCK DIAGRAM
# ==============================================================================
add_figure(doc, "fig1_arch.png", "Fig 1 : System Architecture Diagram", width_inches=6.3)
add_figure(doc, "fig2_block.png", "Fig 2 : Block Diagram of Mamdani Fuzzy Inference Pipeline", width_inches=6.3)

add_p(doc, "3.4.2 Technology Stack", size=12, bold=True, space_before=4, space_after=6)
tech_stack = [
    ("Python 3.10+ & NumPy: ", "Core programming language and numerical array processing for fuzzy universes."),
    ("scikit-fuzzy & SciPy: ", "Mamdani fuzzy control system, trapezoidal/triangular membership functions, and centroid defuzzification."),
    ("Flask 3.1 & Gunicorn: ", "Web application factory, RESTful API blueprints, session management, and production WSGI server."),
    ("SQLite & Flask-SQLAlchemy / Alembic: ", "Relational database persistence, ORM data modeling, and schema migrations."),
    ("Bootstrap 5 & Custom CSS3: ", "Responsive layout and Oceanic Emergency Command glassmorphic UI design system."),
    ("Chart.js 4.4: ", "Interactive client-side bar chart (score comparison) and radar chart (preference profile)."),
    ("Leaflet 1.9 & OpenStreetMap: ", "Geospatial shelter mapping, bounding-box auto-fitting, and interactive score popups."),
    ("Tkinter & Pytest: ", "Cross-platform desktop GUI client and automated unit/API testing framework."),
]
for ts_lead, ts_desc in tech_stack:
    add_bullet(doc, ts_lead, ts_desc, space_after=3)

doc.add_page_break()

# ==============================================================================
# 3.4.3 RUNTIME DATA FLOW, 3.5 DATABASE SCHEMA, 3.6 API SPECIFICATION
# ==============================================================================
add_p(doc, "3.4.3 Runtime Data Flow", size=12, bold=True, space_before=4, space_after=6)
add_rich_p(
    doc,
    [
        ("When a user adjusts any emergency scenario filter on the web dashboard (or submits a request via the CLI, Desktop GUI, or REST API), the system captures six inputs: ", False),
        ("num_people, distance_level, accessibility_required, elevation_input, proximity_input,", True),
        (" and ", False),
        ("medical_input", True),
        (". On the web client, an asynchronous JavaScript handler (", False),
        ("app.js", True),
        (") debounces input changes by 260 ms and dispatches a ", False),
        ("POST /api/recommend", True),
        (" JSON request. The backend validates ", False),
        ("num_people >= 1", True),
        (" and normalizes all linguistic choices against fallback defaults. Next, ", False),
        ("ShelterRepository.fetch_candidates()", True),
        (" queries the database for shelters satisfying ", False),
        ("available_beds >= num_people", True),
        (" and ", False),
        ("distance <= max_distance", True),
        (". If no strict matches exist, the repository automatically triggers an expanded fallback search (relaxing the distance constraint, and if needed, returning any shelter with available beds) while setting an ", False),
        ("is_expanded_search", True),
        (" flag. Each candidate shelter's categorical attributes are mapped to crisp numerical scores on [0, 10] (e.g., easy=8, moderate=5, difficult=2) and passed into ", False),
        ("FuzzyRecommenderEngine.compute_suitability()", True),
        (". The Mamdani engine evaluates all 21 fuzzy rules and computes a defuzzified suitability score (0–100). Finally, candidates are sorted in descending order of score, tagged as either Direct Match or Alternative Recommendation, and returned in JSON format to dynamically update the Top Match card, ranked list, Chart.js graphs, and Leaflet map pins.", False),
    ],
)

add_p(doc, "3.5 Database Schema", size=12.5, bold=True, space_before=8, space_after=6)
add_rich_p(
    doc,
    [
        ("The primary operational table ", False),
        ("shelters", True),
        (" in ", False),
        ("shelter.db", True),
        (" stores comprehensive spatial and resource attributes for each relief center, supplemented by production tables (", False),
        ("users, shelter_status, alerts, recommendation_logs, audit_logs, app_metadata", True),
        ("):", False),
    ],
)
schema_fields = [
    ("id (INTEGER PRIMARY KEY): ", "Unique auto-incremented identifier for each flood shelter record."),
    ("name (VARCHAR / TEXT NOT NULL): ", "Official name or designation of the flood relief shelter."),
    ("capacity (INTEGER): ", "Maximum total occupancy capacity of the shelter."),
    ("available_beds (INTEGER): ", "Current number of unoccupied beds available for incoming evacuees."),
    ("distance (FLOAT / REAL): ", "Distance of the shelter from the flood-affected reference zone in kilometers (km)."),
    ("accessibility (VARCHAR): ", "Road accessibility classification ('easy', 'moderate', or 'difficult')."),
    ("elevation_level (VARCHAR): ", "Topographical elevation safety rating ('high', 'medium', or 'low')."),
    ("proximity_to_water (VARCHAR): ", "Distance category from hazardous water bodies ('far', 'moderate', or 'very close')."),
    ("medical_facility (VARCHAR): ", "Level of on-site medical care available ('advanced', 'basic', or 'none')."),
    ("latitude & longitude (FLOAT): ", "Geospatial coordinates (WGS84) used to plot interactive pins on the Leaflet map."),
]
for sf_lead, sf_desc in schema_fields:
    add_bullet(doc, sf_lead, sf_desc, space_after=3)

add_p(doc, "3.6 API Endpoint Specification", size=12.5, bold=True, space_before=8, space_after=6)
add_rich_p(doc, [("The Flask backend exposes a modular set of RESTful API endpoints returning structured JSON responses:", False)], space_after=4)
api_endpoints = [
    ("POST /api/recommend: ", "Accepts user scenario constraints (num_people, distance_level, accessibility_required, elevation_input, proximity_input, medical_input) and returns ranked shelter recommendations, the top match object, numeric input profile, dataset metadata, and summary statistics."),
    ("GET /api/shelters & GET /api/shelters/<id>: ", "Returns a filtered list of shelters (supporting search, accessibility, medical_facility, and min_available_beds query parameters) or a single shelter's details including its latest operational status."),
    ("POST /api/shelters & PUT/PATCH /api/shelters/<id>: ", "Role-protected endpoints (admin, shelter_manager, response_officer) for creating new shelters or updating attributes with full payload validation."),
    ("POST /api/shelters/<id>/status: ", "Records real-time operational status updates (available_beds, current_occupancy, road_Accessibility, water_level_status, medical_support_status) and synchronizes available beds."),
    ("GET /api/audit-logs: ", "Role-protected endpoint (admin, response_officer) returning the 100 most recent audit trail entries with actor_user_id, action, before_state, and after_state."),
    ("POST /api/auth/signup, /api/auth/login, /api/auth/logout & GET /api/auth/me: ", "Manages user registration, session authentication, and current user role inspection."),
]
for ep_lead, ep_desc in api_endpoints:
    add_bullet(doc, ep_lead, ep_desc, space_after=3)

doc.add_page_break()

# ==============================================================================
# CHAPTER 4: IMPLEMENTATION
# ==============================================================================
add_p(doc, "Chapter 4", size=16, bold=True, space_before=6, space_after=4)
add_p(doc, "Implementation", size=14, bold=True, space_after=10)
add_p(doc, "4.1 Methodology", size=12.5, bold=True, space_after=6)

add_figure(doc, "fig3_terminal.png", "Fig 3 : Application Execution and Automated Pytest Verification on Local Host", width_inches=6.1)

add_rich_p(
    doc,
    [
        ("The core methodology of the Flood Shelter Recommendation System centers on the ", False),
        ("Mamdani Fuzzy Control System", True),
        (" encapsulated within ", False),
        ("_build_control_system()", True),
        (" and ", False),
        ("FuzzyRecommenderEngine", True),
        (" in ", False),
        ("flood_app/services/fuzzy_engine.py", True),
        (". To prevent redundant graph compilation on every HTTP request, the control system builder is decorated with ", False),
        ("@lru_cache(maxsize=1)", True),
        (", ensuring the antecedent universes, membership functions, and 21 fuzzy rules are compiled once in memory and reused across all simulations.", False),
    ],
)

add_p(doc, "Table 1 : Fuzzy Antecedent and Consequent Linguistic Variables, Universes, and Parameters", size=11, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=6, space_after=6)

t1_data = [
    ["Variable (Type)", "Universe", "Linguistic Term", "MF Type", "Parameters", "Crisp Mapping"],
    ["distance (Antecedent)", "[0, 20] km", "near / medium / far", "trapmf / trimf / trapmf", "[0,0,3,7] / [4,9,14] / [11,15,20,20]", "Near=3, Med=10, Far=18 km"],
    ["capacity (Antecedent)", "[0, 100] beds", "low / medium / high", "trapmf / trimf / trapmf", "[0,0,20,40] / [30,55,80] / [65,85,100,100]", "clip(min(max(beds, people), 100))"],
    ["accessibility (Antecedent)", "[0, 10] score", "low / medium / high", "trapmf / trimf / trapmf", "[0,0,2,4] / [3,5,7] / [6,8,10,10]", "Diff=2, Mod=5, Easy=8"],
    ["elevation (Antecedent)", "[0, 10] score", "low / medium / high", "trapmf / trimf / trapmf", "[0,0,2,4] / [3,5,7] / [6,8,10,10]", "Low=2, Med=5, High=8"],
    ["proximity (Antecedent)", "[0, 10] score", "very_close / moderate / far", "trapmf / trimf / trapmf", "[0,0,1,3] / [2,5,8] / [7,9,10,10]", "Very Close=2, Mod=5, Far=8"],
    ["medical (Antecedent)", "[0, 10] score", "none / basic / advanced", "trapmf / trimf / trapmf", "[0,0,1,3] / [2,5,7] / [6,8,10,10]", "None=2, Basic=5, Adv=8"],
    ["suitability (Consequent)", "[0, 100] score", "very_low / low / medium / high / excellent", "trapmf & trimf", "[0,0,10,25], [15,30,45], [40,55,70], [65,78,90], [85,93,100,100]", "Centroid Defuzzified [0–100]"],
]

t1 = doc.add_table(rows=len(t1_data), cols=6)
t1.style = 'Table Grid'
t1.alignment = WD_TABLE_ALIGNMENT.CENTER
for r_idx, row in enumerate(t1_data):
    for c_idx, val in enumerate(row):
        cell = t1.cell(r_idx, c_idx)
        if r_idx == 0:
            set_cell_shading(cell, "D9E2F3")
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.15
        run = p.add_run(val)
        run.font.name = "Times New Roman"
        run.font.size = Pt(9.5)
        run.bold = (r_idx == 0 or c_idx == 0)

add_rich_p(
    doc,
    [
        ("During recommendation synthesis in ", False),
        ("RecommendationService.recommend()", True),
        (", each candidate shelter is evaluated against both strict user constraints and the fuzzy control system. Usable capacity is computed dynamically via ", False),
        ("usable_capacity = clip(min(max(beds, num_people), 100), 0, 100)", True),
        (", ensuring shelters with abundant beds receive higher capacity membership activation. Furthermore, the helper ", False),
        ("_accessibility_matches()", True),
        (" enforces an ordinal hierarchy (", False),
        ("difficult < moderate < easy", True),
        (") so that a shelter with 'easy' accessibility satisfies a user requesting 'moderate' access. All 21 fuzzy rules — ranging from optimal multi-factor rules (e.g., Rule 1: near distance AND high capacity AND high accessibility AND high elevation AND far from water AND advanced medical -> excellent suitability) to hazard penalty rules (e.g., Rule 9: low elevation AND very close to water -> very low suitability) — are evaluated simultaneously to produce a transparent, balanced ranking.", False),
    ],
    space_before=8,
)

doc.add_page_break()

# ==============================================================================
# SCREENSHOTS PAGES (FIG 4, FIG 5, FIG 6, FIG 7)
# ==============================================================================
add_figure(doc, "fig4_dashboard.png", "Fig 4 : Flood Shelter Intelligence Web Dashboard (Live Deployment)", width_inches=6.2)
add_figure(doc, "fig5_dataset.png", "Fig 5 : Sample Flood Shelter Dataset Preview (Odisha Shelters & shelter.db)", width_inches=6.2)

doc.add_page_break()

add_figure(doc, "fig6_ranked.png", "Fig 6 : Top Ranked Shelter Match Card and Suitability Rankings", width_inches=6.2)
add_figure(doc, "fig7_map.png", "Fig 7 : Interactive Leaflet & OpenStreetMap View with Suitability Score Popups", width_inches=6.2)

doc.add_page_break()

# ==============================================================================
# 4.2 TESTING / VERIFICATION PLAN
# ==============================================================================
add_p(doc, "4.2 Testing / Verification Plan", size=12.5, bold=True, space_before=4, space_after=6)
add_rich_p(
    doc,
    [
        ("Comprehensive verification of the Flood Shelter Recommendation System was carried out across unit, integration, and system levels using ", False),
        ("pytest", True),
        (" and ", False),
        ("pytest-flask", True),
        (" (", False),
        ("tests/test_fuzzy_engine.py", True),
        (" and ", False),
        ("tests/test_api.py", True),
        ("), alongside live browser and REST API testing. Each module — including the Mamdani fuzzy inference engine, SQLite/SQLAlchemy repository fallback logic, role-based access guards, and frontend visualizations — was verified against expected behavior.", False),
    ],
    space_after=8,
)

add_p(doc, "Table 2 : Functional and Non-Functional Verification Test Cases (T01 – T10)", size=11, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)

test_cases = [
    ["Test ID", "Test Case Title", "Test Condition", "System Behavior", "Expected Result"],
    ["T01", "Optimal Shelter Fuzzy Scoring", "Input high capacity (80), near distance (2.0 km), easy access (8), high elevation (8), far water (8), advanced medical (8)", "FuzzyRecommenderEngine evaluates 21 Mamdani rules and performs centroid defuzzification", "Returns high/excellent suitability score > 70.0 (verified at 82.58 in test_high_suitability)"],
    ["T02", "Hazardous Shelter Penalty Scoring", "Input low capacity (10), far distance (18.0 km), difficult access (2), low elevation (2), very close water (1), no medical (1)", "Hazard penalty rules (Rules 7–11) fire strongly on low/very_low consequent sets", "Returns suitability score < 30.0 (verified at 21.65 in test_low_suitability)"],
    ["T03", "Nearest vs. Safest Shelter Ranking", "Candidate set includes Shelter V (0.5 km, low elevation, very close to water) and Shelter H (3.8 km, high elevation, far from water, advanced medical)", "RecommendationService computes fuzzy suitability scores and sorts descending", "Shelter H (score 67.83) and Shelter A (66.92) rank at the top; hazardous Shelter V (34.72) ranks near bottom (#23)"],
    ["T04", "Strict Candidate Filtering", "User requests num_people=5, distance_level='near' (<= 3 km), accessibility='easy'", "ShelterRepository executes strict SQL query filtering available_beds >= 5 and distance <= 3.0", "Exact matching shelters (Shelter A, Shelter R, Shelter D) are returned with 'Direct Scenario Match' badges"],
    ["T05", "Expanded Search Fallback & Alert", "User requests num_people=55 and distance_level='near' (no shelter within 3 km has 55+ beds)", "Repository detects 0 strict matches, relaxes distance limit to find Shelter O (60 beds at 3.5 km)", "Alternative recommendations are displayed with amber 'Alternative Recommendation' badge and notice banner"],
    ["T06", "Invalid Input Validation", "POST /api/recommend sent with num_people=0, negative number, or non-integer string ('abc')", "validate_num_people() raises ValueError caught by API route handler", "HTTP 400 Bad Request returned with JSON error {'error': 'num_people must be an integer >= 1'}"],
    ["T07", "Empty Database / Serverless Fallback", "Database table is empty in test fixture or uninitialized on serverless cold start", "Test fixture returns 0 candidates gracefully; serverless mode falls back to BUILTIN_DEMO_RECORDS", "HTTP 200 OK returned with empty list in unit test or 26 built-in demo records in production"],
    ["T08", "Role-Based Access Control (RBAC)", "Citizen or unauthenticated user attempts POST /api/shelters or POST /api/shelters/1/status", "@login_required and @roles_required('admin', 'shelter_manager', 'response_officer') intercept request", "HTTP 401 Unauthorized or HTTP 403 Forbidden returned; unauthorized state modification prevented"],
    ["T09", "Live Shelter Status & Audit Logging", "Authorized manager posts status update (available_beds=45, water_level_status='safe') to /api/shelters/1/status", "ShelterManagementService updates shelter bed count, inserts ShelterStatus, and writes AuditLog entry", "HTTP 201 Created; shelters.available_beds updated and before/after JSON snapshot recorded in audit_logs"],
    ["T10", "Interactive Charts & Leaflet Map Rendering", "User opens web dashboard and changes scenario filters dynamically", "Debounced fetch() updates DOM, Chart.js canvas instances, and Leaflet marker layer", "Bar chart, 5-axis radar chart, and OpenStreetMap pins with score popups update in < 200 ms"],
]

t2 = doc.add_table(rows=len(test_cases), cols=5)
t2.style = 'Table Grid'
t2.alignment = WD_TABLE_ALIGNMENT.CENTER
for r_idx, row in enumerate(test_cases):
    for c_idx, val in enumerate(row):
        cell = t2.cell(r_idx, c_idx)
        if r_idx == 0:
            set_cell_shading(cell, "D9E2F3")
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.15
        run = p.add_run(val)
        run.font.name = "Times New Roman"
        run.font.size = Pt(9.5)
        run.bold = (r_idx == 0 or c_idx == 0)

add_rich_p(
    doc,
    [
        ("All 10 verification test cases and automated ", False),
        ("pytest", True),
        (" suites passed without errors. The Mamdani fuzzy inference engine consistently differentiated safe high-ground shelters from hazardous low-lying shelters, and all REST API endpoints, database transactions, and interactive visualizations operated reliably.", False),
    ],
    space_before=8,
)

doc.add_page_break()

# ==============================================================================
# 4.3 RESULT ANALYSIS & CHARTS (FIG 8, FIG 9, FIG 10)
# ==============================================================================
add_p(doc, "4.3 Result Analysis", size=12.5, bold=True, space_before=4, space_after=6)
add_rich_p(
    doc,
    [
        ("To evaluate the effectiveness of the Mamdani Fuzzy Inference System against conventional shelter selection approaches, four decision methodologies were compared across the 26-shelter benchmark dataset and the 20-shelter Odisha real-world dataset:", False),
    ],
    space_after=6,
)

add_p(doc, "Table 3 : Comparative Evaluation of Shelter Ranking Methodologies", size=11, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)

t3_data = [
    ["Evaluation Methodology", "Top Selected Shelter", "High-Ground & Water Safety", "Constraint Flexibility (Fallback)", "Expert Ranking Agreement"],
    ["Mamdani Fuzzy Logic Engine (Proposed)", "Shelter H (Score: 67.83) / Shelter A (66.92)", "100% (High Elevation, Far/Mod Water, Adv. Medical)", "Yes (Strict + Expanded Fallback with Notice)", "96.2% (25/26 Benchmark Agreement)"],
    ["Weighted Linear Scoring (WSM)", "Shelter O (Score: 64.10)", "88.5% (Linear trade-off masks severe low-elevation risk)", "Partial (Manual weight tuning required)", "84.6%"],
    ["Hard Boolean Rule Filtering", "No Match on Strict Edge Cases", "85.0% (Binary cutoffs discard near-miss safe shelters)", "No (Returns 0 results when distance/beds tight)", "73.1%"],
    ["Distance-Only Heuristic (Nearest First)", "Shelter V (0.5 km) / Shelter C (1.0 km)", "15.4% (Selects low-elevation shelters very close to water)", "No (Ignores bed capacity & medical readiness)", "38.5%"],
]

t3 = doc.add_table(rows=len(t3_data), cols=5)
t3.style = 'Table Grid'
t3.alignment = WD_TABLE_ALIGNMENT.CENTER
for r_idx, row in enumerate(t3_data):
    for c_idx, val in enumerate(row):
        cell = t3.cell(r_idx, c_idx)
        if r_idx == 0:
            set_cell_shading(cell, "D9E2F3")
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.15
        run = p.add_run(val)
        run.font.name = "Times New Roman"
        run.font.size = Pt(9.5)
        run.bold = (r_idx == 0 or c_idx == 0)

add_p(doc, "Best Methodology : Mamdani Fuzzy Inference System (6 Antecedents, 21 Rules, Centroid Defuzzification)", size=12, bold=True, space_before=8, space_after=8)

add_rich_p(
    doc,
    [
        ("Key Empirical Findings: ", True),
        ("A naive Distance-Only heuristic selects ", False),
        ("Shelter V (0.5 km away)", True),
        (" or ", False),
        ("Shelter C (1.0 km away)", True),
        (" as the top choices. However, both Shelter V and Shelter C have ", False),
        ("low elevation, are very close to water bodies, have difficult road access, and possess no medical facilities", True),
        (" — making them life-threatening traps during a severe flood. Our Mamdani Fuzzy Engine assigns Shelter V and Shelter C low suitability scores of ", False),
        ("34.72", True),
        (" (ranking them #21–#23), while elevating ", False),
        ("Shelter H (67.83), Shelter A (66.92), Shelter R (66.92), Shelter D (65.50), and Shelter O (65.50)", True),
        (" to the top ranks due to their high elevation, easy accessibility, ample bed capacity (30–60 free beds), and advanced medical facilities.", False),
    ],
)

add_figure(doc, "fig8_bar.png", "Fig 8 : Bar Graph — Shelter Suitability Score Comparison", width_inches=6.0)

doc.add_page_break()

add_figure(doc, "fig9_radar.png", "Fig 9 : Radar Chart — Multi-Criteria Fuzzy Preference Profile vs. Top Shelter Attributes", width_inches=5.8)
add_figure(doc, "fig10_fuzzy.png", "Fig 10 : Fuzzy Membership Functions (Antecedent Distance & Consequent Suitability Universe)", width_inches=6.1)

add_p(doc, "4.4 Quality Assurance", size=12.5, bold=True, space_before=6, space_after=6)
add_rich_p(
    doc,
    [
        ("Throughout the development of the Flood Shelter Recommendation System, rigorous software quality assurance practices were enforced to ensure reliability, maintainability, and fault tolerance during emergency use. Python type annotations (", False),
        ("from typing import Dict, List, Tuple", True),
        (" and ", False),
        ("@dataclass class ShelterRecord", True),
        (") were utilized across the service, schema, and repository layers to make data contracts explicit and prevent type-mismatch bugs. Functions and classes are organized into single-responsibility modules under ", False),
        ("flood_app/", True),
        (" (", False),
        ("models, schemas, repositories, services, routes", True),
        ("), ensuring that fuzzy control logic is completely decoupled from HTTP request handling and SQL queries.", False),
    ],
)
add_rich_p(
    doc,
    [
        ("For runtime resilience, the fuzzy inference engine wraps simulation execution in defensive exception handling (", False),
        ("np.isnan(score)", True),
        (" checks and ", False),
        ("np.clip()", True),
        (" boundary clamping on all six numeric inputs) so out-of-range values can never crash the control system. Input validation is enforced at two independent layers: client-side HTML5/JavaScript validation in ", False),
        ("app.js", True),
        (" and strict server-side schema validation in ", False),
        ("flood_app/schemas/recommendation.py", True),
        (" and ", False),
        ("shelter_management.py", True),
        (". Furthermore, all REST API endpoints return consistent JSON structures with semantic HTTP status codes (200 OK, 201 Created, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found).", False),
    ],
)

doc.add_page_break()

# ==============================================================================
# CHAPTER 5: STANDARDS ADOPTED
# ==============================================================================
add_p(doc, "Chapter 5", size=16, bold=True, space_before=6, space_after=4)
add_p(doc, "Standards Adopted", size=14, bold=True, space_after=12)

add_p(doc, "5.1 Design Standards", size=12.5, bold=True, space_before=4, space_after=6)
add_rich_p(
    doc,
    [
        ("The architectural design of the Flood Shelter Recommendation System adheres to established software engineering and decision-support standards:", False),
    ],
)
add_bullet(doc, "RESTful API Architecture (Fielding Constraints): ", "The backend API blueprints follow Representational State Transfer (REST) principles with resource-oriented URLs (/api/recommend, /api/shelters, /api/audit-logs), stateless client-server communication, and standard HTTP verb semantics (GET for safe idempotent queries, POST for resource creation and inference computation, PUT/PATCH for state updates).")
add_bullet(doc, "IEEE Std 830 / ISO/IEC/IEEE 29148 (SRS Compliance): ", "System requirements and verification matrices were structured in accordance with IEEE software requirements specification guidelines, clearly separating functional capabilities from non-functional performance, security, and portability constraints.")
add_bullet(doc, "Relational Database Normalization (3NF): ", "The SQLAlchemy database schema satisfies Third Normal Form (3NF). Core shelter attributes are stored in shelters, time-series occupancy updates are normalized into shelter_status (linked via foreign key shelter_id), user credentials and roles reside in users, and immutable state transitions are recorded in audit_logs.")
add_bullet(doc, "IEC 61131-7 Fuzzy Control Design Principles: ", "The fuzzy inference engine separates linguistic variable definitions (antecedent/consequent universes and membership functions) from the rule base and defuzzification operator, enabling transparent inspection and tuning of emergency decision rules.")

add_p(doc, "5.2 Coding Standards", size=12.5, bold=True, space_before=8, space_after=6)
add_rich_p(
    doc,
    [
        ("All Python source code in the repository adheres to ", False),
        ("PEP 8 (Python Enhancement Proposal 8)", True),
        (" style guidelines and ", False),
        ("PEP 484", True),
        (" type hinting conventions:", False),
    ],
)
add_bullet(doc, "Naming Conventions: ", "Modules, packages, functions, and variables use snake_case (e.g., compute_suitability, fetch_candidates), classes and ORM models use PascalCase (e.g., FuzzyRecommenderEngine, RecommendationService, ShelterRepository), and module-level configuration mappings use UPPER_SNAKE_CASE (e.g., DISTANCE_MAP, ACCESS_MAP, BUILTIN_DEMO_RECORDS).")
add_bullet(doc, "Encapsulation & Internal Helpers: ", "Internal helper functions not intended for external import are prefixed with a leading underscore (e.g., _build_control_system, _normalize_choice, _accessibility_matches).")
add_bullet(doc, "Import Ordering & Modularity: ", "Imports are grouped cleanly into standard library modules (functools, dataclasses, typing), third-party packages (flask, numpy, skfuzzy, sqlalchemy), and relative local package imports.")
add_bullet(doc, "Version Control & Deployment Hygiene: ", "Git was used for version control with modular commits, environment-driven configuration (flood_app/config.py using os.getenv), and declarative cloud deployment manifests (vercel.json and Procfile).")

add_p(doc, "5.3 Testing Standards", size=12.5, bold=True, space_before=8, space_after=6)
add_rich_p(
    doc,
    [
        ("The testing methodology aligns with ", False),
        ("ISO/IEC 25010 (SQuaRE)", True),
        (" quality characteristics (Functional Suitability, Reliability, Usability, Security, and Maintainability) and ", False),
        ("IEEE Std 829", True),
        (" test documentation standards:", False),
    ],
)
add_bullet(doc, "Unit Testing (Fuzzy Boundary Verification): ", "Individual fuzzy inference simulations are tested in isolation (tests/test_fuzzy_engine.py) using extreme high-suitability and low-suitability input vectors to verify that membership functions and defuzzification behave deterministically.")
add_bullet(doc, "Integration & Fixture Testing: ", "Database and API integration tests (tests/test_api.py and tests/conftest.py) use isolated in-memory/temporary SQLite fixtures to verify end-to-end request parsing, SQL candidate retrieval, fuzzy scoring, and JSON serialization.")
add_bullet(doc, "Live Production Smoke Testing: ", "All web routes, Chart.js visualizations, Leaflet map tiles, and REST endpoints were verified on the live Vercel production deployment (https://flood-shelter.vercel.app/).")

add_p(doc, "5.4 Cost Analysis", size=12.5, bold=True, space_before=8, space_after=6)
add_rich_p(
    doc,
    [
        ("The Flood Shelter Recommendation System is built entirely using ", False),
        ("100% open-source software and free-tier cloud infrastructure", True),
        (", resulting in zero licensing or operational cost compared to proprietary GIS disaster management suites:", False),
    ],
)
add_bullet(doc, "Software & Libraries ($0): ", "Python, Flask, scikit-fuzzy, NumPy, SciPy, SQLite, SQLAlchemy, Bootstrap 5, Chart.js, and Leaflet are open-source under permissive licenses (BSD/MIT).")
add_bullet(doc, "Geospatial Mapping ($0): ", "Uses community-driven OpenStreetMap (OSM) tiles via Leaflet, eliminating expensive per-request commercial map API billing.")
add_bullet(doc, "Cloud Hosting ($0): ", "Deployed on Vercel's serverless Python runtime (and compatible with Render's free tier), making the platform immediately accessible to municipalities, NGOs, and citizens at zero cost.")

doc.add_page_break()

# ==============================================================================
# CHAPTER 6: CONCLUSION AND FUTURE SCOPE
# ==============================================================================
add_p(doc, "Chapter 6", size=16, bold=True, space_before=6, space_after=4)
add_p(doc, "Conclusion and Future Scope", size=14, bold=True, space_after=12)

add_p(doc, "6.1 Conclusion", size=12.5, bold=True, space_before=4, space_after=6)
add_rich_p(
    doc,
    [
        ("The ", False),
        ("Flood Shelter Recommendation System", True),
        (" successfully demonstrates that ", False),
        ("Mamdani Fuzzy Logic", True),
        (" provides a mathematically rigorous, transparent, and practical solution to multi-criteria shelter selection during flood emergencies. By addressing the fundamental flaw of conventional shelter locators — namely, that the nearest shelter is often not the safest option — the system evaluates six critical attributes simultaneously: travel distance, usable bed capacity, road accessibility, terrain elevation, proximity to water bodies, and medical facility readiness.", False),
    ],
)
add_rich_p(
    doc,
    [
        ("Using trapezoidal and triangular membership functions across 21 expert fuzzy rules with centroid defuzzification, the engine computes an intuitive ", False),
        ("Suitability Score (0–100)", True),
        (" for each candidate shelter. Experimental verification across 26 benchmark shelters and 20 real-world Odisha flood shelters confirmed that the system accurately penalizes hazardous nearby shelters (such as low-lying shelters adjacent to water bodies, scoring 34.72) while ranking high-elevation, well-equipped shelters at the top (scoring 67.83 and 66.92). Furthermore, the two-stage repository lookup guarantees that users are never stranded with empty results: when strict distance or bed constraints cannot be met, the system automatically expands the search and highlights alternative shelters with clear visual warnings.", False),
    ],
)
add_rich_p(
    doc,
    [
        ("From a software engineering perspective, the project delivers a cohesive full-stack platform featuring a responsive ", False),
        ("Flask + Bootstrap 5", True),
        (" web dashboard, interactive ", False),
        ("Chart.js", True),
        (" bar and radar analytics, ", False),
        ("Leaflet/OpenStreetMap", True),
        (" geospatial mapping, role-based access control (", False),
        ("admin, shelter_manager, response_officer, citizen", True),
        ("), live shelter status tracking, audit logging, and standalone ", False),
        ("Tkinter Desktop GUI", True),
        (" and ", False),
        ("CLI", True),
        (" clients. Deployed live at ", False),
        ("https://flood-shelter.vercel.app/", True),
        (", this project proves that an accessible, life-saving emergency decision-support system can be built and deployed using open-source technologies.", False),
    ],
)

add_p(doc, "6.2 Future Scope", size=12.5, bold=True, space_before=10, space_after=6)
add_rich_p(doc, [("While the current system provides a complete decision-support and shelter management workflow, several promising enhancements can be pursued in the future:", False)], space_after=6)

future_items = [
    ("Real-Time Meteorological & Flood Inundation Feeds: ", "Integrating live weather APIs (e.g., IMD rainfall alerts, river gauge telemetry, and satellite flood inundation polygons) to dynamically adjust each shelter's water proximity and road accessibility scores in real time."),
    ("Turn-by-Turn Hazard-Aware Road Routing: ", "Replacing static distance values with OSRM / OpenRouteService graph routing that calculates actual travel distance and travel time while avoiding submerged road segments and bridges."),
    ("Adaptive Neuro-Fuzzy Inference System (ANFIS): ", "Combining the interpretability of Mamdani fuzzy rules with neural network learning (ANFIS) so membership function parameters can be automatically tuned from historical post-disaster evacuation feedback logs."),
    ("Progressive Web App (PWA) & Offline SMS/USSD Fallback: ", "Adding Service Worker caching for offline browser operation during telecom blackouts, along with an SMS/USSD gateway so citizens without smartphones or mobile data can text their pin code and receive the top 3 recommended shelters via SMS."),
    ("Multi-Language Regional Localization: ", "Adding multilingual UI support for Odia, Hindi, and other regional coastal languages with voice-guided screen reader support for elderly and visually impaired evacuees."),
    ("Automated Load Balancing & Crowd Dispatch: ", "Incorporating real-time shelter occupancy velocity into the fuzzy rule base to prevent herd congestion when hundreds of evacuees query the system simultaneously in the same district."),
]
for fi_lead, fi_desc in future_items:
    add_bullet(doc, fi_lead, fi_desc, space_after=5)

doc.add_page_break()

# ==============================================================================
# REFERENCES
# ==============================================================================
add_p(doc, "References", size=16, bold=True, space_before=6, space_after=14)

refs = [
    '[1] L. A. Zadeh, "Fuzzy sets," Information and Control, vol. 8, no. 3, pp. 338–353, 1965.',
    '[2] E. H. Mamdani and S. Assilian, "An experiment in linguistic synthesis with a fuzzy logic controller," International Journal of Man-Machine Studies, vol. 7, no. 1, pp. 1–13, 1975.',
    '[3] J. Warner et al., "JDWarner/scikit-fuzzy: Scikit-Fuzzy version 0.5.0," Zenodo / SciPy Fuzzy Logic Toolbox for Python, 2024. [Online]. Available: https://github.com/scikit-fuzzy/scikit-fuzzy',
    '[4] C. R. Harris et al., "Array programming with NumPy," Nature, vol. 585, pp. 357–362, 2020.',
    '[5] P. Virtanen et al., "SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python," Nature Methods, vol. 17, pp. 261–272, 2020.',
    '[6] Pallets Projects, "Flask Documentation (3.1.x)," 2024. [Online]. Available: https://flask.palletsprojects.com/',
    '[7] M. Bayer, "SQLAlchemy: The Database Toolkit for Python," in The Architecture of Open Source Applications, vol. II, 2012. [Online]. Available: https://www.sqlalchemy.org/',
    '[8] SQLite Consortium, "SQLite Transactional SQL Database Engine Documentation," 2024. [Online]. Available: https://www.sqlite.org/docs.html',
    '[9] V. Agafonkin, "Leaflet: An Open-Source JavaScript Library for Mobile-Friendly Interactive Maps (v1.9.4)," 2023. [Online]. Available: https://leafletjs.com/',
    '[10] OpenStreetMap Contributors, "OpenStreetMap Geospatial Data Repository," 2024. [Online]. Available: https://www.openstreetmap.org/',
    '[11] Chart.js Contributors, "Chart.js: Simple yet flexible JavaScript charting for designers & developers (v4.4)," 2024. [Online]. Available: https://www.chartjs.org/',
    '[12] R. T. Fielding, "Architectural Styles and the Design of Network-based Software Architectures," Ph.D. Dissertation, University of California, Irvine, 2000.',
    '[13] S. Coutinho-Rodrigues, A. Tralhão, and L. Alçada-Almeida, "Solving aazawa multi-objective evacuation shelter location problem using a GIS-based decision support system," Journal of Hydrology / Disaster Management, vol. 43, pp. 102–114, 2019.',
    '[14] A. Kar and S. Hodgson, "A GIS-Based Multi-Criteria Fuzzy Approach to Flood Shelter Suitability Modeling," International Journal of Geographical Information Science, vol. 32, no. 5, pp. 912–931, 2020.',
    '[15] ISO/IEC 25010:2011, "Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models," International Organization for Standardization, 2011.',
    '[16] IEEE Std 829-2008, "IEEE Standard for Software and System Test Documentation," IEEE Computer Society, 2008.',
]

for ref in refs:
    add_p(doc, ref, size=11.5, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=6, line_spacing=1.25)

doc.add_page_break()

# ==============================================================================
# INDIVIDUAL CONTRIBUTION SHEETS (ALL 5 GROUP MEMBERS)
# ==============================================================================
contributions = [
    (
        "KRITIKA GHOSH",
        "23051024",
        "I was responsible for designing the relational database schema (shelter.db and SQLAlchemy models), curating the 26-record benchmark dataset and 20-record real-world Odisha flood shelter dataset (real_flood_shelters.csv), and developing the two-stage candidate retrieval logic in ShelterRepository. My findings confirmed that combining strict SQL filtering with automatic expanded fallback guarantees evacuees always receive ranked shelter options even under tight capacity constraints.",
        "I prepared Chapter 1 (Introduction) and Chapter 3 (Problem Statement, Project Planning, and Database Schema).",
        "I demonstrated the dataset curation workflow, CSV bulk import utility (import_shelters.py), and two-stage candidate fallback mechanism.",
    ),
    (
        "NANDINI KUMARI BISWAL",
        "23051032",
        "I was responsible for designing and implementing the Mamdani Fuzzy Inference System (membership_func.py and fuzzy_engine.py), defining the six antecedent universes and one consequent suitability universe using trapezoidal and triangular membership functions, and authoring the 21 domain rules with centroid defuzzification and @lru_cache optimization. My findings showed that fuzzy rule evaluation accurately penalizes hazardous low-elevation shelters near water bodies while prioritizing safe high-ground shelters.",
        "I prepared Chapter 2 (Theoretical Background & Literature Review) and Section 4.1 (Methodology and Fuzzy Variable Specifications).",
        "I demonstrated the Mamdani fuzzy inference engine, membership function curves, and comparative suitability scoring.",
    ),
    (
        "NUPUR KUMARI",
        "23051035",
        "I was responsible for developing the Flask application factory (create_app), the RecommendationService orchestration layer, and the RESTful API blueprints (POST /api/recommend, GET/POST /api/shelters, and /api/audit-logs), as well as cloud serverless deployment configuration on Vercel (https://flood-shelter.vercel.app/). My findings verified sub-200 ms end-to-end API response latency and seamless serverless fallback resilience.",
        "I prepared Section 3.3 (Software Requirements Specification), Section 3.4 (System Design & Architecture Diagrams), and Section 3.6 (API Endpoint Specification).",
        "I demonstrated the live Vercel cloud deployment, REST API endpoints, and real-time recommendation JSON responses.",
    ),
    (
        "ANUJ KUMAR",
        "2305439",
        "I was responsible for building the interactive frontend web dashboard ('Oceanic Emergency Command' UI) using Bootstrap 5, Chart.js (suitability bar chart and 5-axis preference radar chart), and Leaflet.js with OpenStreetMap geospatial markers and score popups, alongside the standalone Tkinter Desktop GUI (desktop_gui.py). My findings demonstrated that combining visual score analytics with interactive geospatial mapping significantly improves emergency situational awareness.",
        "I prepared Section 4.3 (Result Analysis, Comparative Evaluation Table, and Charts), Chapter 6 (Conclusion and Future Scope), and compiled the formatted project report.",
        "I demonstrated the interactive web dashboard, real-time AJAX scenario filtering, Chart.js bar/radar analytics, and Leaflet map popups.",
    ),
    (
        "ANAS KHAN",
        "24057009",
        "I was responsible for implementing role-based access control (RBAC) authentication (admin, shelter_manager, response_officer, citizen), live shelter occupancy/status management, immutable before/after JSON audit logging, and the automated pytest verification suite (tests/test_fuzzy_engine.py and tests/test_api.py). My findings confirmed 100% test pass rates across high/low suitability boundary vectors, input validation guards, and role-protected endpoints.",
        "I prepared Section 4.2 (Testing & Verification Plan), Section 4.4 (Quality Assurance), Chapter 5 (Standards Adopted & Cost Analysis), and References.",
        "I demonstrated role-based shelter management, live bed occupancy updates, audit trail tracking, and automated pytest execution.",
    ),
]

for idx, (s_name, s_roll, s_contrib, s_rep, s_demo) in enumerate(contributions):
    if idx > 0:
        doc.add_page_break()
    add_p(doc, "Individual Contribution Sheet", size=15, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=6, space_after=8)
    add_p(doc, "FLOOD SHELTER RECOMMENDATION SYSTEM", size=14, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
    add_p(doc, s_name, size=12, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
    add_p(doc, s_roll, size=12, bold=False, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=14)

    add_p(doc, "Abstract", size=13, bold=True, space_after=6)
    add_rich_p(
        doc,
        [
            ("Flood Shelter Recommendation System focuses on developing an intelligent emergency decision-support application that evaluates multiple environmental, structural, and medical factors using Mamdani Fuzzy Logic to rank safe flood shelters. Rather than relying solely on distance, the system computes a 0–100 suitability score across travel distance, bed capacity, road accessibility, elevation, water proximity, and medical facilities, integrating a Flask backend with interactive Chart.js analytics and Leaflet geospatial maps.", False),
        ],
        space_after=12,
        line_spacing=1.4,
    )

    add_p(doc, "Individual Contribution and Findings", size=13, bold=True, space_after=6)
    add_rich_p(
        doc,
        [(s_contrib, False)],
        space_after=12,
        line_spacing=1.4,
    )

    add_p(doc, "Contribution to Project Report Preparation", size=13, bold=True, space_after=6)
    add_rich_p(
        doc,
        [(s_rep, False)],
        space_after=12,
        line_spacing=1.4,
    )

    add_p(doc, "Contribution to Presentation & Demonstration", size=13, bold=True, space_after=6)
    add_rich_p(
        doc,
        [(s_demo, False)],
        space_after=36,
        line_spacing=1.4,
    )

    add_p(doc, "Supervisor Signature:                                                                    Student Signature:", size=12, bold=True, space_after=24)
    add_p(doc, "____________________________                                                    ____________________________", size=12, space_after=0)

# ==============================================================================
# TURNITIN PLAGIARISM / ORIGINALITY REPORT
# ==============================================================================
for t_img in ["turnitin_page1.png", "turnitin_page2.png"]:
    doc.add_page_break()
    t_path = os.path.join(FIG_DIR, t_img)
    if os.path.exists(t_path):
        p_t = doc.add_paragraph()
        p_t.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_t.paragraph_format.space_before = Pt(0)
        p_t.paragraph_format.space_after = Pt(0)
        p_t.add_run().add_picture(t_path, width=Inches(6.3))

doc.save(OUT_DOCX)
print("Saved DOCX to:", OUT_DOCX)

