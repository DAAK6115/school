from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from school.models import Niveau, Classe
from forum.models import Sujet
from student.models import Student


class PostResponseViewTest(TestCase):
    def setUp(self):
        self.niveau = Niveau.objects.create(nom="Niveau 1")
        self.classe = Classe.objects.create(niveau=self.niveau, numeroClasse=1)
        self.user = User.objects.create_user(username="student", password="password")
        self.student = Student.objects.create(
            user=self.user, classe=self.classe, photo=None
        )
        self.sujet = Sujet.objects.create(
            titre="Sujet Test", question="Question Test", user=self.user
        )
        self.client.login(username="student", password="password")

    def test_post_response(self):
        response = self.client.post(
            reverse("forum-thread", args=[self.sujet.id]), {"response": "Réponse Test"}
        )
        self.assertEqual(response.status_code, 302)
