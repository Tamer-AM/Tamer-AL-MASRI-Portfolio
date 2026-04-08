from flask import Blueprint, render_template
from db_functions import select_all_skills
 
about_bp = Blueprint("about", __name__)
 
 
@about_bp.route("/")
def index():
    skills_dict = {}
    for skill in select_all_skills():
        skills_dict.setdefault(skill.category, []).append(skill)
    return render_template("about.html", skills_dict=skills_dict)