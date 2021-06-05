from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("resCard/<str:pk>", views.resCard, name="resCard"),
    path("card3Col", views.card3Col, name="card3Col"),
    # path("categoryCard", views.categoryCard, name="categoryCard"),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
    path("review", views.review, name="review"),
    path("queueManagement", views.queueManagement, name="queueManagement"),
    # path("foodList", views.foodList, name="foodList"),
    path("admin", views.admin, name="adminpage"),
    path("userprofile/<str:pk>", views.userprofile, name="userprofile"),
    path("requestRegistration", views.requestRegistration, name="requestRegistration"),
    path("menu/<str:pk>", views.menu, name="menu"),
    path("editMenu/<str:pk>", views.editMenu, name="editMenu"),
    path("category/<str:pk>", views.category, name="category"),
    path("managerControl/<str:pk>", views.managerControl, name="managerControl"),
    path("staffList/<str:pk>", views.staffList, name="staffList"),
    path("profileDetail/", views.profileDetail, name="profileDetail"),
    path("executiveControl/<str:pk>", views.executiveControl, name="executiveControl"),
    path("managerProfile/<str:pk>", views.managerProfile, name="managerProfile"),
    path("executiveProfile/<str:pk>", views.executiveProfile, name="executiveProfile"),
    path("resProfile/<str:pk>", views.resProfile, name="resProfile"),
    path("staffProfile/<str:pk>", views.staffProfile, name="staffProfile"),
    path("companyProfile/<str:pk>", views.companyProfile, name="companyProfile"),

]
