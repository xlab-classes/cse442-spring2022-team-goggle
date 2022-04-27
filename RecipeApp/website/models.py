
class User:
    def __init__(self, email, first_name, last_name, password, saved_recipes):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.saved_recipes = saved_recipes

class Ingredient:
    def __init__(self, name, recipes):
        self.name = name
        self.recipes = recipes


class Recipe:
    def __init__(self,title,url,ingredients,directions):
        self.title = title
        self.url = url
        self.ingredients = ingredients
        self.directions = directions
