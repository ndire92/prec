from django.forms import ModelForm
from das.models import DimAgroOrganisation
from django import forms


class DimAgroorg(ModelForm):

    name_Organisation  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    TypeServicOfferOP  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    BesoinForm  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    ContrainGlobalAgro  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    ContrainMajFilier  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    InfrasStockCondition  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    FournisEmballag = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))


    class Meta:
        model = DimAgroOrganisation
        fields = ['name_Organisation' , 'TypeServicOfferOP' , 'BesoinForm','ContrainGlobalAgro','ContrainMajFilier','InfrasStockCondition','FournisEmballag']