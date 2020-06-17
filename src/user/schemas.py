from src.ext import ma
from .models import Student, Teacher
from marshmallow import fields

class StudentSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Student
        load_instance = True
        

class TeacherSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Teacher
        load_instance = True


