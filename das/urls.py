
from django.urls import path

from das import views



app_name = 'das'


urlpatterns = [
    path('dimagr/',views.dimagr,name='dimagr'),
    path('dimagroassu/',views.agro_assu_form,name='dimagroassu'),
    path('dimagrocul/',views.dimagrocul_form,name='dimagrocul'),
    path('dimagrofin/',views.dimagrofin_form,name='dimagrofin'),
    path('dimagroog/',views.dimagroorg_form,name='dimagroorg'),
    path('dimagroprod/',views.dimagrprod_form,name='dimagroprod'),
   # path('dimagrovcul/',views.dimagrovcul_form,name='dimagrovcul'),
    path('update_ass/<int:id>/',views.update_a,name='update_ass'),
    path('delete/<int:id>/',views.delete_post,name='delete'),
    path('update_agcl/<int:id>/',views.update_c,name='update_agcl'),
    path('delete_clt/<int:id>/',views.delete_d,name='delete_clt'),
    path('update_fi/<int:id>/',views.update_f,name='update_fi'),
    path('delete_fi/<int:id>/',views.delete_f,name='delete_fi'),
    path('update_org/<int:id>/',views.update_or,name='update_org'),
    path('delete_org/<int:id>/',views.delete_or,name='delete_org'),
    path('update_pr/<int:id>/',views.update_prd,name='update_pr'),
    path('delete_pr/<int:id>/',views.delete_prd,name='delete_pr'),



]