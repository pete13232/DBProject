from django import forms
from django.db.models import fields
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
        fields = ("menuName",)
        widgets = {
            "menuName": TextInput(
                attrs={
                    "id": "menuName",
                    "class": "form-control",
                },
            )
        }