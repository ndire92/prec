from django.forms import ModelForm
from education.models import DimEduc_Perfomance
from django import forms


class DPRF(ModelForm):

    NbrePassants_NiveauEtude = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    NbreRedoublement_NiveauEtude= forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    NbreAbandon_NiveauEtude= forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    BudgetalloueEtatEcoleLycee = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    NbrePassants_SatutEtablissement = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    NbreRedoublement_StatutEtablissemen = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))

    class Meta:
        model = DimEduc_Perfomance
        fields = ['NbrePassants_NiveauEtude','NbreRedoublement_NiveauEtude','NbreAbandon_NiveauEtude','BudgetalloueEtatEcoleLycee','NbrePassants_SatutEtablissement','NbreRedoublement_StatutEtablissemen']