from collections import namedtuple
from django.db.models import fields
from django.forms.forms import Form
from django.forms.widgets import TextInput, Textarea
from django.template.defaultfilters import title
from admin import models
from crispy_forms.layout import Column, Div, MultiField, Row, Submit
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models.fields import Field, TextField
from users.models import Member
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.bootstrap import AppendedText, FormActions, PrependedText


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = (
            "email",
            "password",
            "fName",
            "lName",
            "gender",
            "dob",
        )
        widgets = {
            "email": TextInput(attrs={"placeholder": "superYenYen@getAdatabase.com"}),
            'fName': TextInput(attrs={'placeholder':'xxxxxx'}),
            'lName': TextInput(attrs={'placeholder':'xxxxxx'})


            }


# class UserForm(forms.Form):
#     fName = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "weerawat"}))
#     lName = forms.CharField(
#         widget=forms.TextInput(attrs={"placeholder": "Lappermthawee"})
#     )
#     password1 = forms.CharField(widget=forms.PasswordInput())
#     password2 = forms.CharField(widget=forms.PasswordInput())
#     email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email"}))
#     Phone = forms.CharField(widget=forms.TextInput())
#     GENDER = (
#         ("M", "Male"),
#         ("F", "Female"),
#         ("O", "Other"),
#     )
#     gender = forms.ChoiceField(choices=GENDER)
#     dob = forms.DateField(widget=forms.DateInput(), label="DOB")
#     # class Meta:
#     #     model = User
#     #     fields = "__all__"

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper._form_method = "post"
#         self.helper.layout = Layout(
#             Row(
#                 Column("fName", css_class="form-group col-md-6 mb-0"),
#                 Column("lName", css_class="form-group col-md-6 mb-0"),
#                 css_class="form-row",
#             ),
#             Row(
#                 Column("password1", css_class="form-group col-md-6 mb-0"),
#                 Column("password2", css_class="form-group col-md-6 mb-0"),
#                 css_class="form-row",
#             ),
#             "email",
#             "phone",
#             "gender",
#             "dob",
#             Submit("submit", "Sign in"),
#         )
