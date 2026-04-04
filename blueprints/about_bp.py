from flask import Blueprint, render_template
#from db import Skill
 
about_bp = Blueprint("about", __name__)
 
 
@about_bp.route("/")
def index():
    return render_template("about.html")