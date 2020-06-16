from src.ext import db
from sqlalchemy.orm import relationship


class Teacher(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String, unique=True)
    slug = db.Column(db.String)
    email = db.Column(db.String)
    passowrd = db.Column(db.String(256))

    students = relationship("Student", backref = "teacher" )

class Student(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String, unique=True)
    slug = db.Column(db.String)
    email = db.Column(db.String)
    passowrd = db.Column(db.String(256))

    teacher_id = db.Column(db.Integer, db.ForeignKey("teacher.id"))


