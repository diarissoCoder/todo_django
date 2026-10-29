from django.test import TestCase
from django.urls import reverse
from .models import Tache

# Create your tests here.
# Test pour le Model 
class TacheModelTest(TestCase):
    def test_str_tache(self):
        tache = Tache.objects.create(nom = "karma")
        self.assertEqual(str(tache), "karma")
        self.assertEqual(tache.status,"en cours")
      

class TacheListTest(TestCase):
   # Tester la liste des taches
    def test_liste_tache(self):
        tache_1 = Tache.objects.create(nom="devoir")
        response = self.client.get(reverse("taches:liste_taches"))
        self.assertTrue(response.status_code, 200)
        self.assertContains(response, "devoir")
