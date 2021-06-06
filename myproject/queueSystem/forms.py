from django import forms
from queueSystem.models import Queue


class createQueueForm(forms.ModelForm):
    class Meta:
        model = Queue
        fields = (
            "resID",
            "memberID",
            "peopleNum",
            "reserveTime",
            "reserveDate",
        )


class createNowQueueForm(forms.ModelForm):
    class Meta:
        model = Queue
        fields = (
            "resID",
            "memberID",
            "peopleNum",
        )
