from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Menu
from .forms import editMenuForm

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
