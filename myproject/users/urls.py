from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="users_index"),
    path("signup", views.registerPage, name="users_signup"),
    path("login", views.loginPage, name="users_login"),
]
