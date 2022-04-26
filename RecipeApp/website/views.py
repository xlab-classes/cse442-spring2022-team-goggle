from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")


# should have a 'add recipe' button to add the recipe
@views.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    return render_template("add_recipe.html")


# search should have a 'go' button for post
@views.route('/search_recipe', methods=['GET', 'POST'])
def search_recipe():
    return render_template("search_recipe.html")


# each recipe should have a button with 'go' on it for post
@views.route('/view_saved_recipes', methods=['GET', 'POST'])
def view_saved_recipes():
    return render_template("saved_recipes.html")


@views.route('/my_profile', methods=['GET', 'POST'])
def my_profile():
    return render_template("my_profile.html")
