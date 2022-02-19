from django.http import HttpResponse
from django.shortcuts import render
from RecipeApp import settings

def home(request):
    return render(request, 'index.html')

def register(request):
    if request.method=='GET':
        return render(request, 'auth pages/register.html')
    if request.method=='POST':
        inputUsername=request.POST['username']
        inputPassword=request.POST['password']
        return HttpResponse("User register attempt received: Username was " + inputUsername + " and the password was " + inputPassword + " (dont forget to hash when I add to database)")


def login(request):
    if request.method=='GET':
        return render(request, 'auth pages/login.html')
    if request.method=='POST':
        inputUsername=request.POST['username']
        inputPassword=request.POST['password']
        return HttpResponse("User login attempt received: Username was " + inputUsername + " and the password was " + inputPassword + " (dont forget to hash when I add to database)")

    
