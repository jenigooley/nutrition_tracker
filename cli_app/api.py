from flask import Flask, jsonify, request
import json
import access_logic
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///eats_and_bleeds.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
session = Session()


app = Flask(__name__)


@app.route('/profile/<username>', methods=['GET', 'POST'])
def get_profile(Session, username):
    if request.method == 'GET':
        profiles = {}
        user_stats = access_logic.get_user(username)
        print user_stats
        bmi = access_logic.get_bmi(username)
        profiles.update(bmi)
        profiles.update(user_stats)
        #print ('profiles is', profiles)
        print jsonify(profiles)
        return jsonify(profiles)
    if request.method == 'POST':
        print ("request", request.data)
        input1 = json.loads(request.data)
        access_logic.edit_height(session, username, input1['height'])
        return 'success'

@app.route('/food/<username>', methods=['GET'])
def get_foods(username):
    food = {}
    date = '2016-09-27'
    totals = access_logic.get_food_totals(username, date)
    food.update(totals)
    print jsonify(totals)
    return jsonify(totals)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
