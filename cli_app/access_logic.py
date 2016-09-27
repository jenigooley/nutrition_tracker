import usermanager
import data_events
import data_nutrition
import nutri_API
import bmi
import cli_access
import daily_total
from dateutil import parser
import sqlite3

conn = sqlite3.connect('./eats_and_bleeds.db')
db_profiles = usermanager.UserManager(conn)
db_nutrition = data_nutrition.NutritionData(conn)
db_events = data_events.DataEvents(conn)
nutri_api = nutri_API.FoodApi()


def input_food(username, food):
    nutri_api.api_call(username, food)


def add_food(username, item, count):
    food_item = db_nutrition.query_food_item(item)
    category = 'meals'
    if food_item:
        db_events.add_meals(food_id, count)
        db_events.add_events_meals(username, category)
    else:
        food_data = nutri_api.add_food(username, item, count)
        food_id = db_nutrition.add_nutrition(food_data)
        db_events.add_meals(food_id, count)
        db_events.add_events_meals(username, category)


def get_user(username):
    user_deets = db_profiles.read_user(username)
    profile_dict = {}
    user_id, username, password, email, height, weight = user_deets
    profile_dict = {
        'user_id': user_id,
        'username': username,
        'password': password,
        'email': email,
        'height': height,
        'weight': weight
    }
    return profile_dict


def edit_height(username, height):
    db_profiles.update_height(username, height)


def edit_weight(username, weight):
    db_profiles.update_weight(username, weight)


def delete_user(username):
    db_profiles.remove_user(username)


def get_food_totals(username, date):
    return daily_total.main(conn, str(username), str(date))


def get_bmi(username):
    stats = db_profiles.user_bmi(username)
    return bmi.view_bmi(*stats)


def add_events_meals(category):
    category = 'meals'
    db_events.add_event_meals(category)


def add_events_periods(pain_num, flow_num):
    db_events.add_periods(pain_num, flow_num)


def add_events_sex(rate_num, amount_num):
    db_events.add_sex(rate_num, amount_num)


def add_events_data(username, category):
    if category == '1':
        category = 'periods'
        db_events.add_events(username, category)
    if category == '2':
        category = 'sex_activity'
        db_events.add_events(username, category)
