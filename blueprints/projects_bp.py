from flask import Blueprint, render_template, request, abort
#from db import Project
 
projects_bp = Blueprint("projects", __name__)
 
CATEGORIES = {
    "personal":   "Personal Projects",
    "cwh":        "CodeWizardsHQ Work",
    "university": "University Projects",
    "school":     "School Projects",
}
 
 
@projects_bp.route("/")
def index():
    return render_template("projects.html")

@projects_bp.route("/detail/<slug>")
def detail():
    return render_template('project_info.html')