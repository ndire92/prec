from django.contrib import admin

from peche.models import DimPecheArtisan,DimPecheAssure,DimPecheCommerce,DimPecheFinance

# Register your models here.
admin.site.register(DimPecheArtisan)
admin.site.register(DimPecheAssure)
admin.site.register(DimPecheCommerce)
admin.site.register(DimPecheFinance)