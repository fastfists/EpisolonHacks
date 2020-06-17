from src.ext import db
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.schema import Table
from sqlalchemy.orm import relationship


##############################################################

class Test(db.Model):

    id = Column(Integer, primary_key=True)


# class SubmittedTest(Test):

#     student_id = Column(Integer, db.ForeignKey('student.id'))
#     questions = relationship('SubmittedQuestion', backref='test')

# class EmptyTest(Test):

#     questions = relationship('EmptyQuestion', backref='test')

##############################################################

class Question(db.Model): 

    id = Column(Integer, primary_key=True)
    test_id = Column(Integer, db.ForeignKey('test.id'))
    answers = relationship('Answer', backref='question')
    questionString = Column(String)


# class EmptyQuestion(Question): 

#     id = Column(Integer, primary_key=True)
#     test_id = Column(Integer, db.ForeignKey('emptytest.id'))
#     answers = relationship('EmptyAnswer', backref='question')

# class SubmittedQuestion(Question): 

#     id = Column(Integer, primary_key=True)
#     test_id = Column(Integer, db.ForeignKey('submittedtest.id'))
#     answers = relationship('SubmittedAnswer', backref='question')


##############################################################

class Answer(db.Model):

    id = Column(Integer, primary_key=True)
    answerString = Column(String)
   
    is_correct = Column(Boolean, nullable=False)

# class SubmittedAnswer(Answer):

#     id = Column(Integer, primary_key=True)
   
#     question_id = Column(Integer, db.ForeignKey('submittedquestion.id'))


# class EmptyAnswer(Answer):

#     id = Column(Integer, primary_key=True)
   
#     question_id = Column(Integer, db.ForeignKey('emptyquestion.id'))

##############################################################
