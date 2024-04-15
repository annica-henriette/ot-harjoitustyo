import unittest
from repositories.workout_repository import workout_repository
from entities.workout import Workout
from repositories.user_repository import user_repository
from entities.user import User

class TestWorkoutRepository(unittest.TestCase):
    def setUp(self):
        workout_repository.delete_all_workouts()
        user_repository.delete_all__users()

        self.user = "tupu"
        self.content = "running"
        self.workout_running = Workout(self.content, self.user)

    def test_create_workout(self):
        workout_repository.create_workout(self.workout_running)
        workouts = workout_repository.list_all_workouts()

        self.assertEqual(len(workouts), 1)
        self.assertEqual(workouts[0].user, self.user)
        self.assertEqual(workouts[0].content, self.content)
