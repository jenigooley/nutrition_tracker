import sqlite3


class NutritionData():
    
    def __init__(self):
	self.conn = sqlite3.connect('./users.db')
	self.c = self.conn.cursor()

    def add_nutrition(self, data):
	 
	try:
	    self.c.execute('INSERT INTO nutrition (ID, FOOD, CALORIES, SERVING_AMOUNT, SUGAR, FAT) values (:_id,:item_name, :nf_calories, :serving_amount, :nf_sugars, :nf_total_fat)', data)
	
	except sqlite3.IntegrityError:
	    print( 'This item is already in the database.')
	
	self.c.execute('SELECT rowid , * FROM profiles WHERE name =  
	    self.conn.commit()

	
