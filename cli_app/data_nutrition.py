import sqlite3

class NutritionData():
    
    def __init__(self):
	self.conn = sqlite3.connect('./users.db')
	self.c = self.conn.cursor()
	self.food_id = None
    
    def add_nutrition(self, data):
	try:
	    self.c.execute('INSERT INTO nutrition (ID, FOOD, CALORIES, SUGAR, FAT, PROTEIN, FIBER, CALCIUM) values (:_id, :item_name, :nf_calories, :nf_sugars, :nf_total_fat, :nf_protein, :nf_dietary_fiber, :nf_calcium_dv)', data)
	    self.food_id = self.c.lastrowid
	    print (self.food_id)
	    
	except sqlite3.IntegrityError:
	    print( 'This item is already in the database.')
	self.conn.commit()

    def add_meals(self,username, data ):
	serving_amount = data['serving_amount']
	self.c.execute('SELECT rowid FROM profiles where NAME = (?)',
	(username,))
	user_id = self.c.fetchone()[0]
	self.c.execute('INSERT INTO meals (food_id, user_id, serving_amount) values (?,?,?)', (self.food_id, user_id, serving_amount))	
	self.conn.commit()

    def user_date(self, username, timestamp):
	self.c.execute('SELECT rowid FROM profiles where NAME = (?)',
	(username,))
	username_id = self.c.fetchone()[0]
	food_serving = self.c.execute('SELECT food_id, serving_amount FROM meals WHERE Timestamp like (?) and user_id = (?)', (timestamp + '%', username_id)) 
	if food_serving is not None:
	    user_date  = self.c.fetchall()
	    return user_date
	else:
	    print ('That date or user is not valid.')

    def nutrition_query(self, food):
	food_query = self.c.execute('SELECT calories, sugar, fat, protein, fiber, calcium FROM nutrition WHERE rowid =(?)', (food,))
	if food_query is not None:
	    food_stats = self.c.fetchone()
	    return food_stats
	else:
	    return ' There is no entry for an item in that request.'
