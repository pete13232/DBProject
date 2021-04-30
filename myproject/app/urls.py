from django.urls import path
from . import views


urlpatterns = [
    # path("", views.card3Col, name="card3Col"),
    path("", views.test, name="test"),
    path("resCard", views.resCard, name="resCard"),
    path("card3Col", views.card3Col, name="card3Col"),
    path("login", views.login, name="login"),
    
]
