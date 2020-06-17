from src.ext import db
from sqlalchemy import Column, Integer, String, Boolean, Float
from sqlalchemy.schema import Table
from sqlalchemy.orm import relationship


##############################################################

class SubmittedTest(db.Model):

    id = Column(Integer, primary_key=True)

    student_id = Column(Integer, db.ForeignKey('student.id'))
    questions = relationship('SubmittedQuestion', backref='test')

class EmptyTest(db.Model):

    id = Column(Integer, primary_key=True)

    questions = relationship('EmptyQuestion', backref='test')

##############################################################

class EmptyQuestion(db.Model): 

    id = Column(Integer, primary_key=True)

    points = Column(Float)

    questionString = Column(String)
    test_id = Column(Integer, db.ForeignKey('emptytest.id'))
    answers = relationship('EmptyAnswer', backref='question')

class SubmittedQuestion(db.Model): 

    id = Column(Integer, primary_key=True)

    points = Column(Float)
    
    questionString = Column(String)
    test_id = Column(Integer, db.ForeignKey('submittedtest.id'))
    answers = relationship('SubmittedAnswer', backref='question')


##############################################################

class SubmittedAnswer(db.Model):

    id = Column(Integer, primary_key=True)
    answerString = Column(String)
    is_correct = Column(Boolean, nullable=False)

    is_chosen = Column(Boolean, nullable=False, default=True)

    question_id = Column(Integer, db.ForeignKey('submittedquestion.id'))


class EmptyAnswer(db.Model):

    id = Column(Integer, primary_key=True)
    answerString = Column(String)
    is_correct = Column(Boolean, nullable=False)

    question_id = Column(Integer, db.ForeignKey('emptyquestion.id'))

##############################################################



