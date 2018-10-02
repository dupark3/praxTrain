# $ export FLASK_APP=app.py           lets the terminal know to use flask app
# $ flask run OR python -m flask run    optional flag --host=0.0.0.0 to listen to other IPs
# $ export FLASK_ENV=development        code changes refreshed

from flask import Flask, redirect, url_for, request, render_template

from app import app # app.py
import spreadsheet # spreadsheet.py
import admininfo # admininfo.py

import datetime
import sqlite3
from werkzeug.security import check_password_hash

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = ""
        try:
            firstName = request.form['firstName']
            lastName = request.form['lastName']
            email = request.form['email']
            
            con = sqlite3.connect("database.db")
            cur = con.cursor()
            cur.execute('''INSERT INTO subscribers (firstName, lastName, email)
                VALUES (?,?,?)''',(firstName, lastName, email) )
            con.commit()
            msg = "Record successfully added"
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

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST' and request.form['username'] == admininfo.username and check_password_hash(admininfo.pw_hash, request.form['password']):
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        cur.execute('SELECT * FROM subscribers')
        rows = cur.fetchall()
        con.close()
        return render_template('admin.html', rows=rows)
    else:
        return render_template('adminlogin.html')

if __name__ == '__main__':
    app.run()