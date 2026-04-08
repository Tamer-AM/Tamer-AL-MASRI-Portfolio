from flask import Blueprint, render_template, request, abort
from db_functions import select_all_projects, select_projects_category, select_project_form_slug
 
projects_bp = Blueprint("projects", __name__)
 
CATEGORIES = {
    "personal":   "Personal Projects",
    "cwh":        "CodeWizardsHQ Work",
    "university": "University Projects",
    "school":     "School Projects",
}
 
 
@projects_bp.route("/")
def index():
    active_category = request.args.get("category", "all")
    if active_category == 'all':
        projects = select_all_projects()
    else:
        projects = select_projects_category(active_category)
    return render_template("projects.html", projects=projects, categories=CATEGORIES, active_category=active_category)

@projects_bp.route("/detail/<slug>")
def detail(slug):
    project = select_project_form_slug(slug)
    return render_template('project_info.html', project=project)