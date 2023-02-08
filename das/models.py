from django.db import models

# Create your models here.
class DimAgroAssurance(models.Model):
    OffreuAssurance = models.CharField(max_length=300)
    TypeAssurance = models.CharField(max_length=300)
    CulturAssure = models.CharField(max_length=300)
    NivPrime = models.CharField(max_length=300)




    def __str__(self):
        return self.OffreuAssurance

class DimAgroCulture (models.Model):
    ZonProd_Cult = models.CharField(max_length=300)
    Cultur_Pratique = models.CharField(max_length=300)
    Type_Semence = models.CharField(max_length=300)
    CodeVarietesCultiv = models.IntegerField()
    VarieteCultive = models.CharField(max_length=300)
    Appro_Intrant_mat = models.CharField(max_length=300)
    SourcApprovisIntran = models.CharField(max_length=300)
    SourcApprovisSemenc = models.CharField(max_length=300)
    SourcApprovisEngrProdPhyto = models.CharField(max_length=300)
    SourcApprovisMatAgro = models.CharField(max_length=300)
    TypeAcquisIntran = models.CharField(max_length=300)
    TypeAcquisMat = models.CharField(max_length=300)
    TypeFertilisUtil = models.CharField(max_length=300)
    TypePesticidUtil = models.CharField(max_length=300)
    ModAcquisParcel = models.CharField(max_length=300)




    def __str__(self):

        return self.ZonProd_Cult


class DimAgroFinance(models.Model):
    OffreServicFinance = models.CharField(max_length=300)
    DemandApport=  models.IntegerField()
    TypeGaranExige = models.CharField(max_length=300)
    LongProcedCredi=  models.IntegerField()
    DelaiRembourse = models.IntegerField()

    def __str__(self):
        return self.OffreServicFinance



class DimAgroOrganisation(models.Model):
    name_Organisation = models.CharField(max_length=300)
    TypeServicOfferOP = models.CharField(max_length=300)
    BesoinForm = models.CharField(max_length=300)
    ContrainGlobalAgro= models.CharField(max_length=300)
    ContrainMajFilier = models.CharField(max_length=300)
    InfrasStockCondition = models.CharField(max_length=300)
    FournisEmballag = models.CharField(max_length=300)

    def __str__(self):
        return self.name_Organisation





class DimAgroProduction(models.Model):

    name_Production = models.CharField(max_length=300)
    ProdCultHiver = models.CharField(max_length=300)
    TypeSolExist= models.CharField(max_length=300)
    TypeDegradZonCultur = models.CharField(max_length=300)
    CauseDegrad = models.CharField(max_length=300)

    def __str__(self):
        return self.name_Production


class FactAgriculture(models.Model):
    date = models.DateField()
    idproduction_fk = models.CharField(max_length=300) # Field name made lowercase.
    idorganisation_fk = models.ForeignKey(DimAgroOrganisation,on_delete=models.CASCADE)  # Field name made lowercase.
    idagrofinance_fk = models.ForeignKey(DimAgroFinance,on_delete=models.CASCADE)  # Field name made lowercase.
    idculture_fk = models.ForeignKey(DimAgroCulture,on_delete=models.CASCADE)  # Field name made lowercase.
    #numagrocommercial_fk = models.ForeignKey(dimAgroCommercial,on_delete=models.CASCADE)  # Field name made lowercase.
    idagroassurance_fk = models.ForeignKey(DimAgroAssurance,on_delete=models.CASCADE)  # Field name made lowercase.

    def __str__(self):
        return str(self.date)

