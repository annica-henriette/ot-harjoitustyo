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
        user = self._user
        workout = Workout(content, user)

        return self._workout_repository.create_workout(workout)

    def login(self, username, password):

        user = self._user_repository.find_one_user(username)

        # handle invalid credentials

        self._user = user

        return user

    def logout(self):

        self._user = None

    def create_user(self, username, password, login=True):

        # handle two same usernames

        user = self._user_repository.create_user(User(username, password))

        if login:
            self._user = user

        return user

    def list_all_workouts(self):

        workouts = self._workout_repository.list_all_workouts()

        return workouts

# def get_current_user
# def get_all_users
# def modify_workout


app_service = AppService()
