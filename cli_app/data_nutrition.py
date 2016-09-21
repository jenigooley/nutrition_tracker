import sqlite3


class NutritionData():

    def __init__(self):
        self.conn = sqlite3.connect('./eats_and_bleeds.db')
        self.c = self.conn.cursor()
        self.food_id = None

    def get_user_id(username):
        user_id = self.c.execute('SELECT rowid FROM profiles where NAME = (?)',
                                 (username,))
        if user_id is not None:
            self.username_id = self.c.fetchone()[0]
            print (self.username_id)
        else:
            print('This name is not valid')

    def add_nutrition(self, data):
        try:
            self.c.execute('INSERT INTO nutrition (ID, FOOD, CALORIES, SUGAR, FAT, PROTEIN, FIBER, CALCIUM) values (:_id, :item_name, :nf_calories, :nf_sugars, :nf_total_fat, :nf_protein, :nf_dietary_fiber, :nf_calcium_dv)', data)
            self.c.execute('SELECT last_insert_rowid()')
            self.food_id = self.c.fetchone()[0]
            print (self.food_id)

        except sqlite3.IntegrityError:
            print('This item is already in the database.')
        self.conn.commit()


    def nutrition_query(self, food):
        food_query = self.c.execute('SELECT calories, sugar, fat, protein, fiber, calcium FROM nutrition WHERE rowid =(?)', (food,))
        if food_query is not None:
            food_stats = self.c.fetchone()
            print food_stats
            return food_stats
        else:
            return ' There is no entry for an item in that request.'
