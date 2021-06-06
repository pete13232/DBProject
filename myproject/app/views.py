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

from app.forms import deleteStaffForm, changeProfileForm, editRoleForm
from restaurants.forms import (
    editMenuForm,
    createMenuForm,
    editCompanyForm,
    editRestaurantForm,
)
from users.forms import editMemberForm
from queueSystem.forms import createQueueForm, createNowQueueForm, createReviewForm

from django.db.models import Avg

import sweetify

# Create your views here.


def card3Col(request):
    return render(request, "card3Col.html")


def index(request):
    categorys = Category.objects.all()
    restaurants = Restaurant.objects.all()
    ratings = Review.objects.values("resID").annotate(average_rating=Avg("rating"))
    context = {"categorys": categorys, "restaurants": restaurants, "ratings": ratings}
    print(context)
    return render(request, "app/index.html", context)


def resCard(request, pk):
    restaurant = Restaurant.objects.get(resID=pk)
    reviews = Review.objects.filter(resID=pk)
    rating = reviews.aggregate(Avg("rating"))
    context = {"restaurant": restaurant, "reviews": reviews, "rating": rating}
    return render(request, "app/resCard.html", context)


def category(request):

    return render(request, "app/category.html")


def login(request):
    return render(request, "app/login.html")


def signup(request):
    return render(request, "app/signup.html")


def review(request):
    return render(request, "app/review.html")


@login_required(login_url="users/login")
def userprofile(request, pk):
    profile = Member.objects.get(memberID=pk)
    # queue = Queue.objects.get(memberID=profile)
    form = changeProfileForm()
    context = {"profile": profile, "form": form}
    return render(request, "app/userProfile.html", context)


@login_required(login_url="users/login")
@allowed_users(allowed_roles=["admin", "executive", "manager", "staff"])
def workerprofile(request):
    return render(request, "app/workerProfile.html")


# @login_required(login_url="users/login")
# @allowed_users(allowed_roles=["admin", "executive", "manager"])
# def managerprofile(request):
#     return render(request, "app/managerProfile.html")


@login_required(login_url="users/login")
@allowed_users(allowed_roles=["admin", "executive", "manager", "staff"])
def managerProfile(request, pk):
    restaurant = Restaurant.objects.get(resID=pk)
    context = {"restaurant": restaurant}
    return render(request, "app/managerProfile.html", context)


@login_required(login_url="users/login")
@allowed_users(allowed_roles=["admin", "manager", "staff"])
def queueManagement(request, pk):
    restaurant = Restaurant.objects.get(resID=pk)
    context = {"restaurant": restaurant}
    return render(request, "app/queueManagement.html", context)


@login_required(login_url="users/login")
@admin_only
def admin(request):
    return render(request, "app/admin.html")


@login_required(login_url="users/login")
@admin_only
def requestRegistration(request):
    return render(request, "app/requestRegistration.html")


@login_required(login_url="users/login")
@allowed_users(allowed_roles=["admin", "manager"])
def managerControl(request, pk):
    restaurant = Restaurant.objects.get(resID=pk)
    context = {"restaurant": restaurant}
    return render(request, "app/managerControl.html", context)


def profileDetail(request, pk):  # check ให้หน่อย
    profile = Member.objects.get(memberID=pk)
    queue = Queue.objects.get(memberID=pk)
    context = {"profile": profile, "queue": queue}
    return render(request, "app/profileDetail.html", context)


def executiveControl(request, pk):  # ยังไม่ได้เชื่อมผ่าน company
    restaurants = Restaurant.objects.filter(companyID=pk)
    context = {"restaurants": restaurants}
    return render(request, "app/executiveControl.html", context)





def editRole(request, pk):

    if request.method == "POST":
        instance = get_object_or_404(Member, memberID=request.POST["memberID"])
        form = editRoleForm(request.POST or None, instance=instance)
        print(instance)
        if form.is_valid():
            form.save()
            sweetify.success(
                request,
                icon="success",
                title="DONE !",
                text="Member  " + " was updated",
                timer=1500,
                timerProgressBar=True,
                allowOutsideClick=True,
            )
            return redirect("/staffList/" + pk)
        else:
            sweetify.error(
                request,
                icon="error",
                title="Oops !",
                text="Something went wrong! Try again",
                timer=2500,
                timerProgressBar=True,
                allowOutsideClick=True,
            )
            return redirect("/staffList/" + pk)


def deleteStaff(request, pk):
    if request.method == "POST":
        memberID = request.POST["memberID"]
        instance = get_object_or_404(Member, memberID=memberID)
        form = deleteStaffForm(request.POST or None, instance=instance)
        # name = request.POST["fullName"]
        if form.is_valid():
            form.save()
            sweetify.success(
                request,
                icon="success",
                title="Deleted!",
                text="Staff " + str(instance.fullName()) + " was Delete",
                timer=1500,
                timerProgressBar=True,
                allowOutsideClick=True,
            )
            return redirect("/staffList/" + pk)
        else:
            sweetify.error(
                request,
                icon="error",
                title="Oops !",
                text="Something went wrong! Try again",
                timer=2500,
                timerProgressBar=True,
                allowOutsideClick=True,
            )
            print(form)
            return redirect("/staffList/" + pk)
    else:
        form = deleteStaffForm()


def staffProfile(request, pk):
    restaurant = Restaurant.objects.get(resID=pk)
    context = {"restaurant": restaurant}
    return render(request, "app/staffProfile.html", context)


def executiveProfile(request, pk):
    restaurant = Restaurant.objects.get(resID=pk)
    context = {"restaurant": restaurant}
    return render(request, "app/executiveProfile.html", context)


def resProfile(request, pk):
    restaurant = Restaurant.objects.get(resID=pk)
    context = {"restaurant": restaurant}
    return render(request, "app/resProfile.html", context)


def companyProfile(request, pk):
    restaurant = Restaurant.objects.get(companyID=pk)
    context = {"restaurant": restaurant}
    return render(request, "app/companyProfile.html", context)


def dashboard(request):
    return render(request, "app/dashboard.html")