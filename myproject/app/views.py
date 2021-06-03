from django.shortcuts import render
from restaurants.models import Category, Restaurant, Menu
from users.models import Member
from queueSystem.models import Queue

# Create your views here.
def card3Col(request):
    return render(request, "card3Col.html")


def index(request):
    categorys = Category.objects.all()
    restaurants = Restaurant.objects.all()
    myContext = {"categorys": categorys, "restaurants": restaurants}
    return render(request, "app/index.html", myContext)


def resCard(request, pk):
    restaurant = Restaurant.objects.get(resID=pk)
    myContext = {"restaurant": restaurant}
    return render(request, "app/resCard.html", myContext)


def categoryCard(request):

    return render(request, "app/categoryCard.html")


def login(request):
    return render(request, "app/login.html")


def signup(request):
    return render(request, "app/signup.html")


def review(request):
    return render(request, "app/review.html")


def userprofile(request, pk):
    profile = Member.objects.get(memberID=pk)
    queue = Queue.objects.get(memberID=pk)
    context = {"profile": profile, "queue": queue}
    return render(request, "app/userProfile.html", context)


def workerprofile(request):
    return render(request, "app/workerProfile.html")


def queueManagement(request):

    return render(request, "app/queueManagement.html")


def foodList(request, pk):
    restaurant = Restaurant.objects.get(resID=pk)
    menus = Menu.objects.filter(resID=pk)
    context = {"menus": menus, "restaurant": restaurant}
    return render(request, "app/foodList.html", context)
