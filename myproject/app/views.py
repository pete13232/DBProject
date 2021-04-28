from django.shortcuts import render

# Create your views here.
def card3Col(request):
    return render(request, "card3Col.html")


def test(request):

    return render(request, "test.html")


def queueCard(request):
    return render(request, "queueCard.html")


def navbar(request) : 
    return render(request, "navbar.html")
