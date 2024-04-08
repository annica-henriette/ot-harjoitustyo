from entities.workout import Workout
from entities.user import User

from repositories.user_repository import user_repository
from repositories.workout_repository import workout_repository

class AppService:

    def __init__(self, workout_rep=workout_repository, user_rep=user_repository):
        self._user = None
        self._workout_repository = workout_rep
        self._user_repository = user_rep

    def create_workout(self, content):
        workout = Workout(content, user = self._user)

        return self._workout_repository.create(workout)

# def login
# def logout
# def create_user
# def list_all_users_workouts
# def get_current_user
# def get_all_users
# def modify_workout

app_service = AppService()
