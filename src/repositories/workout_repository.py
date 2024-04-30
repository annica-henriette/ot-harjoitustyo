from entities.workout import Workout
from database_connection import get_database_connection


class WorkoutRepository:
    """Treeneihin liittyvistä tietokantaoperaatioista vastaava luokka.
    """

    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection: Connection-olio, joka vastaa tietokantayhteydestä.
        """

        self._connection = connection

    def create_workout(self, workout):
        """Tallentaa treenin tietokantaan.

        Args:
            workout: Tallennettava treeni Workout-oliona.

        Returns:
            Palauttaa tallennetun treenin Workout-oliona. 
        """

        cursor = self._connection.cursor()
        cursor.execute("insert into workouts (content, date, user) values (?, ?, ?)",
                       (workout.content, workout.date, workout.user))

        self._connection.commit()

        return workout

    def list_all_workouts(self):
        """Palauttaa kaikki treenit.

        Returns:
            Palauttaa listan Workout-olioita.
        """

        cursor = self._connection.cursor()
        cursor.execute("select * from workouts")
        workouts = cursor.fetchall()

        return [Workout(workout["content"], workout["date"], workout["user"]) if workout
                else None for workout in workouts]

    def list_all_user_workouts(self, username):
        """Palauttaa kaikki tietyn käyttäjän treenit.

        Args:
            username: Palautettavien treenien omistajan käyttäjätunnus. 

        Returns:
            Palauttaa listan Workout-olioita tietyn käyttäjän käyttäjätunnuksen perusteella.
        """

        cursor = self._connection.cursor()
        cursor.execute("select * from workouts where user=?", (username,))
        user_workouts = cursor.fetchall()

        return [Workout(workout["content"], workout["date"], workout["user"]) if workout
                else None for workout in user_workouts]

    def delete_all_workouts(self):
        """Poistaa kaikki treenit tietokannasta.
        """

        cursor = self._connection.cursor()
        cursor.execute("delete from workouts")

        self._connection.commit()

    def delete_one_workout(self, username, content, date):
        """Poistaa yhden käyttäjän treenin käyttäjätunnuksen, sisällön ja päivämäärän perusteella.

        Args:
            username: Poistettavan treenin omistajan käyttäjätunnus.
            content: Poistettavan treenin sisältö.
            date: Poistettavan treenin päivämäärä.
        """

        cursor = self._connection.cursor()
        cursor.execute(
            "delete from workouts where user = ? and content = ? and date = ?",
            (username, content, date))

        self._connection.commit()

    def modify_workout(self, username, old_content, new_content, date):
        """Muokkaa käyttäjän treenin sisältöä.

        Args:
            username: Muokattavan treenin omistajan käyttäjätunnus.
            old_content: Muokattavan treenin vanha sisältö.
            new_content: Muokattavan treenin uusi sisältö.
            date: Muokattavan treenin päivämäärä.
        """

        cursor = self._connection.cursor()
        cursor.execute(
            "update workouts set content = ? where user = ? and content = ? and date = ?",
            (new_content, username, old_content, date))

        self._connection.commit()


workout_repository = WorkoutRepository(get_database_connection())
