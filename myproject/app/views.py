from django.shortcuts import render

# Create your views here.
def card3Col(request):
    return render(request, "card3Col.html")


def index(request):
    myContext = {
        "categoryTitles": ["A", "B", "C", "D", "E", "F"],
        "restaurant": {
            "resTitle": ["KFC", "MK"],
            "resDesc": ["Fast Food", "Sukki"],
        },
    }
    return render(request, "app/index.html", myContext)


def resCard(request):

    return render(request, "app/resCard.html")


def categoryCard(request):

    return render(request, "app/categoryCard.html")


def login(request):
    return render(request, "app/login.html")


def signup(request):
    return render(request, "app/signup.html")


def review(request):
    return render(request, "app/review.html")

<<<<<<< HEAD

def profile(request):
    return render(request, "profile.html")
=======
def userprofile(request):
    return render(request, "app/userProfile.html")

def workerprofile(request):
    return render(request, "app/workerProfile.html")
>>>>>>> 7dab4fd21edd690b1baffacfd22e23acaf66eb5a


def queueManagement(request):

    return render(request, "app/queueManagement.html")


def foodList(request):

<<<<<<< HEAD
    return render(request, "foodList.html")
=======
    return render(request, "app/foodList.html")

>>>>>>> 7dab4fd21edd690b1baffacfd22e23acaf66eb5a
