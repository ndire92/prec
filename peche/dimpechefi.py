from django.forms import ModelForm
from peche.models import DimPecheFinance
from django import forms


class DPFI(ModelForm):

    OffrServicFinancPech= forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    DemandApportPech = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    TypGaranExige = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    ActeurFormatPech= forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))



    class Meta:
        model = DimPecheFinance
        fields = ['OffrServicFinancPech','DemandApportPech','TypGaranExige','ActeurFormatPech']