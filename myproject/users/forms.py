from django.contrib.auth.models import User
from django.forms import widgets
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
from django.contrib.auth.forms import UserCreationForm


class MemberForm(forms.ModelForm):
    error_messages = {
        "password_mismatch": ("The two password fields didn't match."),
    }

    confirmPassword = forms.CharField(
        max_length=20,
        widget=forms.PasswordInput(
            attrs={"id": "confirmPassword", "class": "form-control"}
        ),
    )

    class Meta:
        model = Member
        fields = (
            "email",
            "password",
            "fName",
            "lName",
            "gender",
            "tel",
            "dob",
        )
        widgets = {
            "fName": TextInput(
                attrs={
                    "id": "fName",
                    "class": "form-control",
                    "placeholder": "xxxxxx",
                }
            ),
            "lName": TextInput(
                attrs={"id": "lName", "class": "form-control", "placeholder": "xxxxxx"}
            ),
            "password": PasswordInput(
                attrs={"id": "password", "class": "form-control"}
            ),
            "email": EmailInput(
                attrs={
                    "id": "email",
                    "class": "form-control",
                    "placeholder": "superYenYen@getAdatabase.com",
                }
            ),
            "tel": TextInput(
                attrs={
                    "type": "tel",
                    "id": "tel",
                    "class": "form-control",
                    "placeholder": "0864858875",
                    "pattern": "^0[0-9]{9}",
                }
            ),
            "gender": Select(
                attrs={
                    "id": "gender",
                    "class": "form-select",
                },
            ),
            "dob": DateInput(
                attrs={
                    "type": "date",
                    "id": "dob",
                    "class": "form-control",
                }
            ),
        }

    def clean(self):
        cleaned_data = super(MemberForm, self).clean()
        password = cleaned_data.get("password")
        confirmPassword = cleaned_data.get("confirmPassword")

        if password != confirmPassword:
            raise forms.ValidationError("password and confirmPassword does not match")

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get("password")
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except forms.ValidationError as error:
                self.add_error("password", error)


class CreateUserForm(UserCreationForm):
    fName = forms.CharField(max_length=30)
    lName = forms.CharField(max_length=30)
    tel = forms.CharField(
        max_length=10,
        widget=forms.TextInput(
            attrs={
                "type": "tel",
                "id": "tel",
                "class": "form-control",
                "placeholder": "0864858875",
                "pattern": "^0[0-9]{9}",
            }
        ),
    )
    dob = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "id": "dob",
                "class": "form-control",
            }
        ),
    )
    GENDER = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    )
    gender = forms.ChoiceField(choices=GENDER)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


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
        fields = "__all__"