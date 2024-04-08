from entities.workout import Workout
from repositories.user_repository import user_repository
from config import WORKOUT_FILE_PATH

class WorkoutRepository:

    def __init__(self, file_path):
        self._file_path = file_path

    def _file_exists(self):
        Path(self._file_path).touch()

    def _write(self, workouts):
        if self._file_exists():

            with open(self._file_path, "w") as file:
                for workout in workouts:
                    if workout.user:
                        username = workout.user.username
                    else:
                        ""

                    row = f"{workout.id};{username};{workout.content}"

                    file.write(row+"\n")

    def delete_all_workouts(self):

        self._write([])

workout_repository = WorkoutRepository(WORKOUT_FILE_PATH)

