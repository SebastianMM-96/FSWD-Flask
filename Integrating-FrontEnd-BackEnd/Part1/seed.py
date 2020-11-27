import sqlite3

connection = sqlite3.connect('flask_app.db', check_same_thread=False)
cursor = connection.cursor()

cursor.execute(
    """
        INSERT INTO user(
            username,
            password,
            favoriteColor
        )VALUES(
            'Sebastian',
            'sebas123',
            'black'
        );
    """
)

cursor.execute(
    """
        INSERT INTO user(
            username,
            password,
            favoriteColor
        )VALUES(
            'Admin',
            'root123',
            'black'
        );
    """
)

connection.commit()
cursor.close()
connection.close()