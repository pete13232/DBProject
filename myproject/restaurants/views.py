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
    createCompForm,
    createResForm,
    editMenuForm,
    createMenuForm,
    changeStatusForm,
<<<<<<< HEAD
    enableCompanyForm,
    enableRestaurantForm,
=======
    inviteStaffForm,
>>>>>>> c4f2fa53e911d49b3b78db07e8a5dc323da32663
)
from users.forms import editMemberForm
from queueSystem.forms import createQueueForm, createNowQueueForm, createReviewForm

from django.db.models import Avg


import sweetify

# Create your views here.
def indexResCard(request):
    return render(request, "restaurants/indexResCard.html")


def resCard(request, pk):
    restaurant = Restaurant.objects.get(resID=pk)
    reviews = Review.objects.filter(resID=pk)
    rating = reviews.aggregate(Avg("rating"))
    context = {"restaurant": restaurant, "reviews": reviews, "rating": rating}
    return render(request, "restaurants/resCard.html", context)


@login_required(login_url="users/login")
@allowed_users(allowed_roles=["admin", "manager", "staff", "member", "executive"])
def menu(request, pk):
    if request.method == "POST":
        instance = get_object_or_404(Menu, menuID=request.POST["menuID"])
        form = changeStatusForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            sweetify.success(
                request,
                icon="success",
                title="DONE !",
                text="Menu was updated",
                timer=1500,
                timerProgressBar=True,
                allowOutsideClick=True,
            )
            return redirect("/res/menu/" + pk)
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
            return redirect("/res/menu/" + pk)
    else:
        restaurant = Restaurant.objects.get(resID=pk)
        menus = Menu.objects.filter(resID=restaurant)
        edit = editMenuForm()
        create = createMenuForm()
    context = {"menus": menus, "restaurant": restaurant, "edit": edit, "create": create}
    return render(request, "restaurants/menu.html", context)


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
            return redirect("/res/menu/" + pk)
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
            return redirect("/res/menu/" + pk)
    else:
        form = createMenuForm()


@login_required(login_url="users/login")
@allowed_users(allowed_roles=["admin", "manager", "staff", "member", "executive"])
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
            return redirect("/res/menu/" + pk)
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
            return redirect("/res/menu/" + pk)
    else:
        form = editMenuForm()


@login_required(login_url="users/login")
@allowed_users(allowed_roles=["admin", "manager"])
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
        return redirect("/res/menu/" + str(menu.resID))


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
    return render(request, "restaurants/manageStaff.html", context)


@login_required(login_url="users/login")
@allowed_users(allowed_roles=["admin", "executive", "manager"])
def inviteStaff(request, pk):

    if request.method == "POST":
        email = request.POST["email"]
        instance = get_object_or_404(Member, email=email)
        name = Member.objects.get(email=email)
        form = inviteStaffForm(request.POST or None, instance=instance)
        print(instance)
        if form.is_valid():
            form.save()
            sweetify.success(
                request,
                icon="success",
                title="DONE !",
                text="Member  " + name.fullName() + " was invited",
                timer=1500,
                timerProgressBar=True,
                allowOutsideClick=True,
            )
            return redirect("/res/manageStaff/" + pk)
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
            print(print(request.POST["resID"]))
            return redirect("/res/manageStaff/" + pk)


@login_required(login_url="users/login")
@allowed_users(allowed_roles=["admin", "manager"])
def managerHome(request, pk):
    restaurant = Restaurant.objects.get(resID=pk)
    queues = Queue.objects.all()
    context = {
        "restaurant": restaurant,
        "queues": queues,
    }
    return render(request, "restaurants/managerHome.html", context)


@login_required(login_url="users/login")
@allowed_users(allowed_roles=["admin", "executive"])
def executiveHome(request, pk):  # ยังไม่ได้เชื่อมผ่าน company
    restaurants = Restaurant.objects.filter(companyID=pk)
    context = {"restaurants": restaurants}
    return render(request, "restaurants/executiveHome.html", context)


@login_required(login_url="users/login")
@allowed_users(allowed_roles=["admin", "executive", "manager"])
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
            return redirect("/res/manageStaff/" + pk)
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
            return redirect("/res/manageStaff/" + pk)


@login_required(login_url="users/login")
@allowed_users(allowed_roles=["admin", "executive", "manager"])
def removeStaff(request, pk):
    if request.method == "POST":
        memberID = request.POST["memberID"]
        instance = get_object_or_404(Member, memberID=memberID)
        form = deleteStaffForm(request.POST or None, instance=instance)
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
            return redirect("/res/manageStaff/" + pk)
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
            return redirect("/res/manageStaff/" + pk)
    else:
        form = deleteStaffForm()


def staffHome(request, pk):
    restaurant = Restaurant.objects.get(resID=pk)
    queues = Queue.objects.all()
    context = {
        "restaurant": restaurant,
        "queues": queues,
    }
    return render(request, "restaurants/staffHome.html", context)


def createRes(request):

    if request.method == "POST":
        form = createResForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            res = request.POST["resName"]
            sweetify.success(
                request,
                icon="success",
                title="DONE!",
                text="Restaurant " + res + " was created, Please wait for accepting",
                timer=3000,
                timerProgressBar=True,
                allowOutsideClick=True,
            )
            return redirect("/")
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
            print(form.errors)
            return redirect("/")
    else:
        form = createResForm()

def enableComAndRes(request, pk):
    if pk[0] == "C":
        if request.method == "POST":
            instance = get_object_or_404(Company, companyID=pk)
            form = enableCompanyForm(request.POST or None, instance=instance)
            next = request.POST.get('next')
            if form.is_valid():
                form.save()
                sweetify.success(
                    request,
                    icon="success",
                    title="DONE !",
                    text="Company status is update" ,
                    timer=1000,
                    timerProgressBar=True,
                    allowOutsideClick=True,
                )
                return redirect(next)
            else:
                sweetify.error(
                    request,
                    icon="error",
                    title="Oops !",
                    text="Somethings went wrong! Try again.",
                    timer=2500,
                    timerProgressBar=True,
                    allowOutsideClick=True,
                )
                return redirect(next)
    if pk[0] == "R":
        if request.method == "POST":
            instance = get_object_or_404(Restaurant, resID=pk)
            form = enableRestaurantForm(request.POST or None, instance=instance)
            next = request.POST.get('next')
            if form.is_valid():
                form.save()
                sweetify.success(
                    request,
                    icon="success",
                    title="DONE !",
                    text="Company status is update" ,
                    timer=1000,
                    timerProgressBar=True,
                    allowOutsideClick=True,
                )
                return redirect(next)
            else:
                sweetify.error(
                    request,
                    icon="error",
                    title="Oops !",
                    text="Somethings went wrong! Try again.",
                    timer=2500,
                    timerProgressBar=True,
                    allowOutsideClick=True,
                )
                return redirect(next)

def createComp(request):
    if request.method == "POST":
        form = createCompForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            comp = request.POST["companyName"]
            sweetify.success(
                request,
                icon="success",
                title="DONE!",
                text="Company " + comp + " was created, Please wait for accepting",
                timer=3000,
                timerProgressBar=True,
                allowOutsideClick=True,
            )
            return redirect("/")
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
            print(form.errors)
            return redirect("/")
    else:
        form = createCompForm()
