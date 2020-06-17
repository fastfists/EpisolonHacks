from flask import Flask
from .routes import test_bp
from . import models


def init_app(app: Flask):

    app.register_blueprint(test_bp)
