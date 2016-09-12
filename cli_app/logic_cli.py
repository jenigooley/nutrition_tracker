import usermanager
import re
import data_nutrition
import bmi
import logic_cli
import pprint
import cli_access

db = usermanager.UserManager()

LOGGED_IN = 1
WRONG_PASSWORD = 2
NEW_USER = 3

def verify_login(username, password):
    login_username = db.verify_user(username)
    login_password = db.verify_password(username, password)

    if login_username and login_password:
	return LOGGED_IN

    elif login_username and not login_password:
	return WRONG_PASSWORD
    
    elif not  login_username and not login_password:
	return NEW_USER

def confirm_signup(confirm):
    return confirm.lower() == 'y'
	
def validate_password(password, verify):
    pass_re = re.compile(r"^.{3,50}$")
    if pass_re.match(password) and password == verify:
	return True

def validate_email(email):
    email_re = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
    if  email_re.match(email):
	return True

def signup_user(username, password, email, height, weight):
    if validate_password and validate_email  :
	db.create_user(username, password, email, height, weight)
	return True

def access_granted(username):
    if verify_login == LOGGED_IN or signup_user:	
	cli_access.welcome_user(username)

