from django.forms import ModelForm
from foncier.models import DimGeographie
from django import forms


class Dimfgeo(ModelForm):

    codeCommune   = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    nomCommune = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    CodeIndicateur  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    Indicateur  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    CodeDomaine = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))


    class Meta:
        model = DimGeographie
        fields = ['codeCommune' , 'nomCommune' , 'CodeIndicateur','Indicateur','CodeDomaine']