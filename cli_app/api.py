from flask import Flask, jsonify
import access_logic

app = Flask(__name__)


@app.route('/profile/<username>', methods=['GET'])
def get_profile(username):
    profiles = {}
    user_stats = access_logic.get_user(username)
    print user_stats
    bmi = access_logic.get_bmi(username)
    profiles.update(bmi)
    profiles.update(user_stats)
    print jsonify(profiles)
    return jsonify(profiles)


@app.route('/food/<username>', methods=['GET'])
def get_foods(username):
    food = {}
    date = '2016-08-31'
    totals = access_logic.get_food_totals(username, date)
    food.update(totals)
    print jsonify(totals)
    return jsonify(totals)


if __name__ == '__main__':
    app.run()
