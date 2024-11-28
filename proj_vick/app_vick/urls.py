from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('reach', views.reach, name='reach'),
    path('front', views.front, name='front'),
    path('about', views.about, name='about'),
    path('home', views.home, name='home'),
    path('add', views.add, name='add'),   
]