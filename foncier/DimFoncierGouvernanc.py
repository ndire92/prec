from django.forms import ModelForm
from foncier.models import DimFoncierGouvernanc
from django import forms


class Dimfong(ModelForm):

    LoiReglement  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '  ', 'style': 'width: 500px;', 'class': 'form-control'}))
    OutilSecuriseFoncie  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    ActFoncier  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '  ', 'style': 'width: 500px;', 'class': 'form-control'}))
    DegreConnaissanc = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))

    class Meta:
        model = DimFoncierGouvernanc
        fields = ['LoiReglement','OutilSecuriseFoncie','ActFoncier','DegreConnaissanc']