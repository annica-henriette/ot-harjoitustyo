import unittest
from entities.workout import Workout
from entities.user import User
from services.app_service import (
    AppService, InvalidLoginError, UsernameTakenError, InvalidDate, DuplicateWorkoutError, NoSuchWorkoutError)


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

    def delete_one_workout(self, user, content, date):
        for workout in self.workouts:
            if workout.user == user and workout.content == content and workout.date == date:
                self.workouts.remove(workout)
                return

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

    def test_create_user_valid(self):
        username = self.user_hupu.username
        password = self.user_hupu.password

        user = self.app_service.create_user(username, password, login=True)

        users = self.app_service.get_all_users()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, username)

        current_user = self.app_service.loggedin_user()

        self.assertEqual(current_user, user)

    def test_create_user_login_false(self):
        username = self.user_hupu.username
        password = self.user_hupu.password

        user = self.app_service.create_user(username, password, login=False)

        users = self.app_service.get_all_users()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, username)

        current_user = self.app_service.loggedin_user()

        self.assertEqual(current_user, None)

    def test_create_user_invalid(self):
        username = self.user_hupu.username

        self.app_service.create_user(username, "123123")

        self.assertRaises(
            UsernameTakenError, lambda: self.app_service.create_user(username, "password"))

    def login_user(self, user):
        self.app_service.create_user(user.username, user.password)

    def test_loggedin_user(self):
        self.login_user(self.user_hupu)

        current_user = self.app_service.loggedin_user()

        self.assertEqual(current_user.username, self.user_hupu.username)

    def test_logout(self):
        self.login_user(self.user_hupu)

        current_user = self.app_service.loggedin_user()

        self.assertEqual(current_user.username, self.user_hupu.username)

        current_user = self.app_service.logout()

        self.assertEqual(current_user, None)

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

        self.assertRaises(InvalidDate, lambda: self.app_service.create_workout(
            "running", "12.01.2024", user.username))

    def test_create_workout_duplicate(self):
        user = self.user_hupu

        self.app_service.create_workout("running", "2024-04-24", user.username)

        self.assertRaises(DuplicateWorkoutError, lambda: self.app_service.create_workout(
            "running", "2024-04-24", user.username))

    def test_get_user_workouts(self):
        workouts = self.app_service.get_user_workouts()

        self.assertEqual(len(workouts), 0)

        self.login_user(self.user_hupu)

        self.app_service.create_workout(
            "running", "2024-04-24", self.user_hupu.username)
        self.app_service.create_workout(
            "gym", "2024-04-24", self.user_hupu.username)

        workouts = self.app_service.get_user_workouts()

        self.assertEqual(len(workouts), 2)
        self.assertEqual(workouts[0].user, self.user_hupu.username)

    def test_delete_one_workout(self):
        self.login_user(self.user_hupu)
        user = self.user_hupu

        self.app_service.create_workout("running", "2024-04-24", user.username)
        self.app_service.create_workout("gym", "2024-04-22", user.username)

        self.app_service.delete_one_workout("running", "2024-04-24")
        workouts = self.app_service.get_user_workouts()

        self.assertEqual(len(workouts), 1)
        self.assertEqual(workouts[0].content, "gym")
        self.assertEqual(workouts[0].user, user.username)
        self.assertEqual(workouts[0].date, "2024-04-22")

    def test_delete_one_workout_invalid_date(self):
        user = self.user_hupu

        self.assertRaises(InvalidDate, lambda: self.app_service.delete_one_workout(
            "running", "12.01.2024"))

    def test_workout_not_found(self):
        self.login_user(self.user_hupu)
        user = self.user_hupu

        self.app_service.create_workout("running", "2024-04-24", user.username)

        self.assertRaises(NoSuchWorkoutError, lambda: self.app_service.delete_one_workout("gym", "2024-04-24"))
