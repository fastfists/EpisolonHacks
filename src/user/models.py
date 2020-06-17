from src.ext import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.schema import Table
from sqlalchemy.orm import relationship

class Teacher(db.Model):

    id = Column(Integer, primary_key=True)

    email = Column(String, unique=True)
    password = Column(String(256))
    username = Column(String, unique=True)
    slug = Column(String, index= True)

    classes = relationship("Class", backref = "teacher" )


# maps students to classes
student_class = db.Table('student_class',
        Column('student_id', Integer, db.ForeignKey('student.id')),
        Column('class_id', Integer, db.ForeignKey('class.id')),
)

class Class(db.Model):

    id = Column(Integer, primary_key=True)

    name = Column(String)
    joinCode = Column(String(8))
    teacher_id = Column(Integer, db.ForeignKey('teacher.id'))

class Student(db.Model):

    id = Column(Integer, primary_key=True)

    email = Column(String, unique=True)
    password = Column(String(256))
    username = Column(String, unique=True)
    slug = Column(String, index= True)

    classes = relationship('Class', secondary=student_class, backref=db.backref('students', lazy='dynamic'))
    tests = relationship('SubmittedTest', backref='student')


