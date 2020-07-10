from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=5)
    lastname = models.CharField(max_length=5)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    email = models.EmailField(default="xxx@email.com")
    personality = models.TextField(max_length=200, default="这个人很懒哦，什么都没写ฅ(๑ ̀ㅅ ́๑)ฅ")

    def __str__(self):
        return self.user.username


class Message(models.Model):
    user = models.CharField(max_length=20)
    title = models.CharField(max_length=50, default="我是题目")
    type = models.CharField(max_length=10, default=None)
    date = models.DateTimeField(default=datetime.now)
    content = models.TextField(max_length=1000)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.CharField(max_length=20)
    commentuser = models.CharField(max_length=20)
    title = models.CharField(max_length=100, default="")
    comment = models.TextField(max_length=150)
    date = models.DateTimeField(default=datetime.now)


class Wanttohelp(models.Model):
    user = models.CharField(max_length=20)
    wantuser = models.CharField(max_length=20)
    say = models.CharField(max_length=100, default="")
    title = models.CharField(max_length=100, default="")


class Help(models.Model):
    user = models.CharField(max_length=20)
    helper = models.CharField(max_length=20)
    date = models.DateTimeField(default=datetime.now)


class Pets(models.Model):
    petid = models.IntegerField(auto_created=True, default=1, primary_key=True)
    petname = models.CharField(max_length=20)
    pcontent = models.TextField(max_length=1000)
    owner = models.CharField(max_length=20)
    type = models.CharField(max_length=20, default="小可爱")
