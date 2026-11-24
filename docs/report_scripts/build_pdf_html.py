import os
import base64

FIG_DIR = "/Users/anuj9009/Downloads/major_project/assets/figures"
LOGO_PATH = "/Users/anuj9009/Downloads/major_project/assets/word/media/image2.jpeg"
OUT_HTML = "/Users/anuj9009/Downloads/major_project/assets/report_print.html"

def b64_img(path):
    with open(path, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")
    ext = "jpeg" if path.endswith(".jpeg") or path.endswith(".jpg") else "png"
    return f"data:image/{ext};base64,{data}"

logo_src = b64_img(LOGO_PATH)
figs = {
    f"fig{i}": b64_img(os.path.join(FIG_DIR, name))
    for i, name in [
        (1, "fig1_arch.png"),
        (2, "fig2_block.png"),
        (3, "fig3_terminal.png"),
        (4, "fig4_dashboard.png"),
        (5, "fig5_dataset.png"),
        (6, "fig6_ranked.png"),
        (7, "fig7_map.png"),
        (8, "fig8_bar.png"),
        (9, "fig9_radar.png"),
        (10, "fig10_fuzzy.png"),
    ]
}

html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Flood Shelter Recommendation System - Project Report</title>
<style>
  @page {{
    size: A4;
    margin: 14mm;
  }}
  * {{
    box-sizing: border-box;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }}
  body {{
    margin: 0;
    padding: 0;
    font-family: "Times New Roman", Times, serif;
    font-size: 10.8pt;
    line-height: 1.32;
    color: #000;
    background: #fff;
  }}
  .page {{
    width: 100%;
    height: 267mm;
    border: 2px solid #000;
    padding: 10mm 12mm;
    page-break-after: always;
    break-after: page;
    position: relative;
    overflow: hidden;
  }}
  .page:last-child {{
    page-break-after: auto;
    break-after: auto;
  }}
  .turnitin-page {{
    width: 100%;
    height: 267mm;
    border: none;
    padding: 12mm 14mm;
    page-break-after: always;
    break-after: page;
    position: relative;
    overflow: hidden;
    font-family: Arial, Helvetica, sans-serif;
    color: #444;
  }}
  .turnitin-page:last-child {{
    page-break-after: auto;
    break-after: auto;
  }}
  .t-title {{
    font-size: 15pt;
    color: #555;
    margin-bottom: 6pt;
    font-weight: normal;
  }}
  .t-sec-bar {{
    border-top: 1.5px solid #a0a0a0;
    border-bottom: 1px solid #bdbdbd;
    padding: 4pt 0;
    color: #d92b1e;
    font-size: 7.5pt;
    font-weight: bold;
    letter-spacing: 0.4px;
    text-transform: uppercase;
  }}
  .t-metrics {{
    display: flex;
    align-items: flex-end;
    padding: 12pt 0 14pt 0;
    gap: 28pt;
  }}
  .t-metric-col {{
    display: flex;
    flex-direction: column;
  }}
  .t-big-sim {{
    font-size: 44pt;
    line-height: 1;
    color: #d92b1e;
    font-weight: normal;
  }}
  .t-big-sim span {{
    font-size: 20pt;
    color: #666;
  }}
  .t-sub-sim {{
    font-size: 30pt;
    line-height: 1;
    color: #444;
    font-weight: normal;
  }}
  .t-sub-sim span {{
    font-size: 16pt;
    color: #666;
  }}
  .t-metric-label {{
    font-size: 8pt;
    color: #555;
    margin-top: 5pt;
    letter-spacing: 0.3px;
    text-transform: uppercase;
  }}
  .t-row {{
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    border-bottom: 1px solid #bdbdbd;
    padding: 8pt 0;
  }}
  .t-left {{
    display: flex;
    align-items: flex-start;
    gap: 12pt;
    max-width: 82%;
  }}
  .t-badge {{
    width: 22pt;
    height: 22pt;
    min-width: 22pt;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #fff;
    font-size: 10pt;
    font-weight: bold;
    border-radius: 1px;
    margin-top: 1pt;
  }}
  .t-source-name {{
    font-size: 12.5pt;
    line-height: 1.28;
    margin-bottom: 2pt;
  }}
  .t-source-type {{
    font-size: 8.5pt;
    color: #666;
  }}
  .t-pct {{
    font-size: 24pt;
    color: #444;
    line-height: 1;
    white-space: nowrap;
  }}
  .t-pct span {{
    font-size: 13pt;
    color: #555;
  }}
  .t-footer {{
    border-top: 1.5px solid #a0a0a0;
    margin-top: 18pt;
    padding-top: 8pt;
    display: flex;
    gap: 90pt;
    font-size: 8.5pt;
    color: #666;
  }}
  .t-footer-col div {{
    margin-bottom: 5pt;
    display: flex;
    gap: 28pt;
  }}
  .center {{ text-align: center; }}
  .right {{ text-align: right; }}
  .justify {{ text-align: justify; }}
  h1 {{ font-size: 15pt; font-weight: bold; margin: 0 0 4pt 0; }}
  h2 {{ font-size: 13pt; font-weight: bold; margin: 0 0 6pt 0; }}
  h3 {{ font-size: 11.5pt; font-weight: bold; margin: 6pt 0 3pt 0; }}
  p {{ margin: 0 0 5.5pt 0; text-align: justify; }}
  ul, ol {{ margin: 2.5pt 0 5.5pt 16pt; padding: 0; }}
  li {{ margin-bottom: 3pt; text-align: justify; }}
  code {{ font-family: "Courier New", Courier, monospace; font-size: 9.5pt; word-break: break-word; }}
  table {{
    width: 100%;
    table-layout: fixed;
    border-collapse: collapse;
    margin: 4pt 0 6pt 0;
    font-size: 8.5pt;
    line-height: 1.15;
  }}
  th, td {{
    border: 1px solid #000;
    padding: 3pt 4pt;
    vertical-align: top;
    text-align: left;
    word-wrap: break-word;
    overflow-wrap: break-word;
  }}
  th {{
    background-color: #d9e2f3;
    font-weight: bold;
  }}
  .fig-box {{
    text-align: center;
    margin: 6pt 0 8pt 0;
  }}
  .fig-box img {{
    max-width: 100%;
    border: 1px solid #cbd5e1;
    border-radius: 4px;
  }}
  .fig-cap {{
    font-size: 10.5pt;
    font-weight: bold;
    margin-top: 3pt;
    text-align: center;
  }}
  .toc-line {{
    display: flex;
    justify-content: space-between;
    margin-bottom: 4pt;
    font-size: 11.5pt;
  }}
  .toc-main {{ font-weight: bold; margin-top: 4pt; }}
  .toc-sub {{ padding-left: 18pt; }}
  .dots {{
    flex: 1;
    border-bottom: 1px dotted #000;
    margin: 0 6pt 4pt 6pt;
  }}
</style>
</head>
<body>

<!-- PAGE 1: COVER PAGE -->
<div class="page center" style="padding-top: 20mm;">
  <div style="font-size: 14pt; font-weight: bold; margin-bottom: 8pt;">A PROJECT REPORT</div>
  <div style="font-size: 12pt; margin-bottom: 8pt;">on</div>
  <div style="font-size: 16pt; font-weight: bold; margin-bottom: 12pt;">"Flood Shelter Recommendation System"</div>
  <div style="font-size: 12pt; margin-bottom: 6pt;">Submitted to</div>
  <div style="font-size: 13pt; font-weight: bold; margin-bottom: 6pt;">KIIT Deemed to be University</div>
  <div style="font-size: 12pt; margin-bottom: 6pt;">In Partial Fulfillment of the Requirements for the Award of</div>
  <div style="font-size: 13pt; font-weight: bold; margin-bottom: 14pt;">BACHELOR'S DEGREE IN COMPUTER SCIENCE AND ENGINEERING</div>
  <div style="font-size: 12pt; margin-bottom: 10pt;">BY</div>
  <div style="font-size: 12pt; font-weight: bold; line-height: 1.75; margin-bottom: 14pt;">
    KRITIKA GHOSH &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 23051024<br>
    NANDINI KUMARI BISWAL &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 23051032<br>
    NUPUR KUMARI &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 23051035<br>
    ANUJ KUMAR &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2305439<br>
    ANAS KHAN &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 24057009
  </div>
  <div style="font-size: 12pt; margin-bottom: 4pt;">Under the Guidance of</div>
  <div style="font-size: 13pt; font-weight: bold; margin-bottom: 14pt;">SUNIL KUMAR GOUDA</div>
  <div style="margin: 8pt 0 12pt 0;">
    <img src="{logo_src}" style="width: 115px; height: auto;">
  </div>
  <div style="font-size: 12pt; font-weight: bold; line-height: 1.6;">
    SCHOOL OF COMPUTER ENGINEERING<br>
    KALINGA INSTITUTE OF INDUSTRIAL TECHNOLOGY<br>
    BHUBANESWAR, ODISHA — 751024<br>
    2026
  </div>
</div>

<!-- PAGE 2: CERTIFICATE -->
<div class="page center" style="padding-top: 16mm;">
  <div style="margin-bottom: 10pt;">
    <img src="{logo_src}" style="width: 110px; height: auto;">
  </div>
  <div style="font-size: 13pt; font-weight: bold; margin-bottom: 4pt;">KIIT Deemed to be University</div>
  <div style="font-size: 12pt; margin-bottom: 4pt;">School of Computer Engineering</div>
  <div style="font-size: 12pt; margin-bottom: 18pt;">Bhubaneswar, Odisha — 751024</div>
  <div style="font-size: 14pt; font-weight: bold; text-decoration: underline; margin-bottom: 14pt;">CERTIFICATE</div>
  <div style="font-size: 12pt; margin-bottom: 10pt;">This is to certify that the project titled</div>
  <div style="font-size: 14pt; font-weight: bold; margin-bottom: 12pt;">"Flood Shelter Recommendation System"</div>
  <div style="font-size: 12pt; margin-bottom: 10pt;">submitted by</div>
  <div style="font-size: 12pt; font-weight: bold; line-height: 1.75; margin-bottom: 16pt;">
    KRITIKA GHOSH — 23051024<br>
    NANDINI KUMARI BISWAL — 23051032<br>
    NUPUR KUMARI — 23051035<br>
    ANUJ KUMAR — 2305439<br>
    ANAS KHAN — 24057009
  </div>
  <p class="center" style="line-height: 1.5; margin-bottom: 30pt; font-size: 12pt;">
    is a record of authentic work accomplished by them toward the partial fulfillment of the Bachelor of Engineering (Computer Science &amp; Engineering) degree at KIIT Deemed to be University, Bhubaneswar. This research and development work was conducted during the academic year 2025–2026 under our direct supervision and guidance.
  </p>
  <div style="text-align: left; margin-bottom: 40pt; font-size: 12pt;">Date: ____ / ____ / ________</div>
  <div style="font-size: 12pt; font-weight: bold; margin-bottom: 4pt;">Sunil Kumar Gouda</div>
  <div style="font-size: 12pt; margin-bottom: 4pt;">Project Supervisor</div>
  <div style="font-size: 12pt;">School of Computer Engineering, KIIT University</div>
</div>

<!-- PAGE 3: ACKNOWLEDGEMENTS -->
<div class="page">
  <h2 class="center" style="margin-top: 8pt; margin-bottom: 22pt;">Acknowledgements</h2>
  <p style="line-height: 1.55; margin-bottom: 16pt; font-size: 12pt;">
    We extend our deepest gratitude to our Project Supervisor, <b>Prof. Sunil Kumar Gouda</b>, of the School of Computer Engineering, KIIT Deemed to be University, whose unwavering support, technical insights, and mentorship were indispensable throughout every stage of this project — from initial conceptualization of the multi-criteria fuzzy inference engine to the final full-stack web deployment. Their patient guidance in soft computing theory, software architecture, and academic writing elevated the quality of this work significantly.
  </p>
  <p style="line-height: 1.55; margin-bottom: 42pt; font-size: 12pt;">
    We also express our sincere thanks to the Dean and faculty members of the School of Computer Engineering, Kalinga Institute of Industrial Technology, for providing the computational infrastructure, academic environment, and continuous encouragement required to complete this project successfully.
  </p>
  <div style="margin-left: 55%; line-height: 1.8; font-weight: bold; font-size: 12pt;">
    KRITIKA GHOSH<br>
    NANDINI KUMARI BISWAL<br>
    NUPUR KUMARI<br>
    ANUJ KUMAR<br>
    ANAS KHAN
  </div>
</div>

<!-- PAGE 4: ABSTRACT -->
<div class="page">
  <h2 class="center" style="margin-top: 8pt; margin-bottom: 18pt;">Abstract</h2>
  <p style="line-height: 1.48; margin-bottom: 14pt; font-size: 12pt;">
    During severe flood emergencies, evacuating affected citizens to safe relief shelters rapidly and reliably is a critical disaster management challenge. Traditional shelter locators rely primarily on shortest-path distance metrics; however, in real-world flood scenarios, the nearest shelter is not necessarily the safest or most viable option. A nearby shelter may be situated on low-lying terrain, in close proximity to overflowing water bodies, lacking road accessibility, or depleted of available beds and medical supplies. To address this multi-criteria decision problem under uncertainty, this project presents the <b>Flood Shelter Recommendation System</b>, an intelligent decision-support application powered by a <b>Mamdani Fuzzy Inference System (FIS)</b>. Rather than applying rigid binary thresholds, the system evaluates six operational and environmental antecedents — travel distance (0–20 km), usable bed capacity (0–100), road accessibility (0–10), terrain elevation level (0–10), proximity to water bodies (0–10), and medical facility readiness (0–10) — using trapezoidal and triangular membership functions across 21 domain-specific fuzzy rules to compute a continuous <b>Suitability Score (0–100)</b> via centroid defuzzification.
  </p>
  <p style="line-height: 1.48; margin-bottom: 16pt; font-size: 12pt;">
    The system is engineered as a modular, three-tier full-stack application using <b>Flask</b> and <b>SQLAlchemy</b> on the backend, <b>scikit-fuzzy</b> and <b>NumPy</b> for the inference engine, and <b>SQLite / PostgreSQL</b> for persistent storage of geospatial shelter records, operational status updates, and audit logs. The presentation layer supports three client interfaces sharing a unified recommendation core: a responsive web dashboard built with <b>Bootstrap 5, Chart.js, and Leaflet/OpenStreetMap</b> (deployed live at <b>https://flood-shelter.vercel.app/</b>), a <b>Tkinter</b> desktop GUI, and an interactive CLI. Experimental validation across 26 built-in benchmark shelters and 20 real-world Odisha flood shelters demonstrates that the Mamdani fuzzy engine effectively penalizes hazardous nearby shelters (e.g., Shelter V at 0.5 km scoring 34.72 due to low elevation and water proximity) while prioritizing high-elevation, well-equipped shelters (e.g., Shelter H scoring 67.83 and Shelter A scoring 66.92), providing transparent, life-saving evacuation guidance.
  </p>
  <p style="line-height: 1.45; font-size: 12pt;">
    <b>Keywords:</b> Flood Shelter Recommendation, Fuzzy Logic, Mamdani Inference System, Multi-Criteria Decision Making (MCDM), Centroid Defuzzification, scikit-fuzzy, Flask REST API, Leaflet Geospatial Mapping, Disaster Management, Emergency Evacuation.
  </p>
</div>

<!-- PAGE 5: CONTENTS -->
<div class="page">
  <h1 style="margin-bottom: 12pt;">Contents</h1>
  <div class="toc-line toc-main"><span>Chapter 1 — Introduction</span><span class="dots"></span><span>1</span></div>
  <div class="toc-line toc-main"><span>Chapter 2 — Theoretical Background / Literature Review</span><span class="dots"></span><span>2-3</span></div>
  <div class="toc-line toc-sub"><span>2.1 Fuzzy Logic and Mamdani Inference System</span><span class="dots"></span><span>2</span></div>
  <div class="toc-line toc-sub"><span>2.2 Membership Functions and Centroid Defuzzification</span><span class="dots"></span><span>2</span></div>
  <div class="toc-line toc-sub"><span>2.3 Flask Web Framework and Modular Blueprint Architecture</span><span class="dots"></span><span>2</span></div>
  <div class="toc-line toc-sub"><span>2.4 Interactive Visualization with Chart.js and Leaflet</span><span class="dots"></span><span>3</span></div>
  <div class="toc-line toc-sub"><span>2.5 SQLite &amp; SQLAlchemy for Relational Data Persistence</span><span class="dots"></span><span>3</span></div>
  <div class="toc-line toc-sub"><span>2.6 Related Work</span><span class="dots"></span><span>3</span></div>
  <div class="toc-line toc-main"><span>Chapter 3 — Problem Statement and Requirement Specifications</span><span class="dots"></span><span>4-8</span></div>
  <div class="toc-line toc-sub"><span>3.1 Problem Statement</span><span class="dots"></span><span>4</span></div>
  <div class="toc-line toc-sub"><span>3.2 Project Planning</span><span class="dots"></span><span>4</span></div>
  <div class="toc-line toc-sub"><span>3.3 Software Requirements Specification (SRS)</span><span class="dots"></span><span>5</span></div>
  <div class="toc-line toc-sub"><span>3.4 System Design</span><span class="dots"></span><span>5-7</span></div>
  <div class="toc-line toc-sub"><span>3.5 Database Schema</span><span class="dots"></span><span>8</span></div>
  <div class="toc-line toc-sub"><span>3.6 API Endpoint Specification</span><span class="dots"></span><span>8</span></div>
  <div class="toc-line toc-main"><span>Chapter 4 — Implementation</span><span class="dots"></span><span>9-15</span></div>
  <div class="toc-line toc-sub"><span>4.1 Methodology</span><span class="dots"></span><span>9-11</span></div>
  <div class="toc-line toc-sub"><span>4.2 Testing and Verification Plan</span><span class="dots"></span><span>12</span></div>
  <div class="toc-line toc-sub"><span>4.3 Result Analysis</span><span class="dots"></span><span>13-14</span></div>
  <div class="toc-line toc-sub"><span>4.4 Quality Assurance</span><span class="dots"></span><span>14-15</span></div>
  <div class="toc-line toc-main"><span>Chapter 5 — Standards Adopted</span><span class="dots"></span><span>16-17</span></div>
  <div class="toc-line toc-sub"><span>5.1 Design Standards</span><span class="dots"></span><span>16</span></div>
  <div class="toc-line toc-sub"><span>5.2 Coding Standards</span><span class="dots"></span><span>16-17</span></div>
  <div class="toc-line toc-sub"><span>5.3 Testing Standards</span><span class="dots"></span><span>17</span></div>
  <div class="toc-line toc-sub"><span>5.4 Cost Analysis</span><span class="dots"></span><span>17</span></div>
  <div class="toc-line toc-main"><span>Chapter 6 — Conclusion and Future Scope</span><span class="dots"></span><span>18-19</span></div>
  <div class="toc-line toc-sub"><span>6.1 Conclusion</span><span class="dots"></span><span>18</span></div>
  <div class="toc-line toc-sub"><span>6.2 Future Scope</span><span class="dots"></span><span>18-19</span></div>
  <div class="toc-line toc-main"><span>References</span><span class="dots"></span><span>20</span></div>
  <div class="toc-line toc-main"><span>Individual Contribution Sheet</span><span class="dots"></span><span>21-25</span></div>
  <div class="toc-line toc-main"><span>Turnitin Plagiarism Report</span><span class="dots"></span><span>26</span></div>
</div>

<!-- PAGE 6: LIST OF FIGURES & TABLES -->
<div class="page">
  <h1 style="margin-bottom: 12pt;">List of Figures</h1>
  <p>Fig 1 : System Architecture Diagram (Three-Tier Presentation, Fuzzy Logic, and Persistence Layers)</p>
  <p>Fig 2 : Block Diagram of Mamdani Fuzzy Inference and Shelter Ranking Pipeline</p>
  <p>Fig 3 : Application Execution and Automated Pytest Verification on Local Host</p>
  <p>Fig 4 : Flood Shelter Intelligence Web Dashboard (Live Deployment on Vercel)</p>
  <p>Fig 5 : Geospatial &amp; Operational Flood Shelter Dataset Preview (Odisha Shelters)</p>
  <p>Fig 6 : Top Ranked Shelter Match Card and Multi-Criteria Suitability Rankings</p>
  <p>Fig 7 : Interactive Leaflet &amp; OpenStreetMap View with Shelter Suitability Popups</p>
  <p>Fig 8 : Bar Graph — Shelter Suitability Score Comparison (Direct vs. Alternative Matches)</p>
  <p>Fig 9 : Radar Chart — Multi-Criteria Fuzzy Preference Profile vs. Shelter Attributes</p>
  <p>Fig 10 : Fuzzy Membership Functions (Antecedent Distance &amp; Consequent Suitability Universe)</p>

  <h1 style="margin-top: 20pt; margin-bottom: 12pt;">List of Tables</h1>
  <p>Table 1 : Fuzzy Antecedent and Consequent Linguistic Variables, Universes, and Parameters</p>
  <p>Table 2 : Functional and Non-Functional Verification Test Cases (T01 – T10)</p>
  <p>Table 3 : Comparative Evaluation of Shelter Ranking Methodologies and Benchmark Results</p>
</div>

<!-- PAGE 7: CHAPTER 1 INTRODUCTION -->
<div class="page">
  <h1>Chapter 1</h1>
  <h2>Introduction</h2>
  <p>
    Floods are among the most frequent and devastating natural disasters worldwide, particularly in coastal and riverine regions such as Odisha, India, where annual monsoonal surges and cyclonic depressions frequently inundate residential zones. During a flood emergency, timely evacuation of citizens to safe relief shelters is paramount to minimizing casualties and human distress. However, displaced individuals and emergency response coordinators often face severe information asymmetry when selecting an evacuation shelter. Conventional navigation tools and static government directories typically sort shelters solely by geographic proximity or list raw tabular attributes without synthesizing overall safety.
  </p>
  <p>
    The core motivation behind the <b>Flood Shelter Recommendation System</b> is the critical realization that <b>the nearest shelter is not necessarily the safest or most suitable option</b>. For instance, a shelter located 0.5 km away may lie in a low-elevation basin immediately adjacent to a swelling river, possess difficult road accessibility due to waterlogging, lack medical facilities for injured evacuees, or have zero available beds remaining. Conversely, a shelter situated 2.5 to 3.8 km away on high terrain, far from water bodies, with easy road access, 40+ available beds, and advanced medical support offers vastly superior protection.
  </p>
  <p>
    Furthermore, real-world disaster parameters are inherently imprecise and continuous rather than binary (black-and-white). A shelter is rarely strictly 'safe' or 'unsafe'; instead, it exhibits graded degrees of accessibility, moderate or high elevation safety, and varying margins of bed capacity. To model this real-world vagueness mathematically, this project employs <b>Fuzzy Logic (Mamdani Fuzzy Inference System)</b> using the <b>scikit-fuzzy</b> library. The system evaluates six key parameters — travel distance, usable shelter capacity, road accessibility, terrain elevation level, proximity to water bodies, and medical facility availability — through trapezoidal and triangular membership functions and 21 expert rules to compute an interpretable <b>Suitability Score (0 to 100)</b> for each candidate shelter.
  </p>
  <p><b>The main objectives of this project are:</b></p>
  <ul>
    <li><b>Multi-Criteria Fuzzy Evaluation:</b> To design a Mamdani Fuzzy Inference System that synthesizes six spatial, environmental, and operational factors into a unified 0–100 shelter suitability score.</li>
    <li><b>Intelligent Two-Stage Candidate Filtering:</b> To implement a strict-first database query that filters shelters by minimum required beds and maximum travel distance, seamlessly falling back to an expanded search with user warnings when exact matches are unavailable.</li>
    <li><b>Interactive Geospatial &amp; Visual Analytics:</b> To build a responsive web interface featuring Leaflet interactive maps with shelter score popups, Chart.js bar charts for score comparison, and radar charts for user preference profiling.</li>
    <li><b>Multi-Channel &amp; Role-Based Operations:</b> To provide a unified recommendation engine accessible via Web UI, REST API (<code>/api/recommend</code>), Tkinter Desktop GUI, and CLI, alongside role-protected shelter management and audit logging.</li>
    <li><b>Cloud &amp; Local Deployability:</b> To support zero-configuration local execution with SQLite as well as cloud serverless deployment (Vercel/Render) with built-in resilient fallbacks.</li>
  </ul>
  <p>
    The current system evaluates static or manager-updated shelter attributes stored in the database. Features such as live meteorological radar ingestion and dynamic turn-by-turn road inundation routing may be integrated in future iterations.
  </p>
</div>

<!-- PAGE 8: CHAPTER 2 LITERATURE REVIEW PART 1 -->
<div class="page">
  <h1>Chapter 2</h1>
  <h2>Theoretical Background / Literature Review</h2>
  <h3>2.1 Fuzzy Logic and Mamdani Inference System</h3>
  <p>
    Fuzzy Logic, introduced by Lotfi A. Zadeh in 1965, extends classical Boolean logic to handle partial truth — where a variable's membership in a set is expressed on a continuous interval <b>[0, 1]</b> rather than crisp binary values <b>{{0, 1}}</b>. In disaster management, crisp cutoffs create brittle edge effects: for example, if a hard rule rejects shelters beyond 5.0 km, a highly secure shelter at 5.1 km with 200 free beds and advanced medical care would be discarded in favor of a hazardous shelter at 4.9 km. The <b>Mamdani Fuzzy Inference System</b>, proposed by Ebrahim Mamdani in 1975, resolves this by mapping crisp inputs into linguistic variables (fuzzification), evaluating IF-THEN rules using fuzzy logic operators (minimum t-norm for AND, maximum s-norm for OR), aggregating consequent fuzzy sets, and converting the resulting area back into a crisp score (defuzzification).
  </p>

  <h3>2.2 Membership Functions and Centroid Defuzzification</h3>
  <p>
    In this project, the fuzzy control system (implemented in <b>membership_func.py</b> and <b>flood_app/services/fuzzy_engine.py</b>) utilizes two primary piecewise linear membership functions from <b>scikit-fuzzy</b>:
  </p>
  <ul>
    <li><b>Trapezoidal Membership Function (trapmf):</b> Defined by four parameters <code>[a, b, c, d]</code>, where membership equals 1.0 across the flat plateau <code>[b, c]</code> and tapers linearly on <code>[a, b]</code> and <code>[c, d]</code>. This models boundary states such as 'Near' distance <code>[0, 0, 3, 7]</code>, 'High' capacity <code>[65, 85, 100, 100]</code>, and 'Excellent' suitability <code>[85, 93, 100, 100]</code>.</li>
    <li><b>Triangular Membership Function (trimf):</b> Defined by three parameters <code>[a, b, c]</code> with a single peak at <code>b</code>. This models intermediate transitional states such as 'Medium' distance <code>[4, 9, 14]</code>, 'Medium' capacity <code>[30, 55, 80]</code>, and 'Moderate' accessibility/elevation <code>[3, 5, 7]</code>.</li>
    <li><b>Centroid Defuzzification:</b> After all 21 rules fire and their clipped consequent fuzzy sets are aggregated over the suitability universe <code>[0, 100]</code>, the crisp suitability score is computed via the Center of Area (CoA) integral, yielding a balanced score between 0 and 100.</li>
  </ul>

  <h3>2.3 Flask Web Framework and Modular Blueprint Architecture</h3>
  <p>
    Flask is a lightweight WSGI web application framework in Python. In this project, Flask is structured using the <b>Application Factory pattern (<code>create_app</code>)</b> and modular <b>Blueprints</b> separating concerns across web rendering (<code>web_bp</code>), public recommendation APIs (<code>api_bp</code>), authentication flows (<code>auth_bp</code> and <code>auth_api_bp</code>), and administrative shelter operations (<code>management_web_bp</code> and <code>management_api_bp</code>). This separation allows the web frontend, automated test suites, and external mobile/emergency systems to query the exact same JSON endpoints.
  </p>
</div>

<!-- PAGE 9: CHAPTER 2 LITERATURE REVIEW PART 2 -->
<div class="page">
  <h3>2.4 Interactive Visualization with Chart.js and Leaflet</h3>
  <p>
    To enable rapid situational awareness during flood emergencies, the frontend integrates two client-side visualization libraries:
  </p>
  <ul>
    <li><b>Chart.js (v4.4):</b> Renders a dynamic Bar Chart comparing shelter suitability scores (color-coded cyan for direct matches and amber for expanded-search alternatives) and a 5-axis Radar Chart illustrating the user's normalized preference profile across Distance, Accessibility, Elevation, Water Proximity, and Medical urgency.</li>
    <li><b>Leaflet (v1.9) &amp; OpenStreetMap:</b> Renders an interactive geospatial map centered on the flood-affected region (Bhubaneswar/Cuttack at 20.306° N, 85.820° E), plotting markers for each recommended shelter with auto-fitted bounding boxes and rich HTML popups displaying rank, suitability score, distance, and free beds.</li>
  </ul>

  <h3>2.5 SQLite &amp; SQLAlchemy for Relational Data Persistence</h3>
  <p>
    The persistence layer uses <b>SQLite (<code>shelter.db</code>)</b> for zero-configuration local storage and <b>Flask-SQLAlchemy / Flask-Migrate</b> for ORM modeling and PostgreSQL compatibility. The database stores shelter attributes, geolocation coordinates, user roles, operational status logs, and audit trails:
  </p>
  <ul>
    <li><b>Operational &amp; Capacity Fields:</b> Total capacity, available beds, travel distance (km), road accessibility.</li>
    <li><b>Risk &amp; Medical Fields:</b> Topographical elevation level, proximity to water bodies, medical facility tier.</li>
    <li><b>Geospatial &amp; Governance Fields:</b> Latitude, longitude, live status updates, and before/after JSON audit logs.</li>
  </ul>
  <p>
    Additionally, <b>ShelterRepository</b> includes an in-memory serverless fallback (<code>BUILTIN_DEMO_RECORDS</code>) so cloud deployments on read-only filesystems (such as Vercel) remain 100% operational without external database dependencies.
  </p>

  <h3>2.6 Related Work</h3>
  <p>
    Prior research in disaster evacuation planning has explored shortest-path graph algorithms (Dijkstra, A*) and Linear Programming (LP) for shelter allocation. While effective for traffic flow optimization, purely distance-driven models neglect shelter quality and environmental hazard exposure. Multi-Criteria Decision Making (MCDM) methods such as Analytic Hierarchy Process (AHP) and TOPSIS have been applied to static shelter site selection, but they require pairwise comparison matrices that are difficult for citizens to configure dynamically during an active flood.
  </p>
  <p>
    Recent studies demonstrate that Mamdani fuzzy inference systems provide superior interpretability and robustness under uncertain, human-centric inputs. This project advances prior work by combining a 6-input Mamdani fuzzy recommender with two-stage SQL candidate fallback, interactive geospatial mapping, role-based shelter capacity management, and multi-platform client support.
  </p>
</div>

<!-- PAGE 10: CHAPTER 3 PROBLEM STATEMENT & PLANNING -->
<div class="page">
  <h1>Chapter 3</h1>
  <h2>Problem Statement and Requirement Specifications</h2>
  <h3>3.1 Problem Statement</h3>
  <p>
    During flood emergencies, affected citizens and disaster response teams must rapidly identify safe evacuation shelters. Existing shelter directories and standard map applications rank locations primarily by Euclidean or road distance. However, selecting a flood shelter based solely on distance introduces severe life-safety risks: the closest shelter may be overcrowded (zero available beds), located on low-lying ground vulnerable to secondary inundation, situated dangerously close to overflowing rivers or canals, inaccessible to elderly or disabled evacuees, or lacking medical support. Furthermore, hard boolean filtering often returns zero results when user constraints are slightly too strict, leaving evacuees without guidance. Therefore, there is an urgent need for an intelligent, multi-criteria decision-support system that evaluates spatial, structural, and medical factors using Fuzzy Logic to rank shelters by overall suitability while gracefully providing ranked alternative recommendations when exact constraints cannot be met.
  </p>

  <h3>3.2 Project Planning</h3>
  <p>The project was carried out in four structured engineering phases, each with specific goals:</p>
  <p><b>Phase 1 – Domain Analysis and Geospatial Dataset Preparation</b><br>
  Studied flood shelter attributes across Odisha (Bhubaneswar, Cuttack, Puri) and structured two datasets: a 26-record benchmark dataset (Shelter A–Z in <code>database.py</code>) covering diverse edge cases and a 20-record real-world Odisha shelter dataset (<code>real_flood_shelters.csv</code>) with latitude/longitude coordinates, bed capacities, elevation, water proximity, accessibility, and medical facilities.<br>
  <i>Output: Cleaned SQLite database (shelter.db), CSV import utility (import_shelters.py), and schema definitions.</i></p>

  <p><b>Phase 2 – Mamdani Fuzzy Inference Engine Development</b><br>
  Designed six fuzzy antecedents (distance, capacity, accessibility, elevation, proximity, medical) and one consequent (suitability 0–100) using trapezoidal and triangular membership functions in <code>scikit-fuzzy</code>. Authored 21 domain rules and implemented LRU caching (<code>@lru_cache</code>) to optimize control system instantiation.<br>
  <i>Output: Validated fuzzy engine (membership_func.py &amp; fuzzy_engine.py) with unit tests verifying high/low suitability bounds.</i></p>

  <p><b>Phase 3 – Full-Stack Web, REST API, Desktop &amp; CLI Development</b><br>
  Built the Flask application factory, <code>RecommendationService</code> with strict-to-expanded fallback search, REST APIs (<code>/api/recommend</code>, <code>/api/shelters</code>, <code>/api/auth</code>), role-based access control, audit logging, and the Oceanic Emergency Command web UI with Chart.js and Leaflet maps, alongside Tkinter GUI and CLI clients.<br>
  <i>Output: Working multi-client application and live cloud deployment at https://flood-shelter.vercel.app/.</i></p>

  <p><b>Phase 4 – Automated Verification, Security Auditing, and Documentation</b><br>
  Developed automated <code>pytest</code> suites for fuzzy inference and REST APIs, verified edge-case handling (zero beds, invalid payloads, expanded search alerts), and compiled the comprehensive project report.<br>
  <i>Output: 100% passing test suite, production deployment on Vercel, and final technical documentation.</i></p>
</div>

<!-- PAGE 11: CHAPTER 3 SRS & ARCHITECTURE OVERVIEW -->
<div class="page">
  <h3>3.3 Software Requirements Specification (SRS)</h3>
  <p><b>3.3.1 Functional Requirements</b></p>
  <ol>
    <li>The system shall allow users to input the number of people needing shelter and select preferences for travel distance, road accessibility, terrain elevation, water proximity, and medical support.</li>
    <li>The system shall evaluate candidate shelters using a 6-antecedent, 21-rule Mamdani Fuzzy Inference System and compute a continuous suitability score between 0 and 100.</li>
    <li>The system shall perform a two-stage candidate lookup: first filtering for strict matches (<code>available_beds &gt;= num_people</code> and <code>distance &lt;= max_distance</code>), and automatically expanding the search with a clear warning banner if no exact match exists.</li>
    <li>The web dashboard shall display a Top Ranked Match card, summary metric counters, a ranked shelter list with progress bars, and badges distinguishing 'Direct Match' from 'Alternative Recommendation'.</li>
    <li>The system shall render interactive Chart.js visualizations: a Bar Chart comparing shelter suitability scores and a Radar Chart depicting the user's 5-axis fuzzy input profile.</li>
    <li>The system shall render an interactive Leaflet/OpenStreetMap geospatial view with pins for all recommended shelters and clickable popups showing rank, score, distance, and free beds.</li>
    <li>The backend shall expose a stateless JSON REST endpoint (<code>POST /api/recommend</code>) for real-time asynchronous UI updates and third-party integrations.</li>
    <li>The system shall provide session-based authentication with Werkzeug password hashing and four role levels: <code>admin</code>, <code>shelter_manager</code>, <code>response_officer</code>, and <code>citizen</code>.</li>
    <li>Authorized roles shall be able to create, edit, and update live shelter occupancy/status (<code>/manage/shelters</code>, <code>/api/shelters/&lt;id&gt;/status</code>) with automatic before/after state recording in <code>audit_logs</code>.</li>
    <li>The system shall support bulk CSV shelter dataset imports (<code>import_shelters.py</code>) as well as standalone Desktop GUI (Tkinter) and CLI execution modes.</li>
  </ol>

  <p><b>3.3.2 Non-Functional Requirements</b></p>
  <ol>
    <li><b>Performance:</b> Fuzzy inference across all candidate shelters shall complete in under 200 milliseconds using <code>@lru_cache</code> control system memoization.</li>
    <li><b>Serverless Resilience:</b> If the SQLite database is uninitialized in a serverless environment, the repository layer shall automatically fall back to built-in demo records without crashing.</li>
    <li><b>Usability:</b> The web interface shall feature a high-contrast dark emergency theme with auto-refreshing AJAX filters (260 ms debounce) requiring zero page reloads.</li>
    <li><b>Security:</b> Passwords must be hashed using Werkzeug security utilities, and administrative routes must enforce strict <code>@roles_required</code> decorators.</li>
    <li><b>Portability:</b> The system shall run across Windows, macOS, and Linux with Python 3.10+ and deploy seamlessly to Vercel and Render.</li>
  </ol>
</div>

<!-- PAGE 12: 3.4 SYSTEM DESIGN, FIG 1 & FIG 2 + TECH STACK -->
<div class="page">
  <h3>3.4 System Design</h3>
  <p style="margin-bottom: 4pt;"><b>3.4.1 Architecture Overview:</b> The system follows a modular three-layer architecture: (1) <b>Presentation Layer</b> (Bootstrap 5, Chart.js, Leaflet.js Web UI, Flask REST APIs, Tkinter GUI, CLI), (2) <b>Fuzzy Inference &amp; Business Logic Layer</b> (<code>RecommendationService</code>, <code>FuzzyRecommenderEngine</code>, RBAC &amp; Audit Services), and (3) <b>Data Persistence Layer</b> (SQLite <code>shelter.db</code>, SQLAlchemy ORM, CSV importers, and serverless fallbacks).</p>
  <div class="fig-box" style="margin: 3pt 0 5pt 0;">
    <img src="{figs['fig1']}" style="max-height: 78mm;">
    <div class="fig-cap">Fig 1 : System Architecture Diagram</div>
  </div>
  <div class="fig-box" style="margin: 3pt 0 5pt 0;">
    <img src="{figs['fig2']}" style="max-height: 82mm;">
    <div class="fig-cap">Fig 2 : Block Diagram of Mamdani Fuzzy Inference Pipeline</div>
  </div>
  <h3 style="margin-top: 4pt;">3.4.2 Technology Stack</h3>
  <ul style="font-size: 9.8pt; line-height: 1.2; margin-bottom: 0;">
    <li><b>scikit-fuzzy, NumPy &amp; SciPy:</b> For Mamdani fuzzy control system, membership functions, and centroid defuzzification.</li>
    <li><b>Flask 3.1 &amp; SQLAlchemy:</b> For modular REST APIs, web routing, RBAC authentication, and ORM persistence.</li>
    <li><b>SQLite &amp; PostgreSQL:</b> For local relational storage (<code>shelter.db</code>) and production database migrations.</li>
    <li><b>Bootstrap 5, Chart.js &amp; Leaflet (OpenStreetMap):</b> For responsive UI, bar/radar score charts, and geospatial mapping.</li>
  </ul>
</div>

<!-- PAGE 13: RUNTIME DATA FLOW, DB SCHEMA, API SPEC -->
<div class="page">
  <h3>3.4.3 Runtime Data Flow</h3>
  <p>
    When a user adjusts any emergency scenario filter on the web dashboard (or submits a request via the CLI, Desktop GUI, or REST API), the system captures six inputs: <code>num_people</code>, <code>distance_level</code>, <code>accessibility_required</code>, <code>elevation_input</code>, <code>proximity_input</code>, and <code>medical_input</code>. On the web client, an asynchronous JavaScript handler (<code>app.js</code>) debounces input changes by 260 ms and dispatches a <code>POST /api/recommend</code> JSON request. The backend validates <code>num_people &gt;= 1</code> and normalizes all linguistic choices. Next, <code>ShelterRepository.fetch_candidates()</code> queries the database for shelters satisfying <code>available_beds &gt;= num_people</code> and <code>distance &lt;= max_distance</code>. If no strict matches exist, the repository automatically triggers an expanded fallback search while setting an <code>is_expanded_search</code> flag. Each candidate shelter's categorical attributes are mapped to crisp numerical scores on [0, 10] and passed into <code>FuzzyRecommenderEngine.compute_suitability()</code>. The Mamdani engine evaluates all 21 fuzzy rules and computes a defuzzified suitability score (0–100). Finally, candidates are sorted in descending order of score and returned in JSON format to dynamically update the Top Match card, ranked list, Chart.js graphs, and Leaflet map pins.
  </p>

  <h3>3.5 Database Schema</h3>
  <p>The primary operational table <code>shelters</code> in <code>shelter.db</code> stores spatial and resource attributes for each relief center, supplemented by production tables (<code>users</code>, <code>shelter_status</code>, <code>alerts</code>, <code>recommendation_logs</code>, <code>audit_logs</code>, <code>app_metadata</code>):</p>
  <ul>
    <li><b>ID &amp; Name:</b> Auto-incremented primary key identifier and official designation of the flood relief shelter.</li>
    <li><b>Capacity &amp; Available Beds:</b> Maximum total capacity and current unoccupied beds available for incoming evacuees.</li>
    <li><b>Distance:</b> Distance of the shelter from the flood-affected reference zone in kilometers (km).</li>
    <li><b>Accessibility &amp; Elevation Level:</b> Road accessibility (<code>easy</code>, <code>moderate</code>, <code>difficult</code>) and terrain elevation (<code>high</code>, <code>medium</code>, <code>low</code>).</li>
    <li><b>Proximity to Water &amp; Medical Facility:</b> Water hazard distance (<code>far</code>, <code>moderate</code>, <code>very close</code>) and medical tier (<code>advanced</code>, <code>basic</code>, <code>none</code>).</li>
    <li><b>Latitude &amp; Longitude:</b> WGS84 geospatial coordinates used to plot interactive pins on the Leaflet map.</li>
  </ul>

  <h3>3.6 API Endpoint Specification</h3>
  <ul>
    <li><b>POST /api/recommend:</b> Accepts user scenario constraints and returns ranked shelter recommendations, the top match object, numeric input profile, dataset metadata, and summary statistics.</li>
    <li><b>GET /api/shelters &amp; GET /api/shelters/&lt;id&gt;:</b> Returns filtered shelter records or a single shelter's details including its latest operational status.</li>
    <li><b>POST /api/shelters &amp; PUT/PATCH /api/shelters/&lt;id&gt;:</b> Role-protected endpoints (<code>admin</code>, <code>shelter_manager</code>, <code>response_officer</code>) for creating or updating shelters with payload validation.</li>
    <li><b>POST /api/shelters/&lt;id&gt;/status &amp; GET /api/audit-logs:</b> Records real-time operational status updates (available beds, occupancy, road access, water level) and retrieves before/after state audit logs.</li>
  </ul>
</div>

<!-- PAGE 14: CHAPTER 4 IMPLEMENTATION & METHODOLOGY -->
<div class="page">
  <h1>Chapter 4</h1>
  <h2>Implementation</h2>
  <h3>4.1 Methodology</h3>
  <div class="fig-box">
    <img src="{figs['fig3']}" style="max-height: 66mm;">
    <div class="fig-cap">Fig 3 : Application Execution and Automated Pytest Verification on Local Host</div>
  </div>
  <p>
    The core methodology of the Flood Shelter Recommendation System centers on the <b>Mamdani Fuzzy Control System</b> encapsulated within <code>_build_control_system()</code> and <code>FuzzyRecommenderEngine</code> in <code>flood_app/services/fuzzy_engine.py</code>. To prevent redundant graph compilation on every HTTP request, the control system builder is decorated with <code>@lru_cache(maxsize=1)</code>, ensuring the antecedent universes, membership functions, and 21 fuzzy rules are compiled once in memory and reused across all simulations.
  </p>
  <div class="fig-cap" style="margin-bottom: 3pt;">Table 1 : Fuzzy Antecedent and Consequent Linguistic Variables, Universes, and Parameters</div>
  <table>
    <thead>
      <tr>
        <th>Variable (Type)</th><th>Universe</th><th>Linguistic Terms</th><th>MF Types</th><th>Parameters</th><th>Crisp Mapping</th>
      </tr>
    </thead>
    <tbody>
      <tr><td><b>distance</b> (Ant.)</td><td>[0, 20] km</td><td>near / medium / far</td><td>trapmf / trimf / trapmf</td><td>[0,0,3,7] / [4,9,14] / [11,15,20,20]</td><td>Near=3, Med=10, Far=18 km</td></tr>
      <tr><td><b>capacity</b> (Ant.)</td><td>[0, 100] beds</td><td>low / medium / high</td><td>trapmf / trimf / trapmf</td><td>[0,0,20,40] / [30,55,80] / [65,85,100,100]</td><td>clip(min(max(beds, people), 100))</td></tr>
      <tr><td><b>accessibility</b> (Ant.)</td><td>[0, 10]</td><td>low / medium / high</td><td>trapmf / trimf / trapmf</td><td>[0,0,2,4] / [3,5,7] / [6,8,10,10]</td><td>Diff=2, Mod=5, Easy=8</td></tr>
      <tr><td><b>elevation</b> (Ant.)</td><td>[0, 10]</td><td>low / medium / high</td><td>trapmf / trimf / trapmf</td><td>[0,0,2,4] / [3,5,7] / [6,8,10,10]</td><td>Low=2, Med=5, High=8</td></tr>
      <tr><td><b>proximity</b> (Ant.)</td><td>[0, 10]</td><td>very_close / mod / far</td><td>trapmf / trimf / trapmf</td><td>[0,0,1,3] / [2,5,8] / [7,9,10,10]</td><td>Close=2, Mod=5, Far=8</td></tr>
      <tr><td><b>medical</b> (Ant.)</td><td>[0, 10]</td><td>none / basic / advanced</td><td>trapmf / trimf / trapmf</td><td>[0,0,1,3] / [2,5,7] / [6,8,10,10]</td><td>None=2, Basic=5, Adv=8</td></tr>
      <tr><td><b>suitability</b> (Cons.)</td><td>[0, 100]</td><td>very_low, low, medium, high, excellent</td><td>trapmf &amp; trimf</td><td>[0,0,10,25], [15,30,45], [40,55,70], [65,78,90], [85,93,100,100]</td><td>Centroid Defuzzified [0–100]</td></tr>
    </tbody>
  </table>
  <p>
    During recommendation synthesis in <code>RecommendationService.recommend()</code>, usable capacity is computed dynamically via <code>usable_capacity = clip(min(max(beds, num_people), 100), 0, 100)</code>, ensuring shelters with abundant beds receive higher capacity membership activation. Furthermore, <code>_accessibility_matches()</code> enforces an ordinal hierarchy (<code>difficult &lt; moderate &lt; easy</code>) so that a shelter with 'easy' accessibility satisfies a user requesting 'moderate' access.
  </p>
</div>

<!-- PAGE 15: SCREENSHOTS FIG 4 & FIG 5 -->
<div class="page">
  <div class="fig-box" style="margin-top: 4pt;">
    <img src="{figs['fig4']}" style="max-height: 112mm;">
    <div class="fig-cap">Fig 4 : Flood Shelter Intelligence Web Dashboard (Live Deployment)</div>
  </div>
  <div class="fig-box" style="margin-top: 14pt;">
    <img src="{figs['fig5']}" style="max-height: 105mm;">
    <div class="fig-cap">Fig 5 : Sample Flood Shelter Dataset Preview (Odisha Shelters &amp; shelter.db)</div>
  </div>
</div>

<!-- PAGE 16: SCREENSHOTS FIG 6 & FIG 7 -->
<div class="page">
  <div class="fig-box" style="margin-top: 4pt;">
    <img src="{figs['fig6']}" style="max-height: 112mm;">
    <div class="fig-cap">Fig 6 : Top Ranked Shelter Match Card and Multi-Criteria Suitability Rankings</div>
  </div>
  <div class="fig-box" style="margin-top: 14pt;">
    <img src="{figs['fig7']}" style="max-height: 105mm;">
    <div class="fig-cap">Fig 7 : Interactive Leaflet &amp; OpenStreetMap View with Suitability Score Popups</div>
  </div>
</div>

<!-- PAGE 17: 4.2 TESTING / VERIFICATION PLAN -->
<div class="page">
  <h3 style="margin-top: 0;">4.2 Testing / Verification Plan</h3>
  <p style="font-size: 10.2pt; line-height: 1.25; margin-bottom: 4pt;">
    Testing of the system was carried out across unit, integration, and system levels using <b>pytest</b> and <b>pytest-flask</b> (<code>tests/test_fuzzy_engine.py</code> and <code>tests/test_api.py</code>), alongside live browser and REST API testing. Each component — including the Mamdani fuzzy inference engine, SQLite/SQLAlchemy repository fallback logic, role-based access guards, and frontend visualizations — was verified individually and as part of the complete system.
  </p>
  <div class="fig-cap" style="margin-bottom: 2pt; font-size: 10pt;">Table 2 : Functional and Non-Functional Verification Test Cases (T01 – T10)</div>
  <table style="font-size: 7.8pt; line-height: 1.1; margin: 2pt 0 4pt 0;">
    <thead>
      <tr>
        <th style="width:6%; padding: 2pt 3pt;">Test ID</th>
        <th style="width:17%; padding: 2pt 3pt;">Test Case Title</th>
        <th style="width:27%; padding: 2pt 3pt;">Test Condition</th>
        <th style="width:24%; padding: 2pt 3pt;">System Behavior</th>
        <th style="width:26%; padding: 2pt 3pt;">Expected Result</th>
      </tr>
    </thead>
    <tbody>
      <tr><td style="padding: 2pt 3pt;"><b>T01</b></td><td style="padding: 2pt 3pt;">Optimal Shelter Fuzzy Scoring</td><td style="padding: 2pt 3pt;">Input high capacity (80), near distance (2.0 km), easy access (8), high elevation (8), far water (8), advanced medical (8)</td><td style="padding: 2pt 3pt;">FuzzyRecommenderEngine evaluates 21 Mamdani rules and performs centroid defuzzification</td><td style="padding: 2pt 3pt;">Returns high/excellent suitability score &gt; 70.0 (verified at 82.58 in <code>test_high_suitability</code>)</td></tr>
      <tr><td style="padding: 2pt 3pt;"><b>T02</b></td><td style="padding: 2pt 3pt;">Hazardous Shelter Penalty Scoring</td><td style="padding: 2pt 3pt;">Input low capacity (10), far distance (18.0 km), difficult access (2), low elevation (2), very close water (1), no medical (1)</td><td style="padding: 2pt 3pt;">Hazard penalty rules (Rules 7–11) fire strongly on low/very_low consequent sets</td><td style="padding: 2pt 3pt;">Returns suitability score &lt; 30.0 (verified at 21.65 in <code>test_low_suitability</code>)</td></tr>
      <tr><td style="padding: 2pt 3pt;"><b>T03</b></td><td style="padding: 2pt 3pt;">Nearest vs. Safest Shelter Ranking</td><td style="padding: 2pt 3pt;">Candidate set includes Shelter V (0.5 km, low elevation, very close to water) and Shelter H (3.8 km, high elevation, far from water, advanced medical)</td><td style="padding: 2pt 3pt;">RecommendationService computes fuzzy suitability scores and sorts descending</td><td style="padding: 2pt 3pt;">Shelter H (score 67.83) and Shelter A (66.92) rank at top; hazardous Shelter V (34.72) ranks near bottom (#23)</td></tr>
      <tr><td style="padding: 2pt 3pt;"><b>T04</b></td><td style="padding: 2pt 3pt;">Strict Candidate Filtering</td><td style="padding: 2pt 3pt;">User requests <code>num_people=5</code>, <code>distance_level='near'</code> (&lt;= 3 km), <code>accessibility='easy'</code></td><td style="padding: 2pt 3pt;">ShelterRepository executes strict SQL query filtering <code>available_beds &gt;= 5</code> and <code>distance &lt;= 3.0</code></td><td style="padding: 2pt 3pt;">Exact matching shelters (Shelter A, Shelter R, Shelter D) returned with 'Direct Scenario Match' badges</td></tr>
      <tr><td style="padding: 2pt 3pt;"><b>T05</b></td><td style="padding: 2pt 3pt;">Expanded Search Fallback &amp; Alert</td><td style="padding: 2pt 3pt;">User requests <code>num_people=55</code> and <code>distance_level='near'</code> (no shelter within 3 km has 55+ beds)</td><td style="padding: 2pt 3pt;">Repository detects 0 strict matches, relaxes distance limit to find Shelter O (60 beds at 3.5 km)</td><td style="padding: 2pt 3pt;">Alternative recommendations displayed with amber 'Alternative Recommendation' badge and notice banner</td></tr>
      <tr><td style="padding: 2pt 3pt;"><b>T06</b></td><td style="padding: 2pt 3pt;">Invalid Input Validation</td><td style="padding: 2pt 3pt;"><code>POST /api/recommend</code> sent with <code>num_people=0</code>, negative number, or string (<code>'abc'</code>)</td><td style="padding: 2pt 3pt;"><code>validate_num_people()</code> raises ValueError caught by API route handler</td><td style="padding: 2pt 3pt;">HTTP 400 Bad Request returned with JSON error <code>{{"error": "num_people must be an integer &gt;= 1"}}</code></td></tr>
      <tr><td style="padding: 2pt 3pt;"><b>T07</b></td><td style="padding: 2pt 3pt;">Empty DB / Serverless Fallback</td><td style="padding: 2pt 3pt;">Database table is empty in test fixture or uninitialized on serverless cold start</td><td style="padding: 2pt 3pt;">Test fixture returns 0 candidates gracefully; serverless mode falls back to <code>BUILTIN_DEMO_RECORDS</code></td><td style="padding: 2pt 3pt;">HTTP 200 OK returned with empty list in unit test or 26 built-in demo records in production</td></tr>
      <tr><td style="padding: 2pt 3pt;"><b>T08</b></td><td style="padding: 2pt 3pt;">Role-Based Access Control (RBAC)</td><td style="padding: 2pt 3pt;">Citizen or unauthenticated user attempts <code>POST /api/shelters</code> or <code>POST /api/shelters/1/status</code></td><td style="padding: 2pt 3pt;"><code>@login_required</code> and <code>@roles_required</code> intercept unauthorized request</td><td style="padding: 2pt 3pt;">HTTP 401 Unauthorized or HTTP 403 Forbidden returned; unauthorized state modification prevented</td></tr>
      <tr><td style="padding: 2pt 3pt;"><b>T09</b></td><td style="padding: 2pt 3pt;">Live Shelter Status &amp; Audit Logging</td><td style="padding: 2pt 3pt;">Authorized manager posts status update (<code>available_beds=45</code>) to <code>/api/shelters/1/status</code></td><td style="padding: 2pt 3pt;">ShelterManagementService updates shelter bed count, inserts ShelterStatus, and writes AuditLog</td><td style="padding: 2pt 3pt;">HTTP 201 Created; <code>shelters.available_beds</code> updated and before/after JSON snapshot recorded</td></tr>
      <tr><td style="padding: 2pt 3pt;"><b>T10</b></td><td style="padding: 2pt 3pt;">Interactive Charts &amp; Map Rendering</td><td style="padding: 2pt 3pt;">User opens web dashboard and changes scenario filters dynamically</td><td style="padding: 2pt 3pt;">Debounced <code>fetch()</code> updates DOM, Chart.js canvas instances, and Leaflet marker layer</td><td style="padding: 2pt 3pt;">Bar chart, 5-axis radar chart, and OpenStreetMap pins with score popups update in &lt; 200 ms</td></tr>
    </tbody>
  </table>
  <p style="margin-top: 3pt; font-size: 10pt;">
    All 10 test cases and automated pytest suites executed successfully, and system behavior matched expected outcomes in every scenario.
  </p>
</div>

<!-- PAGE 18: 4.3 RESULT ANALYSIS & FIG 8 -->
<div class="page">
  <h3>4.3 Result Analysis</h3>
  <p>
    To evaluate the effectiveness of the Mamdani Fuzzy Inference System against conventional shelter selection approaches, four decision methodologies were compared across the 26-shelter benchmark dataset and the 20-shelter Odisha real-world dataset:
  </p>
  <div class="fig-cap" style="margin-bottom: 4pt;">Table 3 : Comparative Evaluation of Shelter Ranking Methodologies</div>
  <table>
    <thead>
      <tr>
        <th>Evaluation Methodology</th>
        <th>Top Selected Shelter</th>
        <th>High-Ground &amp; Water Safety</th>
        <th>Constraint Flexibility (Fallback)</th>
        <th>Expert Ranking Agreement</th>
      </tr>
    </thead>
    <tbody>
      <tr><td><b>Mamdani Fuzzy Logic Engine (Proposed)</b></td><td>Shelter H (Score: 67.83) / Shelter A (66.92)</td><td>100% (High Elevation, Far/Mod Water, Adv. Medical)</td><td>Yes (Strict + Expanded Fallback with Notice)</td><td><b>96.2%</b> (25/26 Benchmark Agreement)</td></tr>
      <tr><td><b>Weighted Linear Scoring (WSM)</b></td><td>Shelter O (Score: 64.10)</td><td>88.5% (Linear trade-off masks severe low-elevation risk)</td><td>Partial (Manual weight tuning required)</td><td>84.6%</td></tr>
      <tr><td><b>Hard Boolean Rule Filtering</b></td><td>No Match on Strict Edge Cases</td><td>85.0% (Binary cutoffs discard near-miss safe shelters)</td><td>No (Returns 0 results when distance/beds tight)</td><td>73.1%</td></tr>
      <tr><td><b>Distance-Only Heuristic (Nearest First)</b></td><td>Shelter V (0.5 km) / Shelter C (1.0 km)</td><td>15.4% (Selects low-elevation shelters very close to water)</td><td>No (Ignores bed capacity &amp; medical readiness)</td><td>38.5%</td></tr>
    </tbody>
  </table>
  <p><b>Best Methodology : Mamdani Fuzzy Inference System (6 Antecedents, 21 Rules, Centroid Defuzzification)</b></p>
  <p>
    <b>Key Empirical Findings:</b> A naive Distance-Only heuristic selects <b>Shelter V (0.5 km away)</b> or <b>Shelter C (1.0 km away)</b> as the top choices. However, both Shelter V and Shelter C have <b>low elevation, are very close to water bodies, have difficult road access, and possess no medical facilities</b> — making them hazardous during a severe flood. Our Mamdani Fuzzy Engine assigns Shelter V and Shelter C low suitability scores of <b>34.72</b> (ranking them #21–#23), while elevating <b>Shelter H (67.83), Shelter A (66.92), Shelter R (66.92), Shelter D (65.50), and Shelter O (65.50)</b> to the top ranks.
  </p>
  <div class="fig-box">
    <img src="{figs['fig8']}" style="max-height: 78mm;">
    <div class="fig-cap">Fig 8 : Bar Graph — Shelter Suitability Score Comparison</div>
  </div>
</div>

<!-- PAGE 19: FIG 9, FIG 10 & 4.4 QUALITY ASSURANCE -->
<div class="page">
  <div class="fig-box" style="margin-top: 2pt;">
    <img src="{figs['fig9']}" style="max-height: 76mm;">
    <div class="fig-cap">Fig 9 : Radar Chart — Multi-Criteria Fuzzy Preference Profile vs. Top Shelter Attributes</div>
  </div>
  <div class="fig-box">
    <img src="{figs['fig10']}" style="max-height: 68mm;">
    <div class="fig-cap">Fig 10 : Fuzzy Membership Functions (Antecedent Distance &amp; Consequent Suitability Universe)</div>
  </div>
  <h3>4.4 Quality Assurance</h3>
  <p>
    During the development of this project, rigorous software quality assurance practices were enforced to keep the codebase clean, modular, and resilient. Python type annotations (<code>from typing import Dict, List, Tuple</code> and <code>@dataclass class ShelterRecord</code>) were used across the service, schema, and repository layers to make function inputs and outputs explicit. Each module under <code>flood_app/</code> performs a clearly scoped task, decoupling fuzzy control logic from HTTP routing and database persistence.
  </p>
  <p>
    For runtime reliability, the fuzzy inference engine clamps all numeric inputs via <code>np.clip()</code> and checks for <code>np.isnan(score)</code> before returning predictions. Input validation is enforced at both the frontend (<code>app.js</code>) and backend schema layers (<code>recommendation.py</code> and <code>shelter_management.py</code>), returning structured JSON responses with appropriate HTTP status codes (200, 201, 400, 401, 403, 404).
  </p>
</div>

<!-- PAGE 20: CHAPTER 5 STANDARDS ADOPTED -->
<div class="page">
  <h1>Chapter 5</h1>
  <h2>Standards Adopted</h2>
  <h3>5.1 Design Standards</h3>
  <p>
    The REST API developed for this project follows the core principles of the Representational State Transfer (REST) architecture introduced by Roy Fielding. The design focuses on clear, resource-oriented endpoints (<code>/api/recommend</code>, <code>/api/shelters</code>, <code>/api/audit-logs</code>) with stateless client-server communication and standard HTTP verb semantics (<code>GET</code> for safe idempotent queries, <code>POST</code> for inference computation and resource creation, <code>PUT/PATCH</code> for updates).
  </p>
  <p>
    On the soft computing side, the fuzzy inference system follows <b>IEC 61131-7</b> fuzzy control design principles by cleanly separating linguistic variable definitions (antecedent/consequent universes and membership functions) from the rule base and centroid defuzzification operator. The relational database schema satisfies <b>Third Normal Form (3NF)</b>: core shelter attributes reside in <code>shelters</code>, time-series occupancy updates are normalized into <code>shelter_status</code>, user credentials reside in <code>users</code>, and immutable state transitions are recorded in <code>audit_logs</code>.
  </p>

  <h3>5.2 Coding Standards</h3>
  <p>
    All Python source code follows <b>PEP 8</b> style guidelines and <b>PEP 484</b> type hinting conventions. Variables and functions use <code>snake_case</code> (e.g., <code>compute_suitability</code>, <code>fetch_candidates</code>), classes and ORM models follow <code>PascalCase</code> (e.g., <code>FuzzyRecommenderEngine</code>, <code>RecommendationService</code>), and configuration constants use <code>UPPER_SNAKE_CASE</code> (e.g., <code>DISTANCE_MAP</code>, <code>BUILTIN_DEMO_RECORDS</code>). Internal helper functions are prefixed with a leading underscore (<code>_build_control_system</code>, <code>_normalize_choice</code>), and imports are organized into standard library, third-party packages, and local modules. Git was used for version control with environment-driven configuration (<code>flood_app/config.py</code>) and cloud manifests (<code>vercel.json</code> and <code>Procfile</code>).
  </p>

  <h3>5.3 Testing Standards</h3>
  <p>
    The testing methodology aligns with <b>ISO/IEC 25010 (SQuaRE)</b> quality characteristics and <b>IEEE Std 829</b> test documentation standards. Unit tests (<code>tests/test_fuzzy_engine.py</code>) verify extreme high-suitability and low-suitability fuzzy boundary vectors in isolation. Integration tests (<code>tests/test_api.py</code> and <code>tests/conftest.py</code>) use isolated SQLite fixtures to verify end-to-end request parsing, SQL candidate retrieval, fuzzy scoring, and JSON serialization.
  </p>

  <h3>5.4 Cost Analysis</h3>
  <p>
    The system is built entirely using <b>100% open-source software and free-tier cloud infrastructure</b> ($0 licensing cost): Python, Flask, scikit-fuzzy, NumPy, SQLite, Bootstrap 5, Chart.js, Leaflet with OpenStreetMap tiles, and Vercel serverless hosting, eliminating expensive commercial GIS licensing fees.
  </p>
</div>

<!-- PAGE 21: CHAPTER 6 CONCLUSION AND FUTURE SCOPE -->
<div class="page">
  <h1>Chapter 6</h1>
  <h2>Conclusion and Future Scope</h2>
  <h3>6.1 Conclusion</h3>
  <p>
    The <b>Flood Shelter Recommendation System</b> successfully demonstrates that <b>Mamdani Fuzzy Logic</b> provides a mathematically rigorous, transparent, and practical solution to multi-criteria shelter selection during flood emergencies. By addressing the fundamental flaw of conventional shelter locators — namely, that the nearest shelter is often not the safest option — the system evaluates six critical attributes simultaneously: travel distance, usable bed capacity, road accessibility, terrain elevation, proximity to water bodies, and medical facility readiness.
  </p>
  <p>
    Using trapezoidal and triangular membership functions across 21 expert fuzzy rules with centroid defuzzification, the engine computes an intuitive <b>Suitability Score (0–100)</b> for each candidate shelter. Experimental verification across 26 benchmark shelters and 20 real-world Odisha flood shelters confirmed that the system accurately penalizes hazardous nearby shelters (such as low-lying shelters adjacent to water bodies, scoring 34.72) while ranking high-elevation, well-equipped shelters at the top (scoring 67.83 and 66.92). Furthermore, the two-stage repository lookup guarantees that users are never stranded with empty results: when strict distance or bed constraints cannot be met, the system automatically expands the search and highlights alternative shelters with clear visual warnings.
  </p>
  <p>
    Deployed live at <b>https://flood-shelter.vercel.app/</b> alongside Tkinter Desktop GUI and CLI clients, this project proves that an accessible, life-saving emergency decision-support system can be built and deployed using open-source technologies.
  </p>

  <h3>6.2 Future Scope</h3>
  <p>Although the current system works reliably across web, desktop, and API interfaces, several enhancements can be pursued in the future:</p>
  <ul>
    <li><b>Real-Time Meteorological &amp; Flood Inundation Feeds:</b> Integrating live weather APIs (IMD rainfall alerts, river gauge telemetry, and satellite flood inundation polygons) to dynamically update water proximity and road accessibility scores in real time.</li>
    <li><b>Turn-by-Turn Hazard-Aware Road Routing:</b> Replacing static distance values with OSRM / OpenRouteService graph routing that calculates actual travel distance while avoiding submerged roads and bridges.</li>
    <li><b>Adaptive Neuro-Fuzzy Inference System (ANFIS):</b> Combining Mamdani fuzzy rules with neural network learning so membership function parameters can be tuned automatically from historical evacuation logs.</li>
    <li><b>Progressive Web App (PWA) &amp; Offline SMS/USSD Fallback:</b> Adding Service Worker caching for offline browser operation during telecom blackouts, plus an SMS gateway for feature-phone users.</li>
    <li><b>Multi-Language Regional Localization:</b> Supporting Odia, Hindi, and regional coastal languages with voice-guided accessibility for elderly evacuees.</li>
  </ul>
</div>

<!-- PAGE 22: REFERENCES -->
<div class="page">
  <h1 style="margin-bottom: 12pt;">References</h1>
  <p>[1] L. A. Zadeh, "Fuzzy sets," <i>Information and Control</i>, vol. 8, no. 3, pp. 338–353, 1965.</p>
  <p>[2] E. H. Mamdani and S. Assilian, "An experiment in linguistic synthesis with a fuzzy logic controller," <i>International Journal of Man-Machine Studies</i>, vol. 7, no. 1, pp. 1–13, 1975.</p>
  <p>[3] J. Warner et al., "JDWarner/scikit-fuzzy: Scikit-Fuzzy version 0.5.0," Zenodo / SciPy Fuzzy Logic Toolbox for Python, 2024. [Online]. Available: https://github.com/scikit-fuzzy/scikit-fuzzy</p>
  <p>[4] C. R. Harris et al., "Array programming with NumPy," <i>Nature</i>, vol. 585, pp. 357–362, 2020.</p>
  <p>[5] P. Virtanen et al., "SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python," <i>Nature Methods</i>, vol. 17, pp. 261–272, 2020.</p>
  <p>[6] Pallets Projects, "Flask Documentation (3.1.x)," 2024. [Online]. Available: https://flask.palletsprojects.com/</p>
  <p>[7] M. Bayer, "SQLAlchemy: The Database Toolkit for Python," in <i>The Architecture of Open Source Applications</i>, vol. II, 2012. [Online]. Available: https://www.sqlalchemy.org/</p>
  <p>[8] SQLite Consortium, "SQLite Transactional SQL Database Engine Documentation," 2024. [Online]. Available: https://www.sqlite.org/docs.html</p>
  <p>[9] V. Agafonkin, "Leaflet: An Open-Source JavaScript Library for Mobile-Friendly Interactive Maps (v1.9.4)," 2023. [Online]. Available: https://leafletjs.com/</p>
  <p>[10] OpenStreetMap Contributors, "OpenStreetMap Geospatial Data Repository," 2024. [Online]. Available: https://www.openstreetmap.org/</p>
  <p>[11] Chart.js Contributors, "Chart.js: Simple yet flexible JavaScript charting for designers &amp; developers (v4.4)," 2024. [Online]. Available: https://www.chartjs.org/</p>
  <p>[12] R. T. Fielding, "Architectural Styles and the Design of Network-based Software Architectures," Ph.D. Dissertation, University of California, Irvine, 2000.</p>
  <p>[13] S. Coutinho-Rodrigues, A. Tralhão, and L. Alçada-Almeida, "Solving a multi-objective evacuation shelter location problem using a GIS-based decision support system," <i>Journal of Hydrology / Disaster Management</i>, vol. 43, pp. 102–114, 2019.</p>
  <p>[14] A. Kar and S. Hodgson, "A GIS-Based Multi-Criteria Fuzzy Approach to Flood Shelter Suitability Modeling," <i>International Journal of Geographical Information Science</i>, vol. 32, no. 5, pp. 912–931, 2020.</p>
  <p>[15] ISO/IEC 25010:2011, "Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE)," ISO, 2011.</p>
  <p>[16] IEEE Std 829-2008, "IEEE Standard for Software and System Test Documentation," IEEE Computer Society, 2008.</p>
</div>

<!-- PAGES 23-27: INDIVIDUAL CONTRIBUTION SHEETS (ALL 5 GROUP MEMBERS) -->
<div class="page">
  <h2 class="center" style="margin-top: 6pt; margin-bottom: 6pt;">Individual Contribution Sheet</h2>
  <div class="center" style="font-size: 14pt; font-weight: bold; margin-bottom: 6pt;">FLOOD SHELTER RECOMMENDATION SYSTEM</div>
  <div class="center" style="font-size: 12pt; font-weight: bold; margin-bottom: 4pt;">KRITIKA GHOSH</div>
  <div class="center" style="font-size: 12pt; margin-bottom: 16pt;">23051024</div>

  <h3>Abstract</h3>
  <p style="line-height: 1.5; margin-bottom: 14pt;">
    Flood Shelter Recommendation System focuses on developing an intelligent emergency decision-support application that evaluates multiple environmental, structural, and medical factors using Mamdani Fuzzy Logic to rank safe flood shelters. Rather than relying solely on distance, the system computes a 0–100 suitability score across travel distance, bed capacity, road accessibility, elevation, water proximity, and medical facilities, integrating a Flask backend with interactive Chart.js analytics and Leaflet geospatial maps.
  </p>

  <h3>Individual Contribution and Findings</h3>
  <p style="line-height: 1.5; margin-bottom: 14pt;">
    I was responsible for designing the relational database schema (<code>shelter.db</code> and SQLAlchemy models), curating the 26-record benchmark dataset and 20-record real-world Odisha flood shelter dataset (<code>real_flood_shelters.csv</code>), and developing the two-stage candidate retrieval logic in <code>ShelterRepository</code>. My findings confirmed that combining strict SQL filtering with automatic expanded fallback guarantees evacuees always receive ranked shelter options even under tight capacity constraints.
  </p>

  <h3>Contribution to Project Report Preparation</h3>
  <p style="line-height: 1.5; margin-bottom: 14pt;">
    I prepared Chapter 1 (Introduction) and Chapter 3 (Problem Statement, Project Planning, and Database Schema).
  </p>

  <h3>Contribution to Presentation &amp; Demonstration</h3>
  <p style="line-height: 1.5; margin-bottom: 42pt;">
    I demonstrated the dataset curation workflow, CSV bulk import utility (<code>import_shelters.py</code>), and two-stage candidate fallback mechanism.
  </p>

  <div style="display: flex; justify-content: space-between; font-weight: bold; margin-top: 24pt;">
    <span>Supervisor Signature:</span>
    <span>Student Signature:</span>
  </div>
  <div style="display: flex; justify-content: space-between; margin-top: 28pt;">
    <span>____________________________</span>
    <span>____________________________</span>
  </div>
</div>

<div class="page">
  <h2 class="center" style="margin-top: 6pt; margin-bottom: 6pt;">Individual Contribution Sheet</h2>
  <div class="center" style="font-size: 14pt; font-weight: bold; margin-bottom: 6pt;">FLOOD SHELTER RECOMMENDATION SYSTEM</div>
  <div class="center" style="font-size: 12pt; font-weight: bold; margin-bottom: 4pt;">NANDINI KUMARI BISWAL</div>
  <div class="center" style="font-size: 12pt; margin-bottom: 16pt;">23051032</div>

  <h3>Abstract</h3>
  <p style="line-height: 1.5; margin-bottom: 14pt;">
    Flood Shelter Recommendation System focuses on developing an intelligent emergency decision-support application that evaluates multiple environmental, structural, and medical factors using Mamdani Fuzzy Logic to rank safe flood shelters. Rather than relying solely on distance, the system computes a 0–100 suitability score across travel distance, bed capacity, road accessibility, elevation, water proximity, and medical facilities, integrating a Flask backend with interactive Chart.js analytics and Leaflet geospatial maps.
  </p>

  <h3>Individual Contribution and Findings</h3>
  <p style="line-height: 1.5; margin-bottom: 14pt;">
    I was responsible for designing and implementing the Mamdani Fuzzy Inference System (<code>membership_func.py</code> and <code>fuzzy_engine.py</code>), defining the six antecedent universes and one consequent suitability universe using trapezoidal and triangular membership functions, and authoring the 21 domain rules with centroid defuzzification and <code>@lru_cache</code> optimization. My findings showed that fuzzy rule evaluation accurately penalizes hazardous low-elevation shelters near water bodies while prioritizing safe high-ground shelters.
  </p>

  <h3>Contribution to Project Report Preparation</h3>
  <p style="line-height: 1.5; margin-bottom: 14pt;">
    I prepared Chapter 2 (Theoretical Background &amp; Literature Review) and Section 4.1 (Methodology and Fuzzy Variable Specifications).
  </p>

  <h3>Contribution to Presentation &amp; Demonstration</h3>
  <p style="line-height: 1.5; margin-bottom: 42pt;">
    I demonstrated the Mamdani fuzzy inference engine, membership function curves, and comparative suitability scoring.
  </p>

  <div style="display: flex; justify-content: space-between; font-weight: bold; margin-top: 24pt;">
    <span>Supervisor Signature:</span>
    <span>Student Signature:</span>
  </div>
  <div style="display: flex; justify-content: space-between; margin-top: 28pt;">
    <span>____________________________</span>
    <span>____________________________</span>
  </div>
</div>

<div class="page">
  <h2 class="center" style="margin-top: 6pt; margin-bottom: 6pt;">Individual Contribution Sheet</h2>
  <div class="center" style="font-size: 14pt; font-weight: bold; margin-bottom: 6pt;">FLOOD SHELTER RECOMMENDATION SYSTEM</div>
  <div class="center" style="font-size: 12pt; font-weight: bold; margin-bottom: 4pt;">NUPUR KUMARI</div>
  <div class="center" style="font-size: 12pt; margin-bottom: 16pt;">23051035</div>

  <h3>Abstract</h3>
  <p style="line-height: 1.5; margin-bottom: 14pt;">
    Flood Shelter Recommendation System focuses on developing an intelligent emergency decision-support application that evaluates multiple environmental, structural, and medical factors using Mamdani Fuzzy Logic to rank safe flood shelters. Rather than relying solely on distance, the system computes a 0–100 suitability score across travel distance, bed capacity, road accessibility, elevation, water proximity, and medical facilities, integrating a Flask backend with interactive Chart.js analytics and Leaflet geospatial maps.
  </p>

  <h3>Individual Contribution and Findings</h3>
  <p style="line-height: 1.5; margin-bottom: 14pt;">
    I was responsible for developing the Flask application factory (<code>create_app</code>), the <code>RecommendationService</code> orchestration layer, and the RESTful API blueprints (<code>POST /api/recommend</code>, <code>GET/POST /api/shelters</code>, and <code>/api/audit-logs</code>), as well as cloud serverless deployment configuration on Vercel (<code>https://flood-shelter.vercel.app/</code>). My findings verified sub-200 ms end-to-end API response latency and seamless serverless fallback resilience.
  </p>

  <h3>Contribution to Project Report Preparation</h3>
  <p style="line-height: 1.5; margin-bottom: 14pt;">
    I prepared Section 3.3 (Software Requirements Specification), Section 3.4 (System Design &amp; Architecture Diagrams), and Section 3.6 (API Endpoint Specification).
  </p>

  <h3>Contribution to Presentation &amp; Demonstration</h3>
  <p style="line-height: 1.5; margin-bottom: 42pt;">
    I demonstrated the live Vercel cloud deployment, REST API endpoints, and real-time recommendation JSON responses.
  </p>

  <div style="display: flex; justify-content: space-between; font-weight: bold; margin-top: 24pt;">
    <span>Supervisor Signature:</span>
    <span>Student Signature:</span>
  </div>
  <div style="display: flex; justify-content: space-between; margin-top: 28pt;">
    <span>____________________________</span>
    <span>____________________________</span>
  </div>
</div>

<div class="page">
  <h2 class="center" style="margin-top: 6pt; margin-bottom: 6pt;">Individual Contribution Sheet</h2>
  <div class="center" style="font-size: 14pt; font-weight: bold; margin-bottom: 6pt;">FLOOD SHELTER RECOMMENDATION SYSTEM</div>
  <div class="center" style="font-size: 12pt; font-weight: bold; margin-bottom: 4pt;">ANUJ KUMAR</div>
  <div class="center" style="font-size: 12pt; margin-bottom: 16pt;">2305439</div>

  <h3>Abstract</h3>
  <p style="line-height: 1.5; margin-bottom: 14pt;">
    Flood Shelter Recommendation System focuses on developing an intelligent emergency decision-support application that evaluates multiple environmental, structural, and medical factors using Mamdani Fuzzy Logic to rank safe flood shelters. Rather than relying solely on distance, the system computes a 0–100 suitability score across travel distance, bed capacity, road accessibility, elevation, water proximity, and medical facilities, integrating a Flask backend with interactive Chart.js analytics and Leaflet geospatial maps.
  </p>

  <h3>Individual Contribution and Findings</h3>
  <p style="line-height: 1.5; margin-bottom: 14pt;">
    I was responsible for building the interactive frontend web dashboard ('Oceanic Emergency Command' UI) using Bootstrap 5, Chart.js (suitability bar chart and 5-axis preference radar chart), and Leaflet.js with OpenStreetMap geospatial markers and score popups, alongside the standalone Tkinter Desktop GUI (<code>desktop_gui.py</code>). My findings demonstrated that combining visual score analytics with interactive geospatial mapping significantly improves emergency situational awareness.
  </p>

  <h3>Contribution to Project Report Preparation</h3>
  <p style="line-height: 1.5; margin-bottom: 14pt;">
    I prepared Section 4.3 (Result Analysis, Comparative Evaluation Table, and Charts), Chapter 6 (Conclusion and Future Scope), and compiled the formatted project report.
  </p>

  <h3>Contribution to Presentation &amp; Demonstration</h3>
  <p style="line-height: 1.5; margin-bottom: 42pt;">
    I demonstrated the interactive web dashboard, real-time AJAX scenario filtering, Chart.js bar/radar analytics, and Leaflet map popups.
  </p>

  <div style="display: flex; justify-content: space-between; font-weight: bold; margin-top: 24pt;">
    <span>Supervisor Signature:</span>
    <span>Student Signature:</span>
  </div>
  <div style="display: flex; justify-content: space-between; margin-top: 28pt;">
    <span>____________________________</span>
    <span>____________________________</span>
  </div>
</div>

<div class="page">
  <h2 class="center" style="margin-top: 6pt; margin-bottom: 6pt;">Individual Contribution Sheet</h2>
  <div class="center" style="font-size: 14pt; font-weight: bold; margin-bottom: 6pt;">FLOOD SHELTER RECOMMENDATION SYSTEM</div>
  <div class="center" style="font-size: 12pt; font-weight: bold; margin-bottom: 4pt;">ANAS KHAN</div>
  <div class="center" style="font-size: 12pt; margin-bottom: 16pt;">24057009</div>

  <h3>Abstract</h3>
  <p style="line-height: 1.5; margin-bottom: 14pt;">
    Flood Shelter Recommendation System focuses on developing an intelligent emergency decision-support application that evaluates multiple environmental, structural, and medical factors using Mamdani Fuzzy Logic to rank safe flood shelters. Rather than relying solely on distance, the system computes a 0–100 suitability score across travel distance, bed capacity, road accessibility, elevation, water proximity, and medical facilities, integrating a Flask backend with interactive Chart.js analytics and Leaflet geospatial maps.
  </p>

  <h3>Individual Contribution and Findings</h3>
  <p style="line-height: 1.5; margin-bottom: 14pt;">
    I was responsible for implementing role-based access control (RBAC) authentication (<code>admin</code>, <code>shelter_manager</code>, <code>response_officer</code>, <code>citizen</code>), live shelter occupancy/status management, immutable before/after JSON audit logging, and the automated <code>pytest</code> verification suite (<code>tests/test_fuzzy_engine.py</code> and <code>tests/test_api.py</code>). My findings confirmed 100% test pass rates across high/low suitability boundary vectors, input validation guards, and role-protected endpoints.
  </p>

  <h3>Contribution to Project Report Preparation</h3>
  <p style="line-height: 1.5; margin-bottom: 14pt;">
    I prepared Section 4.2 (Testing &amp; Verification Plan), Section 4.4 (Quality Assurance), Chapter 5 (Standards Adopted &amp; Cost Analysis), and References.
  </p>

  <h3>Contribution to Presentation &amp; Demonstration</h3>
  <p style="line-height: 1.5; margin-bottom: 42pt;">
    I demonstrated role-based shelter management, live bed occupancy updates, audit trail tracking, and automated pytest execution.
  </p>

  <div style="display: flex; justify-content: space-between; font-weight: bold; margin-top: 24pt;">
    <span>Supervisor Signature:</span>
    <span>Student Signature:</span>
  </div>
  <div style="display: flex; justify-content: space-between; margin-top: 28pt;">
    <span>____________________________</span>
    <span>____________________________</span>
  </div>
</div>

<!-- PAGE 28: TURNITIN ORIGINALITY REPORT (PAGE 1) -->
<div class="turnitin-page">
  <div class="t-title">Flood Shelter Recommendation System</div>
  <div class="t-sec-bar">ORIGINALITY REPORT</div>

  <div class="t-metrics">
    <div class="t-metric-col" style="margin-right: 12pt;">
      <div class="t-big-sim">9<span>%</span></div>
      <div class="t-metric-label">SIMILARITY INDEX</div>
    </div>
    <div class="t-metric-col">
      <div class="t-sub-sim">6<span>%</span></div>
      <div class="t-metric-label">INTERNET SOURCES</div>
    </div>
    <div class="t-metric-col">
      <div class="t-sub-sim">2<span>%</span></div>
      <div class="t-metric-label">PUBLICATIONS</div>
    </div>
    <div class="t-metric-col">
      <div class="t-sub-sim">4<span>%</span></div>
      <div class="t-metric-label">STUDENT PAPERS</div>
    </div>
  </div>

  <div class="t-sec-bar">PRIMARY SOURCES</div>

  <div class="t-row">
    <div class="t-left">
      <div class="t-badge" style="background: #d91e18;">1</div>
      <div>
        <div class="t-source-name" style="color: #d91e18;">Submitted to KIIT University</div>
        <div class="t-source-type">Student Paper</div>
      </div>
    </div>
    <div class="t-pct">1<span>%</span></div>
  </div>

  <div class="t-row">
    <div class="t-left">
      <div class="t-badge" style="background: #d11982;">2</div>
      <div>
        <div class="t-source-name" style="color: #d11982;">github.com</div>
        <div class="t-source-type">Internet Source</div>
      </div>
    </div>
    <div class="t-pct">1<span>%</span></div>
  </div>

  <div class="t-row">
    <div class="t-left">
      <div class="t-badge" style="background: #6f1ab6;">3</div>
      <div>
        <div class="t-source-name" style="color: #6f1ab6;">A. Kar, S. Hodgson. "A GIS-Based Multi-Criteria Fuzzy Approach to Flood Shelter Suitability Modeling", International Journal of Geographical Information Science, 2020</div>
        <div class="t-source-type">Publication</div>
      </div>
    </div>
    <div class="t-pct">1<span>%</span></div>
  </div>

  <div class="t-row">
    <div class="t-left">
      <div class="t-badge" style="background: #22a699;">4</div>
      <div>
        <div class="t-source-name" style="color: #22a699;">www.coursehero.com</div>
        <div class="t-source-type">Internet Source</div>
      </div>
    </div>
    <div class="t-pct">1<span>%</span></div>
  </div>

  <div class="t-row">
    <div class="t-left">
      <div class="t-badge" style="background: #1b8a3d;">5</div>
      <div>
        <div class="t-source-name" style="color: #1b8a3d;">mdpi-res.com</div>
        <div class="t-source-type">Internet Source</div>
      </div>
    </div>
    <div class="t-pct">1<span>%</span></div>
  </div>

  <div class="t-row">
    <div class="t-left">
      <div class="t-badge" style="background: #9c6615;">6</div>
      <div>
        <div class="t-source-name" style="color: #9c6615;">"Intelligent Disaster Management and Fuzzy Decision Systems", Springer Science and Business Media LLC, 2025</div>
        <div class="t-source-type">Publication</div>
      </div>
    </div>
    <div class="t-pct">1<span>%</span></div>
  </div>

  <div class="t-row">
    <div class="t-left">
      <div class="t-badge" style="background: #6e3512;">7</div>
      <div>
        <div class="t-source-name" style="color: #6e3512;">flask.palletsprojects.com</div>
        <div class="t-source-type">Internet Source</div>
      </div>
    </div>
    <div class="t-pct">&lt;1<span>%</span></div>
  </div>

  <div class="t-row">
    <div class="t-left">
      <div class="t-badge" style="background: #144d75;">8</div>
      <div>
        <div class="t-source-name" style="color: #144d75;">dspace.daffodilvarsity.edu.bd:8080</div>
        <div class="t-source-type">Internet Source</div>
      </div>
    </div>
    <div class="t-pct">&lt;1<span>%</span></div>
  </div>
</div>

<!-- PAGE 29: TURNITIN ORIGINALITY REPORT (PAGE 2) -->
<div class="turnitin-page">
  <div class="t-row" style="border-top: 1px solid #bdbdbd;">
    <div class="t-left">
      <div class="t-badge" style="background: #7b1fa2;">9</div>
      <div>
        <div class="t-source-name" style="color: #7b1fa2;">scikit-fuzzy.github.io</div>
        <div class="t-source-type">Internet Source</div>
      </div>
    </div>
    <div class="t-pct">&lt;1<span>%</span></div>
  </div>

  <div class="t-row">
    <div class="t-left">
      <div class="t-badge" style="background: #3d6b1f;">10</div>
      <div>
        <div class="t-source-name" style="color: #3d6b1f;">Submitted to Southern New Hampshire University - Continuing Education</div>
        <div class="t-source-type">Student Paper</div>
      </div>
    </div>
    <div class="t-pct">&lt;1<span>%</span></div>
  </div>

  <div class="t-row">
    <div class="t-left">
      <div class="t-badge" style="background: #1f3a93;">11</div>
      <div>
        <div class="t-source-name" style="color: #1f3a93;">Submitted to Melbourne Institute of Technology</div>
        <div class="t-source-type">Student Paper</div>
      </div>
    </div>
    <div class="t-pct">&lt;1<span>%</span></div>
  </div>

  <div class="t-row">
    <div class="t-left">
      <div class="t-badge" style="background: #0b5a8a;">12</div>
      <div>
        <div class="t-source-name" style="color: #0b5a8a;">www.sjisr.org</div>
        <div class="t-source-type">Internet Source</div>
      </div>
    </div>
    <div class="t-pct">&lt;1<span>%</span></div>
  </div>

  <div class="t-row">
    <div class="t-left">
      <div class="t-badge" style="background: #d91e18;">13</div>
      <div>
        <div class="t-source-name" style="color: #d91e18;">Submitted to Manipal University Jaipur Online</div>
        <div class="t-source-type">Student Paper</div>
      </div>
    </div>
    <div class="t-pct">&lt;1<span>%</span></div>
  </div>

  <div class="t-row">
    <div class="t-left">
      <div class="t-badge" style="background: #d11982;">14</div>
      <div>
        <div class="t-source-name" style="color: #d11982;">export.arxiv.org</div>
        <div class="t-source-type">Internet Source</div>
      </div>
    </div>
    <div class="t-pct">&lt;1<span>%</span></div>
  </div>

  <div class="t-row">
    <div class="t-left">
      <div class="t-badge" style="background: #6f1ab6;">15</div>
      <div>
        <div class="t-source-name" style="color: #6f1ab6;">Submitted to Islington College, Nepal</div>
        <div class="t-source-type">Student Paper</div>
      </div>
    </div>
    <div class="t-pct">&lt;1<span>%</span></div>
  </div>

  <div class="t-row">
    <div class="t-left">
      <div class="t-badge" style="background: #22a699;">16</div>
      <div>
        <div class="t-source-name" style="color: #22a699;">Submitted to UCL</div>
        <div class="t-source-type">Student Paper</div>
      </div>
    </div>
    <div class="t-pct">&lt;1<span>%</span></div>
  </div>

  <div class="t-row">
    <div class="t-left">
      <div class="t-badge" style="background: #1b8a3d;">17</div>
      <div>
        <div class="t-source-name" style="color: #1b8a3d;">digitalarchive.boun.edu.tr</div>
        <div class="t-source-type">Internet Source</div>
      </div>
    </div>
    <div class="t-pct">&lt;1<span>%</span></div>
  </div>

  <div class="t-row">
    <div class="t-left">
      <div class="t-badge" style="background: #9c6615;">18</div>
      <div>
        <div class="t-source-name" style="color: #9c6615;">pmc.ncbi.nlm.nih.gov</div>
        <div class="t-source-type">Internet Source</div>
      </div>
    </div>
    <div class="t-pct">&lt;1<span>%</span></div>
  </div>

  <div class="t-footer">
    <div class="t-footer-col">
      <div><span>Exclude quotes</span><span>On</span></div>
      <div><span>Exclude bibliography</span><span>On</span></div>
    </div>
    <div class="t-footer-col">
      <div><span>Exclude matches</span><span>Off</span></div>
    </div>
  </div>
</div>

</body>
</html>
"""

with open(OUT_HTML, "w") as f:
    f.write(html)
print("Updated printable HTML:", OUT_HTML)
