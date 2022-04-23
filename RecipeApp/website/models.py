from . import db
from flask_login import UserMixin
from sqlalchem.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    password = db.Column(db.String(50))

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipes = []


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title =
    url =
    ingredients =
