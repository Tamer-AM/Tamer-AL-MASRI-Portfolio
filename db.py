"""
db.py — single SQLAlchemy instance + all ORM models.

Import `db` wherever you need the extension (app.py, blueprints, seeds).
Import individual models where you need to query them.
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------

class Project(db.Model):
    """Represents a portfolio project."""

    __tablename__ = "projects"

    id          = db.Column(db.Integer, primary_key=True)
    title       = db.Column(db.String(120), nullable=False)
    slug        = db.Column(db.String(120), unique=True, nullable=False)   # used in URL  /projects/<slug>
    category    = db.Column(db.String(60),  nullable=False)                # e.g. "personal" | "cwh" | "university" | "school"
    short_desc  = db.Column(db.String(300), nullable=False)                # card blurb
    overview    = db.Column(db.Text, nullable=True)                        # detail page – context & goal
    problem     = db.Column(db.Text, nullable=True)                        # detail page – problem statement
    solution    = db.Column(db.Text, nullable=True)                        # detail page – approach
    challenges  = db.Column(db.Text, nullable=True)                        # detail page – challenges & solutions
    outcome     = db.Column(db.Text, nullable=True)                        # detail page – results
    tech_tags   = db.Column(db.String(300), nullable=True)                 # comma-separated  e.g. "Python,Flask,SQLite"
    preview_imgs = db.Column(db.String(200), nullable=True)                 # path relative to /static/img/
    github_url  = db.Column(db.String(300), nullable=True)
    demo_url    = db.Column(db.String(300), nullable=True)                 # leave None if no live demo
    video_url   = db.Column(db.String(300), nullable=True)                 # YouTube embed URL
    featured    = db.Column(db.Boolean, default=False)                     # shown on home page hero grid
    order       = db.Column(db.Integer, default=0)                         # manual sort order

    # helper ----------------------------------------------------------------
    @property
    def tags_list(self):
        """Return tech_tags as a Python list."""
        if not self.tech_tags:
            return []
        return [t.strip() for t in self.tech_tags.split(",")]
    
    @property
    def images(self):
        """Return images as a Python list."""
        if not self.tech_tags:
            return []
        return [t.strip() for t in self.preview_imgs.split(",")]
    

    def __repr__(self):
        return f"<Project {self.slug}>"


class Skill(db.Model):
    """A single skill shown on the About page and Tech Stack section."""

    __tablename__ = "skills"

    id       = db.Column(db.Integer, primary_key=True)
    name     = db.Column(db.String(80),  nullable=False)
    category = db.Column(db.String(60),  nullable=False)   # "frontend" | "backend" | "tools"
    icon     = db.Column(db.String(200), nullable=True)    # path or CDN URL to SVG/PNG icon
    order    = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"<Skill {self.name}>"


class ContactMessage(db.Model):
    """Stores messages submitted via the contact form."""

    __tablename__ = "contact_messages"

    id         = db.Column(db.Integer, primary_key=True)
    name       = db.Column(db.String(120), nullable=False)
    email      = db.Column(db.String(200), nullable=False)
    message    = db.Column(db.Text,        nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f"<ContactMessage from {self.email}>"