from django.db import models

class Recipe(models.Model):
    recipe_title = models.Charfield(label='Title', max_length=1000)
    recipe_ingredients = models.Charfield(label='Ingredients', max_length=10000)
    recipe_directions = models.Charfield(label='Directions', max_length=10000)
