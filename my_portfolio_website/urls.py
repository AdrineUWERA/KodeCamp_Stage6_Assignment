# imports path from django.urls module
from django.urls import path
# imports every view in views
from . import views

# array of urls and pages they map to
urlpatterns = [
    path('', views.home, name='home'),
    path('about-me/', views.about, name='about-me'), 
    path('projects/', views.projects, name='my-projects')
]