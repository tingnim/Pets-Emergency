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
    list_display = ('date', 'user', 'type')
    list_per_page = 20
    ordering = ('date',)
    list_filter = ('user', 'type',)
    search_fields = ('user',)


class Comment_admin(admin.ModelAdmin):
    list_display = ('user', 'commentuser', 'date')
    list_per_page = 20
    ordering = ('date',)
    list_filter = ('user', 'commentuser',)

class MyPets_admin(admin.ModelAdmin):
    list_display = ('petname', 'type', 'owner')
    list_per_page = 20
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
admin.site.register(Pets, MyPets_admin)
admin.site.register(Help, Help_admin)