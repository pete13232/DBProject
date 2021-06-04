from django import forms
from queueSystem.models import Queue


class createQueueForm(forms.ModelForm):
    class Meta:
        model = Queue
        fields = ("memberID", "resID", "reserveTime", "peopleNum")
