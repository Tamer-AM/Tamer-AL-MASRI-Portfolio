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
        "preview_imgs": "my portfolio homepage.jpg",
        "github_url": "https://github.com/Tamer-AM/Tamer-AL-MASRI-Portfolio",
        "demo_url": None,
        "video_url": None,
        "featured": False,
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

        "preview_imgs": "les debatteurs homepage PROTOTYPE.jpg",

        "github_url": "https://gitlabsu.sorbonne-universite.fr/lu2in013/fev2026/gr1/les-debatteurs",

        "demo_url": None,

        "video_url": None,

        "featured": True,

        "order": 2
    },
    {
        "title": "Data Science Competition - Tree Diagnosis Classification",
        "slug": "data-science-competition-tree-diagnosis-classification",
        "category": "university",
        "short_desc": "A competitive from-scratch machine learning project combining multiple classifiers, feature selection, and weighted voting to achieve a top leaderboard ranking.",

        "overview": "A university data science competition project focused on predicting the classification_diagnostic status of city trees using structured environmental and botanical data. Rather than relying on scikit-learn abstractions, we implemented and tuned the models manually to understand the algorithms deeply.",

        "problem": "The dataset mixed categorical and numerical features, noisy variables, and multiclass outputs. The objective was to maximize prediction accuracy while working under academic constraints and implementing core methods ourselves.",

        "solution": "Built a complete ML workflow including preprocessing, label encoding, normalization, feature selection, custom KNN, Decision Tree, Random Forest, cross-validation, hyperparameter search, and a weighted ensemble voting model.",

        "challenges":"Implementing tree-based models manually, keeping train/test encodings consistent, optimizing expensive feature-combination searches, balancing multiple model outputs, and making the notebook reusable and easy to debug.",

        "outcome": "The final ensemble model significantly outperformed the standalone models and finished tied for 1st place on the class leaderboard.",

        "tech_tags": "Data Science,Python,Pandas,NumPy,Jupyter,Machine Learning,Cross Validation,KNN,Decision Tree,Random Forest,Ensemble Learning",

        "preview_imgs": "royalty free urban trees.jpg",

        "github_url": "https://github.com/Tamer-AM/are-tree-diagnosis-classification-from-scratch",

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

        "preview_imgs": "karting project homepage.jpg,karting project img1.jpeg,karting project img2.jpeg",

        "github_url": "https://github.com/Tamer-AM/Projet-Karting",

        "demo_url": "https://projet-karting.onrender.com/",

        "video_url": "karting project usage footage.mp4",

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

        "preview_imgs": 'wizard typing project homepage.jpg',

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
    "short_desc": "My first coding project - A retro-style Space Invaders remake built in Python with Pygame Zero, featuring custom pixel-art visuals, original gameplay systems, and arcade mechanics.",

    "overview": "Originally developed as a school assignment, this project quickly evolved into a personal challenge to build a complete Space Invaders game independently rather than following the provided tutorial structure. I designed and implemented my own version from scratch, focusing on originality, retro 8-bit aesthetics, and fully playable arcade gameplay.",

    "problem": "The assignment could have been completed by mechanically reproducing the professor’s documentation, but that would not demonstrate creativity, problem-solving ability, or independent programming skills. I wanted to push myself by creating my own architecture and gameplay systems while still learning the fundamentals of coding.",

    "solution": "Built a complete Space Invaders clone in Python using Pygame Zero, featuring custom code-generated pixel sprites, enemy wave movement logic, shooting mechanics, destructible bases, collision systems, score tracking, lives management, sound effects, music integration, and start / win / lose game states.",

    "challenges": "As my first serious programming project, many systems were created through experimentation without prior experience in software architecture or game development patterns. Managing the game loop, collision detection, animation timing, enemy behavior, state transitions, and asset handling while learning Python simultaneously was the main challenge.",

    "outcome": "Successfully delivered a complete and functional arcade game that showcased strong curiosity, self-learning ability, and creative initiative. Although the codebase reflects an early learning stage and can now be significantly improved, the project remains an important milestone in my development journey.",

    "tech_tags": "Python,Pygame Zero,Pygame,Game Development",

    "preview_imgs": "Space Invaders beginning.jpg",

    "github_url": "https://github.com/Tamer-AM/Space-Invaders-pygame",

    "demo_url": None,

    "video_url": "Space Invaders gameplay recording with audio.mp4",

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
        insert_project(title=dico['title'],slug=dico['slug'], category=dico["category"], short_desc=dico["short_desc"], overview=dico['overview'], problem=dico['problem'], solution=dico['solution'], challenges=dico['challenges'], outcome=dico['outcome'], tech_tags=dico['tech_tags'], preview_imgs=dico['preview_imgs'], github_url=dico['github_url'], demo_url=dico['demo_url'], video_url=dico['video_url'], featured=dico['featured'], order=dico['order'])
        
    for dico in SAMPLE_SKILLS:
        insert_skill(name=dico['name'], category=dico['category'], icon=dico["icon"], order=dico["order"])
