from django.db import models



class DimEduc_Equipements(models.Model):
    NbrePlaceAssisPresco = models.IntegerField()
    NbreElevePresco = models.IntegerField()
    NbreEnfantBeneficieDeparasitage = models.IntegerField()
    NbreEnfantPresco= models.IntegerField()
    NbreStructureElementaireDisposantCantinesScolaires= models.IntegerField()



    def __str__(self):
        return self.NbrePlaceAssisPresco

class DimEduc_Gouvernance(models.Model):
    BudgetalloueEtatEcolePrimaire = models.IntegerField()
    BudgetalloueEtatEcoleSecondaire = models.IntegerField()
    BudgetalloueEtatEcoleLycee = models.IntegerField()
    BudgetCTalloueEducation= models.IntegerField()




    def __str__(self):
        return self.BudgetalloueEtatEcoleSecondaire



class DimEduc_Perfomance(models.Model):
    NbrePassants_NiveauEtude = models.IntegerField()
    NbreRedoublement_NiveauEtude = models.IntegerField()
    NbreAbandon_NiveauEtude = models.IntegerField()
    NbrePassants_SatutEtablissement= models.IntegerField()
    NbreRedoublement_StatutEtablissemen= models.IntegerField()


    def __str__(self):
        return self.NbrePassants_NiveauEtude



class DimEduc_Personnel(models.Model):
    EnsPrescolairePubli = models.IntegerField()
    EnsPrescolairePrive = models.IntegerField()
    EnsPrescolaireCommunautaire = models.IntegerField()
    EnseignantPrescoparStatut= models.IntegerField()
    ElevePrecolairePrive= models.IntegerField()



    def __str__(self):
        return self.EnsPrescolairePubli


class DimEduc_Access(models.Model):
    EnsGarcons3_5ans = models.IntegerField()
    EnsFilles3_5ans = models.IntegerField()
    EnsFilles_Garcons3_5ans = models.IntegerField()
    EffectifGarconsInscritPrescolaire= models.IntegerField()
    EffectifFillesnscritPrescolaire= models.IntegerField()
    EffectifTotalElevInscritPrescolaire= models.IntegerField()
    EffectifsPrescPetiteSection= models.IntegerField()
    EffectifPrescoMoyenneSection =models.IntegerField()
    EffectifPrescoGrandeSection= models.IntegerField()
    EffectifsPrescoTT= models.IntegerField()
    NbreGarcons_FillesPS= models.IntegerField()
    NbreGarcons_FillesMS= models.IntegerField()
    NbreGarcons_FillesGS= models.IntegerField()
    NreFillesPrescolaire= models.IntegerField()
    EffectifsTotalElvInscitPrescoPublic= models.IntegerField()
    EffectifsTotalElvInscitPrescoStuctureCommunautaires= models.IntegerField()
    EffectifsTotalElev= models.IntegerField()
    NbreStructurePrescolairePublic= models.IntegerField()
    NbreStructurePrescolairePrive= models.IntegerField()
    NbreStructuresPrescolaireCommunautaires= models.IntegerField()
    NbreDaaraModernes= models.IntegerField()
    NbreDaaraMises_Niveau= models.IntegerField()
    NbreEnfDansElementaire= models.IntegerField()
    NbreGarconsDansElementaire= models.IntegerField()
    NbreFillesDansElementaire= models.IntegerField()
    NbreElvInscritCIPremierFois= models.IntegerField()
    NbreElvQuittantEtablissementCommuneversEtablissemnetHorsCommune= models.IntegerField()
    NbreElvProvenanveEtablissemnetHorsCommune= models.IntegerField()
    NbreEcoleElementairePubliques= models.IntegerField()
    NbreEcoleElementairePrivees= models.IntegerField()
    EnsGarcons_12_15ans= models.IntegerField()
    EnsFilles_12_15ans= models.IntegerField()
    EnsFillesGarcons_12_15ans= models.IntegerField()
    NreElevesElementaire= models.IntegerField()
    NbreGarconsElementaire= models.IntegerField()
    NbreFillesElementaire= models.IntegerField()
    EnsGarcons_16_18ans= models.IntegerField()
    EnsFilles_16_18ans= models.IntegerField()
    EnsGarcons_Filles_16_18ans= models.IntegerField()
    NbreElvSecondaire= models.IntegerField()
    NbreGarconsSecondaire= models.IntegerField()
    NbreFillesSecondaire= models.IntegerField()
    NbreFilleMarieeCoursAnnee_Secondaire= models.IntegerField()
    NbreFillesEnceinteEnCoursAnnee_Secondaire= models.IntegerField()





    def __str__(self):
        return str(self.EnsGarcons3_5ans)



