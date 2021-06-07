from django import forms
from django.db import models
from django.db.models import fields
from django.forms import widgets
from restaurants.models import Menu, Company, Restaurant


class editMenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = "__all__"


class createMenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = (
            "resID",
            "menuName",
            "description",
            "price",
            "avaliable",
            "profilePic",
        )


class editCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"


class changeStatusForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ("menuID", "avaliable")


class editRestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        exclude = ["open", "close", "companyID"]


class createResForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        exclude = ["resID"]
