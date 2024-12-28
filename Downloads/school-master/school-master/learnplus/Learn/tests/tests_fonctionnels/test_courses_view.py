from django.test import TestCase
from django.urls import reverse
from instructor.models import Instructor
from school.models import Matiere, Classe, Niveau
from django.contrib.auth.models import User


class CoursesViewTest(TestCase):
    def setUp(self):
        self.niveau = Niveau.objects.create(nom="Niveau 1")
        self.classe = Classe.objects.create(niveau=self.niveau, numeroClasse=1)
        self.matiere = Matiere.objects.create(nom="Maths")
        self.user = User.objects.create_user(username="instructor", password="password")
        self.instructor = Instructor.objects.create(user=self.user, classe=self.classe)

    def test_courses_view(self):
        self.client.login(username="instructor", password="password")
        response = self.client.get(reverse("instructor-courses"))
        self.assertEqual(response.status_code, 200)
