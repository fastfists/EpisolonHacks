from flask import Blueprint, render_template

home_bp = Blueprint('home', __name__)

@home_bp.route("/")
def home(): 
    return render_template("home/home.html")


@home_bp.route("/dashboard")
def dashboard(): 
    return render_template("home/dashboard.html")

