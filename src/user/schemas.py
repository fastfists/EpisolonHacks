from src.ext import ma
from .models import Student, Teacher
from marshmallow import fields

class StudentSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Student

class TeacherSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Teacher
