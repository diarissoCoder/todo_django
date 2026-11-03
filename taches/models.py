
from django.db import models
from django.db.models.fields import DateTimeField

# Create your models here.'
class Tache(models.Model):
    nom = models.CharField(max_length=100)
    date_creation = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[ ("à faire","A faire"), ("en cours", "En cours"),  ("termine", "Termine")], default="à faire")
    description = models.TextField(max_length = 100, blank=True)

    def __str__(self):
        return self.nom

