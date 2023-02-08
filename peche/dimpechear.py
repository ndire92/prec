from django.forms import ModelForm
from peche.models import DimPecheArtisan
from django import forms


class DPA(ModelForm):

    ActPech_Artisan   = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '  ', 'style': 'width: 500px;', 'class': 'form-control'}))
    GroupPecheur  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '  ', 'style': 'width: 500px;', 'class': 'form-control'}))
    GroupMareyeur  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    TypePirogu  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    TypProdPechPirogBois  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))


    class Meta:
        model = DimPecheArtisan
        fields = ['ActPech_Artisan','GroupPecheur','GroupMareyeur','TypePirogu','TypProdPechPirogBois']