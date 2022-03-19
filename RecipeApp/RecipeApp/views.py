from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from mysqlx import Auth
from RecipeApp import settings
import mysql.connector
from django.contrib.auth import logout


#Connect to sql database here
config = {
  'user': 'msegan',
  'password': '50235812',
  'host': 'oceanus.cse.buffalo.edu',
  'database': 'cse442_2022_spring_team_e_db',
  'raise_on_warnings': True,
  'autocommit' : True
}
conn = mysql.connector.connect(**config)
connCursor=conn.cursor()


#This is the sql statement that created our recipe table. (coupled with our scraper):
"""connCursor.execute("CREATE TABLE recipes(title VARCHAR(200), ingredients TEXT(65000), instructions TEXT(65000))")"""


def home(request):
    #non logged in users will be sent the response here
    if not request.user.is_authenticated:
        return render(request, 'index.html', {'username': 'Guest'})
    #logged in authenticated users are sent the response here
    else:
        return render(request, 'index.html', {'username': request.user.username})

def register_view(request):
    if request.method=='GET':
        form=UserCreationForm()

    if request.method=='POST':
        form=UserCreationForm(data=request.POST)
        if form.is_valid():
            #add user to database
            form.save()
            #SEND USER TO LOGIN PAGE
            return redirect('/login')

    return render(request, 'auth pages/register.html', {'form': form})


def login_view(request):
    if request.method=='GET':
        form=AuthenticationForm()
        return render(request, 'auth pages/login.html', {'form': form})

    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #LOG IN THE USER HERE
            user=form.get_user()
            login(request, user)
            return redirect('/')

def logout_view(request):
    currentUser=request.user
    if (currentUser.is_authenticated):
        logout(request)
        return redirect('/')
    else:
        return redirect('/')

def new_recipe_view(request):
    if request.method=='GET':
        # TODO: need to render a form for the current user
        return render(request, 'new-recipe.html')

def saved_recipes_view(request):
    if request.method=='GET':
        # TODO: need to render a form for the current user
        return render(request, 'saved-recipes.html')

def search_results_view(request):
    if request.method=='GET':
        # TODO: need to render the results for the current user, this wont work as is
        return render(request, 'search-results.html')

def recipe_view(request):
    if request.method=='GET':
        return render(request, 'recipe.html')


#The following code is for debugging purposes to look into the database through print statements when starting app.
"""
connCursor.execute("Show tables;")
result = connCursor.fetchall()

for s in result:
    print(s)
"""


#close mysql database connection
conn.close()
