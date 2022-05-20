from flask import Blueprint, render_template, request,flash,redirect, url_for
from flask_login import login_required, current_user
import pony.orm as pny
from .models import User, Recipe, Ingredient

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        class RecipeBodge:
            def __init__(self,title,url,ingredients,directions):
                self.title = title
                self.url = url
                self.ingredients = ingredients
                self.directions = directions


        display_these_recipes = []
        with pny.db_session:
            usr = User.get(email=current_user.email, first_name = current_user.first_name, last_name = current_user.last_name)

            for rp in usr.saved_recipes:
                display_these_recipes.append(RecipeBodge(rp.title, rp.url, rp.ingredients,rp.directions))
        return render_template("saved_recipes.html", user=current_user, saved_recipes = display_these_recipes)


    return render_template("home.html", user=current_user)


# should have a 'add recipe' button to add the recipe
# TODO
@views.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        title = request.form.get('title')
        ingredients = request.form.get("ingredients").replace(',', "#")
        directions = request.form.get("directions")



        with pny.db_session:
            new_recipe = Recipe(title = title, ingredients = ingredients, directions = directions,url="_")


            for ingredient in ingredients.split('#'):
                ing = Ingredient.select(lambda i: ingredient in i.name).first()
                if ing:
                    ing.recipes.add(new_recipe)
                else:
                    new_ing = Ingredient(name = ingredient)
                    new_ing.recipes.add(new_recipe)

        flash("registered", category='success')
        return redirect(url_for('views.home'))

    return render_template("add_recipe.html", user=current_user)


# search should have a 'go' button for post
@views.route('/search_recipe', methods=['GET', 'POST'])
def search_recipe():
    if request.method == 'POST':
        if request.form.get("ingredients") == '':
            flash("Please enter ingredient(s)", category='error')
            return redirect(url_for('views.search_recipe'))
        if request.form.get("distance") == '':
            flash("Please enter number of missing ingredients", category='error')
            return redirect(url_for('views.search_recipe'))


        ingredients_list = request.form.get("ingredients").split(',')
        distance = int(request.form.get("distance")) + len(ingredients_list) # need to count the current ingredients
        # start with just the first ingredient
        recipe_results = set([])
        with pny.db_session:
            recipe_results = set(Recipe.select(lambda recipe: ingredients_list[0] in recipe.ingredients))

            for ingredient in ingredients_list:
                recipe_results = recipe_results & set(Recipe.select(lambda recipe: ingredient in recipe.ingredients))

        # convert back to a list
        recipe_results = list(recipe_results)
        if int(request.form.get("distance")) == -1:
            return render_template("recipe_search_results.html", recipes=recipe_results, user=current_user)


        results_using_param = []
        for result in recipe_results:
            needed_ingredients = len(result.ingredients.split('#'))
            available_ingredients = len(ingredients_list)
            if needed_ingredients - available_ingredients <= distance:
                results_using_param.append(result)


        return render_template("recipe_search_results.html", recipes=results_using_param, user=current_user)


    return render_template("search_recipe.html", user=current_user)


# each recipe should have a button with 'go' on it for post
@views.route('/saved_recipes', methods=['GET', 'POST'])
@login_required
def saved_recipes():
    return render_template("saved_recipes.html", user=current_user)


@views.route('/my_profile', methods=['GET', 'POST'])
@login_required
def my_profile():
    with pny.db_session:
        number = len(User.get(email=current_user.email, first_name = current_user.first_name, last_name = current_user.last_name).saved_recipes)
    return render_template("my_profile.html", user=current_user,recipe_count = number)



@views.route('/show_recipe/<recipe_title>', methods=['GET', 'POST'])
def show_recipe(recipe_title):
    if request.method =='POST':
        class RecipeBodge:
            def __init__(self,title,url,ingredients,directions):
                self.title = title
                self.url = url
                self.ingredients = ingredients
                self.directions = directions

        display_these_recipes = []
        with pny.db_session:
            recipe = Recipe.select(title = recipe_title).first()
            usr = User.get(email=current_user.email, first_name = current_user.first_name, last_name = current_user.last_name)
            usr.saved_recipes.add(recipe)

            for rp in usr.saved_recipes:
                display_these_recipes.append(RecipeBodge(rp.title, rp.url, rp.ingredients,rp.directions))


        flash("Recipe Saved", category='success')


        return render_template("saved_recipes.html", user=current_user, saved_recipes = display_these_recipes)


    with pny.db_session:
        recipe = Recipe.select(title = recipe_title).first()
    return render_template("show_recipe.html", recipe=recipe, user = current_user)
