import sqlite3
import data_nutrition

class DataTables():
    """manage all tables with specific event data"""

    def __init__(self):
        self.conn = sqlite3.connect('./eats_and_bleeds.db')
        self.c = self.conn.cursor()
        self.db_nutrition = data_nutrition.NutritionData

    def add_meals(self, data):
        serving_amount = data['serving_amount']
        self.c.execute('SELECT max(meal_reference) FROM meals')
        self.meal_reference = self.c.fetchone()[0]
        self.meal_reference += 1
        self.c.execute('INSERT INTO meals (meal_reference, food_id, serving_amount) values(?, ?, ?)',
                       (self.meal_reference, self.food_id, serving_amount))
        self.conn.commit()

    def user_date(self, username, timestamp):
        username_id = self.db_nutrition.get_user_id(username)
        event_reference = self.c.execute('SELECT reference FROM events WHERE user_id = (?)',
                                         (username_id))
        food_serving = self.c.execute('SELECT food_id, serving_amount FROM meals WHERE Timestamp like (?) and meal_reference = (?)',
                                      (timestamp + '%', event_reference))
        if food_serving is not None:
            user_date = self.c.fetchall()
            print (user_date)
            return user_date
        else:
            print ('That date or user is not valid.')


    def add_period(self, pain, flow_amount):
        self.c.execute('SELECT max(period_reference) FROM periods')
        self.period_reference = self.c.fetchone()[0]
        self.period_reference += 1
        self.c.execute('INSERT  INTO periods (period_reference, pain, flow_amount) values(?, ?, ?)',
                       (self.period_reference, pain, flow_amount))

    def add_sex(self, rating, amount):
        self.c.execute('SELECT max(sex_reference) FROM periods')
        self.sex_reference = self.c.fetchone()[0]
        self.sex_reference += 1
        self.c.execute('INSERT INTO sex_activity (sex_reference, rating, amount) values(?, ?, ?)',
                       (self.sex_reference, rating, amount))

    def add_events(self, username, category):
        username_id = db_nutrition.get_user_id(username)
        if category == 'periods':
            reference = self.period_reference
        if category == 'sex_activity':
            reference = self.sex_reference
        if category == 'meals':
            reference = meals_reference
        self.c.execute('INSERT INTO events (reference, user_id, category) values (?, ?, ?)',
                       (reference, username_id, category))
