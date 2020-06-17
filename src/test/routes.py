from flask import Blueprint, render_template, request
# from .models import Student, Teacher
# from .schemas import StudentSchema, TeacherSchema

test_bp = Blueprint('test', __name__)

# @test_bp.route("/api/test")
# def get(classification, slug): 

#     schema = StudentSchema
#     model = Student

#     return schema().dump(model.query.filter_by(slug=slug).first_or_404())

