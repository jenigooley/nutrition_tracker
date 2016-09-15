import json
import requests
import pprint
import sys


class FoodApi():
    
    def __init__(self):
	self.results = []
	self.refined_results = {}
	self.food_data = {}

    def api_call(self, username, food):
	
	payload = {'results':'0:3',
		    'fields':'*',
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
	self.results = r_search['hits'] 
	print (self.results)
	"""show user numbered list of top 3 results"""
	self.refined_results  = {i: item['fields']['item_name'] 
				 for i, item in enumerate(self.results)} 
	pprint.pprint (self.refined_results)

    def add_food(self, username, item, count):
	"""take user input and add it to user dictionary"""     
	
	item = int(item)
	for i in self.results:
	    #print(i['fields']['item_name'], refined_results[item])
	    if i['fields']['item_name'] == self.refined_results[item]:
		self.food_data.update(i)

	self.food_data['serving_amount'] = count
	self.food_data.update(self.food_data['fields'])
	del self.food_data['fields']
	print (self.food_data)
	return self.food_data
	
if __name__ == '__main__':
    FoodApi()
