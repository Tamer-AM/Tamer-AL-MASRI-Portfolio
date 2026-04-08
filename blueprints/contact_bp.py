from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_mail import Message, Mail
from db_functions import insert_contact_message
 
contact_bp = Blueprint("contact", __name__)

mail = Mail()    
 
 
@contact_bp.route("/", methods=["GET", "POST"])
def index():
    '''function for inserting into contact db if post'''
    if request.method == 'POST':
        name = request.form.get('contact-name')
        email = request.form.get('contact-email')
        message = request.form.get('contact-message')
        flash_msg = []
        if name == "":
            flash_msg += ["A valid name is required"]
        if email == "" or "@" not in email:
            flash_msg += ["A valid email is required"]
        if message == "":
            flash_msg += ["A valid message is required"]
        if flash_msg != []:
            for error in flash_msg:
                flash(error, 'danger')
            return render_template('contact.html')
        
        flash("Thanks for reaching out! I'll get back to you soon.", "success")
        insert_contact_message(name, email, message)
        msg = Message(
            subject=f"New contact message from {name} - PORTFOLIO",
            sender="tamergmasri@gmail.com",
            recipients=["tamergmasri@gmail.com"],
            body=f""" You got new message from your: PORTFOLIO WEBSITE
                Name: {name}
                Email: {email}

                Message:
                {message}
                """
            )

        mail.send(msg)

    return render_template("contact.html")