from django.contrib.auth.models import Group
from users.models import Member
from restaurants.models import Company, Restaurant
from django import forms


class deleteStaffForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ("memberID", "resID")


class changeProfileForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ("memberID", "profilePic")


class editRoleForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ("memberID", "role")
