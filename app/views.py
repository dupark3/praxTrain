# $ export FLASK_APP=app.py           lets the terminal know to use flask app
# $ flask run OR python -m flask run    optional flag --host=0.0.0.0 to listen to other IPs
# $ export FLASK_ENV=development        code changes refreshed

from flask import Flask, redirect, url_for, request, render_template

from app import app

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return redirect(url_for('subscribed'))
    else:
        return render_template('index.html')

@app.route('/subscribed', methods=['GET'])
def subscribed():
    return render_template('subscribed.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        return render_template('admin.html')
        # change to authentication
    else:
        return render_template('admin.html')

if __name__ == '__main__':
    app.run()