from src.ext import ma
from .models import Student, Teacher, Class
from marshmallow import fields, Schema

class StudentSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Student
        load_instance = True
        
class TeacherSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Teacher
        load_instance = True

class ClassSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Class
        load_instance = True

class LoginSchema(Schema):

    username = fields.String()
    password = fields.String()

