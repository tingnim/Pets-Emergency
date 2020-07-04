from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth

from petsemergency.models import MyUser

# Create your views here.


def index(request):
    user = request.user if request.user.is_authenticated else None
    content = {
    }
    return render(request, 'petsemergency/WelcomePage.html', content)


def blog(request):
    user = request.user if request.user.is_authenticated else None
    content = {
    }
    return render(request, 'petsemergency/blog.html', content)


def news(request):
    user = request.user if request.user.is_authenticated else None
    content = {
    }
    return render(request, 'petsemergency/news.html', content)

