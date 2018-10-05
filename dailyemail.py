import datetime
from time import sleep
import sqlite3

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import spreadsheet, admininfo, generateEmail, itsdangerous

from itsdangerous import URLSafeSerializer

class server_status:
    status = False
    sleepfor = 0
serverStatusObj = server_status()

def sleep_until_eight():
    today = datetime.datetime.now()
    eight = today.replace(hour=20, minute=0, second=0, microsecond=0)
    if today.hour >= 20:
        eight += datetime.timedelta(days=1)
    sleepfor = (eight-today).seconds
    while sleepfor > 3600:
        print('sleeping for 3600 seconds out of ' + str(sleepfor) + ' seconds.')
        serverStatusObj.sleepfor = sleepfor
        sleepfor -= 3600
        sleep(3600)
    print(str(sleepfor) + ' seconds until sending emails')
    sleep(sleepfor)

def server():
    serverStatusObj.status = True
    while(True):
        print('in while loop of server')
        sleep_until_eight()
        send_emails()

def send_emails():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('SELECT email FROM subscribers WHERE confirmed = 1')
    recipients = [email[0] for email in cur.fetchall()] # convert list of tuples to lists
    con.close()

    todayIndex = spreadsheet.getTodayIndex()
    todaysPraxis = spreadsheet.getSpreadsheet()[todayIndex]

    # Remove columns without a string
    todaysPraxis = {k:v for k, v in todaysPraxis.items() if v is not ''} 

    # Divide into ads and praxis columns
    adsPraxis = {k:v for k, v in todaysPraxis.items() if k[0:3] == 'ads'}
    praxisPraxis = {k:v for k, v in todaysPraxis.items() if k[0:6] == 'praxis'}
    
    sender = 'daily@praxtrain.com'

    smtpserver = smtplib.SMTP('smtp.zoho.com', 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.login(sender, admininfo.zoho_pw)

    serializer = URLSafeSerializer(admininfo.secret_key, salt=admininfo.unsubscribe_salt)
    
    for recipient in recipients:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Your Praxis for " + todaysPraxis['day']
        msg['From'] = 'DailyPrax <'+sender+'>'
        msg['To'] = recipient

        token = serializer.dumps(recipient)
        unsubURL = 'http://praxtrain.com/unsubscribe/' + token
        text = generateEmail.generateText(todaysPraxis, adsPraxis, praxisPraxis, unsubURL)
        html = generateEmail.generateHTML(todaysPraxis, adsPraxis, praxisPraxis, unsubURL)

        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')
        msg.attach(part1)
        msg.attach(part2)

        smtpserver.sendmail(sender, recipient, msg.as_string())
        print('Email sent to ' + recipient)

    smtpserver.quit()

def send_confirmation(email):
    serializer = URLSafeSerializer(admininfo.secret_key, salt=admininfo.confirm_salt)
    token = serializer.dumps(email)
    url = 'http://praxtrain.com/confirm/' + token

    text = generateEmail.generateConfText(url)
    html = generateEmail.generateConfHTML(url)

    sender = 'daily@praxtrain.com'

    smtpserver = smtplib.SMTP('smtp.zoho.com', 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.login(sender, admininfo.zoho_pw)

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Confirm your email subscription to PraxTrain"
    msg['From'] = 'DailyPrax <'+sender+'>'
    msg['To'] = email

    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    msg.attach(part1)
    msg.attach(part2)

    smtpserver.sendmail(sender, email, msg.as_string())
    print('Email sent to ' + email)

    smtpserver.quit()

def send_contact_form(firstname, lastname, email, comments):
    sender = 'daily@praxtrain.com'
    recipients = ['dupark3@gmail.com', 'sonofthemaster1@gmail.com']
   
    smtpserver = smtplib.SMTP('smtp.zoho.com', 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.login(sender, admininfo.zoho_pw)

    for recipient in recipients:
        msg = MIMEText(firstname + ' ' + lastname + ' ' + email + ' \n' + comments)
        msg['Subject'] = 'Comments from ' + firstname + ' ' + lastname
        msg['From'] = 'DailyPrax <'+sender+'>'
        msg['To'] = recipient
        smtpserver.sendmail(sender, recipient, msg.as_string())

    smtpserver.quit()