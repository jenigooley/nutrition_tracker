import os
import re 
import usermanager


USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return email and EMAIL_RE.match(email)


def signup():
    have_error = False
    username = raw_input('username: ')
    password = raw_input('password: ')
    verify = raw_input('verify: ')
    email = raw_input('email: ')
    
    if not valid_username(username):
	have_error = True

    if not  valid_password(password):
	have_error = True
    
    elif password != verify:
	have_error = True
    
    if not valid_email(email):
	have_error = True

    if have_error:
	print('signup.html')
    
    else:
	user_create = usermanager.UserManager()
	user_create.create_user(username, password, email)
	print('/welcome?username='+ username)
	

    
def remove():
    username = raw_input('remove username:')
    user_remove = usermanager.UserManager()
    user_remove.remove_user(username)
    if user_remove.remove_user(username) == True:
	print('/success')
    else:
       print('/error') 


def read():
    username = raw_input('username: ')
    if username:
	user_read = usermanager.UserManager()
	user_read.read_user(username)
    
    else:
	print('/error')


print read()
