from django.urls import path
from django.contrib import admin

from taches import views
from taches.views import liste_taches

urlpatterns = [
    path("", views.liste_taches, name = "liste_taches"),
   
]