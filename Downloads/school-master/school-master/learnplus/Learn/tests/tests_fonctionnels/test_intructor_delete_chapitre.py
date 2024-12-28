from django.test import Client
from django.test import TestCase
from django.contrib.auth.models import User
from school.models import Matiere
from school.models import Niveau, Classe, Chapitre
from django.urls import reverse


class DeleteChapitreTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="instructor", password="password")
        self.client = Client()
        self.client.login(username="instructor", password="password")
        self.niveau = Niveau.objects.create(nom="Niveau 1")
        self.classe = Classe.objects.create(niveau=self.niveau, numeroClasse=1)
        self.matiere = Matiere.objects.create(nom="Maths")
        self.chapitre = Chapitre.objects.create(
            titre="Chapitre 1",
            description="Introduction",
            matiere=self.matiere,
            classe=self.classe,
        )

    def test_delete_chapitre(self):
        response = self.client.post(
            reverse("delete_chapitre"), {"id": self.chapitre.id}
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Chapitre.objects.filter(id=self.chapitre.id).exists())
