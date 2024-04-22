from entities.workout import Workout
from database_connection import get_database_connection


class WorkoutRepository:

    def __init__(self, connection):
        self._connection = connection

    def create_workout(self, workout):
        cursor = self._connection.cursor()
        cursor.execute("insert into workouts (content, date, user) values (?, ?, ?)",
                       (workout.content, workout.date, workout.user))

        self._connection.commit()

        return workout

    def list_all_workouts(self):
        cursor = self._connection.cursor()
        cursor.execute("select * from workouts")
        workouts = cursor.fetchall()

        return [Workout(workout["content"], workout["date"], workout["user"]) if workout
                else None for workout in workouts]

    def list_all_user_workouts(self, username):
        cursor = self._connection.cursor()
        cursor.execute("select * from workouts where user=?", (username,))
        user_workouts = cursor.fetchall()

        return [Workout(workout["content"], workout["date"], workout["user"]) if workout
                else None for workout in user_workouts]

    def delete_all_workouts(self):
        cursor = self._connection.cursor()
        cursor.execute("delete from workouts")

        self._connection.commit()

    def delete_one_workout(self, username, content, date):
        cursor = self._connection.cursor()
        cursor.execute(
            "delete from workouts where user = ? and content = ? and date = ?",
            (username, content, date))

        self._connection.commit()

# def modify_workout()


workout_repository = WorkoutRepository(get_database_connection())
