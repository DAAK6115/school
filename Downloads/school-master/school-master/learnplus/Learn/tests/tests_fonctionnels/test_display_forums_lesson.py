from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from school.models import Niveau, Classe, Chapitre, Matiere, Cours
from student.models import Student


class ForumLessonViewTest(TestCase):
    def setUp(self):
        self.niveau = Niveau.objects.create(nom="Niveau 1")
        self.classe = Classe.objects.create(niveau=self.niveau, numeroClasse=1)
        self.matiere = Matiere.objects.create(nom="Maths")
        self.user = User.objects.create_user(username="student", password="password")
        self.student = Student.objects.create(
            user=self.user, classe=self.classe, photo="default.jpg"
        )
        self.chapitre = Chapitre.objects.create(
            classe=self.classe,
            matiere=self.matiere,
            titre="Chapitre 1",
            description="Description",
        )
        self.cours = Cours.objects.create(
            titre="Cours 1", chapitre=self.chapitre, description="Description"
        )
        self.client.login(username="student", password="password")

    def test_forum_lesson_view(self):
        response = self.client.get(reverse("forum-lesson", args=[self.cours.slug]))
        self.assertEqual(response.status_code, 200)
