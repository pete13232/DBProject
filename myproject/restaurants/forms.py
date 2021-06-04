from django import forms
from django.db.models import fields
from django.forms import widgets
from restaurants.models import Menu
from django.forms.widgets import (
    DateInput,
    EmailInput,
    PasswordInput,
    Select,
    TextInput,
)


class editMenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = "__all__"


class createMenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = "__all__"
