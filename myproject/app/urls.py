from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("resCard/<str:pk>", views.resCard, name="resCard"),
    path("card3Col", views.card3Col, name="card3Col"),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
    path("review", views.review, name="review"),
    path("queueManagement/<str:pk>", views.queueManagement, name="queueManagement"),
    path("admin", views.admin, name="adminpage"),
    path("userprofile/<str:pk>", views.userprofile, name="userprofile"),
    path("changeProfile/<str:pk>", views.changeProfile, name="changeProfile"),
    path("requestRegistration", views.requestRegistration, name="requestRegistration"),
    path("menu/<str:pk>", views.menu, name="menu"),
    path("editMenu/<str:pk>", views.editMenu, name="editMenu"),
    path("category/<str:pk>", views.category, name="category"),
    path("managerControl/<str:pk>", views.managerControl, name="managerControl"),
    path("profileDetail/", views.profileDetail, name="profileDetail"),
    path("executiveControl/<str:pk>", views.executiveControl, name="executiveControl"),
    path("editRole/<str:pk>", views.editRole, name="editRole"),
    path("deleteStaff/<str:pk>", views.deleteStaff, name="deleteStaff"),
    path("dashboard", views.dashboard, name="dashboard"),
]
