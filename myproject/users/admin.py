from django.contrib import admin

# Register your models here.

from .models import Role, Member

admin.site.register(Role)
admin.site.register(Member)
# admin.site.register(CustomUser)
