from instructor.models import ForumQuestion
from django.test import TestCase
from django.contrib.auth.models import User


class ForumQuestionModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="instructor", password="password")
        self.question = ForumQuestion.objects.create(
            title="Comment enseigner Vue.js ?",
            details="Quelles sont les meilleures pratiques pour enseigner Vue.js "
            "à des débutants ?",
            topic="Vue.js",
            user=self.user,
        )

    def test_forum_question_creation(self):
        self.assertEqual(str(self.question), "Comment enseigner Vue.js ?")
        self.assertEqual(self.question.user, self.user)
