from django.shortcuts import render
from .models import Member

# Create your views here.
def index(request):
    # members = Member.objects.all()
    # Context = {"members": members}
    return render(request, "users/usersIndex.html")
