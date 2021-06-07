from restaurants.models import Restaurant
from queueSystem.models import Queue
from django import forms
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from users.decorators import unauthenticated_user, allowed_users, admin_only

from .forms import createQueueForm, createNowQueueForm, createReviewForm

import sweetify

# Create your views here.


def index(request):

    return render(request, "queue/queueIndex.html")



@login_required(login_url="users/login")
@allowed_users(allowed_roles=["member"])
def createQueue(request, pk):
    count = Queue.objects.filter(queueIsPass=False).count()
    if request.method == "POST":
        form = createQueueForm(request.POST)
        member = request.POST["memberID"]
        if count > 1:
            sweetify.error(
                request,
                icon="error",
                title="Oops !",
                text="คุณยังมีรายการคิวอยู่",
                timer=2500,
                timerProgressBar=True,
                allowOutsideClick=True,
            )
            return redirect("/resCard/" + pk)

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
                text="กรุณากรอกฟอร์มให้ถูกต้อง",
                timer=2500,
                timerProgressBar=True,
                allowOutsideClick=True,
            )
            return redirect("/resCard/" + pk)
    else:
        form = createQueueForm()

@login_required(login_url="users/login")
@allowed_users(allowed_roles=["admin", "manager", "staff"])
def createNowQueue(request, pk):
    count = Queue.objects.filter(queueIsPass=False).count()
    if request.method == "POST":
        form = createNowQueueForm(request.POST)
        member = request.POST["memberID"]
        if count > 1:
            sweetify.error(
                request,
                icon="error",
                title="Oops !",
                text="คุณยังมีรายการคิวอยู่",
                timer=2500,
                timerProgressBar=True,
                allowOutsideClick=True,
            )
            return redirect("/resCard/" + pk)
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
                text=forms.ValidationError.message(),
                timer=2500,
                timerProgressBar=True,
                allowOutsideClick=True,
            )
            return redirect("/resCard/" + pk)

@login_required(login_url="users/login")
@allowed_users(allowed_roles=[ "member"])
def createReview(request, pk):
    if request.method == "POST":
        form = createReviewForm(request.POST)
        if form.is_valid():
            form.save()
            sweetify.success(
                request,
                icon="success",
                title="DONE !",
                text="Your review was sent",
                timer=1000,
                timerProgressBar=True,
                allowOutsideClick=True,
            )
            return redirect("/resCard/" + pk)
        else:
            sweetify.error(
                request,
                icon="error",
                title="Oops !",
                text="Somethings went wrong! Try again."
                + request.POST["resID"]
                + request.POST["memberID"]
                + request.POST["detail"],
                timer=2500,
                timerProgressBar=True,
                allowOutsideClick=True,
            )
            return redirect("/resCard/" + pk)
