import unittest
from repositories.user_repository import user_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all_users()
        self.user_tupu = User("tupu", "abc")
        self.user_hupu = User("hupu", "123")

    def test_create_user(self):
        user_repository.create_user(self.user_tupu)
        users = user_repository.find_all_users()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, self.user_tupu.username)

    def test_delete_all(self):
        user_repository.create_user(self.user_hupu)
        users = user_repository.find_all_users()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, self.user_hupu.username)

        user_repository.delete_all_users()
        users = user_repository.find_all_users()

        self.assertEqual(len(users), 0)

    def test_find_all_users(self):
        user_repository.create_user(self.user_hupu)
        user_repository.create_user(self.user_tupu)

        users = user_repository.find_all_users()

        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].username, self.user_hupu.username)
        self.assertEqual(users[1].username, self.user_tupu.username)

    def test_find_one_user(self):
        user = user_repository.find_one_user(self.user_hupu.username)

        self.assertEqual(user, None)

        user_repository.create_user(self.user_hupu)

        user = user_repository.find_one_user(self.user_hupu.username)

        self.assertEqual(user.username, self.user_hupu.username)
        self.assertEqual(user.password, self.user_hupu.password)
