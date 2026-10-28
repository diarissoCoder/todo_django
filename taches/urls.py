from django.urls import path
from . import views


app_name = "taches"

urlpatterns = [
    path("", views.liste_taches, name = "liste_taches"),
    path("ajouter/", views.ajouter_taches, name= "ajouter_taches"),
   
]