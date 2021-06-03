from django import forms
from django.contrib import messages
from django.contrib.auth.models import Group
from django.shortcuts import redirect, render
from users.models import Member

from users.decorators import unauthenticated_user, allowed_users, admin_only
from users.models import Member
from restaurants.models import Category, Restaurant, Menu
from queueSystem.models import Queue

from .forms import createQueueForm
from restaurants.forms import editMenuForm

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


def userprofile(request, pk):
    profile = Member.objects.get(memberID=pk)
    queue = Queue.objects.get(memberID=pk)
    context = {"profile": profile, "queue": queue}
    return render(request, "app/userProfile.html", context)


def workerprofile(request):
    return render(request, "app/workerProfile.html")


def queueManagement(request):

    return render(request, "app/queueManagement.html")


# def foodList(request):

#     return render(request, "app/foodList.html")


def admin(request):
    return render(request, "app/admin.html")


def usermanage(request):
    return render(request, "app/requestRegistration.html")


def foodList(request, pk):
    restaurant = Restaurant.objects.get(resID=pk)
    menus = Menu.objects.filter(resID=pk)
    form = editMenuForm()
    context = {"menus": menus, "restaurant": restaurant, "form": form}
    return render(request, "app/foodList.html", context)
