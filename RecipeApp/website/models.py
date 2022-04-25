from . import db
from flask_login import UserMixin

class User(db.Entity, UserMixin):
    email = Required(str)
    first_name = Required(str)
    last_name = Required(str)
    password = Required(str)

class Ingredient(db.Entity):
    name =  Required(str)
    recipes = Set('Recipe')


class Recipe(db.Entity):
    title =  Required(str)
    url = Required(str)
    ingredients =  Required(str) # store ingredients as a character separated list
    directions =  Required(str)#same with ingredients
