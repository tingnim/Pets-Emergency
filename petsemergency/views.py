from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth

from petsemergency.models import MyUser

# Create your views here.


def index(request):
    content = {
    }
    return render(request, 'petsemergency/WelcomePage.html', content)


def blog(request):
    content = {
    }
    return render(request, 'petsemergency/blog.html', content)


def news(request):
    content = {
    }
    return render(request, 'petsemergency/news.html', content)


def signup(request):
    content = {
    }
    return render(request, 'petsemergency/signup.html', content)


def signin(request):
    content = {
    }
    return render(request, 'petsemergency/signin.html', content)


def myzone(request):
    content = {
    }
    return render(request, 'petsemergency/myzone.html', content)


def aboutme(request):
    content = {
    }
    return render(request, 'petsemergency/myzone_aboutme.html', content)


def mypets(request):
    content = {
    }
    return render(request, 'petsemergency/myzone_mypets.html', content)


def myhelp(request):
    content = {
    }
    return render(request, 'petsemergency/myzone_myhelp.html', content)


def helpother(request):
    content = {
    }
    return render(request, 'petsemergency/myzone_helpother.html', content)


def mying(request):
    content = {
    }
    return render(request, 'petsemergency/myzone_mying.html', content)
