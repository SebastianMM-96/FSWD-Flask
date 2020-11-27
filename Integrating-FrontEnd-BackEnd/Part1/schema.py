import sqlite3

connection = sqlite3.connect('flask_app.db', check_same_thread=False)
cursor = connection.cursor()

cursor.execute(
    """
        CREATE TABLE user(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(16),
            password VARCHAR(32),
            favoriteColor VARCHAR(32)
        );
    """
)

connection.commit()
cursor.close()
connection.close()