import json
import sqlite3


class UserManager():
    """functions to add, amend and remove users"""

    def __init__(self, conn):
        self.conn = conn
        self.c = self.conn.cursor()

    def verify_user(self, username):
        """takes username, confirms if in db, returns True or False"""
        try:
            self.c.execute('SELECT name FROM profiles WHERE name=(?)' (username,))
            user = self.c.fetchone()[0]
            return user == username

        except TypeError:
            return False

    def verify_password(self, username, password):
        """takes username and password, confirms password matches db password,
            returns True or False """

        try:
            self.c.execute('SELECT password FROM profiles WHERE name=(?)', (username,))

            db_pw = self.c.fetchone()[0]
            print(password)

            return db_pw == password

        except TypeError:
            return False

    def create_user(self, username, password, email, height, weight):
        """takes user strings, inserts row in profiles db"""

        try:
            self.c.execute("INSERT INTO profiles VALUES (?,?,?,?,?)", (username, password, email, weight, height))
            self.user_id = self.c.lastrowid
            self.conn.commit()
            return self.user_id

        except sqlite3.IntegrityError:
            print('Somebody already has that name, try again.')

    def update_height(self, username, weight):
        self.c.execute('UPDATE  profiles SET weight=? WHERE name=?',
                       (weight, username))
        self.conn.commit()
        return True

    def update_weight(self, username, height):
        self.c.execute('UPDATE profiles SET height=? WHERE name=?',
                       (height, username))
        self.conn.commit()
        return True

    def remove_user(self, username):
        """take  username string, querys db for username then deletes row from table """

        row = self.c.execute("SELECT * FROM profiles WHERE name =?",
                             (username,))
        for i in row:
            user = i[1]
            print(user)
        if user == username:
            self.c.execute("SELECT id FROM profiles WHERE name=?",
                           (username,))
            i_d = self.c.fetchone()[0]
            self.c.execute("DELETE FROM events WHERE user_id=?", (i_d,))
            self.c.execute("DELETE FROM profiles WHERE name=?", (username,))
            self.conn.commit()
            return True
        else:
            print ('User not found.')

    def read_user(self, username):
        """take username string and returns readable user data"""

        self.c.execute("SELECT * FROM profiles WHERE name=?", (username,))
        user_profile = self.c.fetchone()
        print user_profile
        return user_profile

    def user_bmi(self, username):
        self.c.execute("SELECT height, weight FROM profiles WHERE name=?", (username,))
        bmi_data = self.c.fetchone()
        return bmi_data
