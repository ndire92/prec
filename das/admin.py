from django.contrib import admin
from das.models import DimAgroAssurance, DimAgroCulture, DimAgroFinance, DimAgroOrganisation, DimAgroProduction,  FactAgriculture

# Register your models here.
admin.site.register(DimAgroAssurance)

admin.site.register(DimAgroProduction)
admin.site.register(DimAgroOrganisation)
admin.site.register(DimAgroFinance)
admin.site.register(DimAgroCulture)
admin.site.register(FactAgriculture)