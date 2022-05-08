from . import db
from flask_login import UserMixin
from pony.orm import *


class User(db.Entity, UserMixin):
    id = PrimaryKey(int, auto=True)
    email = Required(str)
    first_name = Required(str)
    last_name = Required(str)
    password = Required(str)
    saved_recipes = Set('Recipe')


class Ingredient(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    recipes = Set('Recipe')


class Recipe(db.Entity):
    id = PrimaryKey(int, auto=True)
    title = Required(str)
    url = Required(str)
    # store ingredients as a character separated list
    ingredients = Required(str)
    directions = Required(str)  # same with ingredients
    users_with_saved = Set(User)
    linked_ingredients = Set(Ingredient)
