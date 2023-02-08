from django.db import models

# Create your models here.
class DimPecheArtisan(models.Model):
    ActPech_Artisan = models.CharField(max_length=250)
    GroupPecheur = models.CharField(max_length=250)
    GroupMareyeur = models.CharField(max_length=250)
    TypePirogu = models.CharField(max_length=250)
    TypProdPechPirogBois = models.CharField(max_length=250)

    def __str__(self):
        return self.ActPech_Artisan

class DimPecheAssure(models.Model):
    TypeAssurancPech = models.CharField(max_length=25)
    BesoinFormatPech = models.CharField(max_length=250)
    ActeurSensibilisePech = models.CharField(max_length=250)
    ActeurFormatPech = models.CharField(max_length=250)
    BesoinSensibilisePech = models.CharField(max_length=250)

    def __str__(self):

        return self.TypeAssurancPech


class DimPecheCommerce(models.Model):
    ProdVendType = models.IntegerField()
    ProdVendCampgnInterSais = models.IntegerField()
    ProdVendCampSaisFroid = models.IntegerField()
    ProdVendCampPrintem = models.IntegerField()
    Type_VentPech= models.CharField(max_length=250)


    def __str__(self):
        return str(self.ProdVendType)



class DimPecheFinance(models.Model):
    OffrServicFinancPech=models.CharField(max_length=25)
    DemandApportPech = models.IntegerField()
    TypGaranExige = models.CharField(max_length=250)
    ActeurFormatPech = models.CharField(max_length=250)


    def __str__(self):
        return self.OffrServicFinancPech





