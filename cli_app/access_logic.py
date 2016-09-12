import usermanager
import usermanager
import data_nutrition
import nutri_API
import bmi
import cli_access

db_profiles = usermanager.UserManager()
db_nutrition = data_nutrition.NutritionData()

def input_food(username, food):
    nutri_API.api_call(username, food)

def add_food(item, count):
    food_data = nutri_API.add_food(username, item, count)
    db_nutrition.add_nutrition(food_data)
    print (food_data)

def get_food(food):
   return db_nutrition.nutrition_query
    

def get_food_totals(username, date):
    return db_nutrition.user_date(username, date)
    
def get_bmi(username):
    bmi_stats = db_profiles.bmi_user(username)
    return bmi.bmi(bmi_stats)

def get_user_profile(username):
    print usermanager.read_user(username)

