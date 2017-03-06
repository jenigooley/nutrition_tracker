import models


def get_meals(session, username, date):
    """creates dict with food_id : serving_amount """

    id_amount = {}
    meals_query = session.query(models.Profile, models.Meal).filter(models.Profile.id).filter(models.Profile.name==username ).filter(models.Meal.user_id==models.Profile.id).all()
    meals_query.as_dict_meals()
    id_amount[food_id] = serving_amount
    print ('id_amount', id_amount)
    session.commit()
    return id_amount
    # meals = db_events.user_date(username, date)



def get_stats_dict(session, id_amount):
    """takes id_amount dict food_id:serving_amount and returns a
       dict {food_id:(calories, sugar, fat)} """
    stats_list = []
    stats_dict = {}
    for food_id in id_amount.iteritems():
        for item in session.query(models.Nutrition).filter(models.Nutrition.id).all():
            nutr = item.as_dict_nutr()
            stats_dict[id_amount[food_id]] = nutr
    print('stats', stats_dict)
    #     stats_dict[food_id] = food_stats
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
        for food_id, list_stats in stats_dict:
            print('food', list_stats)
            for item in list_stats:
                print ('item', item)
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
        print (daily_totals)
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
