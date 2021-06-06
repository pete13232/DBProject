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
def index(request):

    return render(request, "restaurants/resIndex.html")


@login_required(login_url="users/login")
@allowed_users(allowed_roles=["admin", "manager", "staff", "member", "executive"])
def menu(request, pk):
    restaurant = Restaurant.objects.get(resID=pk)
    menus = Menu.objects.filter(resID=restaurant)
    edit = editMenuForm()
    create = createMenuForm()
    context = {"menus": menus, "restaurant": restaurant, "edit": edit, "create": create}
    return render(request, "app/menu.html", context)


@login_required(login_url="users/login")
@allowed_users(allowed_roles=["admin", "executive", "manager"])
def createMenu(request, pk):
    restaurant = Restaurant.objects.get(resID=pk)
    menus = Menu.objects.filter(resID=restaurant)
    if request.method == "POST":
        form = createMenuForm(request.POST or None, request.FILES)
        menu = request.POST["menuName"]
        if form.is_valid():
            form.save()
            sweetify.success(
                request,
                icon="success",
                title="DONE !",
                text="Menu " + menu + " was created",
                timer=1500,
                timerProgressBar=True,
                allowOutsideClick=True,
            )
            return redirect("/menu/" + pk)
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
            return redirect("/menu/" + pk)
    else:
        form = createMenuForm()


@login_required(login_url="users/login")
@allowed_users(allowed_roles=["admin", "manager", "staff", "member"])
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
            sweetify.error(
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


def deleteMenu(request, pk):
    menu = Menu.objects.get(menuID=pk)
    if request.method == "POST":
        menu.delete()
        sweetify.success(
            request,
            icon="success",
            title="Deleted!",
            text="Menu " + menu.menuName + " was Delete",
            timer=1500,
            timerProgressBar=True,
            allowOutsideClick=True,
        )
        return redirect("/menu/" + str(menu.resID))


@login_required(login_url="users/login")
@allowed_users(allowed_roles=["admin", "executive", "manager"])
def manageStaff(request, pk):

    if pk[0] == "C":
        restaurant = Restaurant.objects.filter(companyID=pk)
        print(restaurant)
        staffs = Member.objects.filter(resID__in=restaurant)
    elif pk[0] == "R":
        restaurant = Restaurant.objects.filter(resID=pk)
        print(restaurant)
        staffs = Member.objects.filter(resID__in=restaurant)

    form = editRoleForm()
    # instance = get_object_or_404(Member, groups=request.POST["groups"])
    context = {
        "staffs": staffs,
        "form": form,
        "pk": pk,
        "restaurant": restaurant,
    }
    return render(request, "restaurant/manageStaff.html", context)