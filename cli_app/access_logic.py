import usermanager
import usermanager
import data_nutrition
import nutri_API
import bmi
import cli_access
import daily_total

db_profiles = usermanager.UserManager()
db_nutrition = data_nutrition.NutritionData()
nutri_api = nutri_API.FoodApi()

def input_food(username, food):
    nutri_api.api_call(username, food)

def add_food(username, item, count):
    food_data = nutri_api.add_food(username, item, count)
    db_nutrition.add_nutrition(food_data)
    db_nutrition.add_meals(username, food_data)

def edit_height(username, height):
    db_profiles.update_height(username, height)

def edit_weight(username, weight):
    db_profiles.update_weight(username, weight)
    print ('Your weight is now ', weight)

def delete_user(username):
    db_profiles.remove_user(username)

def get_food_totals(username, date):
   return daily_total.main(username, date)

def get_bmi(username):
    stats =  db_profiles.user_bmi(username )
    return bmi.view_bmi(*stats)
