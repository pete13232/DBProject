from django.shortcuts import render
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from users.decorators import unauthenticated_user, allowed_users, admin_only
# Create your views here.

def index(request):
    
    return render(request, "queueSystem/queueIndex.html")