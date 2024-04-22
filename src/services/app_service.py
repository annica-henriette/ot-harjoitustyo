from entities.workout import Workout
from entities.user import User
from repositories.user_repository import user_repository
from repositories.workout_repository import workout_repository
from datetime import datetime


class UsernameTakenError(Exception):
    pass


class InvalidLoginError(Exception):
    pass


class InvalidDate(Exception):
    pass


class DuplicateWorkoutError(Exception):
    pass


class AppService:

    def __init__(self, workout_rep=workout_repository, user_rep=user_repository):
        self._user = None
        self._workout_repository = workout_rep
        self._user_repository = user_rep

    def create_workout(self, content, date, user):

        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise InvalidDate(
                "Päivämäärä väärässä muodossa. Käytä muotoa YYYY-MM-DD")

        workouts = self._workout_repository.list_all_user_workouts(user)

        for existing_workout in workouts:
            if existing_workout.content == content and existing_workout.date == date:
                raise DuplicateWorkoutError(
                    "Tällä sisällöllä ja päivämäärällä on jo olemassa treeni")

        workout = Workout(content, date, user)
        return self._workout_repository.create_workout(workout)

    def login(self, username, password):
        user = self._user_repository.find_one_user(username)

        if not user or user.password != password:
            raise InvalidLoginError("Väärä käyttäjätunnus tai salasana")

        self._user = user

        return user

    def logout(self):
        self._user = None

    def create_user(self, username, password, login=True):

        taken_username = self._user_repository.find_one_user(username)

        if taken_username:
            raise UsernameTakenError(
                f"Käyttäjätunnus {username} on jo käytössä")

        user = self._user_repository.create_user(User(username, password))

        if login:
            self._user = user

        return user

    def list_all_workouts(self):

        workouts = self._workout_repository.list_all_workouts()

        return workouts

    def loggedin_user(self):
        return self._user

    def get_all_users(self):
        return self._user_repository.find_all_users()

    def get_user_workouts(self):
        if not self._user:
            return []

        workouts = self._workout_repository.list_all_user_workouts(
            self._user.username)
        return workouts

# def modify_workout


app_service = AppService()
