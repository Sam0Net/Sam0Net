import os

os.makedirs("assets", exist_ok=True)

STYLE = """
  <style>
    .bg { fill: #0d1117; }
    .fg { fill: #e6edf3; font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace; }
    .muted { fill: #7d8590; font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace; }
    .line { stroke: #30363d; stroke-width: 1; }
    .box { fill: #0d1117; stroke: #7d8590; stroke-width: 1; rx: 2; }
  </style>
"""

# 1. HEADER + 01 WHOAMI
svg_01 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 500" width="100%">
  {STYLE}
  <rect width="900" height="500" class="bg"/>
  <text x="40" y="75" class="fg" font-size="54" font-weight="bold">Sam0Net</text>
  <text x="40" y="110" class="fg" font-size="18">Full-Stack Developer &amp; Cybersecurity Specialist</text>

  <text x="40" y="155" class="muted" font-size="12" letter-spacing="1">focus &#9656;  java &amp; spring boot &#183; react.js &#183; cybersecurity &#183; postgresql</text>
  <text x="40" y="178" class="muted" font-size="12" letter-spacing="1">open to software engineering &#183; security roles &#183; collaboration</text>

  <line x1="40" y1="210" x2="860" y2="210" class="line"/>
  <text x="40" y="235" class="muted" font-size="11" letter-spacing="3">JAVA &amp; SPRING BOOT       &#183;       REACT.JS FRONTEND       &#183;       CYBERSECURITY DEGREE</text>

  <text x="40" y="325" class="fg" font-size="42" font-weight="bold">01</text>
  <text x="115" y="318" class="muted" font-size="13" letter-spacing="4">WHOAMI</text>
  <line x1="210" y1="313" x2="750" y2="313" class="line"/>
  <text x="770" y="317" class="muted" font-size="11" letter-spacing="1">~/01-whoami</text>

  <text x="40" y="365" class="fg" font-size="13.5">full-stack software developer &amp; cybersecurity graduate.</text>
  <text x="40" y="390" class="fg" font-size="13.5">building across the stack &#8212; Spring Boot &#183; React.js &#183; PostgreSQL &#183; Secure APIs.</text>
  <text x="40" y="415" class="fg" font-size="13.5">focused on clean architecture, relational data design and application security.</text>

  <line x1="40" y1="438" x2="860" y2="438" class="line"/>
  <text x="40" y="463" class="muted" font-size="11" letter-spacing="2">FOCUS</text>
  <text x="140" y="463" class="fg" font-size="13">Backend Architecture &#183; Full-Stack Web &#183; AppSec &amp; DevSecOps</text>
  <text x="40" y="485" class="muted" font-size="11" letter-spacing="2">EDUCATION</text>
  <text x="140" y="485" class="fg" font-size="13">Degree in Cybersecurity &#8212; Secure Software Engineering</text>
</svg>"""

# 2. 02 SYSTEM MAP
svg_02 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 440" width="100%">
  {STYLE}
  <rect width="900" height="440" class="bg"/>
  <text x="40" y="55" class="fg" font-size="42" font-weight="bold">02</text>
  <text x="115" y="48" class="muted" font-size="13" letter-spacing="4">SYSTEM MAP</text>
  <line x1="250" y1="43" x2="730" y2="43" class="line"/>
  <text x="750" y="47" class="muted" font-size="11" letter-spacing="1">~/02-ecosystem</text>

  <text x="40" y="95" class="muted" font-size="11" letter-spacing="3">SYSTEM MAP &#8212; ARCHITECTURE &amp; SECURITY PIPELINE</text>
  <text x="795" y="95" class="muted" font-size="11" letter-spacing="3">FIG. 01</text>
  <line x1="40" y1="108" x2="860" y2="108" class="line"/>

  <line x1="450" y1="240" x2="210" y2="170" class="line"/>
  <line x1="450" y1="240" x2="690" y2="170" class="line"/>
  <line x1="450" y1="240" x2="210" y2="330" class="line"/>
  <line x1="450" y1="240" x2="690" y2="330" class="line"/>
  <line x1="450" y1="240" x2="450" y2="365" class="line"/>

  <rect x="355" y="215" width="190" height="55" class="box"/>
  <text x="450" y="238" text-anchor="middle" class="fg" font-size="14" letter-spacing="2">SAM0NET.SYS</text>
  <text x="450" y="256" text-anchor="middle" class="muted" font-size="10">secure full-stack core</text>

  <rect x="100" y="140" width="220" height="55" class="box"/>
  <text x="210" y="163" text-anchor="middle" class="fg" font-size="13">spring boot backend</text>
  <text x="210" y="181" text-anchor="middle" class="muted" font-size="10">Java &#183; REST APIs &#183; DTOs</text>

  <rect x="580" y="140" width="220" height="55" class="box"/>
  <text x="690" y="163" text-anchor="middle" class="fg" font-size="13">react.js frontend</text>
  <text x="690" y="181" text-anchor="middle" class="muted" font-size="10">SPA &#183; Modern UI &#183; Hooks</text>

  <rect x="100" y="305" width="220" height="55" class="box"/>
  <text x="210" y="328" text-anchor="middle" class="fg" font-size="13">cybersecurity layer</text>
  <text x="210" y="346" text-anchor="middle" class="muted" font-size="10">Spring Security &#183; JWT &#183; OWASP</text>

  <rect x="580" y="305" width="220" height="55" class="box"/>
  <text x="690" y="328" text-anchor="middle" class="fg" font-size="13">postgresql engine</text>
  <text x="690" y="346" text-anchor="middle" class="muted" font-size="10">Relational DB &#183; JPA / Hibernate</text>

  <rect x="355" y="365" width="190" height="50" class="box"/>
  <text x="450" y="387" text-anchor="middle" class="fg" font-size="13">devops &amp; linux</text>
  <text x="450" y="403" text-anchor="middle" class="muted" font-size="10">Docker &#183; Git &#183; CI/CD</text>
</svg>"""

