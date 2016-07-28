from flask import Flask, render_template
from flask import request, redirect

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/signup', methods = ['POST'])
def signup():
    email = request.form['email']
    print("The email address is '" + email + "'")
    month = request.form[ "month"]
    day = request.form["day"]
    year = request.form["year"]
    print("The birthday is " + month + " " + day + " " +  year)
    months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]
    abr_month = dict((m[:3].lower(),m)for m in months)
    def valid_month(month):
        if month:
            short_month = month[:3].lower()
            return abr_month.get(short_month)
            
    def valid_day(day):
        if day.isdigit() == True:
            day = int(day)
        if day in range(1,32):
            return day

    def valid_year(year):
        if year.isdigit() == True:
            year = int(year)
        if year in range(1900,2021):
            return year

    user_month = valid_month(month)
    user_day = valid_day(day)
    user_year = valid_year(year)
    if (user_month and user_day and user_year):
         return render_template('right.html')
    else:
       # print ((month + " " + day + " " +  year + " is a totally date!")
        return render_template('wrong.html')

if __name__ == '__main__':
    app.run(host="", port=8080,debug=True)
