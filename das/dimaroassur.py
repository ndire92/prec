from django.forms import ModelForm
from das.models import DimAgroAssurance
from django import forms


class DimAgroAssurancef(ModelForm):

    OffreuAssurance  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    TypeAssurance  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    CulturAssure  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    NivPrime  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))


    class Meta:
        model = DimAgroAssurance
        fields = ['OffreuAssurance' , 'TypeAssurance' , 'CulturAssure','NivPrime']