from django.contrib import admin 
from django.urls import path
from home import views

urlpatterns = [
    path('index',views.index,name = 'index'),
    path('about',views.about,name = 'about'),
    path('contact',views.contact,name = 'contact'),
    path('menu',views.menu,name = 'menu'),
]