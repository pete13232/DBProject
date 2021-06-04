import email
from django import forms
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Member, Role
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from users.decorators import unauthenticated_user, allowed_users, admin_only

from .forms import CreateMemberForm, MemberForm, CreateUserForm

# Create your views here.
def index(request):
    # members = Member.objects.all()
    # Context = {"members": members}
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


# register page

def registerPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, "Account was created for " + user)
            return redirect("users_login")

    context = {"form": form}

    return render(request, "users/basicSignup.html", context)


# login page
def loginPage(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("users_index")
        else:
            messages.info(request, "Username OR password is incorrect")
    context = {}
    return render(request, "users/basicLogin.html", context)


def logoutPage(request):
    logout(request)
    return redirect("/")

