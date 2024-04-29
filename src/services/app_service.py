from datetime import datetime
from entities.workout import Workout
from entities.user import User
from repositories.user_repository import user_repository
from repositories.workout_repository import workout_repository


class UsernameTakenError(Exception):
    pass


class InvalidLoginError(Exception):
    pass


class InvalidDate(Exception):
    pass


class DuplicateWorkoutError(Exception):
    pass


class NoSuchWorkoutError(Exception):
    pass


class AppService:
    """Sovelluslogiikasta vastaava luokka.
    """

    def __init__(self, workout_rep=workout_repository, user_rep=user_repository):
        """Luokan konstruktori.

        Args:
            workout_rep: 
                        Olio, jolla on WorkoutRepository-luokkaa vastaavat metodit.
                        Vapaaehtoinen, oletusarvolta WorkoutRepository-olio.
            user_rep:
                        Olio, jolla on UserRepository-luokkaa vastaavat metodit.
                        Vapaaehtoinen, oletusarvolta UserRepository-olio.
        """

        self._user = None
        self._workout_repository = workout_rep
        self._user_repository = user_rep

    def create_workout(self, content, date, user):
        """Luo uuden treenin.

        Args:
            content: Merkkijono, joka kuvaa treenin sisältöä.
            date: Merkkijono, joka kuvaa treenin päivämäärää.
            user: Merkkijono, joka kuvaa treenin omistajan käyttäjätunnusta.

        Raises:
            InvalidDate: Virhe, joka tapahtuu, kun päivämäärä on väärässä muodossa.
            DuplicateWorkoutError: Virhe, joka tapahtuu, jos treeni on jo olemassa 
            annetulla sisällöllä ja päivämäärällä.

        Returns:
            Luotu treeni Workout-olion muodossa.

        """

        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError as exception:
            raise InvalidDate(
                "Päivämäärä väärässä muodossa. Käytä muotoa YYYY-MM-DD") from exception

        workouts = self._workout_repository.list_all_user_workouts(user)

        for existing_workout in workouts:
            if existing_workout.content == content and existing_workout.date == date:
                raise DuplicateWorkoutError(
                    "Tällä sisällöllä ja päivämäärällä on jo olemassa treeni")

        workout = Workout(content, date, user)
        return self._workout_repository.create_workout(workout)

    def login(self, username, password):
        """Kirjaa käyttäjän sisään.

        Args:
            username: Merkkijono, joka kuvaa sisäänkirjautuvan käyttäjän käyttäjätunnusta.
            password: Merkkijono, joka kuvaa sisäänkirjautuvan käyttäjän salasanaa.

        Raises:
            InvalidLoginError: Virhe, joka tapahtuu, jos käyttäjätunnus ja salasana eivät täsmää.

        Returns:
            Palauttaa kirjautuneen käyttäjän User-olion muodossa.
        """
        user = self._user_repository.find_one_user(username)

        if not user or user.password != password:
            raise InvalidLoginError("Väärä käyttäjätunnus tai salasana")

        self._user = user

        return user

    def logout(self):
        """Kirjaa kirjautuneen käyttäjän ulos.
        """
        self._user = None

    def create_user(self, username, password, login=True):
        """Luo uuden käyttäjän ja kirjaa käyttäjän sisään.

        Args:
            username: Merkkijono, joka kuvaa käyttäjän käyttäjätunnusta.
            password: Merkkijono, joka kuvaa käyttäjän salasanaa.
            login:
                Vapaaehtoinen, oletusarvo True.
                Boolean-arvo, joka kertoo kirjataanko käyttäjä sisään käyttäjän luonnin jälkeen.


        Raises:
            UsernameTakenError: Virhe, joka tapahtuu, jos käyttäjätunnus on jo olemassa.

        Returns:
            Palauttaa luodun käyttäjän User-olion muodossa.
        """
        taken_username = self._user_repository.find_one_user(username)

        if taken_username:
            raise UsernameTakenError(
                f"Käyttäjätunnus {username} on jo käytössä")

        user = self._user_repository.create_user(User(username, password))

        if login:
            self._user = user

        return user

    def list_all_workouts(self):
        """Palauttaa kaikki treenit.

        Returns:
            Palauttaa kaikki treenit listana Workout-olioita.
        """
        workouts = self._workout_repository.list_all_workouts()

        return workouts

    def loggedin_user(self):
        """Palauttaa kirjautuneen käyttäjän.

        Returns:
            Palauttaa kirjautuneen käyttäjän User-olion muodossa.
        """
        return self._user

    def get_all_users(self):
        """Palauttaa kaikki käyttäjät.

        Returns:
            Palauttaa listan kaikista käyttäjistä User-olioiden muodossa.
        """
        return self._user_repository.find_all_users()

    def get_user_workouts(self):
        """Palauttaa tietyn käyttäjän kaikki treenit.

        Returns:
            Palauttaa listan tietyn käyttäjän treeneistä Workout-olioiden muodossa.
            Jos käyttäjä ei ole kirjautunut, palauttaa tyhjän listan.
        """
        if not self._user:
            return []

        workouts = self._workout_repository.list_all_user_workouts(
            self._user.username)
        return workouts

    def delete_one_workout(self, content, date):
        """Poistaa kirjautuneen käyttäjän yhden treenin.

        Args:
            content: Poistettavan treenin sisältö.
            date: Poistettavan treenin päivämäärä.

        Raises:
            InvalidDate: 
                Virhe, joka tapahtuu, kun poistettavan treenin päivämäärä 
                on annettu väärässä muodossa.
            NoSuchWorkoutError: 
                Virhe, joka tapahtuu, kun poistettavaa treeniä ei löydy käyttäjän treeneistä.
        """

        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError as exception:
            raise InvalidDate(
                "Päivämäärä väärässä muodossa. Käytä muotoa YYYY-MM-DD") from exception

        user_workouts = self.get_user_workouts()

        found_workout = False
        for workout in user_workouts:
            if workout.content == content and workout.date == date:
                self._workout_repository.delete_one_workout(
                    self._user.username, content, date)
                found_workout = True
                break

        if not found_workout:
            raise NoSuchWorkoutError(
                "Treeniä ei löydy annetulla sisällöllä ja päivämäärällä")

# def modify_workout


app_service = AppService()
