from django.shortcuts import render
from .models import Member

from .forms import MemberForm

# Create your views here.
def index(request):
    # members = Member.objects.all()
    # Context = {"members": members}
    return render(request, "users/usersIndex.html")


def signup(request):
    
    data = Member.objects.all()
    context = {"data": data}

    return render(request, "users/signup.html", context)


