from flask import Blueprint, render_template, request, jsonify
from .auth import create_token, get_user
from .models import Student, Teacher
from .schemas import StudentSchema, TeacherSchema, LoginSchema
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
    user.password = bcrypt.generate_password_hash(user.password).decode('utf-8')
    user.slug = slugify(user.username)
    
    if model.query.filter_by(slug=user.slug).first():
        # TODO Handle this
        return 

    db.session.add(user)
    db.session.commit()
    
    return jsonify({ "status" : "Success" })

@user_bp.route("/api/<string:classification>/login", methods=["POST"])
def login(classification): 

    schema = LoginSchema()
    body = schema.load(request.form)
    print(body)

    if classification.lower() == "teacher":
        model = Teacher

    elif classification.lower() == "student":
        model = Student
    
    user = model.query.filter_by(username=body["username"]).first()
    if user and bcrypt.check_password_hash(user.password, body["password"]):
        access_token = create_token(user.id, classification)
        return jsonify(access_token=access_token)
    return jsonify({ "status": "Error", "message": "Wrong username or password" })

