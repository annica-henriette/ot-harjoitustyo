from entities.user import User
from database_connection import get_database_connection

class UserRepository:

    def __init__(self, connection):
        self._connection = connection

    def find_all_users(self):
        cursor = self._connection.cursor()
        cursor.execute("select * from users")
        users = cursor.fetchall()

        return [User(row["username"], row["password"]) if row else None for row in users]

    def create_user(self, user):
        cursor = self._connection.cursor()
        cursor.execute("insert into users (username, password) values (?, ?)", (user.username, user.password))

        self._connection.commit()

        return user

    def delete_all_users(self):
        cursor = self._connection.cursor()
        cursor.execute("delete from users")

        self._connection.commit()

user_repository = UserRepository(get_database_connection())
