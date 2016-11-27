import data_nutrition
import data_events

# def get_tuple(db_events, username, date):
#     print ('get_tuple is starting')
#     id_amount_tuple = db_events.user_date(username, date)
#     print ('IAT', id_amount_tuple)
#     if id_amount_tuple != []:
#         meals = id_amount_tuple
#         print ('meals', meals)
#         return meals
#     else:
#         print ('There is no data for that date or user')


def get_meals(session, username, date):
    """creates dict with user_id : serving_amount """

    id_amount = {}
    for food_id, serving_amount in session.query(models.Profile, models.meals).filter(models.Profile.id).filter(models.Profile.user_id==username ).filter(models.Meal.user_id==models.Profile.user_id).all()
        id_amount[food_id] = serving_amount
        print ('id_amount', id_amount)
        session.commit()
        return id_amount
    # meals = db_events.user_date(username, date)
    print ('meals', meals)
    # if meals is not None:
    #id_amount = dict(meals)
    # if meals is not None:
    #     for i_d, amount in meals:

    # else:
    #     print ('Invalid request.')
    #     pass

def get_stats_dict(session, id_amount):
    """takes id_amount dict food_id:serving_amount and returns a
       dict {food_id:(calories, sugar, fat)} """

    stats_dict = {}
    for food_id in id_amount.keys():
        stats =
        print ('stats', stats)
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


def main(session, username, date):
    id_amount = get_meals(session, username, date)
    stats_dict = get_stats_dict(session, id_amount)
    stats_total = get_stats_total(id_amount, stats_dict)
    return stats_total

if __name__ == '__main__':
    main()
