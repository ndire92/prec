from django.forms import ModelForm
from education.models import DimEduc_Access
from django import forms

class acc(ModelForm):
    class Meta:
        model = DimEduc_Access
        fields = "__all__"