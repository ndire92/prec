from django.forms import ModelForm
from das.models import DimAgroFinance
from django import forms


class DimAgrofinf(ModelForm):

    OffreServicFinance  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    DemandApport  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    TypeGaranExige  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    LongProcedCredi  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    DelaiRembourse  = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))


    class Meta:
        model = DimAgroFinance
        fields = ['OffreServicFinance' , 'DemandApport' , 'TypeGaranExige','LongProcedCredi','DelaiRembourse']