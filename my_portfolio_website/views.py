from django.shortcuts import render
from django.http import HttpResponse 

# function based views

# function for the home page
# renders the home html file
def home(request):
    return render(request, "home.html", {})

# function for the about page
# renders the about html file
def about(request):
    return render(request, "about.html", {})   

# function for the projects page
# renders the projects html file
def projects(request):
    return render(request, "projects.html", {})   