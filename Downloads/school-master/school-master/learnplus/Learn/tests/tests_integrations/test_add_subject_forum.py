from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class PostForumViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="student", password="password")
        self.client.login(username="student", password="password")

    def test_post_forum_success(self):
        response = self.client.post(
            reverse("post_forum"),
            {"titre": "Test Forum", "question": "What is Python?"},
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["success"])
        self.assertEqual(data["message"], "Votre sujet a bien été ajouté!")
        # Vérifie que le slug contient le titre
        self.assertIn("test-forum", data["forum"])
