from django.test import TestCase
from django.urls import reverse
from .models import Tache

# Create your tests here.
# Test pour le Model 
class TacheModelTest(TestCase):
    
    def test_str_tache(self):
        tache = Tache.objects.create(nom = "karma")
        self.assertEqual(str(tache), "karma")

    def test_status_tache(self):
        tache = Tache.objects.create(nom = "karma")
        self.assertEqual(tache.status, "à faire")
        
      

class TacheListTest(TestCase):
   # Tester la liste des taches
    def test_liste_tache(self):
        tache_1 = Tache.objects.create(nom="devoir")
        response = self.client.get(reverse("taches:liste_taches"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "devoir")
        pass

class TacheFunctionTest(TestCase):
    
    def test_ajout_tache_valide(self):
        url = reverse("taches:ajouter_tache")
        donnees = {"nom": "test_tache", "status": "en cours"}

        response = self.client.post(url, donnees)

        self.assertRedirects(response, reverse("taches:liste_taches"))
        self.assertEqual(Tache.objects.count(), 1)
        self.assertEqual(Tache.objects.first().nom, "test_tache")


    def test_ajout_tache_nom_vide(self):
        url = reverse("taches:ajouter_tache")

        response = self.client.post(url, {"nom": "", "status": "en cours"})

        self.assertEqual(response.status_code, 200)   # page réaffichée, pas de redirection
        self.assertEqual(Tache.objects.count(), 0)    # rien n'a été créé


   

class TacheSupprimerTest(TestCase):
    def test_post_supprime_la_tache(self):
        # Attendu : POST -> tâche supprimée, redirection vers la liste
        tache = Tache.objects.create(nom="tache1", status="en cours")
        url = reverse("taches:supprimer_tache", args=[tache.pk])

        response = self.client.post(url)

        self.assertRedirects(response, reverse("taches:liste_taches"))
        self.assertEqual(Tache.objects.count(), 0)

    def test_get_supprimer_affiche_confirmation(self):
        # Attendu : GET -> page de confirmation
        tache = Tache.objects.create(nom="tache1", status="en cours")
        url = reverse("taches:supprimer_tache", args=[tache.pk])

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, tache.nom)
        

    def test_supprimer_tache_inexistante_404(self):
       
        url = reverse("taches:supprimer_tache", args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


      
class TacheTerminerTest(TestCase):
    def test_post_terminer_tache(self):
        tache = Tache.objects.create(nom="tache1", status="en cours")
        url = reverse("taches:terminer_tache", args=[tache.pk])

        response = self.client.post(url)

        tache.refresh_from_db()
        self.assertEqual(tache.status, "termine")
        self.assertRedirects(response, reverse("taches:liste_taches"))

    def test_get_terminer_refuse(self):
        tache = Tache.objects.create(nom="tache1", status="en cours")
        url = reverse("taches:terminer_tache", args=[tache.pk])

        response = self.client.get(url)
        tache.refresh_from_db()

        self.assertEqual(response.status_code, 405)
        self.assertEqual(tache.status, "en cours")   # rien n'a changé
        

    def test_bouton_terminer_disponible_pour_tache_en_cours(self):
        tache = Tache.objects.create(nom="tache1", status="en cours")
        url = reverse("taches:liste_taches")

        response = self.client.get(url)

        self.assertContains(response, reverse("taches:terminer_tache", args=[tache.pk]))


    def test_bouton_terminer_non_disponible_pour_tache_terminee(self):
        tache = Tache.objects.create(nom="tache1", status="termine")
        url = reverse("taches:liste_taches")

        response = self.client.get(url)

        self.assertNotContains(response, reverse("taches:terminer_tache", args=[tache.pk]))