from django.shortcuts import render

# Create your views here.
def card3Col(request):
    return render(request, "card3Col.html")


def test(request):

    return render(request, "test.html")
