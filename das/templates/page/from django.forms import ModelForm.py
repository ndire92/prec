from django.forms import ModelForm
from educations.models import DimEduc_Access
from django import forms


class ass(ModelForm):
    EnsGarcons3_5ans= forms.CharField(widget=forms.TextInput(attrs={'placeholder': '  ', 'style': 'width: 500px;', 'class': 'form-control'}))
    EnsFilles3_5ans = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    EnsFilles_Garcons3_5ans = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    EffectifGarconsInscritPrescolaire = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    EffectifFillesnscritPrescolaire = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    EffectifTotalElevInscritPrescolaire = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    EffectifsPrescPetiteSection = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    EffectifPrescoMoyenneSection = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    EffectifPrescoGrandeSection = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    EffectifsPrescoTT = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    NbreGarcons_FillesPS = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    NbreGarcons_FillesMS = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    NbreGarcons_FillesGS = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    NreFillesPrescolaire = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    EffectifsTotalElvInscitPrescoPublic = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    EffectifsTotalElvInscitPrescoStuctureCommunautaires = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    EffectifsTotalElev = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    NbreStructurePrescolairePublic = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    NbreStructurePrescolairePrive = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    NbreStructuresPrescolaireCommunautaires = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    NbreDaaraModernes = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    NbreDaaraMises_Niveau = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    NbreEnfDansElementaire = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    NbreGarconsDansElementaire = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    NbreFillesDansElementaire = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    NbreElvInscritCIPremierFois = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    NbreElvQuittantEtablissementCommuneversEtablissemnetHorsCommune = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    NbreElvProvenanveEtablissemnetHorsCommune = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    NbreEcoleElementairePubliques = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    NbreEcoleElementairePrivees = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    EnsGarcons_12_15ans = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    EnsFilles_12_15ans = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    EnsFillesGarcons_12_15ans = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    NreElevesElementaire = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    NbreGarconsElementaire = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    NbreFillesElementaire = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    EnsGarcons_16_18ans = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    EnsFilles_16_18ans = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    EnsGarcons_Filles_16_18ans = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    NbreElvSecondaire = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
    NbreGarconsSecondaire = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    NbreFillesSecondaire = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    NbreFilleMarieeCoursAnnee_Secondaire = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 500px;', 'class': 'form-control'}))
    NbreFillesEnceinteEnCoursAnnee_Secondaire = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ', 'style': 'width: 500px;', 'class': 'form-control'}))
	
 




class Meta:
    model = DimEduc_Access
    fields = ['EnsGarcons3_5ans','EnsFilles3_5ans','EnsFilles_Garcons3_5ans','EffectifGarconsInscritPrescolaire','EffectifFillesnscritPrescolaire','EffectifTotalElevInscritPrescolaire','EffectifsPrescPetiteSection','EffectifPrescoMoyenneSection',
    'EffectifPrescoGrandeSection','EffectifsPrescoTT','NbreGarcons_FillesPS','NbreGarcons_FillesMS','NbreGarcons_FillesG','NreFillesPrescolaire',
    'EffectifsTotalElvInscitPrescoPublic','EffectifsTotalElvInscitPrescoStuctureCommunautaires','EffectifsTotalElev','NbreStructurePrescolairePublic','NbreStructurePrescolairePrive','NbreStructuresPrescolaireCommunautaires','NbreDaaraModernes','NbreDaaraMises_Niveau','NbreEnfDansElementaire ','NbreGarconsDansElementaire',
    'NbreFillesDansElementaire','NbreElvInscritCIPremierFois','NbreElvQuittantEtablissementCommuneversEtablissemnetHorsCommune','NbreElvProvenanveEtablissemnetHorsCommune','NbreEcoleElementairePubliques','NbreEcoleElementairePrivees','EnsGarcons_12_15ans','EnsFilles_12_15ans','EnsFillesGarcons_12_15ans','NreElevesElementaire','NbreGarconsElementaire',
    'NbreFillesElementaire','EnsGarcons_16_18ans','EnsFilles_16_18ans' ,'EnsGarcons_Filles_16_18ans','NbreElvSecondaire','NbreGarconsSecondaire','NbreFillesSecondaire','NbreFilleMarieeCoursAnnee_Secondaire','NbreFillesEnceinteEnCoursAnnee_Secondaire']