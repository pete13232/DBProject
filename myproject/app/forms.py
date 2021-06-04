from django import forms
from django.db.models import fields
from queueSystem.models import Queue
from django.forms.widgets import (
    DateInput,
    EmailInput,
    PasswordInput,
    Select,
    TextInput,
)


class createQueueForm(forms.ModelForm):
    class Meta:
        model = Queue
        fields = "__all__"
