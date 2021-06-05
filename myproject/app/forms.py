from django.contrib.auth.models import Group
from users.models import Member
from django import forms

class Meta:
        model = Member
        fields = ("groups",)


class deleteStaffForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ("id", "resID")


class changeProfileForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ("id", "profile")
