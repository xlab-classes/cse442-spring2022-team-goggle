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
    recipes = db.relationship('Recipe')


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000))
    url = db.Column(db.String(1000))
    ingredients = db.Column(db.String(10000)) # store ingredients as a character separated list
    directions =  db.Column(db.String(10000)) #same with ingredients
