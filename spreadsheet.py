import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
sheet = client.open('PraxTrainSheet').sheet1
lastRefreshTime = datetime.datetime.now()

def refreshKey():
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    lastRefreshTime = datetime.datetime.now()

def getSpreadsheet():    
    return sheet.get_all_records()
# for item in records:
#     print(item['day'] + ' ' + item['date'])