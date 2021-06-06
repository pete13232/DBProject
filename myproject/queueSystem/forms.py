from django import forms
from queueSystem.models import Queue, Review
from django.utils import timezone
import datetime


class createQueueForm(forms.ModelForm):
    reserveDateTime = forms.DateTimeField()

    class Meta:
        model = Queue
        fields = (
            "resID",
            "memberID",
            "peopleNum",
        )

    def reserveDateTime(self, *args, **kwargs):
        reserveDateTime = self.cleaned_data.get("reserveDateTime")
        if reserveDateTime <= timezone.now():
            raise forms.ValidationError("กรุณาระบุเวลาล่วงหน้า")


class createNowQueueForm(forms.ModelForm):
    class Meta:
        model = Queue
        fields = (
            "resID",
            "memberID",
            "peopleNum",
        )


class createReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ["reviewID"]
