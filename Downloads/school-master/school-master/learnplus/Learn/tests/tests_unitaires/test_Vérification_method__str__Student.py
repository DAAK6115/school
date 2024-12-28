from django.test import TestCase
from django.contrib.auth.models import User
from student.models import Student


class StudentStrTest(TestCase):
    def test_student_str(self):
        user = User.objects.create_user(username="test_student")
        student = Student.objects.create(user=user)
        self.assertEqual(str(student), "test_student")
