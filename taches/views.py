from django.shortcuts import get_object_or_404, render, redirect
from .forms import TacheForm
from taches.models import Tache

# Create your views here.
def liste_taches(request):
    taches = Tache.objects.all()
    return render(request,'taches/liste.html',{"liste" : taches})


def ajouter_tache(request):
    if request.method == "POST":
       form = TacheForm(request.POST)
       if form.is_valid():
          form.save()
          return redirect("taches:liste_taches")
    else:
        form = TacheForm()
    
    return render(request, 'taches/ajouter.html', {"form" : form})
           

def modifier_tache(request, pk):
    tache = get_object_or_404(Tache, pk=pk)
    if request.method == "POST":
        form = TacheForm(request.POST, instance=tache) 
        if form.is_valid():
            form.save()
            return redirect("taches:liste_taches")
    else:
        form = TacheForm(instance=tache)

    return render(request, "taches/ajouter.html", {"form" : form})


def supprimer_tache(request, pk):   
    tache = get_object_or_404(Tache, pk=pk)
    if request.method == "POST":
        tache.delete()
        return redirect("taches:liste_taches") 
    
    return render(request, "taches/confirmer_suppression.html", {"tache" : tache})


    
       