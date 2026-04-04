"""
seed.py — Populate the database with sample data for development.

Usage:
    python seed.py

Run this once after `flask db create` (or after first app.run())
to get sample projects and skills so the UI renders with content.
"""

from db_functions import insert_project, insert_contact_message, insert_skill, clear_all_db


SAMPLE_PROJECTS = [
    {
        "title": "Portfolio Website",
        "slug": "portfolio-website",
        "category": "personal",
        "short_desc": "This very portfolio — built with Flask, Bootstrap 5, and SQLite.",
        "overview": "A personal portfolio to showcase my projects and skills to recruiters and collaborators.",
        "problem": "Existing portfolio templates didn't reflect my technical background or personal style.",
        "solution": "Built a custom Flask MVC with a SQLite-backed project database, fully templated with Jinja2.",
        "challenges": "Getting glassmorphism to degrade gracefully on older browsers; solved with a solid fallback background.",
        "outcome": "A fully self-hosted, recruiter-ready portfolio with a CMS-lite admin path.",
        "tech_tags": "Python,Flask,Bootstrap 5,SQLite,Jinja2",
        "preview_img": None,
        "github_url": "https://github.com/yourusername/portfolio",
        "demo_url": None,
        "video_url": None,
        "featured": True,
        "order": 1,
    },
    {
        "title": "Data Dashboard",
        "slug": "data-dashboard",
        "category": "university",
        "short_desc": "Interactive data visualisation dashboard built for a data-engineering course.",
        "overview": "Semester project for the Data Engineering module — visualise a public dataset in real time.",
        "problem": "Raw CSV data from the city open-data portal was hard to interpret at a glance.",
        "solution": "Ingested data with pandas, stored aggregates in PostgreSQL, served charts via Chart.js.",
        "challenges": "Handling 2M+ rows without blocking the UI — solved with server-side aggregation and lazy loading.",
        "outcome": "Achieved top grade; dashboard adopted as a course reference by the lecturer.",
        "tech_tags": "Python,Flask,PostgreSQL,Chart.js,pandas",
        "preview_img": None,
        "github_url": "https://github.com/yourusername/data-dashboard",
        "demo_url": None,
        "video_url": None,
        "featured": True,
        "order": 2,
    },
    {
        "title": "Sensor Monitor",
        "slug": "sensor-monitor",
        "category": "school",
        "short_desc": "Raspberry Pi IoT system that logs temperature & humidity and alerts via Telegram.",
        "overview": "Built for a hardware-software integration module in high school.",
        "problem": "The school server room had no automated temperature monitoring; overheating went unnoticed.",
        "solution": "DHT22 sensor → RPi GPIO → Python daemon → SQLite log → Telegram bot alerts.",
        "challenges": "GPIO noise causing false readings; solved with a rolling average filter.",
        "outcome": "System ran for 6 months without false positives; school adopted it permanently.",
        "tech_tags": "Python,Raspberry Pi,SQLite,Telegram API,GPIO",
        "preview_img": None,
        "github_url": "https://github.com/yourusername/sensor-monitor",
        "demo_url": None,
        "video_url": "https://www.youtube.com/embed/dQw4w9WgXcQ",  # replace with real demo
        "featured": True,
        "order": 3,
    },
    {
        "title": "CodeWizards Lesson Builder",
        "slug": "cwh-lesson-builder",
        "category": "cwh",
        "short_desc": "Internal tool to generate structured lesson plans from a topic outline.",
        "overview": "Built during my instructor role at CodeWizardsHQ to speed up curriculum prep.",
        "problem": "Writing new lesson plans from scratch took 2–3 hours per session.",
        "solution": "Template engine + markdown parser that scaffolds exercises, objectives and rubrics automatically.",
        "challenges": "Keeping generated structure flexible enough for different age groups.",
        "outcome": "Reduced lesson-prep time by ~60% across the team.",
        "tech_tags": "Python,Jinja2,Markdown,Click",
        "preview_img": None,
        "github_url": "https://github.com/yourusername/lesson-builder",
        "demo_url": None,
        "video_url": None,
        "featured": True,
        "order": 4,
    },
]

SAMPLE_SKILLS = [
    # Frontend
    {"name": "HTML/CSS",    "category": "frontend", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg",      "order": 1},
    {"name": "JavaScript",  "category": "frontend", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg", "order": 2},
    {"name": "Bootstrap",   "category": "frontend", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bootstrap/bootstrap-original.svg",  "order": 3},
    
    # Backend
    {"name": "Python",      "category": "backend",  "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg",        "order": 1},
    {"name": "Flask",       "category": "backend",  "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg",          "order": 2},
    {"name": "SQLite",      "category": "backend",  "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg",        "order": 3},

    # Tools
    {"name": "Git",         "category": "tools",    "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg",             "order": 1},
    {"name": "GitHub",      "category": "tools",    "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg",       "order": 2},
    {"name": "VS Code",     "category": "tools",    "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg",       "order": 3},
    {"name": "Linux",       "category": "tools",    "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg",         "order": 4},

    # Languages
    {"name": "C",       "category": "languages",    "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/C-original.svg",         "order": 1},
    {"name": "Java",       "category": "languages",    "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/java-original.svg",         "order": 2}
]


def seed_tables():
    
    clear_all_db()
    for dico in SAMPLE_PROJECTS:
        insert_project(title=dico['title'],slug=dico['slug'], category=dico["category"], short_desc=dico["short_desc"], overview=dico['overview'], problem=dico['problem'], solution=dico['solution'], challenges=dico['challenges'], outcome=dico['outcome'], tech_tags=dico['tech_tags'], preview_img=dico['preview_img'], github_url=dico['github_url'], demo_url=dico['demo_url'], video_url=dico['video_url'], featured=dico['featured'], order=dico['order'])
        
    for dico in SAMPLE_SKILLS:
        insert_skill(name=dico['name'], category=dico['category'], icon=dico["icon"], order=dico["order"])
