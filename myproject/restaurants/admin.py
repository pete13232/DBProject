from django.contrib import admin

# Register your models here.

from .models import Category, Company, Restaurant, Menu

admin.site.register(Category)
admin.site.register(Company)
admin.site.register(Menu)
admin.site.register(Restaurant)
