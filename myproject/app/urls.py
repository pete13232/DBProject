from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("manageAdmin", views.admin, name="adminpage"),
    path("registerRequest", views.registerRequest, name="registerRequest"),
    path("dashboard", views.dashboard, name="dashboard"),
    path('chart', views.line_chart, name='line_chart'),
    path('chartJSON', views.line_chart_json, name='line_chart_json'),

]
