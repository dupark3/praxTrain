# $ export FLASK_APP=app.py           lets the terminal know to use flask app
# $ flask run OR python -m flask run    optional flag --host=0.0.0.0 to listen to other IPs
# $ export FLASK_ENV=development        code changes refreshed

from flask import Flask, redirect, url_for, request, render_template
from app import app
import datetime
import sqlite3

import spreadsheet # spreadsheet.py


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = ""
        try:
            msg = "Record successfully added"
            firstName = request.form['firstName']
            lastName = request.form['lastName']
            email = request.form['email']
            print("TEST")
            con = sqlite3.connect("app/database.db")
            cur = con.cursor()
            cur.execute('''INSERT INTO subscribers (firstName, lastName, email)
                VALUES (?,?,?)''',(firstName, lastName, email) )
            con.commit()
        except:
            con.rollback()
            msg = "error in insert operation"
        finally:
            return render_template('subscribed.html', msg=msg)
            con.close()
    
    # METHOD = 'GET'    
    else:
        # find today's date and find the index to print
        indexZero = datetime.date(2018,9,14)
        today = datetime.date.today()
        indexToday = (today - indexZero).days

        # show tomorrow's post starting at 8pm
        timeNow = datetime.datetime.now()
        if timeNow.hour >= 24:
            indexToday += 1
        
        # Refresh gspreads API credentials every 45 minutes (2700 seconds)
        if (spreadsheet.lastRefreshTime - timeNow).seconds > 2700:
            spreadsheet.refreshKey()

        return render_template('index.html', 
                               records=spreadsheet.getSpreadsheet(), 
                               indexToday=indexToday)

@app.route('/subscribed', methods=['GET'])
def subscribed():
    return render_template('subscribed.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()