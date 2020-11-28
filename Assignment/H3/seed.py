import sqlite3

conn = sqlite3.connect('todoApp.db', check_same_thread=False)
cursor = conn.cursor()

cursor.execute(
    """
        INSERT INTO user(
            username,
            password
        )VALUES(
            'poe@mail.com',
            'allanPoe'
        );
    """
)

cursor.execute(
    """
        INSERT INTO user(
            username,
            password
        )VALUES(
            'admin@mail.com',
            'admin123'
        );
    """
)

cursor.execute(
    """
        INSERT INTO todo(
            title,
            complete
        )VALUES(
            'Walk the dog',
            '0'
        );
    """
)

cursor.execute(
    """
        INSERT INTO todo(
            title,
            complete
        )VALUES(
            'Buy groceries',
            '0'
        );
    """
)

conn.commit()
cursor.close()
conn.close()