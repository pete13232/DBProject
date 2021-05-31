from django.contrib import admin

# Register your models here.

from .models import Queue, Review

admin.site.register(Queue)
admin.site.register(Review)