import sqlite3


class NutritionData():

    def __init__(self, conn):
        self.conn = conn
        self.c = self.conn.cursor()
        food_id = None

    def query_food_item(self, food_input):
        self.c.execute("SELECT id FROM nutrition WHERE food like (?)", (food_input))
        id_food = self.c.fetchone()
        if id_food is not None:
            print 'hi'
            return True
        else:
            print 'yo'
            return False

    def add_nutrition(self, data):
            self.c.execute('INSERT INTO nutrition (ID, FOOD, CALORIES, SUGAR, FAT, PROTEIN, FIBER, CALCIUM) values (:_id, :item_name, :nf_calories, :nf_sugars, :nf_total_fat, :nf_protein, :nf_dietary_fiber, :nf_calcium_dv)', data)
            # self.c.execute('SELECT ID FROM nutrition WHERE id=:_id', data)
            # food_id = self.c.fetchone()[0]
            return data['_id']

        # except sqlite3.IntegrityError:
        #     print('This item is already in the database.')
            self.conn.commit()


    def nutrition_query(self, food_id):
        food_query = self.c.execute('SELECT calories, sugar, fat, protein, fiber, calcium FROM nutrition WHERE id =(?)', (food_id,))
        if food_query is not None:
            food_stats = self.c.fetchone()
            print food_stats
            return food_stats
        else:
            return ' There is no entry for an item in that request.'
