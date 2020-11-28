import sqlite3

conn = sqlite3.connect('todoApp.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute(
    """
        CREATE TABLE user(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(16),
            password VARCHAR(32)
        );
    """
)

cursor.execute(
    """
        CREATE TABLE todo(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(40),
            complete INTEGER
        );
    """
)

conn.commit()
cursor.close()
conn.close()