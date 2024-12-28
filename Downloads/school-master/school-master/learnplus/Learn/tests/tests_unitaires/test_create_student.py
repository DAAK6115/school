from django.test import TestCase
from django.contrib.auth.models import User
from school.models import Niveau, Classe
from student.models import Student


class StudentModelTest(TestCase):
    def setUp(self):
        self.niveau = Niveau.objects.create(nom="Niveau 1")
        self.classe = Classe.objects.create(niveau=self.niveau, numeroClasse=1)

    def test_student_creation(self):
        user = User.objects.create_user(username="test_student", password="password")
        student = Student.objects.create(user=user, classe=self.classe, photo=None)
        self.assertEqual(student.user.username, "test_student")
        self.assertEqual(student.classe.numeroClasse, 1)
