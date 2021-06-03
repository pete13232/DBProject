from django.shortcuts import render
from django.contrib.auth.models import Group
from users.decorators import unauthenticated_user, allowed_users, admin_only
# Create your views here.
def index(request):

    return render(request, "restaurants/resIndex.html")