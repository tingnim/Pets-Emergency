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
        'user': user,
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
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('blog'))
    state = None
    if request.method == 'POST':
        password = request.POST.get('password', '')
        repeat_password = request.POST.get('repassword', '')
        if password == '' or repeat_password == '':
            state = 'Empty'
        elif password != repeat_password:
            state = 'Repeat_error'
        else:
            username = request.POST.get('username', '')
            print(username)
            if User.objects.filter(username=username):
                state = 'User_existed'
                print(state)
            else:
                new_user = User.objects.create_user(username=username,
                                                    password=password)
                new_user.save()
                new_myuser = MyUser(user=new_user,
                                    password=password,
                                    username=username,
                                    email=request.POST.get('email', ''),
                                    firstname=request.POST.get('firstName'),
                                    lastname=request.POST.get('lastName'),
                                    city=request.POST.get('city'))
                new_myuser.save()
                return HttpResponseRedirect(reverse('signin'))
    content = {
        'active_menu': 'signin',
        'state': state,
        'user': None,
    }
    return render(request, 'petsemergency/signup.html', content)


def signin(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('blog'))
    state = None
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('blog'))
        else:
            state = 'not_exist_or_password_error'
    content = {
        'active_menu': 'blog',
        'state': state,
        'user': None,
    }
    return render(request, 'petsemergency/signin.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('blog'))


def myzone(request):
    content = {
    }
    return render(request, 'petsemergency/myzone.html', content)


def aboutme(request):
    user = request.user if request.user.is_authenticated else None
    content = {
        'user': user
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
