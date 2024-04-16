from database_connection import get_database_connection

def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''drop table if exists users;''')
    cursor.execute('''drop table if exists workouts;''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table users (username text primary key, password text);
    ''')

    cursor.execute('''
        CREATE TABLE workouts (
            workout_id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT,
            user TEXT,
            FOREIGN KEY(user) REFERENCES users(username)
        );
    ''')

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)

if __name__ == "__main__":
    initialize_database()
