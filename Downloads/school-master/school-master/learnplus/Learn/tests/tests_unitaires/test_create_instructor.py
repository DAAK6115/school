from django.test import TestCase
from instructor.models import Instructor
from django.contrib.auth.models import User
from school.models import Classe, Niveau


class InstructorModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="instructor", password="password")
        self.niveau = Niveau.objects.create(nom="Niveau 1")
        self.classe = Classe.objects.create(niveau=self.niveau, numeroClasse=1)
        self.instructor = Instructor.objects.create(
            user=self.user,
            contact="0123456789",
            adresse="123 Rue des Instructeurs",
            classe=self.classe,
            photo="default.jpg",
            bio="Professeur passionné",
        )

    def test_instructor_creation(self):
        self.assertEqual(str(self.instructor), self.user.username)
        self.assertEqual(self.instructor.classe, self.classe)
        self.assertEqual(self.instructor.contact, "0123456789")
