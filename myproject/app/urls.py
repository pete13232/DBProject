from django.urls import path
from . import views


urlpatterns = [
    # path("", views.card3Col, name="card3Col"),
    path("", views.test, name="test"),
    path("/queue", views.queueCard, name="queueCard"),
]
