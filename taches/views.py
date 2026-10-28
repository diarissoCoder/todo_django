from django.shortcuts import render

from taches.models import Tache

# Create your views here.
def liste_taches(request):
    liste = Tache.objects.all()
    return render(request,'taches/liste.html',{"liste" : liste})