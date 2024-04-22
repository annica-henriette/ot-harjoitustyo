import unittest
from entities.workout import Workout
from entities.user import User
from services.app_service import (
    AppService, InvalidLoginError, UsernameTakenError, InvalidDate, DuplicateWorkoutError)


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

    def list_all_user_workouts(self, user):
        return [workout for workout in self.workouts if workout.user == user]

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
        self.app_service = AppService(
            WorkoutRepositoryForTesting(), UserRepositoryForTesting())

        self.user_hupu = User("hupu", "123")

    def login_user(self, user):
        self.app_service.create_user(user.username, user.password)

    def test_create_workout(self):
        user = self.user_hupu

        self.app_service.create_workout("running", "2024-04-24", user.username)

        workouts = self.app_service.list_all_workouts()

        self.assertEqual(len(workouts), 1)
        self.assertEqual(workouts[0].content, "running")
        self.assertEqual(workouts[0].user, user.username)
        self.assertEqual(workouts[0].date, "2024-04-24")

    def test_login_valid(self):
        self.app_service.create_user(
            self.user_hupu.username, self.user_hupu.password)

        user = self.app_service.login(
            self.user_hupu.username, self.user_hupu.password)

        self.assertEqual(user.username, self.user_hupu.username)

    def test_login_invalid(self):
        self.assertRaises(InvalidLoginError,
                          lambda: self.app_service.login("test", ""))

    def test_create_workout_invalid_date(self):
        user = self.user_hupu

        self.assertRaises(InvalidDate, lambda: self.app_service.create_workout("running", "12.01.2024", user.username))

    def test_create_workout_duplicate(self):
        user = self.user_hupu

        self.app_service.create_workout("running", "2024-04-24", user.username)

        self.assertRaises(DuplicateWorkoutError, lambda: self.app_service.create_workout("running", "2024-04-24", user.username))
