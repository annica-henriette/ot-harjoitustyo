from entities.user import User
from database_connection import get_database_connection

class UserRepository:

    def __init__(self, connection):
        self._connection = connection

    def find_all_users(self):
        cursor = self._connection.cursor()
        cursor.execute("select * from users")
        users = cursor.fetchall()

        return [User(user["username"], user["password"]) if user else None for user in users]

    def create_user(self, user):
        cursor = self._connection.cursor()
        cursor.execute("insert into users (username, password) values (?, ?)", (user.username, user.password))

        self._connection.commit()

        return user

    def delete_all_users(self):
        cursor = self._connection.cursor()
        cursor.execute("delete from users")

        self._connection.commit()

    def find_one_user(self, user):
        cursor = self._connection.cursor()
        cursor.execute("select * from users where username=?", (user.username,))
        user = cursor.fetchone()

        return User(user["username"], user["password"]) if user else None


user_repository = UserRepository(get_database_connection())
