import unittest
from repositories.workout_repository import workout_repository
from entities.workout import Workout


class TestWorkoutRepository(unittest.TestCase):
    def setUp(self):
        workout_repository.delete_all_workouts()
        self.workout_running = Workout("tupu", "running")

    def test_create_workout(self):
        workout_repository.create_workout(self.workout_running)
        workouts = workout_repository.list_all_workouts()

        self.assertEqual(len(workouts), 1)
        self.assertEqual(workouts[0].user, self.workout_running.user)
