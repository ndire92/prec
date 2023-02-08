from django.forms import ModelForm
from peche.models import DimPecheAssure
from django import forms


class DPAS(ModelForm):


    TypeAssurancPech= forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    BesoinFormatPech  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    ActeurSensibilisePech = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    ActeurFormatPech= forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    BesoinSensibilisePech= forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))


    class Meta:
        model = DimPecheAssure
        fields = ['TypeAssurancPech','BesoinFormatPech','ActeurSensibilisePech','ActeurFormatPech','BesoinSensibilisePech']