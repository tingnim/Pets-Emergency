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
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
