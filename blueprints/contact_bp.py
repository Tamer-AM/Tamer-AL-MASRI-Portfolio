from flask import Blueprint, render_template, request, flash, redirect, url_for
#from db import db, ContactMessage
 
contact_bp = Blueprint("contact", __name__)
 
 
@contact_bp.route("/", methods=["GET", "POST"])
def index():
    '''function for inserting into contact db if post'''
    return render_template("contact.html")