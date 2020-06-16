from src.ext import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.schema import Table
from sqlalchemy.orm import relationship


class Teacher(db.Model):

    id = Column(Integer, primary_key=True)

    username = Column(String, unique=True)
    slug = Column(String, index= True)
    email = Column(String)
    passowrd = Column(String(256))

    students = relationship("Student", backref = "teacher" )

# maps students to classes
student_class = db.Table('student_class',
        Column('student_id', Integer, db.ForeignKey('student.id')),
        Column('class_id', Integer, db.ForeignKey('class.id')),
)

class Class(db.Model):

    id = Column(Integer, primary_key=True)

    name = Column(String)
    joinCode = Column(String(8))

class Student(db.Model):

    id = Column(Integer, primary_key=True)

    username = Column(String, unique=True)
    slug = Column(String, index= True)
    email = Column(String)
    passowrd = Column(String(256))

    classes = relationship('Class', secondary=student_class, backref=db.backref('students', lazy='dynamic'))

    teacher_id = Column(Integer, db.ForeignKey("teacher.id"))

