from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth

from petsemergency.models import *


# Create your views here.


def index(request):
    user = request.user if request.user.is_authenticated else None
    content = {
        'user': user,
    }
    return render(request, 'petsemergency/WelcomePage.html', content)


def blog(request):
    user = request.user if request.user.is_authenticated else None
    if request.method == 'POST':
        message = request.POST.get('con', '')
        title = request.POST.get('title', '')
        type = message[0:2]
        if type == "jl":
            new_mess = Message(user=user.username,
                               title=title,
                               type="交流",
                               content=message[2:])
        else:
            new_mess = Message(user=user.username,
                               title=title,
                               type="求助",
                               content=message[2:])
        new_mess.save()

    com = Message.objects.filter(type="交流")
    help = Message.objects.filter(type="求助")

    content = {
        'user': user,
        'com': com,
        'help': help
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
    state = None
    user = request.user if request.user.is_authenticated else None
    pet = Pets.objects.filter(owner=user.username)
    if pet.count() == 0:
        state = 'none'
    else:
        state = 'have'
    content = {
        'user': user,
        'state': state,
        'pet': pet
    }
    return render(request, 'petsemergency/myzone_mypets.html', content)


def myhelp(request):
    state = None
    user = request.user if request.user.is_authenticated else None
    help = Message.objects.filter(type="求助", user=user.username)
    if help.count() == 0:
        state = 'none'
    else:
        state = 'have'
    content = {
        'user': user,
        'state': state,
        'help': help
    }
    return render(request, 'petsemergency/myzone_myhelp.html', content)


def helpother(request):
    state = None
    user = request.user if request.user.is_authenticated else None
    help = Help.objects.filter(helper=user.username)
    if help.count() == 0:
        state = 'none'
    else:
        state = 'have'
    content = {
        'user': user,
        'state': state,
        'help': help
    }
    return render(request, 'petsemergency/myzone_helpother.html', content)


def mying(request):
    content = {
    }
    return render(request, 'petsemergency/myzone_mying.html', content)


def messagedetail(request):
    user = request.user if request.user.is_authenticated else None
    title = request.GET.get('title')
    con = Message.objects.filter(title=title)
    comment = request.POST.get('comment')
    helpcomment = request.POST.get('helpcomment')
    state = None
    if con.count() != 0 and user.username == con[0].user:
        state = 'isme'
    else:
        state = 'notme'
    if comment is not None:
        new_comm = Comment(user=user.username,
                           comment=comment,
                           title=title,
                           commentuser=con[0].user)
        new_comm.save()
    if con.count() != 0:
        all_comm = Comment.objects.filter(commentuser=con[0].user, title=title)
    if helpcomment is not None:
        if Wanttohelp.objects.filter(user=user.username, wantuser=user.username, title=title).count() != 0:
            state = 'help_again'
        new_want = Wanttohelp(
            user=user.username,
            wantuser=con[0].user,
            say=helpcomment,
            title=title
        )
        new_want.save()
    want_people = Wanttohelp.objects.filter(wantuser=user.username, title=title)
    content = {
        'user': user,
        'content': con[0],
        'all_comm': all_comm,
        'state': state,
        'want_people': want_people
    }
    return render(request, 'petsemergency/messagedetail.html', content)


def addpets(request):
    user = request.user if request.user.is_authenticated else None
    if request.method == 'POST':
        petname = request.POST.get('petname', '')
        type = request.POST.get('type', '')
        petcontent = request.POST.get('con', '')
        new_pet = Pets.objects.create(
            petname=petname,
            type=type,
            pcontent=petcontent,
            owner=user.username,
        )
        new_pet.save()

    content = {
        'active_menu': 'myzone_mypets',
        'user': user,
    }
    return render(request, 'petsemergency/myzone_addpets.html', content)
