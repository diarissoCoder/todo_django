from django.urls import path
from . import views


app_name = "taches"

urlpatterns = [
    path("", views.liste_taches, name = "liste_taches"),
    path("ajouter/", views.ajouter_tache, name= "ajouter_tache"),
    path("<int:pk>/modifier/", views.modifier_tache, name ="modifier_tache"),
    path("<int:pk>/supprimer/", views.supprimer_tache, name="supprimer_tache"),
     path("<int:pk>/terminer/", views.terminer_tache, name="terminer_tache"),
   
]