# Tamer-AL-MASRI-Portfolio
# Personal Portfolio — Flask + Bootstrap 5

A recruiter-ready personal portfolio with a dark theme, blue accents,
glassmorphism cards, and a SQLite-backed project database.

---

## Project Structure

```
portfolio/
├── app.py                  # App factory — wires everything together
├── db.py                   # SQLAlchemy instance + all ORM models
├── seed.py                 # Dev helper: populates DB with sample data
├── requirements.txt
├── .gitignore
│
├── blueprints/             # One blueprint per page group
│   ├── __init__.py
│   ├── main_bp.py          # / → home page
│   ├── projects_bp.py      # /projects + /projects/<slug>
│   ├── about_bp.py         # /about
│   └── contact_bp.py       # /contact (GET + POST)
│
├── templates/
│   ├── layout.html         # Base template: navbar, footer, flash msgs
│   ├── index.html          # Home: hero, featured projects, tech stack
│   ├── projects.html       # Project grid with filter tabs
│   ├── project_info.html   # Case-study detail page
│   ├── about.html          # Bio + grouped skills + CV download
│   ├── contact.html        # Contact form + direct links
│   └── partials/
│       └── project_card.html   # Reusable card component ({% include %})
│
├── static/
│   ├── css/
│   │   └── main.css        # Full design system (tokens, components, layout)
│   ├── js/
│   │   └── main.js         # Micro-interactions (scroll shadow, fade-in)
│   ├── img/                # portrait.jpg + project preview images
│   └── cv/                 # your-cv.pdf (gitignored — add manually)
│
└── instance/               # Auto-created by Flask — holds portfolio.db
```

---

## Quick Start

```bash
# 1. Clone & enter
git clone https://github.com/yourusername/portfolio.git
cd portfolio

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your portrait
cp /path/to/photo.jpg static/img/portrait.jpg

# 5. Run once to create the DB
python app.py


# 7. Visit http://127.0.0.1:5000
```

---

## Adding Your Own Projects

Edit `seed.py` and re-run it, **or** add projects directly in Python:

```python
from app import create_app
from db import db, Project

app = create_app()
with app.app_context():
    p = Project(
        title="My Cool Project",
        slug="my-cool-project",          # becomes /projects/my-cool-project
        category="personal",             # personal | cwh | university | school
        short_desc="One-line summary shown on the card.",
        overview="Full context paragraph for the detail page.",
        problem="What problem did this solve?",
        solution="How did you approach it?",
        challenges="What was hard and how did you fix it?",
        outcome="What was the result?",
        tech_tags="Python,Flask,Bootstrap",   # comma-separated
        preview_img="myproject.png",           # file in static/img/
        github_url="https://github.com/...",
        demo_url=None,                         # omit if no live demo
        video_url=None,                        # YouTube embed URL
        featured=True,                         # show on home page
        order=5,
    )
    db.session.add(p)
    db.session.commit()
```


## Design System

All visual tokens live in `static/css/main.css` under `:root`:

| Token | Default | Purpose |
|---|---|---|
| `--pf-accent` | `#3b82f6` | Primary blue — buttons, links, glows |
| `--pf-bg` | `#0d1117` | Page background |
| `--pf-surface` | `#161d27` | Card background |
| `--pf-radius` | `12px` | Card border radius |
| `--pf-font` | `DM Sans` | Body typeface |
| `--pf-font-mono` | `DM Mono` | Code / brand monospace |

Change `--pf-accent` to instantly re-theme the entire site.