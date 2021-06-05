from django import forms
from django.contrib import messages
from django.contrib.auth.models import Group
from django.shortcuts import redirect, render, get_object_or_404

from users.models import Member

from django.shortcuts import render
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required
from restaurants.models import Category, Restaurant, Menu
from users.decorators import unauthenticated_user, allowed_users, admin_only
from users.models import Member
from queueSystem.models import Queue

from .forms import deleteStaffForm, changeProfileForm, editRoleForm
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
def userprofile(request, pk):
    profile = Member.objects.get(id=pk)
    # queue = Queue.objects.get(memberID=profile)
    form = changeProfileForm()
    context = {"profile": profile, "form": form}
    return render(request, "app/userProfile.html", context)


def changeProfile(request, pk):
    restaurant = Restaurant.objects.get(resID=pk)
    menus = Menu.objects.filter(resID=restaurant)
    if request.method == "POST":
        instance = get_object_or_404(Member, id=request.POST["id"])
        form = changeProfileForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            sweetify.success(
                request,
                icon="success",
                title="DONE !",
                text="Profile changed",
                timer=1500,
                timerProgressBar=True,
                allowOutsideClick=True,
            )
            return redirect("/userprofile/" + pk)
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
            return redirect("/userprofile/" + pk)
    else:
        form = changeProfileForm()


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


@login_required(login_url="users/login")
@admin_only
def admin(request):
    return render(request, "app/admin.html")


@login_required(login_url="users/login")
@admin_only
def requestRegistration(request):
    return render(request, "app/requestRegistration.html")


@login_required(login_url="users/login")
@allowed_users(allowed_roles=["admin", "manager", "staff", "member"])
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
    restaurants = Restaurant.objects.filter(companyID=pk)
    context = {"restaurants": restaurants}
    return render(request, "app/executiveControl.html", context)


@login_required(login_url="users/login")
@allowed_users(allowed_roles=["admin", "executive", "manager"])
def staffList(request, pk):

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
    }
    return render(request, "app/staffList.html", context)


def editRole(request, pk):
    if request.method == "POST":
        instance = get_object_or_404(Member, groups=request.POST["groups"])
        member = Member.objects.update()
        form = editRoleForm(request.POST or None, instance=instance)
        # name = request.POST["fullName"]
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
            print(form)
            return redirect("/staffList/" + pk)
    else:
        form = editRoleForm()


def deleteStaff(request, pk):
    if request.method == "POST":
        id = request.POST["id"]
        instance = get_object_or_404(Member, id=id)
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


def resProfile(request):

    return render(request, "app/resProfile.html")


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
    restaurant = Restaurant.objects.get(resID=pk)
    context = {"restaurant": restaurant}
    return render(request, "app/companyProfile.html", context)
