from django import forms
from search.models import RegModel, logModel


class RegForm(forms.ModelForm):
    class Meta:
        model = RegModel
        fields = "__all__"


class Logform(forms.ModelForm):
    class Meta:
        model = logModel
        fields = "__all__"
