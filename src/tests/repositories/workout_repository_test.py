import unittest
from repositories.workout_repository import workout_repository
from entities.workout import Workout

class TestWorkoutRepository(unittest.TestCase):
    def SetUp(self):
        workout_repository.delete_all_workouts()
