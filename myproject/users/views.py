from django import forms
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Member, Role
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout


from .forms import MemberForm, CreateUserForm

# Create your views here.
def index(request):
    # members = Member.objects.all()
    # Context = {"members": members}
    return render(request, "users/usersIndex.html")


def signup(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            fName = form.cleaned_data["fName"]
            lName = form.cleaned_data["lName"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            tel = form.cleaned_data["tel"]
            gender = form.cleaned_data["gender"]
            dob = form.cleaned_data["dob"]

            form.save()
            return HttpResponseRedirect("signup")
    else:
        form = MemberForm()
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

    return render(request, "users/signup.html", context)


# login page
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("users_index")
        else:
            messages.info(request, "Username OR password is incorrect")
    context = {}
    return render(request, "users/basicLogin.html", context)


def logoutUser(request):
    logout(request)
    return redirect("users_login")

