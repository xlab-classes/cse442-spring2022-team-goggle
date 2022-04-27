from flask import Blueprint, render_template, request
from .global_vars import *
from .models import *

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")


# should have a 'add recipe' button to add the recipe
@views.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        title = request.form.get('title')
        ingredients_string = request.form.get("ingredients")
        directions_string = request.form.get("directions")
        global recipes
        global saved_recipes
        new_recipe = Recipe(url='',title=title, directions=directions_string.split('#'),ingredients=ingredients_string.split(','))
        recipes += [new_recipe]
        saved_recipes += [new_recipe]
        return render_template("saved_recipes.html",saved_recipes=saved_recipes)


    return render_template("add_recipe.html")


# search should have a 'go' button for post
@views.route('/search_recipe', methods=['GET', 'POST'])
def search_recipe():
    if request.method == 'POST':
        ingredients_list = request.form.get("ingredients").split(',')

        recipes_to_show = []
        for recipe in recipes:
            ingredients = recipe.ingredients
            if set(ingredients_list).issubset(set(ingredients)):
                recipes_to_show += [recipe]


        return render_template("recipe_search_results.html", recipes=recipes_to_show)
    return render_template("search_recipe.html")


# each recipe should have a button with 'go' on it for post
@views.route('/saved_recipes', methods=['GET', 'POST'])
def view_saved_recipes():
    if request.method =='POST':
        return render_template("show_recipe.html",recipe)
    return render_template("saved_recipes.html", saved_recipes=saved_recipes)


@views.route('/my_profile', methods=['GET', 'POST'])
def my_profile():
    return render_template("my_profile.html")

@views.route('/show_recipe/<recipe_title>', methods=['GET', 'POST'])
def show_recipe(recipe_title):
    recipe = None
    for r in recipes:
        if r.title == recipe_title:
            recipe = r
            break

    return render_template("show_recipe.html", recipe=recipe)

@views.route('/recipe_search_results', methods=['GET', 'POST'])
def recipe_search_results():
    if request.method == 'POST':
        return render_template("show_recipe.html",recipe)


    return render_template("recipe_search_results.html")
