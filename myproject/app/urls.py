from django.urls import path
from . import views


urlpatterns = [
    # path("", views.card3Col, name="card3Col"),
    path("test", views.test, name="test"),
    path("resCard", views.resCard, name="resCard"),
]
