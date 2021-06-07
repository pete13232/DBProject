from django.urls import path
from . import views


urlpatterns = [
    path("createMenu/<str:pk>", views.createMenu, name="createMenu"),
    path("deleteMenu/<str:pk>", views.deleteMenu, name="deleteMenu"),
    path("manageStaff/<str:pk>", views.manageStaff, name="manageStaff"),
    path("menu/<str:pk>", views.menu, name="menu"),
    path("editMenu/<str:pk>", views.editMenu, name="editMenu"),
    path("managerHome/<str:pk>", views.managerHome, name="managerHome"),
    path("executiveHome/<str:pk>", views.executiveHome, name="executiveHome"),
    path("editRole/<str:pk>", views.editRole, name="editRole"),
    path("removeStaff/<str:pk>", views.removeStaff, name="removeStaff"),
    path("resCard/<str:pk>", views.resCard, name="resCard"),
    path("indexResCard", views.indexResCard, name="indexResCard"),
    path("staffHome/<str:pk>", views.staffHome, name="staffHome"),
    path("createRes", views.createRes, name="createRes"),
    path("enableComAndRes/<str:pk>", views.enableComAndRes ,name = "enableComAndRes"),
]
