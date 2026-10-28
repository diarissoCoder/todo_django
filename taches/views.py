from webbrowser import get


from django.shortcuts import render, redirect
from .forms import TacheForm
from taches.models import Tache

# Create your views here.
def liste_taches(request):
    taches = Tache.objects.all()
    return render(request,'taches/liste.html',{"liste" : taches})


def ajouter_taches(request):
    if request.method == "POST":
       form = TacheForm(request.POST)
       if form.is_valid():
          form.save()
          return redirect("taches:liste_taches")
    else:
        form = TacheForm()
    
    return render(request, 'taches/ajouter.html', {"form" : form})
           
          
    
       