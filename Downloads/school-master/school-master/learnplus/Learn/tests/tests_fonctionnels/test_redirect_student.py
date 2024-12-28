from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from school.models import Niveau, Classe
from student.models import Student


class IndexViewTest(TestCase):
    def setUp(self):
        self.niveau = Niveau.objects.create(nom="Niveau 1")
        self.classe = Classe.objects.create(niveau=self.niveau, numeroClasse=1)
        self.user = User.objects.create_user(username="student", password="password")
        self.student = Student.objects.create(
            user=self.user, classe=self.classe, photo="default.jpg"
        )
        self.client.login(username="student", password="password")

    def test_index_view_for_student(self):
        response = self.client.get(reverse("index_student"))
        self.assertEqual(response.status_code, 200)
