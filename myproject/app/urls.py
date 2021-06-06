from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("admin", views.admin, name="adminpage"),
    path("registerRequest", views.registerRequest, name="registerRequest"),
    path("dashboard", views.dashboard, name="dashboard"),
]
