from flask import Flask

from pony.orm import *
from os import path
import pdb

db = Database()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'jflsiejwlkjsdf'


    from .models import User, Ingredient, Recipe

    """
     Pony tries to establish a test connection to the database.
     If the specified parameters are not correct or the database is not available,
     an exception will be raised. After the connection to the database was established,
     Pony retrieves the version of the database and returns the connection to the connection pool.
     https://ponyorm.readthedocs.io/en/latest/api_reference.html#Database.bind
    """
    db.bind('mysql', host='oceanus.cse.buffalo.edu', user='jlchugh',
            passwd='50335580', db='cse442_2022_spring_team_e_db')

    db.generate_mapping(create_tables=True)
    #db.set_sql_debug(True)
    # import the views
    from .views import views
    from .auth import auth

    # register the views
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
