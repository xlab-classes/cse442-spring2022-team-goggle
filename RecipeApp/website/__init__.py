from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "cse442_2022_spring_team_e_db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'jflsiejwlkjsdf'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://jlchugh:50335580@oceanus.cse.buffalo.edu/db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # import the views
    from .views import views
    from .auth import auth

    # register the views
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Ingredient, Recipe

    create_database(app)


    return app

def create_database(app):
    if not path.exists('website/'+ DB_NAME):
        db.create_all(app=app)
        print("database created.")
