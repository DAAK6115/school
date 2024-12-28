from forum.models import Sujet, Reponse
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class ForumThreadReplyTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="instructor", password="password")
        self.forum = Sujet.objects.create(
            titre="Sujet Test", question="Question ?", user=self.user
        )

    def test_forum_reply(self):
        self.client.login(username="instructor", password="password")
        response = self.client.post(
            reverse("forum-thread-reply", args=[self.forum.slug]),
            {"comment": "Ceci est une réponse."},
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Reponse.objects.filter(sujet=self.forum).exists())
