import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']


def getTodayIndex():
    # find today's date and find the index to print
    indexZero = datetime.date(2018,9,14)
    today = datetime.date.today()
    indexToday = (today - indexZero).days

    # show tomorrow's post starting at 8pm (12am in AWS time)
    timeNow = datetime.datetime.now()
    if timeNow.hour >= 20:
        indexToday += 1
    return indexToday

def getSpreadsheet():    
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('PraxTrainSheet').sheet1
    return sheet.get_all_records()