# 3. 03 PROJECTS / AREAS
svg_03 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 390" width="100%">
  {STYLE}
  <rect width="900" height="390" class="bg"/>
  <text x="40" y="55" class="fg" font-size="42" font-weight="bold">03</text>
  <text x="115" y="48" class="muted" font-size="13" letter-spacing="4">ENGINEERING</text>
  <line x1="255" y1="43" x2="730" y2="43" class="line"/>
  <text x="750" y="47" class="muted" font-size="11" letter-spacing="1">~/03-focus</text>

  <text x="40" y="105" class="fg" font-size="16" font-weight="bold" letter-spacing="2">01 / ENTERPRISE BACKEND &amp; REST APIs</text>
  <text x="40" y="130" class="muted" font-size="13">Modular API architecture with Spring Boot, strict data validation, DTO layers and clean separation</text>
  <text x="40" y="150" class="muted" font-size="13">of concerns for scalable business systems.</text>
  <text x="40" y="172" class="fg" font-size="11" letter-spacing="1.5">JAVA &#183; SPRING BOOT &#183; REST API &#183; MAVEN &#183; CLEAN ARCHITECTURE</text>
  <line x1="40" y1="190" x2="860" y2="190" class="line"/>

  <text x="40" y="220" class="fg" font-size="16" font-weight="bold" letter-spacing="2">02 / CYBERSECURITY &amp; SECURE DEVELOPMENT</text>
  <text x="40" y="245" class="muted" font-size="13">Implementation of authentication, role-based access control, encryption and vulnerability</text>
  <text x="40" y="265" class="muted" font-size="13">mitigation aligned with OWASP Top 10 standards.</text>
  <text x="40" y="287" class="fg" font-size="11" letter-spacing="1.5">CYBERSECURITY &#183; SPRING SECURITY &#183; JWT &#183; KALI LINUX &#183; OWASP</text>
  <line x1="40" y1="305" x2="860" y2="305" class="line"/>

  <text x="40" y="335" class="fg" font-size="16" font-weight="bold" letter-spacing="2">03 / FULL-STACK WEB &amp; RELATIONAL DATA</text>
  <text x="40" y="360" class="muted" font-size="13">Responsive interfaces built with React.js connected to optimized PostgreSQL schemas.</text>
  <text x="40" y="382" class="fg" font-size="11" letter-spacing="1.5">REACT.JS &#183; JAVASCRIPT &#183; POSTGRESQL &#183; SQL &#183; HTML5 &amp; CSS3</text>
