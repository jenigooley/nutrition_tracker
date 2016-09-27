import access_logic
import usermanager
import bmi


def welcome_user(username):
    action_list = ['add_food', 'get food totals',
                   'add event', 'edit profile',
                   'get bmi', 'view user profile']
    print (action_list)
    for num, item in enumerate(action_list, start=1):
        print (num, item)
    action = raw_input('What would you like to do ' + username + '? ')
    welcome(username, action)


def welcome(username, action):
    if action == '1':
        input_food_item(username)
        add_food_item(username)
    if action == '2':
        show_food_totals(username)
    if action == '3':
        input_events(username)
    if action == '4':
        edit_user(username)
    if action == '5':
        show_bmi(username)
    if action == '6':
        show_user_profile(username)


def input_food_item(username):
    food = raw_input('Please enter a food: ')
    access_logic.input_food(username, food)


def add_food_item(username):
    item = raw_input('Enter the number that best matches your food: ')
    count = raw_input('Enter the amount of servings: ')
    access_logic.add_food(username, item, count)


def show_food_totals(username):
    date = raw_input('What date would you like the totals for? ')
    print (access_logic.get_food_totals(username, date))


def edit_user(username):
    edit_list = ['update height', 'update weight', 'remove user']
    for num, item in enumerate(edit_list, start=1):
        print (num, item)
    edit_action = raw_input('What would you like to do? ')
    if edit_action == '1':
        height = raw_input('What is your current height? ')
        access_logic.edit_height(username, height)
        print ('Your height is now ', height)
    if edit_action == '2':
        weight = raw_input('What is your current weight? ')
        access_logic.edit_weight(username, weight)
        print ('Your weight is now ', weight)
    if edit_action == '3':
        confirm = raw_input('Are you sure you want to delete this user? (y/n) ')
        if confirm == 'y':
            access_logic.delete_user(username)
            print ("You have been deleted.")
        else:
            print ('boy, bye')


def show_bmi(username):
    print (access_logic.get_bmi(username))


def show_user_profile(username):
    user_deets = access_logic.get_user(username)
    print user_deets


def input_events(username):
    category = raw_input('What type of event would you like to enter, (1)period or (2)sexual activity?')
    if category == '1':
        pain_num = raw_input('How severe was your pain today, on a scale of 1-5? ')
        flow_num = raw_input('How plentiful was your flow today, on a scale of 1-5? ')
        access_logic.add_events_periods(pain_num, flow_num)
        access_logic.add_events_data(username, category)
    if category == '2':
        rate_num = raw_input('How did you feel about your sexual existence today, on a scale of 1-5 ')
        amount_num = raw_input('How many sexual expierences did you have today? ')
        access_logic.add_events_sex(rate_num, amount_num)
        access_logic.add_events_data(username, category)
