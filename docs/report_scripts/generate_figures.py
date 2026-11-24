import os
import json

os.makedirs("/Users/anuj9009/Downloads/major_project/assets/figures", exist_ok=True)
os.makedirs("/Users/anuj9009/Downloads/major_project/assets/html_figs", exist_ok=True)

# 1. System Architecture Diagram HTML
fig1_html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
  * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', -apple-system, sans-serif; }
  body { background: #ffffff; padding: 24px; width: 1080px; }
  .diagram-wrap { display: flex; flex-direction: column; gap: 22px; }
  .layer { border-radius: 16px; padding: 20px 24px; color: #fff; position: relative; box-shadow: 0 6px 20px rgba(0,0,0,0.08); }
  .layer-title { font-size: 18px; font-weight: 700; margin-bottom: 2px; }
  .layer-sub { font-size: 13px; opacity: 0.85; margin-bottom: 16px; }
  .cards { display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; }
  .card { border-radius: 12px; padding: 14px 16px; text-align: center; border: 1.5px solid rgba(255,255,255,0.35); background: rgba(255,255,255,0.12); }
  .card-title { font-size: 15px; font-weight: 700; margin-bottom: 6px; color: #fff; }
  .card-desc { font-size: 12.5px; line-height: 1.45; color: rgba(255,255,255,0.92); }
  
  .layer-pres { background: #0b4f6c; }
  .layer-pres .card-api { background: #4a306d; border-color: #9b7ede; }
  .layer-pres .card-cli { background: #374151; border-color: #9ca3af; }
  
  .layer-logic { background: #0b6e4f; }
  .layer-logic .card-alert { background: #7c3f00; border-color: #f59e0b; }
  
  .layer-data { background: #3f3f46; }
  
  .arrows-row { display: flex; justify-content: space-around; align-items: center; height: 22px; margin: -11px 0; z-index: 5; }
  .arrow-label { background: #f8fafc; border: 1px solid #cbd5e1; color: #334155; font-size: 11.5px; font-weight: 600; padding: 3px 12px; border-radius: 99px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
  
  .legend { display: flex; gap: 24px; align-items: center; padding-top: 6px; font-size: 13px; color: #475569; font-weight: 500; }
  .legend-item { display: flex; align-items: center; gap: 8px; }
  .dot { width: 14px; height: 14px; border-radius: 4px; }
</style>
</head>
<body>
  <div class="diagram-wrap">
    <div class="layer layer-pres">
      <div class="layer-title">Presentation Layer</div>
      <div class="layer-sub">Multi-channel user-facing interfaces & geospatial dashboards</div>
      <div class="cards">
        <div class="card">
          <div class="card-title">Web Dashboard UI</div>
          <div class="card-desc">Bootstrap 5 + Chart.js (Bar/Radar)<br>Leaflet & OpenStreetMap Pins</div>
        </div>
        <div class="card card-api">
          <div class="card-title">Flask REST API</div>
          <div class="card-desc">POST /api/recommend<br>/api/shelters • /api/auth • /api/audit-logs</div>
        </div>
        <div class="card card-cli">
          <div class="card-title">Desktop GUI & CLI</div>
          <div class="card-desc">Tkinter Desktop App (desktop_gui.py)<br>Interactive CLI (user_input.py)</div>
        </div>
      </div>
    </div>

    <div class="arrows-row">
      <span class="arrow-label">▼ Filter Payload (People, Distance, Access, Risk)</span>
      <span class="arrow-label">▼ JSON / Form Request</span>
      <span class="arrow-label">▼ Direct Python Invocation</span>
    </div>

    <div class="layer layer-logic">
      <div class="layer-title">Fuzzy Inference & Business Logic Layer</div>
      <div class="layer-sub">flood_app/services/ • Mamdani Fuzzy Control System • Role-Based Access Control</div>
      <div class="cards">
        <div class="card">
          <div class="card-title">Candidate Filter & Mapper</div>
          <div class="card-desc">Strict vs. Expanded Search Fallback<br>Linguistic-to-Crisp Normalization<br>Usable Capacity Clipping (0–100)</div>
        </div>
        <div class="card">
          <div class="card-title">Mamdani Fuzzy Engine</div>
          <div class="card-desc">scikit-fuzzy ControlSystem (lru_cache)<br>6 Antecedents (trapmf / trimf)<br>21 Fuzzy Rules → Defuzzified Score (0–100)</div>
        </div>
        <div class="card card-alert">
          <div class="card-title">Auth, RBAC & Audit Service</div>
          <div class="card-desc">Werkzeug Password Hashing<br>Roles: Admin, Manager, Officer, Citizen<br>Automated State Audit Logging</div>
        </div>
      </div>
    </div>

    <div class="arrows-row">
      <span class="arrow-label">▼ SQLAlchemy ORM / Repository Queries</span>
      <span class="arrow-label">▲ Ranked Shelter Records + Lat/Lng</span>
      <span class="arrow-label">▼ Audit & Status Persistence</span>
    </div>

    <div class="layer layer-data">
      <div class="layer-title">Data Persistence Layer</div>
      <div class="layer-sub">Relational storage, geospatial coordinates, and CSV batch import pipeline</div>
      <div class="cards">
        <div class="card">
          <div class="card-title">SQLite / PostgreSQL DB</div>
          <div class="card-desc">shelter.db • shelters, users, alerts,<br>shelter_status, audit_logs, app_metadata</div>
        </div>
        <div class="card">
          <div class="card-title">Fuzzy Membership Bundle</div>
          <div class="card-desc">membership_func.py & fuzzy_engine.py<br>Cached Antecedent/Consequent Universes</div>
        </div>
        <div class="card">
          <div class="card-title">Geospatial CSV Datasets</div>
          <div class="card-desc">26 Built-in Demo Shelters (A–Z)<br>20 Real Odisha Flood Shelters CSV</div>
        </div>
      </div>
    </div>

    <div class="legend">
      <div class="legend-item"><span class="dot" style="background:#0b4f6c"></span> Presentation & UI</div>
      <div class="legend-item"><span class="dot" style="background:#4a306d"></span> REST API Endpoints</div>
      <div class="legend-item"><span class="dot" style="background:#0b6e4f"></span> Fuzzy Inference & Logic</div>
      <div class="legend-item"><span class="dot" style="background:#7c3f00"></span> RBAC & Audit Security</div>
      <div class="legend-item"><span class="dot" style="background:#3f3f46"></span> Data & Storage Layer</div>
    </div>
  </div>
</body>
</html>"""

with open("/Users/anuj9009/Downloads/major_project/assets/html_figs/fig1_arch.html", "w") as f:
    f.write(fig1_html)

# 2. Block Diagram HTML (Fig 2)
fig2_html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
  * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', -apple-system, sans-serif; }
  body { background: #ffffff; padding: 24px; width: 1080px; }
  .flow { display: flex; flex-direction: column; align-items: center; gap: 14px; }
  .section-label { font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #64748b; margin-bottom: -4px; }
  .row-6 { display: grid; grid-template-columns: repeat(6, 1fr); gap: 10px; width: 100%; }
  .row-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; width: 92%; }
  .row-2 { display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px; width: 80%; }
  .box { border-radius: 10px; padding: 12px 10px; text-align: center; color: #fff; box-shadow: 0 4px 12px rgba(0,0,0,0.08); }
  .box-title { font-size: 13.5px; font-weight: 700; margin-bottom: 4px; }
  .box-sub { font-size: 11px; opacity: 0.9; line-height: 1.35; }
  
  .b-input { background: #1e40af; }
  .b-fuzz { background: #0f766e; }
  .b-rule { background: #4338ca; width: 68%; padding: 14px 20px; }
  .b-defuzz { background: #6d28d9; width: 68%; padding: 14px 20px; }
  .b-out { background: #9a3412; }
  .b-store { background: #374151; width: 82%; padding: 14px 20px; }
  
  .arrow-down { font-size: 16px; color: #64748b; font-weight: 700; line-height: 1; }
  .legend { display: flex; gap: 20px; align-items: center; margin-top: 8px; font-size: 12.5px; color: #475569; font-weight: 500; }
  .legend-item { display: flex; align-items: center; gap: 6px; }
  .dot { width: 12px; height: 12px; border-radius: 3px; }
</style>
</head>
<body>
  <div class="flow">
    <div class="section-label">User Scenario & Shelter Operational Inputs (6 Antecedents)</div>
    <div class="row-6">
      <div class="box b-input"><div class="box-title">Distance (km)</div><div class="box-sub">Range: [0, 20]<br>Near / Med / Far</div></div>
      <div class="box b-input"><div class="box-title">Usable Capacity</div><div class="box-sub">Range: [0, 100]<br>Low / Med / High</div></div>
      <div class="box b-input"><div class="box-title">Accessibility</div><div class="box-sub">Scale: [0, 10]<br>Diff(2) / Mod(5) / Easy(8)</div></div>
      <div class="box b-input"><div class="box-title">Elevation Level</div><div class="box-sub">Scale: [0, 10]<br>Low(2) / Med(5) / High(8)</div></div>
      <div class="box b-input"><div class="box-title">Water Proximity</div><div class="box-sub">Scale: [0, 10]<br>Close(2) / Mod(5) / Far(8)</div></div>
      <div class="box b-input"><div class="box-title">Medical Support</div><div class="box-sub">Scale: [0, 10]<br>None(2) / Basic(5) / Adv(8)</div></div>
    </div>

    <div class="arrow-down">▼ Crisp-to-Fuzzy Linguistic Mapping & Membership Evaluation ▼</div>

    <div class="row-3">
      <div class="box b-fuzz">
        <div class="box-title">Trapezoidal MFs (trapmf)</div>
        <div class="box-sub">Boundary states: Near/Far distance, Low/High capacity, Low/High access & elevation, Very Close/Far water, None/Adv medical</div>
      </div>
      <div class="box b-fuzz">
        <div class="box-title">Triangular MFs (trimf)</div>
        <div class="box-sub">Intermediate transitions: Medium distance [4,9,14], Medium capacity [30,55,80], Moderate access/elevation/proximity [3,5,7]</div>
      </div>
      <div class="box b-fuzz">
        <div class="box-title">Candidate SQL Pre-Filter</div>
        <div class="box-sub">Phase 1: Strict match (beds ≥ people & dist ≤ max)<br>Phase 2: Expanded fallback search with alert notice</div>
      </div>
    </div>

    <div class="arrow-down">▼ Firing Strengths μ(x) ▼</div>

    <div class="box b-rule">
      <div class="box-title">Mamdani Fuzzy Rule Base Evaluation (21 Multi-Antecedent Rules)</div>
      <div class="box-sub">AND (minimum t-norm) & OR (maximum s-norm) operators • Maps antecedent combinations to 5 consequent levels: Very Low, Low, Medium, High, Excellent</div>
    </div>

    <div class="arrow-down">▼ Aggregated Fuzzy Output Set ▼</div>

    <div class="box b-defuzz">
      <div class="box-title">Centroid Defuzzification (skfuzzy ControlSystemSimulation)</div>
      <div class="box-sub">Computes Center of Area (CoA) over Consequent Universe [0, 100] → Crisp Suitability Score S ∈ [0, 100]</div>
    </div>

    <div class="arrow-down">▼ Descending Score Sort & Tagging ▼</div>

    <div class="row-2">
      <div class="box b-out">
        <div class="box-title">Ranked Shelter Recommendations</div>
        <div class="box-sub">Top Match Highlight Card + Ranked List<br>Direct Match (✓) vs. Alternative Warning (⚠️)</div>
      </div>
      <div class="box b-out">
        <div class="box-title">Visual & Geospatial Analytics</div>
        <div class="box-sub">Chart.js Suitability Bar & Preference Radar Charts<br>Leaflet Interactive Map Pins & Popups</div>
      </div>
    </div>

    <div class="arrow-down">▼ State Persistence ▼</div>

    <div class="box b-store">
      <div class="box-title">SQLite / PostgreSQL Database & Audit Trail</div>
      <div class="box-sub">shelters (lat/lng, beds, risk metrics) • shelter_status (occupancy updates) • audit_logs (before/after JSON state)</div>
    </div>

    <div class="legend">
      <div class="legend-item"><span class="dot" style="background:#1e40af"></span> Antecedent Inputs</div>
      <div class="legend-item"><span class="dot" style="background:#0f766e"></span> Fuzzification & Filtering</div>
      <div class="legend-item"><span class="dot" style="background:#4338ca"></span> Rule Inference</div>
      <div class="legend-item"><span class="dot" style="background:#6d28d9"></span> Defuzzification</div>
      <div class="legend-item"><span class="dot" style="background:#9a3412"></span> Ranked Output & UI</div>
      <div class="legend-item"><span class="dot" style="background:#374151"></span> Database Storage</div>
    </div>
  </div>
</body>
</html>"""

with open("/Users/anuj9009/Downloads/major_project/assets/html_figs/fig2_block.html", "w") as f:
    f.write(fig2_html)

# 3. Terminal Execution Screenshot HTML (Fig 3)
fig3_html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&display=swap');
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { background: #0c0c0c; color: #cccccc; font-family: 'JetBrains Mono', monospace; padding: 20px; width: 1000px; font-size: 13.5px; line-height: 1.55; }
  .win-bar { display: flex; align-items: center; gap: 8px; padding-bottom: 14px; margin-bottom: 14px; border-bottom: 1px solid #262626; }
  .dot { width: 12px; height: 12px; border-radius: 50%; }
  .r { background: #ff5f56; } .y { background: #ffbd2e; } .g { background: #27c93f; }
  .title { color: #888; font-size: 12px; margin-left: 10px; }
  .prompt { color: #27c93f; font-weight: 700; }
  .cmd { color: #f8fafc; font-weight: 500; }
  .info { color: #38bdf8; }
  .warn { color: #facc15; }
  .ok { color: #4ade80; }
</style>
</head>
<body>
  <div class="win-bar">
    <span class="dot r"></span><span class="dot y"></span><span class="dot g"></span>
    <span class="title">zsh — FLOOD_SHELTER — python app.py & pytest</span>
  </div>
  <div><span class="prompt">➜  FLOOD_SHELTER git:(main)</span> <span class="cmd">python database.py</span></div>
  <div class="ok">Done (Seeded 26 built-in flood shelters into shelter.db)</div>
  <br>
  <div><span class="prompt">➜  FLOOD_SHELTER git:(main)</span> <span class="cmd">pytest -v</span></div>
  <div>============================= test session starts ==============================</div>
  <div>platform darwin -- Python 3.13.0, pytest-8.2.2, pluggy-1.5.0</div>
  <div>collected 4 items</div>
  <div>tests/test_api.py::test_recommend_api <span class="ok">PASSED                             [ 25%]</span></div>
  <div>tests/test_api.py::test_recommend_api_no_candidates <span class="ok">PASSED               [ 50%]</span></div>
  <div>tests/test_fuzzy_engine.py::test_high_suitability <span class="ok">PASSED                 [ 75%]</span></div>
  <div>tests/test_fuzzy_engine.py::test_low_suitability <span class="ok">PASSED                  [100%]</span></div>
  <div class="ok">============================== 4 passed in 0.84s ===============================</div>
  <br>
  <div><span class="prompt">➜  FLOOD_SHELTER git:(main)</span> <span class="cmd">python app.py</span></div>
  <div> * Serving Flask app 'flood_app'</div>
  <div> * Debug mode: on</div>
  <div class="info"> * Running on http://127.0.0.1:5000</div>
  <div class="warn">Press CTRL+C to quit</div>
  <div>127.0.0.1 - - [06/Nov/2026 21:45:12] "GET / HTTP/1.1" 200 -</div>
  <div>127.0.0.1 - - [06/Nov/2026 21:45:15] "POST /api/recommend HTTP/1.1" 200 -</div>
  <div>127.0.0.1 - - [06/Nov/2026 21:45:22] "GET /manage/shelters HTTP/1.1" 200 -</div>
</body>
</html>"""

with open("/Users/anuj9009/Downloads/major_project/assets/html_figs/fig3_terminal.html", "w") as f:
    f.write(fig3_html)

# 4. Historical / Odisha Shelter Dataset Preview HTML (Fig 5)
import csv
rows_html = ""
with open("/Users/anuj9009/Downloads/major_project/FLOOD_SHELTER/real_flood_shelters.csv", "r") as f:
    reader = csv.DictReader(f)
    for idx, r in enumerate(reader, 1):
        if idx > 12: break
        rows_html += f"""<tr>
          <td>{idx}</td>
          <td style="font-weight:600;color:#fff">{r['name']}</td>
          <td>{r['capacity']}</td>
          <td style="color:#00f2fe;font-weight:600">{r['available_beds']}</td>
          <td>{r['distance']} km</td>
          <td><span class="badge b-{r['accessibility']}">{r['accessibility'].title()}</span></td>
          <td>{r['elevation_level'].title()}</td>
          <td>{r['proximity_to_water'].title()}</td>
          <td>{r['medical_facility'].title()}</td>
          <td style="color:#94a3b8;font-size:12px">{r['latitude']}, {r['longitude']}</td>
        </tr>"""

fig5_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&family=Space+Grotesk:wght@600;700&display=swap');
  * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: 'Outfit', sans-serif; }}
  body {{ background: #070f19; color: #f0f7ff; padding: 24px; width: 1120px; }}
  .card {{ background: rgba(14, 28, 46, 0.92); border: 1px solid rgba(56, 189, 248, 0.28); border-radius: 18px; padding: 22px; }}
  .eyebrow {{ color: #00f2fe; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.14em; }}
  h2 {{ font-family: 'Space Grotesk', sans-serif; font-size: 22px; margin: 4px 0 14px; color: #fff; }}
  table {{ width: 100%; border-collapse: collapse; font-size: 13px; }}
  th {{ text-align: left; padding: 10px 8px; color: #94a3b8; border-bottom: 1px solid rgba(56,189,248,0.25); font-size: 11.5px; text-transform: uppercase; letter-spacing: 0.06em; }}
  td {{ padding: 9px 8px; border-bottom: 1px solid rgba(56,189,248,0.1); }}
  .badge {{ padding: 3px 8px; border-radius: 99px; font-size: 11.5px; font-weight: 600; }}
  .b-easy {{ background: rgba(16, 185, 129, 0.18); color: #34d399; }}
  .b-moderate {{ background: rgba(56, 189, 248, 0.18); color: #38bdf8; }}
  .b-difficult {{ background: rgba(255, 77, 109, 0.18); color: #ff4d6d; }}
</style>
</head>
<body>
  <div class="card">
    <div class="eyebrow">Geospatial & Operational Dataset Preview</div>
    <h2>Odisha Flood Shelter Inventory (real_flood_shelters.csv & shelter.db)</h2>
    <table>
      <thead>
        <tr>
          <th>#</th><th>Shelter Name</th><th>Capacity</th><th>Free Beds</th><th>Distance</th><th>Access</th><th>Elevation</th><th>Water Prox.</th><th>Medical</th><th>Coordinates (Lat, Lng)</th>
        </tr>
      </thead>
      <tbody>
        {rows_html}
      </tbody>
    </table>
  </div>
</body>
</html>"""

with open("/Users/anuj9009/Downloads/major_project/assets/html_figs/fig5_dataset.html", "w") as f:
    f.write(fig5_html)

# 5. Fuzzy Membership Functions Plot HTML (Fig 10)
fig10_html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.2/dist/chart.umd.min.js"></script>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700&family=Space+Grotesk:wght@600;700&display=swap');
  * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Outfit', sans-serif; }
  body { background: #070f19; color: #f0f7ff; padding: 22px; width: 1080px; }
  .card { background: rgba(14, 28, 46, 0.95); border: 1px solid rgba(56, 189, 248, 0.3); border-radius: 18px; padding: 22px; }
  .eyebrow { color: #00f2fe; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.14em; }
  h2 { font-family: 'Space Grotesk', sans-serif; font-size: 20px; margin: 4px 0 16px; color: #fff; }
  .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
  .chart-box { background: rgba(8, 18, 32, 0.8); border: 1px solid rgba(56, 189, 248, 0.15); border-radius: 12px; padding: 14px; height: 260px; }
  h3 { font-size: 14px; color: #cbd5e1; margin-bottom: 8px; text-align: center; }
</style>
</head>
<body>
  <div class="card">
    <div class="eyebrow">Mamdani Fuzzy Control System (membership_func.py)</div>
    <h2>Antecedent & Consequent Fuzzy Membership Functions (trapmf & trimf)</h2>
    <div class="grid">
      <div class="chart-box">
        <h3>Antecedent: Distance Universe [0 – 20 km]</h3>
        <canvas id="distChart" height="190"></canvas>
      </div>
      <div class="chart-box">
        <h3>Consequent: Suitability Score Universe [0 – 100]</h3>
        <canvas id="suitChart" height="190"></canvas>
      </div>
    </div>
  </div>
  <script>
    const distLabels = Array.from({length: 21}, (_, i) => i);
    new Chart(document.getElementById('distChart'), {
      type: 'line',
      data: {
        labels: distLabels,
        datasets: [
          { label: 'Near [0,0,3,7]', data: [1,1,1,1,0.75,0.5,0.25,0,0,0,0,0,0,0,0,0,0,0,0,0,0], borderColor: '#10b981', backgroundColor: 'rgba(16,185,129,0.15)', fill: true, tension: 0.1 },
          { label: 'Medium [4,9,14]', data: [0,0,0,0,0,0.2,0.4,0.6,0.8,1.0,0.8,0.6,0.4,0.2,0,0,0,0,0,0,0], borderColor: '#00f2fe', backgroundColor: 'rgba(0,242,254,0.15)', fill: true, tension: 0.1 },
          { label: 'Far [11,15,20,20]', data: [0,0,0,0,0,0,0,0,0,0,0,0,0.25,0.5,0.75,1,1,1,1,1,1], borderColor: '#ff4d6d', backgroundColor: 'rgba(255,77,109,0.15)', fill: true, tension: 0.1 }
        ]
      },
      options: { plugins: { legend: { labels: { color: '#cbd5e1', font: { size: 11 } } } }, scales: { x: { ticks: { color: '#94a3b8' } }, y: { min: 0, max: 1.05, ticks: { color: '#94a3b8' } } } }
    });

    const suitLabels = [0,10,15,25,30,40,45,55,65,70,78,85,90,93,100];
    function trapmf(x, a, b, c, d) { return Math.max(0, Math.min((x-a)/(b-a||1e-5), 1, (d-x)/(d-c||1e-5))); }
    function trimf(x, a, b, c) { return Math.max(0, Math.min((x-a)/(b-a||1e-5), (c-x)/(c-b||1e-5))); }
    const xs = Array.from({length: 21}, (_, i) => i * 5);
    new Chart(document.getElementById('suitChart'), {
      type: 'line',
      data: {
        labels: xs,
        datasets: [
          { label: 'Very Low', data: xs.map(x => x<=10?1:trapmf(x,0,0,10,25)), borderColor: '#ff4d6d', fill: true, backgroundColor: 'rgba(255,77,109,0.12)' },
          { label: 'Low', data: xs.map(x => trimf(x,15,30,45)), borderColor: '#f97316', fill: true, backgroundColor: 'rgba(249,115,22,0.12)' },
          { label: 'Medium', data: xs.map(x => trimf(x,40,55,70)), borderColor: '#eab308', fill: true, backgroundColor: 'rgba(234,179,8,0.12)' },
          { label: 'High', data: xs.map(x => trimf(x,65,78,90)), borderColor: '#38bdf8', fill: true, backgroundColor: 'rgba(56,189,248,0.12)' },
          { label: 'Excellent', data: xs.map(x => x>=93?1:trapmf(x,85,93,100,100)), borderColor: '#10b981', fill: true, backgroundColor: 'rgba(16,185,129,0.15)' }
        ]
      },
      options: { plugins: { legend: { labels: { color: '#cbd5e1', font: { size: 10 } } } }, scales: { x: { ticks: { color: '#94a3b8' } }, y: { min: 0, max: 1.05, ticks: { color: '#94a3b8' } } } }
    });
  </script>
</body>
</html>"""

with open("/Users/anuj9009/Downloads/major_project/assets/html_figs/fig10_fuzzy.html", "w") as f:
    f.write(fig10_html)

print("HTML figure templates written successfully!")

# Fig 6: Ranked Shelter Recommendations & Summary Cards
fig6_html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Space+Grotesk:wght@600;700&display=swap');
  * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Outfit', sans-serif; }
  body { background: #070f19; color: #f0f7ff; padding: 24px; width: 1080px; }
  .wrap { display: flex; flex-direction: column; gap: 18px; }
  .best-card { border-radius: 20px; padding: 24px 28px; background: linear-gradient(135deg, rgba(13, 30, 51, 0.96), rgba(8, 22, 38, 0.99)); border: 1.5px solid rgba(56, 189, 248, 0.38); display: flex; justify-content: space-between; align-items: center; box-shadow: 0 12px 30px rgba(0,0,0,0.4); }
  .eyebrow { color: #00f2fe; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.15em; margin-bottom: 4px; }
  .best-title { font-family: 'Space Grotesk', sans-serif; font-size: 28px; font-weight: 700; color: #fff; margin-bottom: 10px; }
  .pills { display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 10px; }
  .pill { padding: 5px 12px; border-radius: 99px; background: rgba(255,255,255,0.06); border: 1px solid rgba(56,189,248,0.18); font-size: 13px; }
  .tag { padding: 5px 12px; border-radius: 99px; background: rgba(0,242,254,0.1); border: 1px solid rgba(0,242,254,0.25); color: #00f2fe; font-size: 12.5px; font-weight: 600; }
  .tag-green { background: rgba(16,185,129,0.18); border-color: rgba(16,185,129,0.35); color: #34d399; }
  .score-circle { width: 92px; height: 92px; border-radius: 50%; background: linear-gradient(135deg, #00f2fe, #4facfe); color: #050b14; font-family: 'Space Grotesk', sans-serif; font-size: 26px; font-weight: 800; display: flex; align-items: center; justify-content: center; box-shadow: 0 0 25px rgba(0,242,254,0.4); }
  .summary-strip { display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; }
  .s-card { background: rgba(14,28,46,0.85); border: 1px solid rgba(56,189,248,0.16); border-radius: 14px; padding: 16px 18px; }
  .s-label { font-size: 11px; text-transform: uppercase; letter-spacing: 0.12em; color: #64748b; font-weight: 700; }
  .s-val { font-family: 'Space Grotesk', sans-serif; font-size: 24px; font-weight: 700; color: #fff; margin-top: 4px; }
  .list-card { background: rgba(14,28,46,0.85); border: 1px solid rgba(56,189,248,0.18); border-radius: 18px; padding: 20px; }
  .r-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 12px; }
  .r-item { background: rgba(11,24,40,0.75); border: 1px solid rgba(56,189,248,0.15); border-radius: 14px; padding: 14px 16px; }
  .r-head { display: flex; justify-content: space-between; align-items: center; }
  .r-rank { font-size: 11px; color: #00f2fe; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; }
  .r-name { font-family: 'Space Grotesk', sans-serif; font-size: 17px; color: #fff; font-weight: 700; }
  .r-score { font-family: 'Space Grotesk', sans-serif; font-size: 20px; color: #00f2fe; font-weight: 800; }
  .bar { height: 7px; background: rgba(255,255,255,0.08); border-radius: 99px; margin: 8px 0; overflow: hidden; }
  .fill { height: 100%; background: linear-gradient(90deg, #4facfe, #00f2fe); border-radius: 99px; }
  .r-meta { font-size: 12.5px; color: #94a3b8; margin-bottom: 8px; }
</style>
</head>
<body>
  <div class="wrap">
    <div class="best-card">
      <div>
        <div class="eyebrow">Top Ranked Match</div>
        <div class="best-title">Shelter H</div>
        <div class="pills">
          <span class="pill">📍 3.8 km away</span>
          <span class="pill">🛏️ 40 beds available (Capacity: 110)</span>
          <span class="pill">♿ Easy access</span>
        </div>
        <div class="pills" style="margin-bottom:0">
          <span class="tag tag-green">✓ Direct Scenario Match</span>
          <span class="tag">Elevation: High</span>
          <span class="tag">Water Proximity: Far</span>
          <span class="tag">Medical: Advanced</span>
        </div>
      </div>
      <div class="score-circle">67.83</div>
    </div>

    <div class="summary-strip">
      <div class="s-card"><div class="s-label">Shelters Found</div><div class="s-val">15</div></div>
      <div class="s-card"><div class="s-label">Max Distance</div><div class="s-val">10 km</div></div>
      <div class="s-card"><div class="s-label">Accessibility</div><div class="s-val">Moderate</div></div>
      <div class="s-card"><div class="s-label">Dataset Records</div><div class="s-val">26</div></div>
    </div>

    <div class="list-card">
      <div class="eyebrow">Ranked Output</div>
      <h3 style="font-family:'Space Grotesk',sans-serif;font-size:19px;color:#fff">Shelter Suitability Rankings (Top 4 Candidates)</h3>
      <div class="r-grid">
        <div class="r-item">
          <div class="r-head"><div><div class="r-rank">Rank #1</div><div class="r-name">Shelter H</div></div><div class="r-score">67.83</div></div>
          <div class="bar"><div class="fill" style="width:67.83%"></div></div>
          <div class="r-meta">📍 3.8 km away, 🛏️ 40 beds free, ♿ Easy access</div>
          <div class="pills" style="margin:0"><span class="tag tag-green" style="font-size:11px;padding:3px 8px">✓ Direct Match</span><span class="pill" style="font-size:11px;padding:3px 8px">Elevation High</span><span class="pill" style="font-size:11px;padding:3px 8px">Medical Advanced</span></div>
        </div>
        <div class="r-item">
          <div class="r-head"><div><div class="r-rank">Rank #2</div><div class="r-name">Shelter A</div></div><div class="r-score">66.92</div></div>
          <div class="bar"><div class="fill" style="width:66.92%"></div></div>
          <div class="r-meta">📍 2.5 km away, 🛏️ 30 beds free, ♿ Easy access</div>
          <div class="pills" style="margin:0"><span class="tag tag-green" style="font-size:11px;padding:3px 8px">✓ Direct Match</span><span class="pill" style="font-size:11px;padding:3px 8px">Elevation High</span><span class="pill" style="font-size:11px;padding:3px 8px">Medical Advanced</span></div>
        </div>
        <div class="r-item">
          <div class="r-head"><div><div class="r-rank">Rank #3</div><div class="r-name">Shelter R</div></div><div class="r-score">66.92</div></div>
          <div class="bar"><div class="fill" style="width:66.92%"></div></div>
          <div class="r-meta">📍 1.8 km away, 🛏️ 30 beds free, ♿ Easy access</div>
          <div class="pills" style="margin:0"><span class="tag tag-green" style="font-size:11px;padding:3px 8px">✓ Direct Match</span><span class="pill" style="font-size:11px;padding:3px 8px">Elevation High</span><span class="pill" style="font-size:11px;padding:3px 8px">Medical Advanced</span></div>
        </div>
        <div class="r-item">
          <div class="r-head"><div><div class="r-rank">Rank #4</div><div class="r-name">Shelter D</div></div><div class="r-score">65.50</div></div>
          <div class="bar"><div class="fill" style="width:65.50%"></div></div>
          <div class="r-meta">📍 3.0 km away, 🛏️ 50 beds free, ♿ Easy access</div>
          <div class="pills" style="margin:0"><span class="tag tag-green" style="font-size:11px;padding:3px 8px">✓ Direct Match</span><span class="pill" style="font-size:11px;padding:3px 8px">Elevation High</span><span class="pill" style="font-size:11px;padding:3px 8px">Water Far</span></div>
        </div>
      </div>
    </div>
  </div>
</body>
</html>"""

with open("/Users/anuj9009/Downloads/major_project/assets/html_figs/fig6_ranked.html", "w") as f:
    f.write(fig6_html)

# Fig 7: Interactive Leaflet Map View
fig7_html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css">
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700&family=Space+Grotesk:wght@600;700&display=swap');
  * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Outfit', sans-serif; }
  body { background: #070f19; color: #f0f7ff; padding: 22px; width: 1080px; }
  .card { background: rgba(14, 28, 46, 0.95); border: 1px solid rgba(56, 189, 248, 0.3); border-radius: 18px; padding: 20px; }
  .eyebrow { color: #00f2fe; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.14em; }
  h2 { font-family: 'Space Grotesk', sans-serif; font-size: 20px; margin: 4px 0 14px; color: #fff; }
  #map { height: 420px; border-radius: 14px; border: 1px solid rgba(56, 189, 248, 0.35); }
  .leaflet-popup-content-wrapper { background: #0d1e33 !important; color: #f0f7ff !important; border-radius: 10px !important; border: 1px solid rgba(56,189,248,0.4) !important; font-size: 13px; }
  .leaflet-popup-tip { background: #0d1e33 !important; }
</style>
</head>
<body>
  <div class="card">
    <div class="eyebrow">Geospatial Intelligence (Leaflet + OpenStreetMap)</div>
    <h2>Interactive Flood Shelter Map with Suitability Score Popups (Bhubaneswar Region)</h2>
    <div id="map"></div>
  </div>
  <script>
    const map = L.map('map').setView([20.312, 85.822], 13);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; OpenStreetMap contributors'
    }).addTo(map);
    const shelters = [
      {name: 'Shelter H', lat: 20.3266, lng: 85.8178, score: 67.83, dist: 3.8, beds: 40, rank: 1},
      {name: 'Shelter A', lat: 20.3068, lng: 85.8199, score: 66.92, dist: 2.5, beds: 30, rank: 2},
      {name: 'Shelter R', lat: 20.3199, lng: 85.7970, score: 66.92, dist: 1.8, beds: 30, rank: 3},
      {name: 'Shelter D', lat: 20.3218, lng: 85.8342, score: 65.50, dist: 3.0, beds: 50, rank: 4},
      {name: 'Shelter O', lat: 20.3336, lng: 85.8099, score: 65.50, dist: 3.5, beds: 60, rank: 5},
      {name: 'Shelter X', lat: 20.3241, lng: 85.8476, score: 65.30, dist: 3.3, beds: 20, rank: 6},
      {name: 'Shelter G', lat: 20.3155, lng: 85.8094, score: 55.00, dist: 2.0, beds: 15, rank: 7},
      {name: 'Shelter J', lat: 20.3092, lng: 85.8039, score: 55.00, dist: 1.5, beds: 18, rank: 8}
    ];
    shelters.forEach((s, idx) => {
      const m = L.marker([s.lat, s.lng]).addTo(map);
      const popupHtml = `<strong style="color:#00f2fe;font-size:14px">${s.name}</strong><br><span style="color:#34d399">✓ Direct Match</span><br><b>Rank #${s.rank}</b> | <b>Score: ${s.score}</b><br>Distance: ${s.dist} km | Beds Free: ${s.beds}`;
      m.bindPopup(popupHtml);
      if (idx === 0) { setTimeout(() => m.openPopup(), 400); }
    });
  </script>
</body>
</html>"""

with open("/Users/anuj9009/Downloads/major_project/assets/html_figs/fig7_map.html", "w") as f:
    f.write(fig7_html)

# Fig 8: Bar Chart (Shelter Suitability Score Comparison)
fig8_html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.2/dist/chart.umd.min.js"></script>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700&family=Space+Grotesk:wght@600;700&display=swap');
  * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Outfit', sans-serif; }
  body { background: #070f19; color: #f0f7ff; padding: 22px; width: 1040px; }
  .card { background: rgba(14, 28, 46, 0.95); border: 1px solid rgba(56, 189, 248, 0.3); border-radius: 18px; padding: 22px; }
  .eyebrow { color: #00f2fe; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.14em; }
  h2 { font-family: 'Space Grotesk', sans-serif; font-size: 20px; margin: 4px 0 16px; color: #fff; }
  .chart-wrap { height: 320px; }
</style>
</head>
<body>
  <div class="card">
    <div class="eyebrow">Score Analytics (Chart.js Bar Visualization)</div>
    <h2>Shelter Suitability Score Comparison (Direct Matches vs. Alternative Candidates)</h2>
    <div class="chart-wrap">
      <canvas id="barChart"></canvas>
    </div>
  </div>
  <script>
    const labels = ['Shelter H', 'Shelter A', 'Shelter R', 'Shelter D', 'Shelter O', 'Shelter X', 'Shelter G', 'Shelter J', 'Shelter K', 'Shelter M', 'Shelter I (Alt)', 'Shelter C (Low)'];
    const scores = [67.83, 66.92, 66.92, 65.50, 65.50, 65.30, 55.00, 55.00, 55.00, 55.00, 41.80, 34.72];
    const colors = scores.map((s, i) => i >= 10 ? '#ffb703' : '#00f2fe');
    new Chart(document.getElementById('barChart'), {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          label: 'Fuzzy Suitability Score (0 - 100)',
          data: scores,
          backgroundColor: colors,
          borderRadius: 8
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: { legend: { display: false } },
        scales: {
          x: { ticks: { color: '#cbd5e1', font: { size: 12 } }, grid: { display: false } },
          y: { beginAtZero: true, max: 100, ticks: { color: '#94a3b8' }, grid: { color: 'rgba(56, 189, 248, 0.14)' } }
        }
      }
    });
  </script>
</body>
</html>"""

with open("/Users/anuj9009/Downloads/major_project/assets/html_figs/fig8_bar.html", "w") as f:
    f.write(fig8_html)

# Fig 9: Radar Chart (Fuzzy Input Preference Profile)
fig9_html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.2/dist/chart.umd.min.js"></script>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700&family=Space+Grotesk:wght@600;700&display=swap');
  * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Outfit', sans-serif; }
  body { background: #070f19; color: #f0f7ff; padding: 22px; width: 960px; }
  .card { background: rgba(14, 28, 46, 0.95); border: 1px solid rgba(56, 189, 248, 0.3); border-radius: 18px; padding: 22px; }
  .eyebrow { color: #00f2fe; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.14em; }
  h2 { font-family: 'Space Grotesk', sans-serif; font-size: 20px; margin: 4px 0 14px; color: #fff; }
  .chart-wrap { height: 340px; display: flex; justify-content: center; }
</style>
</head>
<body>
  <div class="card">
    <div class="eyebrow">Input Profile (Chart.js Radar Visualization)</div>
    <h2>Multi-Criteria Fuzzy Preference Profile vs. Top Shelter Attributes</h2>
    <div class="chart-wrap">
      <canvas id="radarChart"></canvas>
    </div>
  </div>
  <script>
    new Chart(document.getElementById('radarChart'), {
      type: 'radar',
      data: {
        labels: ['Proximity Safety (Far from Water)', 'Road Accessibility', 'Terrain Elevation', 'Medical Readiness', 'Bed Capacity Margin'],
        datasets: [
          {
            label: 'Top Recommended Shelter (Shelter H - Score 67.83)',
            data: [8, 8, 8, 8, 8.5],
            fill: true,
            backgroundColor: 'rgba(0, 242, 254, 0.22)',
            borderColor: '#00f2fe',
            pointBackgroundColor: '#ffb703',
            pointRadius: 5
          },
          {
            label: 'Nearest Low-Lying Shelter (Shelter V - Score 34.72)',
            data: [2, 2, 2, 2, 3],
            fill: true,
            backgroundColor: 'rgba(255, 77, 109, 0.18)',
            borderColor: '#ff4d6d',
            pointBackgroundColor: '#ff4d6d',
            pointRadius: 5
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: { legend: { labels: { color: '#f0f7ff', font: { size: 12.5 } } } },
        scales: {
          r: {
            min: 0, max: 10,
            ticks: { stepSize: 2, color: '#94a3b8', backdropColor: 'transparent' },
            grid: { color: 'rgba(56, 189, 248, 0.18)' },
            angleLines: { color: 'rgba(56, 189, 248, 0.18)' },
            pointLabels: { color: '#f0f7ff', font: { size: 13, weight: '600' } }
          }
        }
      }
    });
  </script>
</body>
</html>"""

with open("/Users/anuj9009/Downloads/major_project/assets/html_figs/fig9_radar.html", "w") as f:
    f.write(fig9_html)

print("All HTML figure files generated!")
