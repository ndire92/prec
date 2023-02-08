
from django.urls import path

from peche import views



app_name ='peche'


urlpatterns = [
    path('dimpecart/',views.pec_art,name='dimpecart'),
    path('dimpecass/',views.pech_assu,name='dimpecass'),
    path('dimpecec/',views.pech_ec,name='dimpecec'),
    path('dimpecfin/',views.pech_fin,name='dimpecfin'),
    path('up_ar<int:id>/',views.update_ar,name='up_ar'),
    path('de_ar<int:id>/',views.delete_ar,name='de_ar'),
    path('up_ass<int:id>/',views.update_ass,name='up_ass'),
    path('de_ass<int:id>/',views.delete_ass,name='de_ass'),
    path('up_fin<int:id>/',views.update_fin,name='up_fin'),
    path('de_fin<int:id>/',views.delete_fin,name='de_fin'),
    path('up_com<int:id>/',views.update_com,name='up_com'),
    path('de_com<int:id>/',views.delete_com,name='de_com'),
    #ath('dimagroog/',views.dimagroorg_form,name='dimagroorg'),

]