from django.forms import ModelForm
from foncier.models import FactFoncier
from django import forms


class Dimff(ModelForm):

    DateDomainFoncier_FK  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'DateDomainFoncier_FK', 'style': 'width: 500px;', 'class': 'form-control'}))
    TypeServicOfferOP  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'DemandApport ', 'style': 'width: 500px;', 'class': 'form-control'}))
    BesoinForm  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'BesoinForm ', 'style': 'width: 500px;', 'class': 'form-control'}))
    ContrainGlobalAgro  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'ContrainGlobalAgro', 'style': 'width: 500px;', 'class': 'form-control'}))
    ContrainMajFilier  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'ContrainMajFilier ', 'style': 'width: 500px;', 'class': 'form-control'}))
    InfrasStockCondition  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'InfrasStockCondition', 'style': 'width: 500px;', 'class': 'form-control'}))
    FournisEmballag = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'FournisEmballag', 'style': 'width: 500px;', 'class': 'form-control'}))


    class Meta:
        model = FactFoncier
        fields = ['DateDomainFoncier_FK' , 'TypeServicOfferOP' , 'BesoinForm','ContrainGlobalAgro','ContrainMajFilier','InfrasStockCondition','FournisEmballag']