from django.http import HttpResponse
from django.shortcuts import render



def webpage1(request):
    return render(request,'login.html')

def webpage2(request):
    return render(request,'register.html')

def webpage3(request):
    return render(request,'recipe.html')

def webpage4(request):
    return render(request,'new-recipe.html')

def webpage5(request):
    return render(request,'saved-recipes.html')

def webpage6(request):
    return render(request,'search-result.html')