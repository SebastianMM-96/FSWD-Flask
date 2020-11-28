import sqlite3


def checkPass(username):
    conn = sqlite3.connect('todoApp.db', check_same_thread=False)
    cursor = conn.cursor()

    cursor.execute(
        """
            SELECT password FROM user WHERE username = '{username}' ORDER BY pk DESC;
        """.format(username=username)
    )

    password = cursor.fetchone()[0]

    conn.commit()
    cursor.close()
    conn.close()

    # Return the password
    return password

def checkUsers():
    conn = sqlite3.connect('todoApp.db', check_same_thread=False)
    cursor = conn.cursor()

    cursor.execute(
        """
            SELECT username FROM user ORDER BY pk DESC;
        """
    )
    # List of all user's
    dbUsers = cursor.fetchall()
    users = []

    for i in range(len(dbUsers)):
        person = dbUsers[i][0]
        users.append(person)

    conn.commit()
    cursor.close()
    conn.close()

    # Return the password
    return users


def signup(username, password):
    conn = sqlite3.connect('todoApp.db', check_same_thread=False)
    cursor = conn.cursor()

    cursor.execute(
        """
            SELECT password FROM user WHERE username = '{username}';
        """.format(username=username)
    )
    exist = cursor.fetchone()

    # insert into db
    if exist is None:
        cursor.execute(
            """
                INSERT INTO user(username, password)
                VALUES('{username}', '{password}');
            """.format(username=username, password=password)
        )
        conn.commit()
        cursor.close()
        conn.close()

    else:
        return('User alredy existed')

    return 'You have successfully signed up'
