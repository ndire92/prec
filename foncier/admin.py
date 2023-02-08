

# Register your models here.
from django.contrib import admin
from foncier.models import DimFoncier, DimFoncierGouvernanc, DimGeographie, DimTemps, FactFoncier
# Register your models here.

admin.site.register(DimFoncier)
admin.site.register(DimFoncierGouvernanc)
admin.site.register(DimGeographie)
admin.site.register(DimTemps)
admin.site.register(FactFoncier)
