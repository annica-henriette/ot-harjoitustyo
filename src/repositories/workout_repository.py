from entities.workout import Workout
from repositories.user_repository import user_repository
from database_connection import get_database_connection


class WorkoutRepository:

    def __init__(self, connection):
        self._connection = connection

    def create_workout(self, workout):
        cursor = self._connection.cursor()
        cursor.execute("insert into workouts (content, user) values (?, ?)",
                       (workout.content, workout.user))

        self._connection.commit()

        return workout

    def list_all_workouts(self):
        cursor = self._connection.cursor()
        cursor.execute("select * from workouts")
        workouts = cursor.fetchall()

        return [Workout(workout["content"], workout["user"]) if workout
                else None for workout in workouts]

    def list_all_user_workouts(self, username):
        cursor = self._connection.cursor()
        cursor.execute("select * from workouts where user=?", (username,))
        user_workouts = cursor.fetchall()

        return [Workout(workout["content"], workout["user"]) if workout
                else None for workout in user_workouts]

    def delete_all_workouts(self):
        cursor = self._connection.cursor()
        cursor.execute("delete from workouts")

        self._connection.commit()

# def delete_one_workout()
# def modify_workout()


workout_repository = WorkoutRepository(get_database_connection())
