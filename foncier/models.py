from django.db import models

# Create your models here.
from django.db import models

  #foncier
class DimFoncier(models.Model):
	TypeFoncier= models.CharField(max_length=300)
	StatuFoncier= models.CharField(max_length=300)
	TerrDeclas5D_Ans = models.CharField(max_length=300)
	ActFonciePresen =models.CharField(max_length=300)
	TxtFoncier= models.CharField(max_length=300)
	OutilGesFoncier = models.CharField(max_length=300)
	TypeConflit = models.CharField(max_length=300)
	TypeUsage= models.CharField(max_length=300)
	ExistCadrConcert = models.CharField(max_length=300)
	EchelCadrConcert = models.CharField(max_length=300)
	Entrepris_Indust_IncidFonc = models.CharField(max_length=300)
 
 
 
def __str__(self):
    
    return str(self.TypeFoncier)
 
 
 
 
class DimFoncierGouvernanc(models.Model):
    
    
    LoiReglement = models.CharField(max_length=300)
    OutilSecuriseFoncie= models.CharField(max_length=300)
    ActFoncier = models.CharField(max_length=300)
    DegreConnaissanc = models.CharField(max_length=300)
    NivComprehension = models.CharField(max_length=300)
    Resume = models.CharField(max_length=300)
    AtelierBonInformat = models.CharField(max_length=300)
    SecuritAjout = models.CharField(max_length=300)
    ActImplique = models.CharField(max_length=300)
    CauseAvance = models.CharField(max_length=300)
    SolutionPropose = models.CharField(max_length=300)
    SolutionRetenu = models.CharField(max_length=300)
    VerificatProcedur = models.CharField(max_length=300)
    ControlPermanant = models.CharField(max_length=300)

    def __str__(self):
       return str(self.LoiReglement)
    

    
class DimGeographie(models.Model):
    
	codeCommune = models.IntegerField()
	nomCommune =models.CharField(max_length=300)
	CodeIndicateur = models.IntegerField()
	Indicateur =models.CharField(max_length=300)
	CodeDomaine = models.IntegerField()
	NomDomaine =models.CharField(max_length=300)
    
def __str__(self):
        
        return str(self.codeCommune)
 
     
 

 



class DimTemps(models.Model):
	
	Date =models.DateField()
	Jour =models.CharField(max_length=300)
	AnneeCode = models.IntegerField()
	AnneeDate =models.DateField()
	AnneeNom =models.CharField(max_length=300)
	SemestreCode = models.IntegerField()
	SemestreDate =models.DateField()
	SemestreNom =models.CharField(max_length=300)
	TrimestreCode = models.IntegerField()
	TrimestreDate =models.DateField()
	TrimestreNom =models.CharField(max_length=300)
	MoisCode = models.IntegerField()
	MoisDate =models.DateField()
	MoisNom =models.CharField(max_length=300)
	SemaineCode = models.IntegerField()
	SemaineDate =models.DateField()
	SemaineNom =models.CharField(max_length=300)
	JourDelannée = models.IntegerField()
	JourDelannéeNom =models.CharField(max_length=300)
	JourDuSemestre = models.IntegerField()
	JourDuSemestreNom =models.CharField(max_length=300),
	JourDuTrimestre = models.IntegerField()
	JourDuTrimestreNom =models.CharField(max_length=300)
	JourDuMois = models.IntegerField()
	JourDuMoisNom =models.CharField(max_length=300)
	JourDeLaSemaine = models.IntegerField(),
	JourDeLaSemaineNom =models.CharField(max_length=300),
	SemaineDelannée = models.IntegerField()
	SemaineDelannéeNom =models.CharField(max_length=300),
	MoisDelannée = models.IntegerField()
	MoisDelannéeNom =models.CharField(max_length=300)
	MoisDuSemestre = models.IntegerField(),
	MoisDuSemestreNom =models.CharField(max_length=300)
	MoisDuTrimestre = models.IntegerField()
	MoisDuTrimestreNom =models.CharField(max_length=300)
	TrimestreDelannée = models.IntegerField()
	TrimestreDelannéeNom =models.CharField(max_length=300),
	TrimestreDuSemestre = models.IntegerField(),
	TrimestreDuSemestreNom =models.CharField(max_length=300)
	SemestreDelannée = models.IntegerField()
	SemestreDelannéeNom =models.CharField(max_length=300)
	Annee =models.CharField(max_length=300)
 
def __str__(self):
    return str(self.date)

class FactFoncier(models.Model):
    
	DateDomainFoncier_FK =models.DateField()
	IdFoncier_FK = models.ForeignKey(DimFoncier,on_delete=models.CASCADE)
	IdGouvFoncier_FK = models.ForeignKey(DimFoncierGouvernanc,on_delete=models.CASCADE)
	NreConflitAnnComm = models.IntegerField()
	NbreIndustri_FoncComm =models.IntegerField()
	SuperfiAlloueIndustri =models.IntegerField()
	NbreIndustri_FoncCommMoy= models.IntegerField()
	SupTypeFoncier =models.IntegerField()
	ConfliFoncieEnregMois =models.IntegerField
	SuperficConced =models.IntegerField()
	SuperficExploite = models.IntegerField()
	Superfic_Deja_Exploite =models.IntegerField()