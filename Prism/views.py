from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def project(request):
    return render(request,'project.html')

def team(request):
    return render(request,'team.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

def evaluate(request):
    return render(request,'evaluate.html')

def leaderboard(request):
    return render(request,'leaderboard.html')

def updates(request):
    return render(request,'updates.html')