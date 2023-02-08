
from . import views
from django.urls import path
app_name = 'posts'


urlpatterns = [
path('',views.home,name="index"),
path('post/<int:id>/',views.detail,name="detail"),
path('post',views.all,name="all"),
path('new_post',views.new_post,name="new_post"),
path('update_post/<int:id>/',views.update_post,name="update_post"),
path('delete_post/<int:id>/',views.delete_post,name="delete_post"),
#path('search/',views.search,name='search')
path('commun/',views.commun,name="commun"),
#path('domaine/',views.domaine,name="domaine"),
#path('student/',views.student,name="student"),
#path('dash',views.dash,name="dash"),
#path('homee/',views.Homee,name="homee"),
path('peche/',views.peche,name="peche"),
path('foncier/',views.foncier,name="foncier"),
path('agriculture/',views.agriculture,name="agriculture"),
path('sante/',views.sante,name="sante"),
path('education/',views.education,name="education"),
path('tabview/',views.tabview,name="tabview"),
#path('Sli/',views.Sli,name="Slider")

]