import sqlite3

def showUserColor(username):
    connection = sqlite3.connect('flask_app.db', check_same_thread=False)
    cursor = connection.cursor()
    
    cursor.execute(
        """
            SELECT favoriteColor FROM user WHERE username='{username}' ORDER BY pk DESC;
        """.format(username = username)
    )
    # get the first color
    color = cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()

    message = '{username}\'s favorite color is {color}.'.format(username=username, color=color)

    return message