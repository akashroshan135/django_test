from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'blog-home'),              #runs home() in the views.py
    path('about/', views.about, name = 'blog-about'),      #runs about() in the views.py
]
