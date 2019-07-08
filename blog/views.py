from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1> Blog Home </h1>') #http response to the home url

def about(request):
    return HttpResponse('<h1> Blog About Page </h1>') #http response to the about url