import json
import requests
import urllcdcdib
import pprint
from flask import Flask, render_template
from flask import request, redirect


user_item = {}
food = request.ge
payload = {'results':'0:3',
           'fields':'item_name,nf_calories,nf_serving_size,nf_sugars,nf_total_fat',
           'appId':'7f0a2caa',
           'appKey':'65f3c1d9a1d3c6f7edcf2802023fe069'}

print(food)

try:    
    r_search = requests.get('https://api.nutritionix.com/v1_1/search/' + food,  
    params=payload)
except requests.exceptions.RequestException as e:
    #print(e)
    print("there is a connection error.")
    sys.exit(1)   

r_search = r_search.json()
results = [] 
results = r_search['hits']   
print(results)

#show user numbered list of top 3 results
refined_results  = {i: item["fields"] 
for i, item in enumerate(results)} 
pprint.pprint(refined_results)

#take user input and add it to user dictionary 
def item_choice():
    food_item = int(input("Please enter the item number that best matches your food."))
    count= int(input('Number of servings:'))
    
    user_item[food] = [count,refined_results[food_item]]
    print(user_item)

class User():
    def __init_(self, *args, **kwargs):
        for k,v in refined_results.items():
            print(setattr(self, k, v))

if __name__=='__main__':
    app.run(host="", port=8000,debug=True)

#User() 
