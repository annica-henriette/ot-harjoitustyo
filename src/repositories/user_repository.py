from entities.user import User
from database_connection import get_database_connection

def get_user(row):
    if row:
        return User(row["username"], row["password"])
    else:
        None

class UserRepository:

    def __init__(self, connection):
        self._connection = connection

    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute("select * from users")
        users = cursor.fetchall()

        return list(map(get_user, users))

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
