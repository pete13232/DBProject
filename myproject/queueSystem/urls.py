from django.urls import path
from . import views


urlpatterns = [
    path("createQueue/<str:pk>", views.createQueue, name="createQueue"),
    path("createNowQueue/<str:pk>", views.createNowQueue, name="createNowQueue"),
    path("createReview/<str:pk>", views.createReview, name="createReview"),
]
