from django.test import TestCase
from django.urls import reverse
from instructor.models import Instructor
from school.models import Matiere, Classe, Niveau
from django.contrib.auth.models import User


class AddCourseTest(TestCase):
    def setUp(self):
        self.niveau = Niveau.objects.create(nom="Niveau 1")
        self.classe = Classe.objects.create(niveau=self.niveau, numeroClasse=1)
        self.user = User.objects.create_user(username="instructor", password="password")
        self.instructor = Instructor.objects.create(user=self.user, classe=self.classe)
        self.matiere = Matiere.objects.create(nom="Mathématiques", instructor=self.user)

    def test_add_course(self):
        self.client.login(username="instructor", password="password")
        response = self.client.post(
            reverse("post_cours"),
            {
                "title": "Introduction aux fractions",
                "matiere": self.matiere.id,
                "classe": self.classe.id,
                "description": "Cours sur les fractions",
                "duration": 5,
                "date_debut": "2024-01-01",
                "date_fin": "2024-01-31",
            },
        )
        self.assertEqual(response.status_code, 200)