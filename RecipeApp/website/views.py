from flask import Blueprint, render_template, request
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)


# should have a 'add recipe' button to add the recipe
@views.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    return render_template("add_recipe.html", user=current_user)


# search should have a 'go' button for post
@views.route('/search_recipe', methods=['GET', 'POST'])
def search_recipe():
    return render_template("search_recipe.html", user=current_user)


# each recipe should have a button with 'go' on it for post
@views.route('/view_saved_recipes', methods=['GET', 'POST'])
@login_required
def view_saved_recipes():
    return render_template("saved_recipes.html", user=current_user)


@views.route('/my_profile', methods=['GET', 'POST'])
@login_required
def my_profile():
    return render_template("my_profile.html", user=current_user)
