from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    image = models.URLField(
        default='https://pic3.zhimg.com/80/v2-acd060b9f86eb0b988c8d1d6b242fd3d_1440w.jpg')
    personality = models.TextField(max_length=200, default="这个人很懒哦，什么都没写ฅ(๑ ̀ㅅ ́๑)ฅ")

    def __str__(self):
        return self.user.username


class Message(models.Model):
    user = models.ForeignKey('MyUser', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=10, default=None)
    date = models.DateTimeField(default=datetime.now)
    content = models.TextField(max_length=2000)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey('MyUser', on_delete=models.CASCADE, related_name='Comment_user')
    commentuser = models.ForeignKey('MyUser', on_delete=models.CASCADE, related_name='Comment_commentuser')
    comment = models.ForeignKey('Message', on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now)


class ChatRecord(models.Model):
    curruser = models.ForeignKey('MyUser', on_delete=models.CASCADE, related_name='Char_curr')
    other = models.ForeignKey('MyUser', on_delete=models.CASCADE, related_name='Chat_other')
    date = models.DateTimeField(default=datetime.now)
    summary = models.TextField(max_length=2000)


class Pets(models.Model):
    petname = models.CharField(max_length=20)
    petid = models.CharField(max_length=20, unique=True, primary_key=True)
    owner = models.ForeignKey('MyUser', on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now)
    type = models.CharField(max_length=20, default="小可爱")


class Help(models.Model):
    user = models.ForeignKey('MyUser', on_delete=models.CASCADE, related_name='Help_user')
    helper = models.ForeignKey('MyUser', on_delete=models.CASCADE, related_name='Help_helper')
    date = models.DateTimeField(default=datetime.now)
