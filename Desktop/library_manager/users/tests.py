import unittest
from users.models import User
from users.services import UserService

class TestUserService(unittest.TestCase):
    def test_add_user(self):
        user_service = UserService()
        user = User("johndoe", "john@example.com")
        user_service.add_user(user)
        self.assertIn(user, user_service.get_users())
