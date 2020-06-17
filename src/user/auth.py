from flask_jwt_extended import create_access_token, get_jwt_identity
from .models import Student, Teacher

def create_token(user_id, classification: str):

    return create_access_token(identity=f"{classification[0:3].lower()}{user_id}")

def get_user():

    token = get_jwt_identity()
    if token[0:3].lower() == "stu":
        model =  Student
    elif token[0:3].lower() == "tea":
        model = Teacher

    return model.get(int(token[3:]))

