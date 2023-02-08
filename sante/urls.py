
from django.urls import path

from sante import views





app_name ='sante'


urlpatterns = [
    path('PlanificationFamiliale/',views.pltfm,name='PlanificationFamiliale'),
   # path('ReproductionEtJeune/',views.repjeu,name='ReproductionEtJeune'),
   ## path('SanteAlimentationEtNutrition/',views.sant,name='SanteAlimentationEtNutrition'),
    ###path('SantePaludisme/',views.spld,name='SantePaludisme'),
    #path('dimagroog/',views.dimagroorg_form,name='dimagroorg'),
    path('updatepl/<int:id>/',views.update_P,name='updatepl'),
    path('deletepl/<int:id>/',views.delete_P,name='deletepl'),

]