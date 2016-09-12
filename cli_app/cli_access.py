import access_logic

def welcome_user(username):
    action_list = [ 'add_food', 'get food totals', 'see food data', 
		    'edit profile', 'get bmi']     
    print (action_list)
    for num, item in enumerate(action_list, start=1):
	print (num, item)
    action = raw_input('What would you like to do ' + username + '? ')
    print(action)
    welcome(username, action)
    
def welcome(username, action):
    print ('foo')
    if action == '1':
	input_food_item(username)
	add_food_item(username)
    if action == '2':
	show_food_totals(username)
    if action == '3':
	show_food(username)
    if action == '4':
	    pass
    if action == '5':
	show_bmi(username)

def input_food_item(username):
    food = raw_input('Please enter a food: ')
    access_logic.input_food(username, food)

def add_food_item(username):
    item = raw_input('Enter the number that best matches your food: ')
    count = raw_input('Enter the amount of servings: ')
    access_logic.add_food(username, item, count)

def show_food(username):
    food = raw_input('Which food would you like to get stats on?')
    print (food + show_food(food))

def show_food_totals(username):
    date = raw_input('What date would you like to totals for?')
    print (access_logic.get_food_totals(username, date))

def show__bmi(username):
    print ('Current BMI is ' + access_logic.get_bmi)
