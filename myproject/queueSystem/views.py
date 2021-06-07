from django.db.models.aggregates import Sum
from users.models import Member
from restaurants.models import Restaurant
from queueSystem.models import Queue
from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from users.decorators import unauthenticated_user, allowed_users, admin_only

from .forms import (
    createQueueForm,
    createNowQueueForm,
    createReviewForm,
    updateQueueForm,
)

import sweetify

# Create your views here.


def index(request):

    return render(request, "queue/queueIndex.html")


@login_required(login_url="users/login")
@allowed_users(allowed_roles=["admin", "manager", "staff"])
def staffHome(request, pk):
    restaurant = Restaurant.objects.get(resID=pk)
    context = {"restaurant": restaurant}
    return render(request, "queue/staffHome.html", context)


@login_required(login_url="users/login")
@allowed_users(allowed_roles=["member"])
def createQueue(request, pk):
    member = request.POST["memberID"]
    queues = Queue.objects.filter(memberID=member)
    count = Queue.objects.filter(memberID=member, queueIsPass=False).count()
    point = queues.aggregate(Sum("point"))
    my_point = point.get("point__sum")
    print(my_point)
    if my_point == None:
        my_point = 0
    if request.method == "POST":
        form = createQueueForm(request.POST)
        member = request.POST["memberID"]
        if my_point < 0:
            sweetify.error(
                request,
                icon="error",
                title="Oops !",
                text="คะแนนคุณน้อยเกินไป",
                timer=2500,
                timerProgressBar=True,
                allowOutsideClick=True,
            )
            return redirect("/res/resCard/" + pk)
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
            return redirect("/res/resCard/" + pk)

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
            return redirect("/res/resCard/" + pk)
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
@allowed_users(allowed_roles=["member"])
def createNowQueue(request, pk):
    count = Queue.objects.filter(queueIsPass=False).count()
    member = request.POST["memberID"]
    queues = Queue.objects.filter(memberID=member)
    point = queues.aggregate(Sum("point"))
    my_point = point.get("point__sum")
    print(point)
    print(my_point)
    if my_point == None:
        my_point = 0
    if request.method == "POST":
        form = createNowQueueForm(request.POST)
        member = request.POST["memberID"]
        if my_point < 0:
            sweetify.error(
                request,
                icon="error",
                title="Oops !",
                text="คะแนนคุณน้อยเกินไป",
                timer=2500,
                timerProgressBar=True,
                allowOutsideClick=True,
            )
            return redirect("/res/resCard/" + pk)
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
            return redirect("/res/resCard/" + pk)
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
            return redirect("/res/resCard/" + pk)
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
@allowed_users(allowed_roles=["member"])
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


@login_required(login_url="users/login")
@allowed_users(allowed_roles=["admin", "manager", "staff"])
def updateQueue(request, pk):
    if request.method == "POST":
        instance = get_object_or_404(Queue, queueID=pk)
        form = updateQueueForm(request.POST or None, instance=instance)
        next = request.POST.get("next")
        status = request.POST.get("next")
        if form.is_valid() and status != "cancel":
            form.save()
            sweetify.success(
                request,
                icon="success",
                title="DONE !",
                text="Queue status is update",
                timer=1000,
                timerProgressBar=True,
                allowOutsideClick=True,
            )
            return redirect(next)
        else:
            sweetify.error(
                request,
                icon="error",
                title="Oops !",
                text="Somethings went wrong! Try again.",
                timer=2500,
                timerProgressBar=True,
                allowOutsideClick=True,
            )
            return redirect(next)
