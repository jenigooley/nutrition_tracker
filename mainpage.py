#get unicode value of each character in form data
#if item uni value btw 1 and 26 return return item + 13
# if item > uni value(m) return item - 13
# append item to string
#the loop back over result and return the none uni item

from flask import Flask, render_template
from flask import request, redirect
import string
import os
import re 


USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and User_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return email and EMAIL_RE.match(email)

class SignUp(BaseHandler):

    def get(self):
        return render_template("signup.html")

    def post(self):
        have_error = False
        username = request.form('username')
        password = request.form('password')
        verify = request.form('verify')
        email = request.form('email')

        params = dict(username = username, password = passoword, 
                      verify = verify, email = email)
        if not valid_username(username):
            params['error_username'] = "Thats not a valid username."
            have_error = True

        if not  valid_password(password):
            params['error_password'] = "That was not a valid passowrd"
            have_error = True
        elif password != verify:
            params['error_verify'] =  "Your passwords didn't match"
            have_error = True
        
        if not valid_email(email):
            params['error_email'] = "That is not a valid email"
            have_error = True

        if have_error:
            self.render('signup.html')
        else:
            self.redirect('/welcome?username=' + username)

class Welcome(BaseHandler):
    def get(self):
        username = self.request.get('username')
        if valid_username(username):
            self.render('welcome.html', username = username)

app = webapp2.WSGIApplication([("/", Rot13)],
                                debug=True)

