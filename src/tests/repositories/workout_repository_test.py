import unittest
from repositories.workout_repository import workout_repository
from entities.workout import Workout
from repositories.user_repository import user_repository
from entities.user import User


class TestWorkoutRepository(unittest.TestCase):
    def setUp(self):
        workout_repository.delete_all_workouts()
        user_repository.delete_all_users()

        self.user_tupu = "tupu"
        self.user_hupu = User("hupu", "abc")
        self.user_lupu = User("lupu", "def")
        self.content_running = "running"
        self.date = "2024-04-24"
        self.workout_running = Workout(self.content_running, self.date, self.user_tupu)
        self.workout_gym = Workout("gym", self.date, self.user_tupu)

    def test_create_workout(self):
        workout_repository.create_workout(self.workout_running)
        workouts = workout_repository.list_all_workouts()

        self.assertEqual(len(workouts), 1)
        self.assertEqual(workouts[0].user, self.user_tupu)
        self.assertEqual(workouts[0].content, self.content_running)
        self.assertEqual(workouts[0].date, "2024-04-24")

    def test_list_all_workouts(self):
        workout_repository.create_workout(self.workout_running)
        workout_repository.create_workout(self.workout_gym)
        workouts = workout_repository.list_all_workouts()

        self.assertEqual(len(workouts), 2)
        self.assertEqual(workouts[0].user, self.user_tupu)
        self.assertEqual(workouts[0].content, self.content_running)
        self.assertEqual(workouts[1].content, "gym")
        self.assertEqual(workouts[1].user, self.user_tupu)

    def test_list_all_user_workouts(self):
        hupu = user_repository.create_user(self.user_hupu)
        lupu = user_repository.create_user(self.user_lupu)

        workout_repository.create_workout(
            Workout(content="running", date="2024-04-24", user=hupu.username))
        workout_repository.create_workout(
            Workout(content="gym", date="2024-04-24", user=lupu.username))

        hupu_workouts = workout_repository.list_all_user_workouts(
            hupu.username)

        self.assertEqual(len(hupu_workouts), 1)
        self.assertEqual(hupu_workouts[0].content, "running")

        lupu_workouts = workout_repository.list_all_user_workouts(
            self.user_lupu.username)

        self.assertEqual(len(lupu_workouts), 1)
        self.assertEqual(lupu_workouts[0].content, "gym")

    def test_delete_all_workouts(self):
        workout = workout_repository.create_workout(self.workout_running)
        workouts = workout_repository.list_all_workouts()

        self.assertEqual(len(workouts), 1)

        workout_repository.delete_all_workouts()

        workouts = workout_repository.list_all_workouts()
        self.assertEqual(len(workouts), 0)
