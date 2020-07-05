from django.urls import path
from . import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='WelcomePage'),
    path('blog/', views.blog, name='blog'),
    path('news/', views.news, name='news'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('myzone/', views.myzone, name='myzone'),
    path('myzone/aboutme', views.aboutme, name='myzone_aboutme'),
    path('myzone/mypets', views.mypets, name='myzone_mypets'),
    path('myzone/myhelp', views.myhelp, name='myzone_myhelp'),
    path('myzone/helpother', views.myhelp, name='myzone_helpother'),
    path('myzone/mying', views.mying, name='myzone_mying'),
    path('logout/', views.logout, name='logout'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
