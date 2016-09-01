import sqlite3

class NutritionData():
    
    def __init__(self):
	self.conn = sqlite3.connect('./users.db')
	self.c = self.conn.cursor()

    def add_nutrition(self, data):
	 
	try:
	    self.c.execute('INSERT INTO nutrition (ID, FOOD, CALORIES, SUGAR, FAT) values (:_id,:item_name, :nf_calories, :nf_sugars, :nf_total_fat)', data)
	    self.food_id = self.c.lastrowid
	    print (self.food_id)
	    
	except sqlite3.IntegrityError:
	    print( 'This item is already in the database.')
     
    def meals(self, data ):
	username = data['username']
	serving_amount = data['serving_amount']
	print(username)
	self.c.execute('SELECT rowid FROM profiles where NAME = (?)',
	(username,))
	user_id = self.c.fetchone()[0]
	print(user_id)
	self.c.execute('INSERT INTO meals (food_id, user_id, serving_amount) values (?,?, ?)', (self.food_id, user_id, serving_amount))	
	self.conn.commit()

    def daily_total(self, username, timestamp):
	self.c.execute('SELECT rowid FROM profiles where NAME = (?)',
	(username,))
	username_id = self.c.fetchone()[0]
	self.c.execute('SELECT * FROM meals WHERE Timestamp like (?) and user_id = (?)', (timestamp + '%', username_id)) 
	daily = self.c.fetchallr)
	print daily
	return daily
