import data_nutrition
import data_tables

def get_meals(db_events, username, date):
    """takes user, date, querys db and creates dict
    user_id : serving_amount """

    id_amount = {}
    meals = db_events.user_date(username, date)
    if meals is not None:
        for i_d, amount in meals:
            id_amount[i_d] = amount
        return id_amount
    else:
        print ('Invalid request.')
        pass


def get_stats_dict(db, id_amount):
    """takes id_amount dict food_id:serving_amount and returns a
       dict {food_id:(calories, sugar, fat)} """

    stats_dict = {}
    for food_id in id_amount.keys():
        stats = db.nutrition_query(food_id)
        food_stats = list(stats)
        stats_dict[food_id] = food_stats
    return stats_dict


def get_stats_total(id_amount, stats_dict):
    """takes stats_dict {food_id:[calorie, sugar, fat, ...] and id_amount,
       multiplies each item of stats_dict """

    total_calories = 0
    total_fat = 0
    total_sugar = 0
    total_protein = 0
    total_fiber = 0
    total_calcium = 0
    if stats_dict is not None:
        for food_id, (calories, sugar, fat, protein, fiber, calcium) in stats_dict.items():
            amount = id_amount[food_id]
            total_calories += calories * amount
            total_sugar += sugar * amount
            total_fat += fat * amount
            total_protein += protein * amount
            total_fiber += fiber * amount
            total_calcium += calcium * amount
        daily_totals = {'Calories: ': total_calories, 'Sugar': total_sugar,
                        'Fat': total_fat, 'Protein': total_protein,
                        'Fiber': total_fiber, 'Calcium': total_calcium}
        return daily_totals
    else:
        print('Invalid request.')
        pass


def main(username, date):

    db = data_nutrition.NutritionData()
    db_events = data_tables.DataTables()
    id_amount = get_meals(db_events, username, date)
    stats_dict = get_stats_dict(db, id_amount)
    stats_total = get_stats_total(id_amount, stats_dict)
    return stats_total

if __name__ == '__main__':
    main()
