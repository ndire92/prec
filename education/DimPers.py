from django.forms import ModelForm
from education.models import DimEduc_Personnel
from django import forms


class DPR(ModelForm):

    EnsPrescolairePubli= forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    EnsPrescolairePrive= forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    EnsPrescolaireCommunautaire= forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    EnseignantPrescoparStatut = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    ElevePrecolairePrive = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))

    class Meta:
        model = DimEduc_Personnel
        fields = ['EnsPrescolairePubli','EnsPrescolairePrive','EnsPrescolaireCommunautaire','EnseignantPrescoparStatut','ElevePrecolairePrive']