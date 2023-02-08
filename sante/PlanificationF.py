from django.forms import ModelForm
from sante.models import PlanificationFamiliale
from django import forms





class PLANFF(ModelForm):

    CodeDistrict   = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    CodeDomaine  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '  ', 'style': 'width: 500px;', 'class': 'form-control'}))
    CodeTemps  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    TauxdeRecrutementPF = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    TauxdAbandonPF  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))


    class Meta:
        model = PlanificationFamiliale
        fields = ['CodeDistrict','CodeDomaine','CodeTemps','TauxdeRecrutementPF','TauxdAbandonPF']