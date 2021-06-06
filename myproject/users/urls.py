from django.urls import path
from . import views


urlpatterns = [
    path("signup", views.signup, name="users_signup"),
    path("login", views.loginPage, name="users_login"),
    path("logout", views.logoutPage, name="users_logout"),
    path("profile/<str:pk>", views.profile, name="profile"),
]
