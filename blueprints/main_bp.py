from flask import Blueprint, render_template
from db_functions import select_featured_projects, select_all_skills
 
main_bp = Blueprint("main", __name__)
 
 
@main_bp.route("/")
def index():
    projects = select_featured_projects()
    skills = select_all_skills()
    return render_template("index.html", projects=projects, skills=skills)