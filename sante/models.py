from django.db import models


class PlanificationFamiliale(models.Model):
    CodeDistrict =models.IntegerField()
    CodeDomaine =models.IntegerField()
    CodeTemps =models.IntegerField()
    TauxdeRecrutementPF =models.IntegerField()
    TauxdAbandonPF =models.IntegerField()

    def __str__(self):

        return str(self.CodeDistrict)


