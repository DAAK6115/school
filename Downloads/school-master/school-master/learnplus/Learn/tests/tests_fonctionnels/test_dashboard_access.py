from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from instructor.models import Instructor


class DashboardViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="instructor", password="password")
        self.instructor = Instructor.objects.create(
            user=self.user, contact="0123456789"
        )

    def test_dashboard_access(self):
        self.client.login(username="instructor", password="password")
        response = self.client.get(reverse("instructor-dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/instructor-dashboard.html")
