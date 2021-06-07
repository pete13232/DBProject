from django import forms
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group

from users.decorators import unauthenticated_user, allowed_users, admin_only

from .forms import CreateMemberForm, editMemberForm
from restaurants.forms import editMenuForm, editCompanyForm, editRestaurantForm

from .models import Member
from restaurants.models import Company, Restaurant, Category

import sweetify

# Create your views here.
def index(request):
    return render(request, "users/usersIndex.html")


@unauthenticated_user
def signup(request):

    if request.method == "POST":
        form = CreateMemberForm(request.POST)
        if form.is_valid():
            form.save()
            user = request.POST["fName"] + " " + request.POST["lName"]
            messages.success(request, "Account was created for " + user)
            return redirect("users_login")
        else:
            messages.info(request, form.errors)
    else:
        form = CreateMemberForm()
    context = {"form": form}
    return render(request, "users/signup.html", context)


# login page
@unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Username OR password is incorrect")
    context = {}
    return render(request, "users/basicLogin.html", context)


def logoutPage(request):
    logout(request)
    return redirect("/")

@login_required(login_url="users/login")
def profile(request, pk):
    if request.method == "POST":
        if pk[0] == "C":
            instance = get_object_or_404(Company, companyID=pk)
            company = Company.objects.get(companyID=pk)
            form = editCompanyForm(request.POST or None, instance=instance)
            if form.is_valid():
                form.save()
                sweetify.success(
                    request,
                    icon="success",
                    title="DONE!",
                    text="Company " + str(company.companyName) + " was updated",
                    timer=1500,
                    timerProgressBar=True,
                    allowOutsideClick=True,
                )
                return redirect("/profile/" + pk)
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
                return redirect("/profile/" + pk)
        elif pk[0] == "R":
            instance = get_object_or_404(Restaurant, resID=pk)
            restaurant = Restaurant.objects.get(resID=pk)
            form = editRestaurantForm(request.POST or None, instance=instance)
            # open =  Restaurant.objects.get(resID=pk).open
            # close =  Restaurant.objects.get(resID=pk).close
            open = request.POST["open"]
            close = request.POST["close"]
            # form.open = open
            # form.close = close
            if form.is_valid():
                form.save()
                sweetify.success(
                    request,
                    icon="success",
                    title="DONE!",
                    text="Restaurat " + str(restaurant.resName) + " was updated",
                    timer=1500,
                    timerProgressBar=True,
                    allowOutsideClick=True,
                )
                return redirect("/profile/" + pk)
            else:
                sweetify.error(
                    request,
                    icon="error",
                    title="Oops !",
                    text="Something went wrong! Try again" + str(open) + str(close),
                    timer=2500,
                    timerProgressBar=True,
                    allowOutsideClick=True,
                )
                print(form)
                return redirect("/profile/" + pk)
        else:
            print("0")
    else:
        company = None
        restaurant = None
        profile = None
        categories = Category.objects.all()
        if pk[0] == "C":
            company = Company.objects.get(companyID=pk)
            form = editCompanyForm()
        elif pk[0] == "R":
            restaurant = Restaurant.objects.get(resID=pk)
            form = editRestaurantForm()
        else:
            profile = Member.objects.get(memberID=pk)
            form = editMemberForm()
        context = {
            "company": company,
            "categories": categories,
            "restaurant": restaurant,
            "profile": profile,
            "form": form,
            "pk": pk,
        }
    return render(request, "users/profile.html", context)