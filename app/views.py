# $ export FLASK_APP=app.py           lets the terminal know to use flask app
# $ flask run OR python -m flask run    optional flag --host=0.0.0.0 to listen to other IPs
# $ export FLASK_ENV=development        code changes refreshed

from flask import Flask, redirect, url_for, request, render_template
from app import app
import datetime

import spreadsheet # spreadsheet.py


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return redirect(url_for('subscribed'))
    else:
        # find today's date and find the index to print
        indexZero = datetime.date(2018,9,14)
        today = datetime.date.today()
        indexToday = (today - indexZero).days

        # show tomorrow's post starting at 8pm
        timeNow = datetime.datetime.now()
        if timeNow.hour >= 20:
            indexToday += 1
        spreadsheet.refreshKey()
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