from django.http import HttpResponse
from django.shortcuts import render
from RecipeApp import settings

def home(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'auth pages/register.html')

def login(request):
    return render(request, 'auth pages/login.html')

def registerForm(request):
    return HttpResponse("User register attempt received.")

def loginForm(request):
    return HttpResponse("User login attempt received.")
