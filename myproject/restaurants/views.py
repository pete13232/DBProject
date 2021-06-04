from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Menu, Restaurant
from .forms import createMenuForm

from django.shortcuts import render
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from users.decorators import unauthenticated_user, allowed_users, admin_only
from django.shortcuts import get_list_or_404, get_object_or_404

import sweetify

# Create your views here.
def index(request):

    return render(request, "restaurants/resIndex.html")


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
