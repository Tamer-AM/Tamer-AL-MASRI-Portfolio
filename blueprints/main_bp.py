from flask import Blueprint, render_template
#from db import Project, Skill
 
main_bp = Blueprint("main", __name__)
 
 
@main_bp.route("/")
def index():
    return render_template("index.html")