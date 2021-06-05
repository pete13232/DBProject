from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group
# Register your models here.

from .models import  Member

admin.site.unregister(Group)
admin.site.register(Member)
# admin.site.register(CustomUser)
