from flask import Blueprint, render_template, request, jsonify
from .models import Student, Teacher
from .schemas import StudentSchema, TeacherSchema
from src.ext import bcrypt, db
from slugify import slugify
from sqlalchemy import or_

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

@user_bp.route("/api/<string:classification>/register", methods=["POST"])
def register(classification): 

    if classification.lower() == "teacher":
        schema = TeacherSchema()
        model = Teacher

    elif classification.lower() == "student":
        schema = StudentSchema()
        model = Student

    user = schema.load(request.form)
    user.password = bcrypt.generate_password_hash(user.password)
    user.slug = slugify(user.username)
    
    if model.query.filter_by(slug=user.slug).first():

        return 


    db.session.add(user)
    db.session.commit()
    
    return jsonify({ "status" : "Success" })

@user_bp.route("/api/<string:classification>/login", methods=["POST"])
def login(classification): 

    if classification.lower() == "teacher":
        schema = TeacherSchema
        model = Teacher

    elif classification.lower() == "student":
        schema = StudentSchema
        model = Student

    return schema().dump(model.query.filter_by(slug=slug).first_or_404())
