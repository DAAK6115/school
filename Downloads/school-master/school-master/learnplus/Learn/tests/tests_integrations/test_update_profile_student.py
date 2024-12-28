from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from student.models import Student


class UpdateProfilTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="student",
            password="password",
            email="oldemail@test.com"
        )
        self.student = Student.objects.create(user=self.user, bio="Old Bio")
        self.client.login(username="student", password="password")

    def test_update_profil(self):
        response = self.client.post(
            reverse("update_profil"),
            {
                "nom": "NewLastName",
                "prenom": "NewFirstName",
                "email": "newemail@test.com",
                "bio": "New Bio",
            },
        )
        # Vérification du statut de la réponse
        self.assertEqual(response.status_code, 200)

        # Rechargez les données depuis la base pour vérifier les mises à jour
        self.user.refresh_from_db()
        self.student.refresh_from_db()

        # Vérifiez que les données ont été mises à jour
        self.assertEqual(self.user.last_name, "NewLastName")
        self.assertEqual(self.user.first_name, "NewFirstName")
        self.assertEqual(self.user.email, "newemail@test.com")
        self.assertEqual(self.student.bio, "New Bio")
