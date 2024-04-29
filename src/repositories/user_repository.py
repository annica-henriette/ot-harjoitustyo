from entities.user import User
from database_connection import get_database_connection


class UserRepository:
    """Luokka, joka vastaa käyttäjiin liittyvistä tietokantaoperaatioista.
    """

    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection: Connection-olio, joka vastaa tietokantayhteydestä.
        """

        self._connection = connection

    def find_all_users(self):
        """Palauttaa kaikki käyttäjät.

        Returns:
            Palauttaa listan User-olioita.
        """

        cursor = self._connection.cursor()
        cursor.execute("select * from users")
        users = cursor.fetchall()

        return [User(user["username"], user["password"]) if user else None for user in users]

    def create_user(self, user):
        """Tallentaa käyttäjän tietokantaan.

        Args:
            user: Tallennettava käyttäjä User-oliona.

        Returns:
            Palauttaa tallennetun käyttäjän User-oliona.
        """

        cursor = self._connection.cursor()
        cursor.execute("insert into users (username, password) values (?, ?)",
                       (user.username, user.password))

        self._connection.commit()

        return user

    def delete_all_users(self):
        """Poistaa kaikki käyttäjät.
        """

        cursor = self._connection.cursor()
        cursor.execute("delete from users")

        self._connection.commit()

    def find_one_user(self, username):
        """Palauttaa yhden käyttäjän käyttäjätunnuksen perusteella.

        Args:
            username: Palautettavan käyttäjän käyttäjätunnus.

        Returns:
            Jos käyttäjätunnuksen perusteella löytyy käyttäjä tietokannasa, 
            alauttaa User-olion, muuten None.
        """
        
        cursor = self._connection.cursor()
        cursor.execute("select * from users where username=?",
                       (username,))
        user = cursor.fetchone()

        if user:
            return User(user["username"], user["password"])

        return None


user_repository = UserRepository(get_database_connection())
