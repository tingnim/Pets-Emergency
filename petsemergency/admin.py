from django.contrib import admin
from petsemergency.models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.


class MyUserInline(admin.TabularInline):
    model = MyUser
    can_delete = False


class UserAdmin(BaseUserAdmin):
    inlines = (MyUserInline,)


class Message_admin(admin.ModelAdmin):
    list_display = ('title', 'date', 'user', 'type')
    list_per_page = 20
    ordering = ('date',)
    list_filter = ('user', 'type',)
    search_fields = ('title', 'user',)


class Comment_admin(admin.ModelAdmin):
    list_display = ('user', 'commentuser', 'date')
    list_per_page = 20
    ordering = ('date',)
    list_filter = ('user', 'commentuser',)


class ChatRecord_admin(admin.ModelAdmin):
    list_display = ('curruser', 'other', 'date')
    list_per_page = 20
    ordering = ('date',)
    list_filter = ('curruser', 'other',)


class Pets_admin(admin.ModelAdmin):
    list_display = ('petid', 'petname', 'type', 'owner', 'date')
    list_per_page = 20
    ordering = ('date',)
    list_filter = ('owner', 'type')


class Help_admin(admin.ModelAdmin):
    list_display = ('user', 'helper', 'date')
    list_per_page = 20
    ordering = ('date',)
    list_filter = ('user', 'helper')


admin.site.site_header = 'Pets Emergency'
admin.site.site_title = 'Pets Emergency'

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Message, Message_admin)
admin.site.register(Comment, Comment_admin)
admin.site.register(MyUser)
admin.site.register(ChatRecord, ChatRecord_admin)
admin.site.register(Pets, Pets_admin)
admin.site.register(Help, Help_admin)