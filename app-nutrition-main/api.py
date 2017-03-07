from flask import Flask, jsonify, request
import json
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import models
import bmi
import daily_total
from nutri_API import FoodApi
from time import strftime, strptime
import datetime
from sqlalchemy import Date, cast

engine = create_engine('sqlite:///eats_and_bleeds.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
session = Session()
nutri = FoodApi()

app = Flask(__name__)


@app.route('/users/create', methods=['POST'])
def add_user():

    user_data = request.json
    print('data', user_data)
    user = models.User(name=user_data.get('name'),
                       password=user_data.get('password'),
                       email=user_data.get('email'),
                       height=user_data.get('height'),
                       weight=user_data.get('weight'))
    session.add(user)
    session.commit()
    print "SUCCESS"
    return json.dumps(user.as_dict_user())


@app.route('/users/<username>', methods=['GET', 'PUT', 'DELETE'])
def get_user(username):
    '''get user profile json'''

    if request.method == 'GET':
        users = {}
        for user in session.query(models.User).filter(models.User.name==username).all():
            print("Dict", user.as_dict_user())
            return (json.dumps(user.as_dict_user()))

    if request.method == 'PUT':
        print ("request", request.json)
        update_user = session.query(models.User).filter_by(name=username).update(user_data)
        session.commit()
        if update_prof >= 1:
            return ('1 record updated {}'.format(user_data))

    if request.method == 'DELETE':
        user_delete = session.query(models.User).filter(name=username).delete()
        session.commit()
        if user_delete >= 1:
            return ('Record was deleted')


@app.route('/food/<username>', methods=['POST'])
def get_food_nutriton(username):
    '''add food item'''
    
    if request.method == 'POST':
        data = request.json
        print data        # print data
        food = data['food']
        top_three = nutri.api_call(username, food)
        print top_three
        return(json.dumps(top_three))


@app.route('/food/<username>/count', methods=['POST'])
def get_nutrition_count(username):
    if request.method == 'POST':
        data = request.json
        choice = data["choice"]
        print ('CHOICE', choice)
        count = data["count"]
        food_data = nutri.add_food(username, choice, count)
        print ('FOOD stuff', food_data)

        food_stuff = models.Nutrition(food=food_data.get('item_name'),
                                      Calories=food_data.get('nf_calories'),
                                      Sugar=food_data.get('nf_sugars'),
                                      Fat=food_data.get('nf_total_fat'),
                                      Protein=food_data.get('nf_protein'),
                                      Fiber=food_data.get('nf_dietary_fiber'),
                                      Calcium=food_data.get('nf_calcium_dv'))
        id = session.query(models.User.id).filter_by(name=username).first()
        user_id = id
        category = 'meals'
        session.add(food_stuff)
        # session.add(user_id, 'meals')
        session.commit()
        event_stuff = models.Event(user_id=str(user_id), category='meals')
        print event_stuff.id
        print event_stuff
        session.add(event_stuff)
        meal_stuff = models.Meal(food_id=food_stuff.id, serving_amount=count, event_id=event_stuff.id)
        session.add(meal_stuff)
        session.commit()

        return json.dumps(models.Nutrition.as_dict_nutr(food_stuff))
        # else:
#     return 'invalid request '

@app.route('/events/<username>', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def events(username):
    '''create, read, update or delete event data'''

    if request.method == 'POST':
        event_data = request.json
        category = event_data['category']
        print('CATEGORY', category)
        # date = event_data['date']
        user_id = session.query(models.User.id).filter_by(name=username).first()
        print user_id[0]
        event_obj = models.Event(category=category, user_id=user_id[0])
        session.add(event_obj)

        if category == 'period':
            specific_event = models.Period(flow_amount=event_data.get('flow_amount'),
                                           pain=event_data.get('pain'),
                                            event=event_obj)
            specific_event_dict = models.Period.as_dict_period(specific_event)

        if category == 'sex_activities':
            specific_event = models.SexActivity(rating=event_data.get('rating'),
                                                amount=event_data.get('amount'),
                                                event=event_obj)
            specific_event_dict = models.SexActivity.as_dict_sex_activity(specific_event)

        session.add(specific_event)
        session.commit()
        return json.dumps(specific_event_dict)

    if request.method == 'GET':
        date = request.args.get('date')
        category = request.args.get('category')
        user_id = session.query(models.User.id).filter_by(name=username).first()
        print ("EVENT", category)
        start_time = datetime.datetime.strptime(date, '%m-%d-%Y')
        delta = datetime.timedelta(hours=23, minutes=59, seconds=59)
        end_time =  (start_time + delta)
        print ('DATE', date)
        print ('USER',user_id[0])
        print ('start_time', start_time)
        print ('END_time', end_time)
        print ('DELTA', delta)
        query_results =[]
        for event in session.query(models.Event).filter(models.Event.user_id==user_id[0],
                                                        models.Event.category==category,
                                                        models.Event.date_time >= start_time,
                                                        models.Event.date_time <= end_time):

            print ('EVENT DICT', event.as_dict_events())

            query_results.append(event.as_dict_events())
        return json.dumps(str(query_results))

    if request.method == 'DELETE':
        user_id = session.query(models.User.id).filter_by(name=username).first()
        event_delete = session.query(models.Event).filter(user_id=user_id[0]).delete()
        session.commit()
        if event_delete >= 1:
            return ('Record was deleted')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
#
# curl -H "Content-Type: application/json" -X POST -d '{"food":"beets"}'  http://localhost:5000/food/jeni
