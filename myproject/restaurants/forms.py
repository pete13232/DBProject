from django import forms
from django.db.models import fields
from django.forms import widgets
from restaurants.models import Menu, Company, Restaurant
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
        fields = ("resID", "menuName", "description", "price", "avaliable", "picture")

class editCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"

class editRestaurantForm(forms.ModelForm):
    open = forms.DateTimeField(required=False)
    close = forms.DateTimeField(required=False)
    class Meta:
        model = Restaurant
        exclude = ["open","close"]
    # def get_close(self,*args, **kwargs):
    #     resID = self.cleaned_data("resID")
    #     open = self.cleaned_data("open")
    #     close = self.cleaned_data("close")
    #     if open == None and close == None:
    #         open = Restaurant.objects.get(resID=resID).open
    #         close = Restaurant.objects.get(resID=resID).close
        