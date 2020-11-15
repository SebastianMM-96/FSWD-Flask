# Create a database in SQLite 3
import sqlite3

# Name the database
connection = sqlite3.connect('todoFlaskApp.db', check_same_thread=False)
cursor = connection.cursor()

# Table
cursor.execute(
    """
    CREATE TABLE users (
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        email VARCHAR(20),
        password VARCHAR(40)
    );
    """
)

connection.commit()
cursor.close()
connection.close()