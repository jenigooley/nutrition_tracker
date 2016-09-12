import json
import requests
import pprint
import data_nutrition

results = []
refined_results = []
food_data = {}

def api_call(username, food):
    
    payload = {'results':'0:3',
	    'fields':'item_name,nf_calories,nf_serving_size,nf_sugars,nf_total_fat',
	       'appId':'7f0a2caa',
	       'appKey':'65f3c1d9a1d3c6f7edcf2802023fe069'}
    try:    
	r_search = requests.get(
	'https://api.nutritionix.com/v1_1/search/' + food,  
	params=payload)
    except requests.exceptions.RequestException as e:
	print('there is a connection error.')
	sys.exit(1)   

    r_search = r_search.json()
    results = r_search['hits'] 
    #show user numbered list of top 3 results
    refined_results  = {i: item['fields']['item_name'] 
			     for i, item in enumerate(results)} 


def add_food(username, item, count):
    """take user input and add it to user dictionary"""     
    for i in results:
	if i['fields']['item_name'] == refined_results[item]:
	    food_data.update(i)
    food_data['serving_amount'] = count
    food_data['username'] = username
    food_data.update(food_data['fields'])
    del food_data['fields']
    add_data = data_nutrition.NutritionData()
    add_data.add_nutrition(food_data)
    add_data.meals(food_data)
    return food_data

if __name__ == '__main__':
    api_call()
