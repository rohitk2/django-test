from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

posts = [
    {
        'author': 'CoreyMS',
        'title': 'da;jkf'
    },
    {
        'author': 'CoreyMS2',
        'title': 'da;jkf2'
    }
]

def home(request) :
    context = {
        'posts': posts
    }
    return render(request, "home.html", context)


def about(request):
    return render(request, "about.html", {})


