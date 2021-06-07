from django.contrib.auth import models
from django.contrib.auth.models import User
from django.forms import fields, widgets
from django.forms.widgets import (
    DateInput,
    EmailInput,
    PasswordInput,
    Select,
    TextInput,
)
from django import forms
from users.models import Member
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CreateMemberForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Member
        fields = (
            "email",
            "fName",
            "lName",
            "gender",
            "tel",
            "dob",
        )
        widgets = {
            "fName": TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "xxxxxx",
                }
            ),
            "lName": TextInput(
                attrs={"class": "form-control", "placeholder": "xxxxxx"}
            ),
            "email": EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "superYenYen@getAdatabase.com",
                }
            ),
            "tel": TextInput(
                attrs={
                    "type": "tel",
                    "class": "form-control",
                    "placeholder": "0864858875",
                    "pattern": "^0[0-9]{9}",
                }
            ),
            "gender": Select(
                attrs={
                    "class": "form-select",
                },
            ),
            "dob": DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                }
            ),
        }


class editMemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = (
            "memberID",
            "email",
            "fName",
            "lName",
            "gender",
            "tel",
            "profilePic",
        )


class editProfileForm(forms.ModelForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Member
        fields = (
            "email",
            "fName",
            "lName",
            "gender",
            "tel",
            "dob",
            "profilePic",
        )
