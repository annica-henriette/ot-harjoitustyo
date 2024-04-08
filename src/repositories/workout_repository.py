from entities.workout import Workout
from repositories.user_repository import user_repository
from database_connection import get_database_connection

class WorkoutRepository:

    def __init__(self, connection):
        self._connection = connection

    def create_workout(self, workout):
        cursor = self._connection.cursor()
        cursor.execute("insert into workouts (content, user, id) values (?, ?, ?)", (workout.content, workout.user, workout.id))

        self._connection.commit()

        return workout

    def delete_all_workouts(self):
        cursor = self._connection.cursor()
        cursor.execute("delete from workouts")
        self._connection.commit()

# def list_all_workouts()
# def delete_one_workout()
# def modify_workout()


workout_repository = WorkoutRepository(get_database_connection())

