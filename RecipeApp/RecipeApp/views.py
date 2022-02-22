from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from mysqlx import Auth
from RecipeApp import settings
import mysql.connector
import bcrypt


#Connect to sql database here
config = {
  'user': 'admin',
  'password': 'admin',
  'host': '127.0.0.1',
  'database': 'recipeapp',
  'raise_on_warnings': True
}

conn = mysql.connector.connect(**config)



def home(request):
    #non logged in users will be sent the response here
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    #logged in authenticated users are sent the response here
    else:
        return HttpResponse("You are an authenticated user who is currently logged in and at the home page!")

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

#close mysql database connection    
conn.close()