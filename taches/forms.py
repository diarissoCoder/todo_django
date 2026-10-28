from django import forms

from taches.models import Tache


class TacheForm(forms.ModelForm):

    class Meta:
        model = Tache
        fields = ['nom', 'status','description']
       