# Populate the table
import sqlite3

connection = sqlite3.connect('todoFlaskApp.db', check_same_thread=False)
cursor = connection.cursor()

# Insert data into table
cursor.execute(
    """
    INSERT INTO users (
        email,
        password
        ) VALUES (

            'sebastian@email.com',
            'sebastian'

        );
    """
)

cursor.execute(
    """
    INSERT INTO users (
        email,
        password
        ) VALUES (

            'jesus@email.com',
            'jesus'
        );
    """
)

connection.commit()
cursor.close()
connection.close()