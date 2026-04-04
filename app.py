from flask import Flask
from blueprints.main_bp import main_bp
from blueprints.projects_bp import projects_bp
from blueprints.about_bp import about_bp
from blueprints.contact_bp import contact_bp
from db import db
 
def create_app():
    app = Flask(__name__)
 
    # --- Config ---
    app.config["SECRET_KEY"] = "change-me-before-deploy"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///portfolio.db"  # stored in /instance/
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
 
    # --- Extensions ---
    db.init_app(app)
 
    # --- Blueprints ---
    app.register_blueprint(main_bp)
    app.register_blueprint(projects_bp, url_prefix="/projects")
    app.register_blueprint(about_bp, url_prefix="/about")
    app.register_blueprint(contact_bp, url_prefix="/contact")
 
    # --- DB init (first run) ---
    with app.app_context():
        db.create_all()
 
    return app
 
 
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)