from django import forms
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.models import Group
from django.shortcuts import redirect, render, get_object_or_404

from users.models import Member

from django.shortcuts import render
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required
from restaurants.models import Category, Restaurant, Menu, Company
from users.decorators import unauthenticated_user, allowed_users, admin_only
from users.models import Member
from queueSystem.models import Queue, Review

from app.forms import deleteStaffForm, editRoleForm
from restaurants.forms import (
    editMenuForm,
    createMenuForm,
    editCompanyForm,
    editRestaurantForm,
)
from users.forms import editMemberForm
from queueSystem.forms import createQueueForm, createNowQueueForm, createReviewForm

from django.db.models import Avg
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView

import sweetify

# Create your views here.


def index(request):
    categorys = Category.objects.all()
    restaurants = Restaurant.objects.all()
    ratings = Review.objects.values("resID").annotate(average_rating=Avg("rating"))
    context = {"categorys": categorys, "restaurants": restaurants, "ratings": ratings}
    print(context)
    return render(request, "app/index.html", context)


@login_required(login_url="users/login")
@admin_only
def admin(request):
    return render(request, "admin/admin.html")


@login_required(login_url="users/login")
@admin_only
def registerRequest(request):
    return render(request, "admin/registerRequest.html")
    
@allowed_users(allowed_roles=["admin", "executive", "manager"])
@login_required(login_url="users/login")
def dashboard(request):
    return render(request, "admin/dashboard.html")





# class LineChartJSONView(BaseLineChartView):
#     def get_labels(self):
#         """Return 7 labels for the x-axis."""
#         return ["January", "February", "March", "April", "May", "June", "July"]

#     def get_providers(self):
#         """Return names of datasets."""
#         return ["Central", "Eastside", "Westside"]

#     def get_data(self):
#         """Return 3 datasets to plot."""
#         return [[75, 44, 92, 11, 44, 95, 35],
#                 [41, 92, 18, 3, 73, 87, 92],
#                 [87, 21, 94, 3, 90, 13, 65]]
        
# line_chart = TemplateView.as_view(template_name='app/line_chart.html')
# line_chart_json = LineChartJSONView.as_view()
