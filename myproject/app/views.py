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

from .forms import createQueueForm
from restaurants.forms import editMenuForm, createMenuForm

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

    if request.method == "POST":
        form = createQueueForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Success")
            redirect("resCard/" + pk)
        else:
            messages.info(request, form.errors)
            redirect("resCard/" + pk)
    else:
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

@login_required(login_url='login')
def userprofile(request, pk):
    profile = Member.objects.get(id=pk)
    queue = Queue.objects.get(memberID=pk)
    context = {"profile": profile, "queue": queue}
    return render(request, "app/userProfile.html", context)

@login_required(login_url='login')
def workerprofile(request):
    return render(request, "app/workerProfile.html")

def managerprofile(request):
    return render(request, "app/managerProfile.html")

@login_required(login_url='login')
def queueManagement(request):

    return render(request, "app/queueManagement.html")


# def foodList(request):

#     return render(request, "app/foodList.html")


def admin(request):
    return render(request, "app/admin.html")


def requestRegistration(request):
    return render(request, "app/requestRegistration.html")


def menu(request, pk):
    restaurant = Restaurant.objects.get(resID=pk)
    menus = Menu.objects.filter(resID=restaurant)
    edit = editMenuForm()
    create = createMenuForm()
    context = {"menus": menus, "restaurant": restaurant, "edit": edit, "create": create}
    return render(request, "app/menu.html", context)


def managerControl(request, pk):
    restaurant = Restaurant.objects.get(resID=pk)
    context = {"restaurant": restaurant}
    return render(request, "app/managerControl.html", context)


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


def staffList(request):
    return render(request, "app/staffList.html")
