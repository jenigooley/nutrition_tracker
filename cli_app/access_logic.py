import usermanager
import data_tables
import data_nutrition
import nutri_API
import bmi
import cli_access
import daily_total
from dateutil import parser

db_profiles = usermanager.UserManager()
db_nutrition = data_nutrition.NutritionData()
db_events = data_tables.DataTables()

nutri_api = nutri_API.FoodApi()


def input_food(username, food):
    nutri_api.api_call(username, food)


def add_food(username, item, count):
    food_data = nutri_api.add_food(username, item, count)
    db_nutrition.add_nutrition(food_data)
    db_nutrition.add_meals(food_data)


def get_user(username):
    user_deets = db_profiles.read_user(username)
    profile_dict = {}
    username, password, email, height, weight = user_deets
    profile_dict = {
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
    return daily_total.main(str(username), str(date))


def get_bmi(username):
    stats = db_profiles.user_bmi(username)
    return bmi.view_bmi(*stats)

def add_events_data(username, category, pain, flow_amount, rating, amount):
    if input_events == 1:
        db_events.add_period(pain, flow_amount)
    if inpur_events == 2:
        db_events.add_sex(rating, amount)
    db_events.add_events(username, category)
