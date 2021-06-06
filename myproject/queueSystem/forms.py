from django import forms
from queueSystem.models import Queue
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

    # def clean_reserveDate(self, *args, **kwargs):
    #     reserveDate = self.cleaned_data.get("reserveDate")

    #     if reserveDate <= datetime.date.today():
    #         raise forms.ValidationError("กรุณาระบุเวลาล่วงหน้า")

    # def clean_reserveTime(self, *args, **kwargs):
    #     reserveTime = self.cleaned_data.get("reserveTime")

    #     if reserveTime <= timezone.localtime():
    #         raise forms.ValidationError("กรุณาระบุเวลาล่วงหน้า")


class createNowQueueForm(forms.ModelForm):
    class Meta:
        model = Queue
        fields = (
            "resID",
            "memberID",
            "peopleNum",
        )
