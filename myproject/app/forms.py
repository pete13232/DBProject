from django.contrib.auth.models import Group
from users.models import Member
from restaurants.models import Company, Restaurant
from django import forms

class editRoleForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ("memberID", "role")
