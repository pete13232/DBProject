from queueSystem.models import Queue
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from users.decorators import unauthenticated_user, allowed_users, admin_only

from .forms import createQueueForm

import sweetify

# Create your views here.


def index(request):

    return render(request, "queueSystem/queueIndex.html")


def createQueue(request, pk):
    if request.method == "POST":
        form = createQueueForm(request.POST)
        member = request.POST["memberID"]
        if form.is_valid():
            form.save()
            queue = Queue.objects.get(memberID=member, queueIsPass=False)
            sweetify.success(
                request,
                icon="success",
                title="CREATED !",
                text="Your queue is " + str(queue.queueID),
                timer=3000,
                timerProgressBar=True,
                allowOutsideClick=True,
            )
            return redirect("/resCard/" + pk)
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
            return redirect("/resCard/" + pk)
    else:
        form = createQueueForm()