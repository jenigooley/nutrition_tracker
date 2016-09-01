import data_nutrition


def daily_count():
    date = raw_input('Date you looking for: ')
    user = raw_input('Username are you looking for: ' )
    total = data_nutrition.NutritionData()
    nutrition_in_day = total.daily_total(user, date)
    print(nutrition_in_day)
    
    
if __name__ == '__main__':
    daily_count()
