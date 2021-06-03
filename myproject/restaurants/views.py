from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Menu
from .forms import editMenuForm

from django.shortcuts import render
from django.contrib.auth.models import Group
from users.decorators import unauthenticated_user, allowed_users, admin_only
# Create your views here.
def index(request):

    return render(request, "restaurants/resIndex.html")


def editMenu(request):
    if request.method == "POST":
        form = editMenuForm(request.POST)
        if form.is_valid():
            resID = form.cleaned_data("resID")
            form.save()
            messages.info(request, "Success")
            redirect("foodList/" + resID)
        else:
            messages.info(request, form.errors)
            redirect("/")
    else:
        form = editMenuForm()
    context = {"form": form}
    return render(request, "restaurants/editMenuModal.html", context)
