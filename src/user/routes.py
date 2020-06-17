from flask import Blueprint, render_template, request, jsonify
from .auth import create_token, get_user
from .models import Student, Teacher
from .schemas import StudentSchema, TeacherSchema, LoginSchema
from src.ext import bcrypt, db
from slugify import slugify
from flask_jwt_extended import jwt_required

user_bp = Blueprint('user', __name__)

def getObjects(classification):

    if classification.lower() == "teacher":
        schema = TeacherSchema()
        model = Teacher

    elif classification.lower() == "student":
        schema = StudentSchema()
        model = Student
    else:
        return None, None

    return model, schema

@user_bp.route("/api/<string:classification>/register", methods=["POST"])
def register(classification): 

    model, schema = getObjects(classification)

    user = schema.load(request.form)
    user.password = bcrypt.generate_password_hash(user.password).decode('utf-8')
    user.slug = slugify(user.username)
    
    if model.query.filter_by(slug=user.slug).first():
        return jsonify({"status" : "Error", "msg" : "Username already exists"})

    if model.query.filter_by(email=user.email).first():
        return jsonify({"status" : "Error", "msg" : "Email already exists"})

    db.session.add(user)
    db.session.commit()
    
    return jsonify({ "status" : "Success" })

@user_bp.route("/api/<string:classification>/login", methods=["POST"])
def login(classification): 

    schema = LoginSchema()
    body = schema.load(request.form)
    print(body)

    model, _ = getObjects(classification)
    
    user = model.query.filter_by(username=body["username"]).first()
    if user and bcrypt.check_password_hash(user.password, body["password"]):
        access_token = create_token(user.id, classification)
        return jsonify(access_token=access_token)
    return jsonify({ "status": "Error", "message": "Wrong username or password" })

@user_bp.route("/api/<string:classification>/<string:token>")
@jwt_required
def getUser(classification, token): 
    
    _, schema = getObjects(classification)

    return jsonify(schema.dump(get_user()))

@user_bp.route("/api/class/join/<string:code>")
@jwt_required
def joinClass(code):

    return "hi"

