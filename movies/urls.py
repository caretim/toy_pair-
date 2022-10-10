from django.contrib import admin
from django.urls import path, include
from . import views


app_name = "movies"
urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("delete/<int:pk>", views.delete, name="delete"),
    path("search/", views.search, name="search"),
]
