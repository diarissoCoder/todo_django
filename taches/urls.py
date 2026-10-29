from django.urls import path
from . import views
from .views import *

app_name = "taches"

urlpatterns = [
    path("", views.liste_taches, name = "liste_taches"),
    path("ajouter/", views.ajouter_tache, name= "ajouter_tache"),
    path("<int:pk>/modifier/", views.modifier_tache, name ="modifier_tache"),
   
]