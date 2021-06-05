from django import forms
from django.contrib import messages
from django.contrib.auth.models import Group
from django.shortcuts import redirect, render, get_object_or_404

from users.models import Member

from django.shortcuts import render
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from restaurants.models import Category, Restaurant, Menu
from users.decorators import unauthenticated_user, allowed_users, admin_only
from users.models import Member
from queueSystem.models import Queue

from restaurants.forms import editMenuForm, createMenuForm
from queueSystem.forms import createQueueForm

import sweetify

# Create your views here.


def card3Col(request):
    return render(request, "card3Col.html")


def index(request):
    categorys = Category.objects.all()
    restaurants = Restaurant.objects.all()
    context = {"categorys": categorys, "restaurants": restaurants}
    return render(request, "app/index.html", context)


def resCard(request, pk):
    restaurant = Restaurant.objects.get(resID=pk)
    form = createQueueForm()
    context = {"restaurant": restaurant, "form": form}
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
@allowed_users(allowed_roles=["admin", "member"])
def userprofile(request, pk):
    profile = Member.objects.get(id=pk)
    queue = Queue.objects.get(memberID=pk)
    context = {"profile": profile, "queue": queue}
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
@allowed_users(allowed_roles=["admin", "executive", "manager"])
def managerProfile(request, pk):
    restaurant = Restaurant.objects.get(resID=pk)
    context = {"restaurant": restaurant}
    return render(request, "app/managerProfile.html", context)


@login_required(login_url="users/login")
@allowed_users(allowed_roles=["admin", "manager", "staff"])
def queueManagement(request):

    return render(request, "app/queueManagement.html")


# def foodList(request):

#     return render(request, "app/foodList.html")


@login_required(login_url="users/login")
@allowed_users(allowed_roles=["admin"])
def admin(request):
    return render(request, "app/admin.html")


@login_required(login_url="users/login")
@allowed_users(allowed_roles=["admin"])
def requestRegistration(request):
    return render(request, "app/requestRegistration.html")


@login_required(login_url="users/login")
@allowed_users(allowed_roles=["admin", "member"])
def menu(request, pk):
    restaurant = Restaurant.objects.get(resID=pk)
    menus = Menu.objects.filter(resID=restaurant)
    edit = editMenuForm()
    create = createMenuForm()
    context = {"menus": menus, "restaurant": restaurant, "edit": edit, "create": create}
    return render(request, "app/menu.html", context)


@login_required(login_url="users/login")
@allowed_users(allowed_roles=["admin", "manager"])
def managerControl(request, pk):
    restaurant = Restaurant.objects.get(resID=pk)
    context = {"restaurant": restaurant}
    return render(request, "app/managerControl.html", context)


@login_required(login_url="users/login")
@allowed_users(allowed_roles=["admin", "manager", "staff"])
def editMenu(request, pk):
    restaurant = Restaurant.objects.get(resID=pk)
    menus = Menu.objects.filter(resID=restaurant)
    if request.method == "POST":
        instance = get_object_or_404(Menu, menuID=request.POST["menuID"])
        form = editMenuForm(request.POST or None, instance=instance)
        menu = request.POST["menuName"]
        if form.is_valid():
            form.save()
            sweetify.success(
                request,
                icon="success",
                title="DONE !",
                text="Menu " + menu + " was updated",
                timer=1500,
                timerProgressBar=True,
                allowOutsideClick=True,
            )
            return redirect("/menu/" + pk)
        else:
            sweetify.success(
                request,
                icon="error",
                title="Oops !",
                text="Something went wrong! Try again",
                timer=2500,
                timerProgressBar=True,
                allowOutsideClick=True,
            )
            return redirect("/menu/" + pk)
    else:
        form = editMenuForm()


@login_required(login_url="users/login")
@allowed_users(allowed_roles=["admin", "executive", "manager"])
def createMenu(request, pk):
    restaurant = Restaurant.objects.get(resID=pk)
    menus = Menu.objects.filter(resID=restaurant)
    if request.method == "POST":
        instance = get_object_or_404(Menu, menuID=request.POST["menuID"])
        form = createMenuForm(request.POST or None, instance=instance)
        menu = request.POST["menuName"]
        if form.is_valid():
            form.save()
            sweetify.success(
                request,
                icon="success",
                title="DONE !",
                text="Menu " + menu + " was updated",
                timer=1500,
                timerProgressBar=True,
                allowOutsideClick=True,
            )
            return redirect("/foodList/" + pk)
        else:
            sweetify.success(
                request,
                icon="error",
                title="Oops !",
                text="Something went wrong! Try again",
                timer=2500,
                timerProgressBar=True,
                allowOutsideClick=True,
            )
            return redirect("/foodList/" + pk)
    else:
        form = createMenuForm()


def profileDetail(request, pk):  # check ให้หน่อย
    profile = Member.objects.get(id=pk)
    queue = Queue.objects.get(memberID=pk)
    context = {"profile": profile, "queue": queue}
    return render(request, "app/profileDetail.html", context)


def executiveControl(request, pk):  # ยังไม่ได้เชื่อมผ่าน company
    restaurant = Restaurant.objects.get(resID=pk)
    context = {"restaurant": restaurant}
    return render(request, "app/executiveControl.html", context)


@login_required(login_url="users/login")
@allowed_users(allowed_roles=["admin", "executive", "manager"])
def staffList(request, pk):
    restaurant = Restaurant.objects.get(resID=pk)
    staff = Member.objects.get(resID=restaurant)
    context = {"restaurant": restaurant, "staff": staff}
    return render(request, "app/staffList.html", context)



def staffProfile(request,pk):
    restaurant = Restaurant.objects.get(resID=pk)
    context = {"restaurant": restaurant}
    return render(request, "app/staffProfile.html", context)

def executiveProfile(request,pk):
    restaurant = Restaurant.objects.get(resID=pk)
    context = {"restaurant": restaurant}
    return render(request, "app/executiveProfile.html",context)

def resProfile(request,pk):
    restaurant = Restaurant.objects.get(resID=pk)
    context = {"restaurant": restaurant}
    return render(request, "app/resProfile.html", context)

def companyProfile(request,pk):
    restaurant = Restaurant.objects.get(resID=pk)
    context = {"restaurant": restaurant}
    return render(request, "app/companyProfile.html", context)

