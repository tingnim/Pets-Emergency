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
    comment = models.ForeignKey('Message', on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now)


class ChatRecord(models.Model):
    curruser = models.CharField(max_length=20)
    other = models.CharField(max_length=20)
    date = models.DateTimeField(default=datetime.now)
    summary = models.TextField(max_length=2000)


class Pets(models.Model):
    petname = models.CharField(max_length=20)
    petid = models.CharField(max_length=20, unique=True, primary_key=True)
    owner = models.CharField(max_length=20)
    date = models.DateTimeField(default=datetime.now)
    type = models.CharField(max_length=20, default="小可爱")


class Help(models.Model):
    user = models.CharField(max_length=20)
    helper = models.CharField(max_length=20)
    date = models.DateTimeField(default=datetime.now)
