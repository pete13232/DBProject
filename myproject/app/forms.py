from django.contrib.auth.models import Group
from users.models import Member, Role
from django import forms


class editRoleForm(forms.ModelForm):
    group = forms.ModelChoiceField(
        queryset=Role.objects.all(), widget=forms.widgets.RadioSelect()
    )

    class Meta:
        model = Member
        fields = ("groups",)
