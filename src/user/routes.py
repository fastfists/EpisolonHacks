from flask import Blueprint, render_template, request
from .models import Student, Teacher
from .schemas import StudentSchema, TeacherSchema

user_bp = Blueprint('user', __name__)

@user_bp.route("/api/<string:classification>/<string:slug>")
def get(classification, slug): 

    if classification.lower() == "teacher":
        schema = TeacherSchema
        model = Teacher

    elif classification.lower() == "student":
        schema = StudentSchema
        model = Student

    return schema().dump(model.query.filter_by(slug=slug).first_or_404())

