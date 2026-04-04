from db import db, Project, Skill, ContactMessage
from sqlalchemy import delete, select
from datetime import datetime

###insertions
def insert_project(title:str, slug:str, category:str, short_desc:str, overview:str, problem:str, solution:str, challenges:str, outcome:str, tech_tags:str, preview_img:str, github_url:str, demo_url:str, video_url:str, featured:bool, order:int):
    p = Project(title=title, slug=slug, category=category, short_desc=short_desc,overview=overview, problem=problem, solution=solution, challenges=challenges, outcome=outcome, tech_tags=tech_tags, preview_img=preview_img, github_url=github_url, demo_url=demo_url, video_url=video_url, featured=featured, order=order)
    db.session.add(p)
    db.session.commit()


def insert_skill(name:str, category:str, icon:str, order:int):
    skill = Skill(name=name, category=category, icon=icon, order=order)
    db.session.add(skill)
    db.session.commit()


def insert_contact_message(name:str, email:str, message:str, date:str=datetime.today().strftime('%d-%m-%Y')):
    contact = ContactMessage(name=name, email=email, message=message, date=date)
    db.session.add(contact)
    db.session.commit()

###-----------------------------------------
###selections
def select_featured_projects():
    query = select(Project).where(Project.featured == True)
    result = db.session.scalars(query).all()
    return result



###deletions
def clear_all_db():
    Skill.query.delete()
    Project.query.delete()
    db.session.commit()
    
    
