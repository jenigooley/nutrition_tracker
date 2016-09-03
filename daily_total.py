import data_nutrition

def get_meals(db, user, date):
    """takes user, date, querys db and creates dict 
    {user_id : serving_amount} """
    
    id_amount = {}
    meals = db.user_date(user, date)
    print meals
    for i_d, amount in meals:
	id_amount[i_d] = amount
    return id_amount

def get_stats_dict(db, id_amount):
    """takes id_amount dict {food_id:serving_amount} and returns a
       dict {food_id:(calories, sugar, fat)} """
    
    stats_dict = {}
    for food_id  in id_amount.keys():
	stats = db.nutrition_query(food_id)
	food_stats = list(stats)
	stats_dict[food_id] = food_stats
    return stats_dict

def get_stats_total(id_amount, stats_dict):
    """takes stats_dict {food_id:[calorie, sugar, fat] and id_amount,
       multiplies each item of stats_dict """
    
    total_calories = 0
    total_fat = 0
    total_sugar = 0
    for food_id, (calories, sugar, fat) in stats_dict.items():
	amount = id_amount[food_id]
	total_calories += calories * amount
	total_sugar += sugar * amount
	total_fat += fat * amount
    return total_calories, total_sugar, total_fat

def main():
    db = data_nutrition.NutritionData()
    date = raw_input('Date you looking for: ')
    user = raw_input('Username are you looking for: ' )
    id_amount = get_meals(db,user, date)
    stats_dict = get_stats_dict(db, id_amount)
    stats_total = get_stats_total(id_amount, stats_dict)
    print stats_total

if __name__ == '__main__':
    main()
