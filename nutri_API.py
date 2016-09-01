import json
import requests
import pprint
import data_nutrition


    
food_data = {}
username = raw_input('Please enter Username: ')
food = raw_input('Please enter a food: ')
payload = {'results':'0:3',
	    'fields':'item_name,nf_calories,nf_serving_size,nf_sugars,nf_total_fat',
	       'appId':'7f0a2caa',
	       'appKey':'65f3c1d9a1d3c6f7edcf2802023fe069'}

def api_call():
    try:    
	r_search = requests.get(
	'https://api.nutritionix.com/v1_1/search/' + food,  
	params=payload)
    except requests.exceptions.RequestException as e:
	print('there is a connection error.')
	sys.exit(1)   

    r_search = r_search.json()
    results = [] 
    results = r_search['hits'] 
    #show user numbered list of top 3 results
    refined_results  = {i: item['fields']['item_name'] 
			     for i, item in enumerate(results)} 
    pprint.pprint(refined_results)

    #take user input and add it to user dictionary 
    item = int(input(
		'Please enter the item number that best matches your food.'))
    count= int(input('Number of servings:'))
    for i in results:
	if i['fields']['item_name'] == refined_results[item]:
	    food_data.update(i)
    food_data['serving_amount'] = count
    food_data['username'] = username
    food_data.update(food_data['fields'])
    del food_data['fields']
    print(food_data)
    add_data = data_nutrition.NutritionData()
    add_data.add_nutrition(food_data)
    add_data.meals(food_data)

if __name__ == '__main__':
    api_call()
