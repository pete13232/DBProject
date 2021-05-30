from django.shortcuts import render

# Create your views here.
def card3Col(request):
    return render(request, "card3Col.html")


def index(request):
    myContext = {
        "titles": ["A", "B", "C", "D", "E", "F"]
        }
    return render(request, "index.html", myContext)


def resCard(request):

    return render(request, "resCard.html")


def categoryCard(request):

    return render(request, "categoryCard.html")


def login(request):
    return render(request, "login.html")


def signup(request):
    return render(request, "signup.html")


def review(request):
    return render(request, "review.html")
