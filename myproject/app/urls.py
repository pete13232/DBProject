from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("resCard", views.resCard, name="resCard"),
    path("card3Col", views.card3Col, name="card3Col"),
    path("categoryCard", views.categoryCard, name="categoryCard"),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
    path("review", views.review, name="review"),
]
