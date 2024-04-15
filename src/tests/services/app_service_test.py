import unittest
from entities.workout import Workout
from entities.user import User
from services.app_service import AppService

class WorkoutRepositoryForTesting:
    def __init__(self, workouts=None):
        self.workouts = workouts or []

    def create_workout(self, workout):
        self.workouts.append(workout)

        return workout

    def list_all_workouts(self):
        return self.workouts

    def delete_all_workouts(self):
        self.workouts = []

class UserRepositoryForTesting:
    def __init__(self, users=None):
        self.users = users or []

    def find_all_users(self):
        return self.users

    def create_user(self, user):
        self.users.append(user)
        return user

    def delete_all_users(self):
        self.users = []

    def find_one_user(self, username):
        users = self.users
        if len(users) > 0:
            for user in users:
                if user.username == username:
                    return user
        else:
            return None

class TestAppService(unittest.TestCase):
    def setUp(self):
        self.app_service = AppService(WorkoutRepositoryForTesting(), UserRepositoryForTesting())

        self.workout_running = Workout("hupu", "running")
        self.workout_gym = Workout("hupu", "gym")
        self.user_hupu = User("hupu", "123")

    def login_user(self, user):
        self.app_service.create_user(user.username, user.password)

    def test_create_workout(self):
        self.login_user(self.user_hupu)

        self.app_service.create_workout(self.workout_running)
        workouts = self.app_service.list_all_workouts()

        self.assertEqual(len(workouts), 1)
        self.assertEqual(workouts[0].content, "running")
        self.assertEqual(woekouts[0].user.username, self.user_hupu.username)

    def test_login(self):
        self.app_service.create_user(self.user_hupu.username, self.user_hupu.password)

        user = self.app_service.login(self.user_hupu.username, self.user_hupu.password)

        self.assertEqual(user.username, self.user_hupu.username)
