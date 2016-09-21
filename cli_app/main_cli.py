import os
import re
import usermanager
import data_nutrition
import bmi

def valid_username(username, have_error):
    USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    if not  USER_RE.match(username):
        have_error = True
    return have_error
def valid_password(password):
    PASS_RE = re.compile(r"^.{3,20}$")
    if not PASS_RE.match(password):
        have_error = True
    return have_error


def valid_email(email):
    EMAIL_RE = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
    if not EMAIL_RE.match(email):
        have_error = True
    return have_error


def signup(db, username, password, email, have_error):
    if have_error:
        print('/signup')

    else:
        db = user_create.create_user(username, password, email)
        print('/welcome?username=' + username)


def get_bmi(db, username):
    bmi_data = db.bmi_user(username)
    bmi = bmi.get_bmi(bmi_data)
    return bmi


def remove(db, username, confirm_remove):
    db.remove_user(username)
    if confirm_remove == 'y':
        if user_remove.remove_user(username) == True:
            print('/success')
        else:
            print('/error')
    else:
        print ('ok, nevermind')


def read(db, username):
    if username:
        db.read_user(username)
    else:
        print('/error')


def main():

    db = usermanager.Usermanager()
    username = raw_input('Please enter username: ')
    have_error = False
    password = raw_input('Password: ')
    verify = raw_input('Verify: ')
    email = raw_input('Email: ')
    height = raw_input('height: ')
    weight = raw_input('Weight: ')
    confirm_remove = raw_input('Are you sure you want to remove'
    + username + '(, y/n)?')
