# $ export FLASK_APP=app.py           lets the terminal know to use flask app
# $ flask run OR python -m flask run    optional flag --host=0.0.0.0 to listen to other IPs
# $ export FLASK_ENV=development        code changes refreshed

from flask import Flask, redirect, url_for, request, render_template

from app import app # app.py
import spreadsheet # spreadsheet.py
import admininfo # admininfo.py
import dailyemail

import datetime, sqlite3, threading, re
from werkzeug.security import check_password_hash
from itsdangerous import URLSafeSerializer

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', 
                records=spreadsheet.getSpreadsheet(), 
                indexToday=spreadsheet.getTodayIndex())

@app.route('/recent', methods=['GET'])
def recent():
    return render_template('recent.html', 
                           records=spreadsheet.getSpreadsheet(), 
                           indexToday=spreadsheet.getTodayIndex())    

@app.route('/subscribed', methods=['POST'])
def subscribed():
    msg = ""
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    email = request.form['email'].lower()
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return render_template('subscribed.html', 
            msg="Invalid email address. Please try again.", 
            records=spreadsheet.getSpreadsheet(), 
            indexToday=spreadsheet.getTodayIndex())
    elif firstName == '':
        return render_template('subscribed.html', 
            msg="Please enter a first name.", 
            records=spreadsheet.getSpreadsheet(), 
            indexToday=spreadsheet.getTodayIndex())
    elif lastName == '':
        return render_template('subscribed.html', 
            msg="Please enter a last name.", 
            records=spreadsheet.getSpreadsheet(), 
            indexToday=spreadsheet.getTodayIndex())
    try:
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        
        # Check if email already exists
        cur.execute('''SELECT * FROM subscribers WHERE email="{}"'''.format(email))
        rows = cur.fetchall()
        if rows:
            if rows[0][4] == 0:
                msg = "This email is already subscribed. A new confirmation email has been sent."
                dailyemail.send_confirmation(email)
            elif rows[0][4] == 1:
                msg = "This email has already been subscribed and confirmed."
            return render_template('subscribed.html', msg=msg, records=spreadsheet.getSpreadsheet(), 
                               indexToday=spreadsheet.getTodayIndex())

        # Email does not exist, insert into table
        cur.execute('''INSERT INTO subscribers (firstName, lastName, email)
            VALUES (?,?,?)''',(firstName, lastName, email) )
        con.commit()
        msg = "You have been successfully subscribed. Please check your email for a confirmation email."
    except:
        con.rollback()
        msg = "There was an error in your subscription."
    finally:
        dailyemail.send_confirmation(email)
        return render_template('subscribed.html', msg=msg, records=spreadsheet.getSpreadsheet(), 
                           indexToday=spreadsheet.getTodayIndex())
        con.close()

@app.route('/unsubscribe/<token>', methods=['GET'])
def unsubscribe(token):
    serializer = URLSafeSerializer(admininfo.secret_key, salt=admininfo.unsubscribe_salt)
    # add try-catch statement here with itsdangerous.BadData
    email = serializer.loads(token)

    # Check if valid unsubscribe url
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return render_template('subscribed.html', 
            msg="Invalid URL. Please check your unsubscribe email address again. Contact the admin if unable to unsubscribe.", 
            records=spreadsheet.getSpreadsheet(), 
            indexToday=spreadsheet.getTodayIndex())
    msg = ""
    try:
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        cur.execute('''DELETE FROM subscribers 
            WHERE email="{}";'''.format(email))
        con.commit()
        msg = email + " has been successfully unsubscribed from PraxTrain."
    except:
        con.rollback()
        msg = "There was an error in your unsubscription."
    finally:
        return render_template('subscribed.html', msg=msg, records=spreadsheet.getSpreadsheet(), 
                               indexToday=spreadsheet.getTodayIndex())
        con.close()
    

@app.route('/confirm/<token>', methods=['GET'])
def confirm(token):
    serializer = URLSafeSerializer(admininfo.secret_key, salt=admininfo.confirm_salt)
    # add try-catch statement here with itsdangerous.BadData
    email = serializer.loads(token)
    # Check if valid unsubscribe url
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return render_template('subscribed.html', 
            msg="Invalid URL. Please check your confirmation email address again. Contact the admin if unable to confirm.", 
            records=spreadsheet.getSpreadsheet(), 
            indexToday=spreadsheet.getTodayIndex())
    msg = ""
    try:
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        cur.execute('''UPDATE subscribers SET confirmed=1
            WHERE email="{}";'''.format(email))
        con.commit()
        msg = email + " has been successfully confirmed."
    except:
        con.rollback()
        msg = "There was an error in your confirmation."
    finally:
        return render_template('subscribed.html', msg=msg, records=spreadsheet.getSpreadsheet(), 
                               indexToday=spreadsheet.getTodayIndex())
        con.close()

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        dailyemail.send_contact_form(request.form['firstName'], request.form['lastName'], request.form['email'], request.form['comments'])
        return render_template('subscribed.html', msg='Your comments have been emailed to the PraxTrain team. We will get back to you as soon as possible.', 
                    records=spreadsheet.getSpreadsheet(), 
                    indexToday=spreadsheet.getTodayIndex())
    else:
        return render_template('contact.html')


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST' and request.form['username'] == admininfo.username and check_password_hash(admininfo.pw_hash, request.form['password']):
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        cur.execute('SELECT * FROM subscribers')
        rows = cur.fetchall()
        con.close()
        today = datetime.datetime.now()
        
        serializer = URLSafeSerializer(admininfo.secret_key, salt=admininfo.unsubscribe_salt)
        unsubscribe_links = ['http://praxtrain.com/unsubscribe/' + serializer.dumps(row[3]) for row in rows]
        serializer = URLSafeSerializer(admininfo.secret_key, salt=admininfo.confirm_salt)
        confirm_links = ['http://praxtrain.com/confirm/' + serializer.dumps(row[3]) for row in rows]

        print('Email scheduling server status is ' + str(dailyemail.serverStatusObj.status))
        return render_template('admin.html', 
                                rows=rows, 
                                unsubscribe_links=unsubscribe_links, 
                                confirm_links=confirm_links, 
                                hour=today.hour, 
                                minute=today.minute, 
                                second=today.second, 
                                server_status=dailyemail.serverStatusObj.status, 
                                sleepfor=dailyemail.serverStatusObj.sleepfor)
    else:
        return render_template('adminlogin.html')

@app.route('/manualemail', methods=['POST'])
def manualemail():
    dailyemail.send_emails()
    return render_template('subscribed.html', msg='Emails sent to subscribers manually.', records=spreadsheet.getSpreadsheet(), 
                               indexToday=spreadsheet.getTodayIndex())

@app.route('/startserver', methods=['POST'])
def startserver():
    threadObj = threading.Thread(target=dailyemail.server)
    threadObj.start()
    return render_template('subscribed.html', msg='Threaded server started.', records=spreadsheet.getSpreadsheet(), 
                               indexToday=spreadsheet.getTodayIndex())

if __name__ == '__main__':
    app.run()