from django.forms import ModelForm
from education.models import DimEduc_Equipements
from django import forms


class equi(ModelForm):

    NbrePlaceAssisPresco  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '    ', 'style': 'width: 500px;', 'class': 'form-control'}))
    NbreElevePresco = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    NbreEnfantBeneficieDeparasitage = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    NbreEnfantPresco = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    NbreStructureElementaireDisposantCantinesScolaires  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '  ', 'style': 'width: 500px;', 'class': 'form-control'}))


    class Meta:
        model = DimEduc_Equipements
        fields = ['NbrePlaceAssisPresco','NbreElevePresco','NbreEnfantBeneficieDeparasitage','NbreEnfantPresco','NbreStructureElementaireDisposantCantinesScolaires']