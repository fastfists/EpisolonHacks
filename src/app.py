from flask import Flask
from src import test, user, home
from src.ext import db, migrate, bcrypt, ma, jwt

def create_app(config_object='src.settings'):

    app = Flask(__name__)
    app.config.from_object(config_object)
    init_modules(app)
    init_extensions(app, db)

    return app


def init_modules(app):

    test.init_app(app)
    user.init_app(app)
    home.init_app(app)

def init_extensions(app, db):

    db.init_app(app)
    db.app = app
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    jwt.init_app(app)


if __name__ == '__main__':

    create_app().run(debug=True)
