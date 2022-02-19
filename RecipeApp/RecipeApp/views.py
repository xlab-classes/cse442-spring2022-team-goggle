from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from mysqlx import Auth
from RecipeApp import settings

def home(request):
    return render(request, 'index.html')

def register(request):
    if request.method=='GET':
        form=UserCreationForm()
        
    if request.method=='POST':
        form=UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            #LOG IN THE USER HERE

    return render(request, 'auth pages/register.html', {'form': form})


def login(request):
    if request.method=='GET':
        form=AuthenticationForm()
        return render(request, 'auth pages/login.html', {'form': form})

    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #LOG IN THE USER HERE
            return HttpResponse("valid login!")
    
