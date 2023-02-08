from django.forms import ModelForm
from education.models import DimEduc_Gouvernance
from django import forms


class Dg(ModelForm):

    BudgetalloueEtatEcolePrimaire  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    NbreElevePresco = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    BudgetalloueEtatEcoleSecondaire = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    BudgetalloueEtatEcoleLycee = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    BudgetCTalloueEducation = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))


    class Meta:
        model = DimEduc_Gouvernance
        fields = ['BudgetalloueEtatEcolePrimaire','NbreElevePresco','BudgetalloueEtatEcoleSecondaire','BudgetalloueEtatEcoleLycee','BudgetCTalloueEducation']