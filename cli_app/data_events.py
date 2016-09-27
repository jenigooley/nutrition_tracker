import sqlite3
import data_nutrition


class DataEvents():
    """manage all tables with specific event data"""

    def __init__(self, conn):
        self.conn = conn
        self.c = self.conn.cursor()

    def add_meals(self, food_id, count):
        self.c.execute('INSERT INTO meals (food_id, serving_amount) values(?, ?)',
                       (food_id, count))
        self.c.execute('SELECT last_insert_rowid() FROM meals')
        self.meal_ref = self.c.fetchone()[0]
        self.conn.commit()
        print 'insert meals complete'

    def user_date(self, username, timestamp):
        self.c.execute("SELECT serving_amount, food_id FROM profiles INNER JOIN  events INNER JOIN meals ON user_id=(?) AND id =user_id and meals. timestamp like (?)", (username, timestamp + '%'))
        amount_food = self.c.fetchone()[0]
        # self.c.execute('SELECT id FROM profiles where NAME = (?)',
        #                (username,))
        # username_id = self.c.fetchone()[0]
        # print username_id
        # user_event = self.c.execute('SELECT reference FROM events WHERE user_id = (?)',
        #                                  (username_id,))
        # print user_event
        #
        # if user_event is not None:
        #     event_reference = self.c.fetchone()[0]
        #     food_serving = self.c.execute('SELECT food_id, serving_amount FROM meals WHERE Timestamp like (?) and meal_reference = (?)',
        #                                   (timestamp + '%', event_reference))
        #     if food_serving is not None:
        #         user_date = self.c.fetchall()
        #         print (user_date)
        #         return user_date
        #     else:
        #         print ('There is not meal data for that date and user')
        # else:
        #     print ('There is no food data for that date and user')

    def add_periods(self, pain_num, flow_num):
        self.c.execute('INSERT  INTO periods (pain, flow_amount) values(?, ?)',
                       (pain_num, flow_num))
        self.c.execute('SELECT last_insert_rowid() FROM periods')
        self.period_ref = self.c.fetchone()[0]
        self.conn.commit()
        print ('period insert complete')

    def add_sex(self, rate_num, amount_num):
        self.c.execute('INSERT INTO sex_activity (rating, amount) values(?, ?)',
                       (rate_num, amount_num))
        self.c.execute('SELECT last_insert_rowid() FROM sex_activity')
        self.sex_ref = self.c.fetchone()[0]
        self.conn.commit()
        print ('sex insert completed')


    def add_events_meals(self, username, category):
        self.c.execute('SELECT id FROM profiles where NAME = (?)',
                                 (username,))
        user_id = self.c.fetchone()[0]
        reference = self.meal_ref
        print (reference)
        print (user_id)
        print(category)
        self.c.execute('INSERT INTO events (reference, user_id, category) values (?, ?, ?)',
                       (reference, user_id, category))
        self.conn.commit()
        print ('meal event insert completed')

    def add_events(self, username, category):
        user_id = self.c.execute('SELECT id FROM profiles where NAME = (?)',
                                 (username,))
        username_id = self.c.fetchone()[0]
        print username_id
        print category
        if category == 'periods':
            reference = self.period_ref
            print reference
            # self.c.execute('INSERT INTO events (reference, user_id, category) values (?, ?, ?)',
            #                (reference, username_id, category))
            # print ('event insert completed')

        elif category == 'sex_activity':
            reference = self.sex_ref
            print reference
        self.c.execute('INSERT INTO events (reference, user_id, category) values (?, ?, ?)',
                      (reference, username_id, category))
        print ('event insert completed')

        self.conn.commit()
