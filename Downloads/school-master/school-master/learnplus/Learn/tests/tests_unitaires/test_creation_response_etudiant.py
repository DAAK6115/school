from django.test import TestCase
from django.contrib.auth.models import User
from student.models import Student, StudentReponse


class StudentReponseModelTest(TestCase):
    def test_student_reponse_creation(self):
        user = User.objects.create_user(username="student")
        student = Student.objects.create(user=user)
        reponse = StudentReponse.objects.create(
            student=student, question="What is Django?", answer="A framework"
        )
        self.assertEqual(reponse.question, "What is Django?")
        self.assertEqual(reponse.answer, "A framework")
