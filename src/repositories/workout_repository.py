from entities.workout import Workout
from repositories.user_repository import user_repository
from config import WORKOUT_FILE_PATH

class WorkoutRepository:

    def __init__(self, file_path):
        self._file_path = file_path

    def _file_exists(self):
        Path(self._file_path).touch()

    def _write(sefl, workouts):
        self._file_exists()

        with open(self._file_path, "w", encoding="utf-8") as file:
            for workout in workouts:
                username = workout.user.username if workout.user else ""

                row = f"{workout.id};{workout.content};{username}"

                file.write(row+"\n")

    def delete_all(self):

        self._write([])

workout_repository = WorkoutRepository(WORKOUT_FILE_PATH)

