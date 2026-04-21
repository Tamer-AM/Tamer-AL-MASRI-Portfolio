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
        "title": "Enterprise Deliberation Platform",
        "slug": "enterprise-deliberation-platform",
        "category": "university",
        "short_desc": "A collaborative internal discussion platform for companies, featuring structured debates, hierarchy-based permissions, and group-targeted discussions.",

        "overview": "A web application designed for enterprise environments where employees, managers, and executives can create, participate in, and moderate internal discussions. The platform supports open debates, closed decision-oriented threads, nested replies, role-based access control, and team/group visibility systems.",

        "problem": "Traditional messaging tools are noisy and unstructured for internal decision-making. Companies often lack a dedicated space for organized deliberation, role-aware participation, and traceable debates tied to departments or project groups.",

        "solution": "Built a custom Flask-based platform with SQLite relational modeling to support hierarchical user roles, group-scoped discussions, likes/dislikes, threaded comments, AJAX interactions, and multiple discussion types with distinct behaviors.",

        "challenges": "Designing a scalable relational schema for users, groups, memberships, discussions, comments, and reactions while avoiding duplicate query results in many-to-many joins. Implementing dynamic UI behavior with JavaScript (live likes, dropdown actions, lazy-loaded replies) and maintaining clean architecture between discussion types required careful backend/frontend separation.",

        "outcome": "Delivered a functional prototype demonstrating real-world product thinking, backend architecture, SQL design, permission systems, and interactive frontend features. The project showcases the ability to build business-oriented software beyond tutorial-level CRUD apps.",

        "tech_tags": "Python,Flask,SQLite,JavaScript,HTML,CSS,Jinja2,SQL",

        "preview_img": None,

        "github_url": None,

        "demo_url": None,

        "video_url": None,

        "featured": True,

        "order": 2
    },
    {
        "title": "Ensemble Data Science Competition Project",
        "slug": "ensemble-data-science-competition",
        "category": "university",
        "short_desc": "A competitive machine learning project combining multiple classifiers, feature selection, and weighted voting to achieve a top leaderboard ranking.",

        "overview": "A university data science project focused on building high-performing predictive models on a real dataset under competitive evaluation. Multiple machine learning algorithms were implemented, compared, tuned, and combined into an ensemble pipeline that significantly outperformed individual models.",

        "problem": "Single-model approaches often plateaued in accuracy or reacted differently to noisy, categorical, and numerical features. The challenge was to identify the strengths of each algorithm and combine them into a more robust final predictor.",

        "solution": "Implemented Naïve Bayes, k-NN with cross-validation, Decision Trees, and Random Forest models using Python scientific libraries. Added preprocessing workflows, feature selection methods such as Cramér's V for categorical relevance, parameter search utilities, and a weighted voting ensemble to merge predictions.",

        "challenges": "Balancing feature engineering, preprocessing quality, hyperparameter tuning cost, and model variance required repeated experimentation. Building reusable validation utilities and combining heterogeneous models into a stable ensemble was the main technical challenge.",

        "outcome": "The final ensemble model substantially outperformed the standalone classifiers and finished tied for #1 on the competition leaderboard. The project demonstrated strong analytical reasoning, experimentation discipline, and practical machine learning workflow design.",

        "tech_tags": "Data Science,Python,Pandas,NumPy,Jupyter,Machine Learning,Cross Validation,Ensemble Learning",

        "preview_img": None,

        "github_url": None,

        "demo_url": None,

        "video_url": None,

        "featured": True,

        "order": 3
    },
    {
        "title": "Motion-Control Karting Game",
        "slug": "motion-control-karting-game",
        "category": "university",
        "short_desc": "A Raspberry Pi-powered karting game using motion sensors as steering controllers, combined with a web interface and race time tracking.",

        "overview": "An interactive racing game project combining embedded systems and web technologies. Players control karts through physical motion using accelerometer sensors connected to a Raspberry Pi, creating a hybrid experience between hardware input and browser-based gameplay.",

        "problem": "Traditional keyboard-only controls lacked originality and physical interaction. The goal was to create a more immersive karting experience using motion sensors, while still keeping the system practical enough for a university environment with limited hardware resources.",

        "solution": "Developed a karting game using Grove motion sensors and Raspberry Pi hardware to capture player movement and translate it into in-game controls. To improve performance, sensor data was transmitted from the Raspberry Pi to a separate computer hosting the game logic and web interface. A hybrid multiplayer mode was also implemented using one motion-controlled player and one keyboard-controlled player.",

        "challenges": "Learning Raspberry Pi development, sensor integration, and real-time motion input handling from scratch was a major challenge. Hosting the game directly on the Raspberry Pi caused performance bottlenecks, which required designing a communication layer to send sensor data to another machine. Two-player sensor mode introduced hardware conflicts that required additional components unavailable at the university, forcing an adaptive fallback solution. Since the game engine ran in an external Python file rather than JavaScript, race timing and score persistence also required custom workaround logic.",

        "outcome": "Delivered a fully functional prototype demonstrating practical hardware/software integration, real-time input systems, networking between devices, and adaptability under hardware constraints. The project highlighted problem-solving skills beyond standard web development.",

        "tech_tags": "Python,Raspberry Pi,Grove Sensors,Flask, Pygame, Hardware Integration,Game Development,Networking,Embedded Systems",

        "preview_img": None,

        "github_url": None,

        "demo_url": "https://projet-karting.onrender.com/",

        "video_url": None,

        "featured": True,

        "order": 4
    },
    {
        "title": "Wizard Typing",
        "slug": "wizard-typing",
        "category": "cwh",
        "short_desc": "A browser-based typing speed game focused on reaction time, accuracy, and competitive keyboard training.",

        "overview": "An interactive typing web application designed to improve typing speed and accuracy through real-time word challenges. The platform emphasizes fast feedback, responsiveness, and engaging gameplay mechanics to make keyboard practice more enjoyable than traditional typing tests. Implemented in my internship with CWHQ",

        "problem": "Most typing websites feel outdated, repetitive, or visually uninspired. Many focus only on raw WPM metrics without creating an engaging experience that motivates users to keep improving.",

        "solution": "Built a custom typing platform with dynamic word generation, real-time scoring, accuracy tracking, and a game-oriented interface. Designed the UX to feel faster, cleaner, and more rewarding than conventional typing trainers.",

        "challenges": "Balancing responsive keyboard input handling with smooth UI updates required careful front-end event management. Creating an experience that remained lightweight while feeling interactive and polished was a key technical focus.",

        "outcome": "Delivered a functional typing game that demonstrates strong front-end fundamentals, DOM manipulation, event-driven programming, UX thinking, and browser performance awareness.",

        "tech_tags": "JavaScript,HTML,CSS,Frontend,Backend,Flask, sqlite3, Matplotlib",

        "preview_img": None,

        "github_url": None,

        "demo_url": "https://9543.wizardtyping.com/",

        "video_url": None,

        "featured": True,

        "order": 5
    },
    {
        "title": "8-Bit Space Invaders",
        "slug": "8bit-space-invaders",
        "category": "school",
        "short_desc": "A custom Space Invaders remake built with Pygame in a retro 8-bit style, developed as my first programming project.",

        "overview": "A school assignment that evolved into a personal passion project. Instead of following the provided step-by-step documentation, I independently designed and implemented my own version of Space Invaders using Pygame, focusing on originality, retro aesthetics, and complete gameplay functionality.",

        "problem": "The assignment could have been completed mechanically by following the professor’s documentation, but that approach would not have reflected creativity, independent problem-solving, or personal coding style. I wanted to challenge myself by building the game from scratch with my own architecture.",

        "solution": "Created a fully playable Space Invaders game using Python and Pygame, featuring custom enemy movement systems, collision logic, scoring mechanics, player controls, and a stylized 8-bit visual identity. The project prioritized originality and experimentation over template-driven implementation.",

        "challenges": "As my first real programming project, I built many systems without prior experience or formal patterns, leading to unconventional implementations and trial-and-error problem solving. Managing game loops, sprite behavior, collisions, and clean state transitions while learning programming fundamentals in parallel was a significant challenge.",

        "outcome": "Delivered a complete and functional arcade game that demonstrated early creativity, persistence, and strong self-learning instincts. While the code can now be optimized with more experience, the project remains an important milestone that reflects initiative and genuine passion for programming.",

        "tech_tags": "Python,Pygame,Game Development",

        "preview_img": None,

        "github_url": None,

        "demo_url": None,

        "video_url": None,

        "featured": False,

        "order": 6
    }
]


