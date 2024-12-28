from django.test import TestCase
from django.urls import reverse
from instructor.models import Instructor
from school.models import Classe, Niveau
from django.contrib.auth.models import User


class PrivateChatTest(TestCase):
    def setUp(self):
        self.niveau = Niveau.objects.create(nom="Niveau 1")
        self.classe = Classe.objects.create(niveau=self.niveau, numeroClasse=1)
        self.user = User.objects.create_user(username="instructor", password="password")
        self.instructor = Instructor.objects.create(user=self.user, classe=self.classe)

    def test_private_chat_view(self):
        self.client.login(username="instructor", password="password")
        response = self.client.get(
            reverse("instructor-messages", args=[self.classe.id])
        )
        self.assertEqual(response.status_code, 200)
