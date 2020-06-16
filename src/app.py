from flask import Flask
from src import user, home
from src.ext import db, migrate, bcrypt, ma

def create_app(config_object='src.settings'):


    app = Flask(__name__)
    app.config.from_object(config_object)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ycjhowiv:il_SSZ6oD47EEf2diqvorCMY9_W0Nrho@ruby.db.elephantsql.com:5432/ycjhowiv'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    init_modules(app)
    init_extensions(app, db)

    return app


def init_modules(app):

    user.init_app(app)
    home.init_app(app)


def init_extensions(app, db):
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)


if __name__ == '__main__':

    create_app().run(debug=True)