SAMPLE_SKILLS = [
    # Languages
    {"name": "Python",      "category": "languages",  "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg",        "order": 1},
    
    {"name": "C",       "category": "languages",    "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/c/c-original.svg",         "order": 2},
    {"name": "Java",       "category": "languages",    "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg",         "order": 3},
    {"name": "HTML/CSS",    "category": "languages", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg",      "order": 4},
    {"name": "JavaScript",  "category": "languages", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg", "order": 5},
    
    # Backend
    {"name": "Flask",       "category": "backend",  "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg",          "order": 1},
    {"name": "SQLite",      "category": "backend",  "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg",        "order": 2},
    {"name": "SQLAlchemy",  "category": "backend",  "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/sqlalchemy/sqlalchemy-original.svg",  "order": 3},

    # Tools
    {"name": "Git",         "category": "tools",    "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg",             "order": 1},
    {"name": "GitHub",      "category": "tools",    "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/github/github-original-wordmark.svg",       "order": 2},
    {"name": "VS Code",     "category": "tools",    "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg",       "order": 3},
    {"name": "Bootstrap",   "category": "tools", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bootstrap/bootstrap-original.svg",  "order": 4},
    {"name": "Linux",       "category": "tools",    "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg",         "order": 5}
]


def seed_tables():
    
    clear_all_db()
    for dico in SAMPLE_PROJECTS:
        insert_project(title=dico['title'],slug=dico['slug'], category=dico["category"], short_desc=dico["short_desc"], overview=dico['overview'], problem=dico['problem'], solution=dico['solution'], challenges=dico['challenges'], outcome=dico['outcome'], tech_tags=dico['tech_tags'], preview_img=dico['preview_img'], github_url=dico['github_url'], demo_url=dico['demo_url'], video_url=dico['video_url'], featured=dico['featured'], order=dico['order'])
        
    for dico in SAMPLE_SKILLS:
        insert_skill(name=dico['name'], category=dico['category'], icon=dico["icon"], order=dico["order"])