</svg>"""

# 4. 04 TELEMETRY
svg_04 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 310" width="100%">
  {STYLE}
  <rect width="900" height="310" class="bg"/>
  <text x="40" y="55" class="fg" font-size="42" font-weight="bold">04</text>
  <text x="115" y="48" class="muted" font-size="13" letter-spacing="4">TELEMETRY</text>
  <line x1="245" y1="43" x2="730" y2="43" class="line"/>
  <text x="750" y="47" class="muted" font-size="11" letter-spacing="1">~/04-telemetry</text>

  <text x="40" y="95" class="muted" font-size="11" letter-spacing="3">TELEMETRY &#8212; CORE COMPETENCIES &amp; DISTRIBUTION</text>
  <text x="795" y="95" class="muted" font-size="11" letter-spacing="3">FIG. 02</text>
  <line x1="40" y1="108" x2="860" y2="108" class="line"/>

  <text x="40" y="138" class="muted" font-size="11" letter-spacing="2">STACK DISTRIBUTION &#183; EST.</text>

  <text x="40" y="165" class="fg" font-size="12">java / spring boot</text>
  <rect x="40" y="173" width="230" height="6" fill="#e6edf3"/>
  <text x="280" y="179" class="muted" font-size="11">40%</text>

  <text x="40" y="203" class="fg" font-size="12">react.js / javascript</text>
  <rect x="40" y="211" width="150" height="6" fill="#e6edf3"/>
  <text x="200" y="217" class="muted" font-size="11">25%</text>

  <text x="40" y="241" class="fg" font-size="12">postgresql / sql</text>
  <rect x="40" y="249" width="115" height="6" fill="#e6edf3"/>
  <text x="165" y="255" class="muted" font-size="11">20%</text>

  <text x="40" y="279" class="fg" font-size="12">cybersecurity / linux</text>
  <rect x="40" y="287" width="90" height="6" fill="#e6edf3"/>
  <text x="140" y="293" class="muted" font-size="11">15%</text>

  <line x1="360" y1="125" x2="360" y2="295" class="line"/>

  <text x="390" y="138" class="muted" font-size="11" letter-spacing="2">ACTIVITY VELOCITY &#183; 2024 &#8594; 2026</text>
  <polyline fill="none" stroke="#e6edf3" stroke-width="2" points="390,260 440,250 490,225 540,190 590,145"/>
  <circle cx="440" cy="250" r="3" fill="#e6edf3"/>
  <circle cx="490" cy="225" r="3" fill="#e6edf3"/>
  <circle cx="540" cy="190" r="3" fill="#e6edf3"/>
  <circle cx="590" cy="145" r="3" fill="#e6edf3"/>
  <line x1="390" y1="270" x2="600" y2="270" class="line"/>
  <text x="390" y="290" class="muted" font-size="11">trend &#8212; accelerating</text>

  <line x1="630" y1="125" x2="630" y2="295" class="line"/>

  <text x="660" y="170" class="fg" font-size="34" font-weight="bold">4</text>
  <text x="710" y="165" class="muted" font-size="11" letter-spacing="2">CORE PILLARS</text>

  <text x="660" y="225" class="fg" font-size="34" font-weight="bold">100%</text>
  <text x="760" y="220" class="muted" font-size="11" letter-spacing="2">SECURITY FOCUS</text>

  <text x="660" y="280" class="fg" font-size="34" font-weight="bold">&#8734;</text>
  <text x="710" y="275" class="muted" font-size="11" letter-spacing="2">TERMINAL TABS OPEN</text>
</svg>"""

# 5. 05 STACK
svg_05 = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 340" width="100%">
  {STYLE}
  <rect width="900" height="340" class="bg"/>
  <text x="40" y="55" class="fg" font-size="42" font-weight="bold">05</text>
  <text x="115" y="48" class="muted" font-size="13" letter-spacing="4">STACK</text>
  <line x1="205" y1="43" x2="730" y2="43" class="line"/>
  <text x="750" y="47" class="muted" font-size="11" letter-spacing="1">~/05-stack</text>

  <line x1="140" y1="85" x2="140" y2="255" class="line"/>

  <text x="40" y="105" class="muted" font-size="11" letter-spacing="2">LANGUAGES</text>
  <text x="160" y="105" class="fg" font-size="13.5">Java &#183; JavaScript &#183; SQL &#183; HTML5 &#183; CSS3 &#183; Bash</text>

  <text x="40" y="135" class="muted" font-size="11" letter-spacing="2">BACKEND</text>
  <text x="160" y="135" class="fg" font-size="13.5">Spring Boot &#183; Spring Security &#183; Spring Data JPA &#183; REST APIs &#183; Maven</text>

  <text x="40" y="165" class="muted" font-size="11" letter-spacing="2">FRONTEND</text>
  <text x="160" y="165" class="fg" font-size="13.5">React.js &#183; Hooks &#183; Fetch / Axios &#183; Responsive UI</text>

  <text x="40" y="195" class="muted" font-size="11" letter-spacing="2">DATA</text>
  <text x="160" y="195" class="fg" font-size="13.5">PostgreSQL &#183; Relational Modeling &#183; Query Optimization</text>

  <text x="40" y="225" class="muted" font-size="11" letter-spacing="2">SECURITY</text>
  <text x="160" y="225" class="fg" font-size="13.5">Cybersecurity &#183; OWASP Top 10 &#183; JWT &#183; Kali Linux &#183; DevSecOps</text>

  <text x="40" y="255" class="muted" font-size="11" letter-spacing="2">TOOLING</text>
  <text x="160" y="255" class="fg" font-size="13.5">Git &#183; GitHub &#183; Docker &#183; Linux &#183; Postman &#183; IntelliJ IDEA &#183; VS Code</text>

  <line x1="40" y1="280" x2="860" y2="280" class="line"/>
  <circle cx="50" cy="312" r="4" fill="#e6edf3"/>
  <text x="68" y="308" class="muted" font-size="11" letter-spacing="2">STATUS &#8212; BUILDING SECURE SYSTEMS</text>
  <text x="68" y="326" class="muted" font-size="11" letter-spacing="1">java &#183; spring boot &#183; react &#183; cybersecurity</text>
  <text x="640" y="316" class="fg" font-size="13">github.com/Sam0Net &#183; &#169; 2026</text>
</svg>"""

files = {
    "assets/01-whoami.svg": svg_01,
    "assets/02-system-map.svg": svg_02,
    "assets/03-projects.svg": svg_03,
    "assets/04-telemetry.svg": svg_04,
    "assets/05-stack.svg": svg_05,
}

for path, content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip())
