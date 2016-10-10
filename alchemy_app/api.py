from flask import Flask, jsonify, request
import json
import access_logic
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import models
import bmi
import daily_total
from nutri_API import FoodApi

engine = create_engine('sqlite:///eats_and_bleeds.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
session = Session()
nutri = FoodApi()

app = Flask(__name__)


@app.route('/profiles/create', methods=['GET', 'POST'])
def add_profile():
    if request.method == 'POST':
        print('data', request.data)
        #import pdb;pdb.set_trace()
        user_data = json.loads(request.data)
        print user_data
        user = models.Profile(name=user_data.get('name'), password=user_data.get('password'),
                       email=user_data.get('email'), height=user_data.get('height'),
                       weight=user_data.get('weight'))
        session.add(user)
        session.commit()
        return json.dumps(user.as_dict_prof())

@app.route('/profiles/<username>', methods=['GET', 'POST', 'DELETE'])
def get_profile(username):
    if request.method == 'GET':
        profiles = {}
        for profile in session.query(models.Profile).filter(models.Profile.name==username).all():
            print("Dict", profile.as_dict_prof())
            return ("Json", json.dumps(profile.as_dict_prof()))

    if request.method == 'POST':
        print ("request", request.data)
        user_data = json.loads(request.data)
        print ('data', user_data)
        update_prof = session.query(models.Profile).filter_by(name=username).update(user_data)
        session.commit()
        if update_prof >= 1:
            return ('1 record updated {}'.format(user_data))

    if request.method == 'DELETE':
        user_delete = session.query(models.Profile).filter(name=username).delete()
        session.commit()
        if user_delete >= 1:
            return ('Record was deleted')

@app.route('/food/<username>/<food>', methods=['GET', 'POST'])
def get_foods(username, food):
    # if request.method == 'GET':
    #     date = '2016-09-27'
    #     totals = daily_total.main(session, username, date)
    #     print jsonify(totals)
    #     return jsonify(totals)
    if request.method == 'POST':
        print ("request", request.data)
        nutri_query = session.query(models.Nutrition).filter(food == '%food%').all()
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
            category = 'meals'
            id = session.query(models.Profile.id).filter_by(name=username).all()
            print (id)
            user_id=id
            category='meals'
            session.add(food_stuff)
            session.add(user_id, 'meals')
            session.commit()
            return jsonify(models.Nutrition.as_dict_nutr(food_stuff))
        else:
            return 'invalid request '
if __name__ == '__main__':
    app.run(host='0.0.0.0')
