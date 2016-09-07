import json
import sqlite3

class UserManager():
    """functions to add, amend and remove users"""
    
    def __init__(self):
	self.conn = sqlite3.connect('./users.db')
	self.c = self.conn.cursor()

    def verify_user(self, username):
	"""takes username, confirms if in db, returns True or False"""
	try:
	    self.c.execute('SELECT name FROM profiles WHERE name=(?)', 
				    (username,))
	    user = self.c.fetchone()[0]
	    return user == username
	
	except TypeError:
	    return False

    def verify_password(self, username, password):
	"""takes username and password, confirms password matches db password,
	returns True or False """
	
	try:
	    self.c.execute('SELECT password FROM profiles WHERE name=(?)', 
		    (username,))
	    	
	    db_pw = self.c.fetchone()[0]
	    print(password)
	 
	    return db_pw == password
	
	except TypeError:
	    return False
	
    def create_user(self, username, password, email, height, weight):
        """takes user strings, inserts row in profiles db"""
	
	try:
	    self.c.execute("INSERT INTO profiles VALUES (?,?,?,?,?)", 
			(username,password, email, weight, height))
	    self.user_id = self.c.lastrowid
	    self.conn.commit()	    
	    return self.user_id
	
	except sqlite3.IntegrityError: 
	    print('Somebody already has that name, try again.')
    
    def remove_user(self, username):
        """take  username string, querys db for username then deletes row from
	table """
	
	row = self.c.execute("SELECT * FROM profiles WHERE name =?",
	(username,))
	for i in row:
	    user = i[1]
	    print(user)
	    if user  == username:     
		self.c.execute("DELETE FROM profiles WHERE name=?", (username,))
		print("User was deleted")
		return True
	    
	    else:
		print ("Username not found, check your spelling homegirl.")
		return False
	self.conn.commit()
    
    def read_user(self, username):
        """take username string and returns readable user data"""

	self.c.execute(
		"SELECT * FROM profiles WHERE name=?", (username,))
	print(self.c.fetchone())
	
	self.conn.commit()

    def bmi_user(self, username):
	self.c.execute("SELECT height, weight FROM profiles WHERE name=?",
	(username,))
	bmi_data = self.c.fetchall()
	return bmi_data
