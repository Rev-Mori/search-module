from django.urls import path
from django.contrib import admin

from . import views


urlpatterns = [
    path('search', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),

]
