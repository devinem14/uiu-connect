from django.contrib import admin
from django.urls import include, path
from register import views as v
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("view/", views.view, name="view"),
    path("<int:id>", views.index, name="index"),
    path('', include("django.contrib.auth.urls")),
]