from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from school.models import Niveau, Classe, Matiere, Chapitre
from student.models import Student


class QuizResultsViewTest(TestCase):
    def setUp(self):
        self.niveau = Niveau.objects.create(nom="Niveau 1")
        self.classe = Classe.objects.create(niveau=self.niveau, numeroClasse=1)
        self.user = User.objects.create_user(username="student", password="password")
        self.student = Student.objects.create(
            user=self.user, classe=self.classe, photo="default.jpg"
        )
        self.matiere = Matiere.objects.create(nom="Maths", instructor=self.user)
        self.chapitre = Chapitre.objects.create(
            classe=self.classe,
            matiere=self.matiere,
            titre="Chapitre 1",
            description="Description",
        )
        self.client.login(username="student", password="password")

    def test_quiz_results_view(self):
        response = self.client.get(reverse("quiz-results"))
        self.assertEqual(response.status_code, 200)
