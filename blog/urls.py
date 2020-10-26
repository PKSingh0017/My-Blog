from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),            # Empty path means the home page
    path('about/', views.about, name='blog-about'),
]
