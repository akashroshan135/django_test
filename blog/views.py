from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author':'Man 1',
        'title':'Blog post 1',
        'content':'Content for blog post 1',
        'date_posted':'08 July, 2019'
    },
    {
        'author':'Man 1',
        'title':'Blog post 2',
        'content':'Content for blog post 2',
        'date_posted':'08 July, 2019'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', context={'title':'About'})
