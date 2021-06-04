from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("createMenu/<str:pk>", views.createMenu, name="createMenu"),
    path("deleteMenu/<str:pk>", views.deleteMenu, name="deleteMenu"),
]
