from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Menu
from .forms import editMenuForm

from django.shortcuts import render
from django.contrib.auth.models import Group
from users.decorators import unauthenticated_user, allowed_users, admin_only
from django.shortcuts import get_list_or_404, get_object_or_404

# Create your views here.
def index(request):

    return render(request, "restaurants/resIndex.html")


def editMenu(
    request,
):
    if request.method == "POST":
        instance = get_object_or_404(Menu, menuID=request.POST["menuID"])
        form = editMenuForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            messages.info(request, "Success")
            return redirect("/foodlist" + "/" + str(form.cleaned_data["resID"]))
        else:
            messages.info(request, form.errors)
            return redirect("foodList" + "/R001")
    else:
        form = editMenuForm()
    context = {"form": form}
    return render(request, "restaurants/editMenuModal.html", context)
