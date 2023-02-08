from django.forms import ModelForm
from foncier.models import DimFoncier
from django import forms


class DimAgroprd(ModelForm):

    name_Production  = forms.CharField(widget=forms.TextInput(attrs={ 'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    ProdCultHiver  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    TypeSolExist = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    TypeDegradZonCultur  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    CauseDegrad  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))


    class Meta:
        model = DimFoncier
        fields = ['name_Production', 'ProdCultHiver' , 'TypeSolExist','TypeDegradZonCultur','CauseDegrad' ]