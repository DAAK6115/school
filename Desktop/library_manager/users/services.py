from users.models import User

class UserService:
    def __init__(self):
        self.users = []

    def add_user(self, user: User):
        self.users.append(user)

    def get_users(self):
        return self.users
