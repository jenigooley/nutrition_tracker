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

@app.route('/food/<username>/<food>', methods=['GET', 'POST'])
def foods(username, food):
    # if request.method == 'GET':
    #     date = '2016-09-27'
    #     totals = daily_total.main(session, username, date)
    #     print jsonify(totals)
    #     return jsonify(totals)
    if request.method == 'POST':
        print ("request", request.json)
        nutri_query = session.query(models.Nutrition).filter(food == '%' + food + '%').all()
        print ('QUERY', nutri_query)
        if nutri_query == []:
            count_choice = json.loads(request.data)
            # {"count": 1, "choice": 3}
            choice = count_choice["choice"]
            count = count_choice["count"]
            nutri.api_call(username, food)
            food_data = nutri.add_food(username, choice, count)
            print ('FOOD stuff', food_data)

            food_stuff = models.Nutrition(food=food_data.get('item_name'),
                                          Calories=food_data.get('nf_calories'),
                                          Sugar=food_data.get('nf_sugars'),
                                          Fat=food_data.get('nf_total_fat'),
                                          Protein=food_data.get('nf_protein'),
                                          Fiber=food_data.get('nf_dietary_fiber'),
                                          Calcium=food_data.get('nf_calcium_dv'))
            id = session.query(models.User.id).filter_by(name=username).all()
            print (id)
            user_id = id
            category = 'meals'
            session.add(food_stuff)
            session.add(user_id, 'meals')
            session.commit()
            return json.dumps(models.Nutrition.as_dict_nutr(food_stuff))
        else:
            return 'invalid request '

@app.route('/events/<username>/<category>', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def events(username, category):
    '''create, read, update or delete event data'''

    if request.method == 'POST':
        event_data = request.json
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
        event_data = request.json
        print ("DATA", event_data)
        print ("EVENT", category)
        user_id = session.query(models.User.id).filter_by(name=username).first()
        date = event_data['date']
        date_object = strptime(date, '%m-%d-%Y')
        print ('DATEOBJ', date_object)
        print ('DATE', date)
        print ('USER',user_id[0])
        query_results =[]
        for event in session.query(models.Event).filter(models.Event.user_id==user_id[0], models.Event.category==category, models.Event.date_time==date_object).all():
            print ('EVNET DICT', event.as_dict_events())
            query_results.append(event.as_dict_events())
        return json.dumps(query_results)

    if request.method == 'DELETE':
        user_id = session.query(models.User.id).filter_by(name=username).first()
        event_delete = session.query(models.Event).filter(user_id=user_id[0]).delete()
        session.commit()
        if event_delete >= 1:
            return ('Record was deleted')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
