from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('<int:id>/Video', views.Video, name='Video'),
    path('VideoList', views.ListAllVideos, name="VideoList"),
    path('login', views.loginPage, name="LoginPage")
]
