from flask import Blueprint, render_template
from db_functions import select_featured_projects
 
main_bp = Blueprint("main", __name__)
 
 
@main_bp.route("/")
def index():
    projects = select_featured_projects()
    print(projects)
    return render_template("index.html", projects=projects)