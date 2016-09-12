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
	self.c.execute('SELECT rowid FROM profiles where NAME = (?)',
	(username,))
	user_id = self.c.fetchone()[0]
	self.c.execute('INSERT INTO meals (food_id, user_id, serving_amount) values (?,?, ?)', (self.food_id, user_id, serving_amount))	
	self.conn.commit()

    def user_date(self, username, timestamp):
	self.c.execute('SELECT rowid FROM profiles where NAME = (?)',
	(username,))
	username_id = self.c.fetchone()[0]
	self.c.execute('SELECT food_id, serving_amount FROM meals WHERE Timestamp like (?) and user_id = (?)', (timestamp + '%', username_id)) 
	user_date  = self.c.fetchall()
	return user_date
    
    def nutrition_query(self, food):
	self.c.execute('SELECT calories, sugar, fat FROM nutrition WHERE rowid =(?)', (food,))
	food_stats = self.c.fetchone()
	return food_stats
