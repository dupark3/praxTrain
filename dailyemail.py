import datetime
from time import sleep
import sqlite3

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import spreadsheet
import admininfo

def sleep_until_eight():
    today = datetime.datetime.now()
    eight = today.replace(hour=20, minute=0, second=0, microsecond=0)
    if today.hour >= 20:
        eight += datetime.timedelta(days=1)
    sleep((eight - today).seconds)

def server():
    while(True):
        sleep_until_eight()
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        cur.execute('SELECT email FROM subscribers WHERE confirmed = 0')
        emails = [email[0] for email in cur.fetchall()] # convert list of tuples to lists
        send_emails(emails)

def send_emails(recipients):
    html = '''<!doctype html><html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office"><head><title></title><!--[if !mso]><!-- --><meta http-equiv="X-UA-Compatible" content="IE=edge"><!--<![endif]--><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style type="text/css">#outlook a { padding:0; }
              .ReadMsgBody { width:100%; }
              .ExternalClass { width:100%; }
              .ExternalClass * { line-height:100%; }
              body { margin:0;padding:0;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%; }
              table, td { border-collapse:collapse;mso-table-lspace:0pt;mso-table-rspace:0pt; }
              img { border:0;height:auto;line-height:100%; outline:none;text-decoration:none;-ms-interpolation-mode:bicubic; }
              p { display:block;margin:13px 0; }</style><!--[if !mso]><!--><style type="text/css">@media only screen and (max-width:480px) {
                @-ms-viewport { width:320px; }
                @viewport { width:320px; }
              }</style><!--<![endif]--><!--[if mso]>
            <xml>
            <o:OfficeDocumentSettings>
              <o:AllowPNG/>
              <o:PixelsPerInch>96</o:PixelsPerInch>
            </o:OfficeDocumentSettings>
            </xml>
            <![endif]--><!--[if lte mso 11]>
            <style type="text/css">
              .outlook-group-fix { width:100% !important; }
            </style>
            <![endif]--><!--[if !mso]><!--><link href="https://fonts.googleapis.com/css?family=Ubuntu:300,400,500,700" rel="stylesheet" type="text/css"><style type="text/css">@import url(https://fonts.googleapis.com/css?family=Ubuntu:300,400,500,700);</style><!--<![endif]--><style type="text/css">@media only screen and (min-width:480px) {
            .mj-column-px-600 { width:600px !important; max-width: 600px; }
    .mj-column-per-50 { width:50% !important; max-width: 50%; }
          }</style><style type="text/css">@media only screen and (max-width:480px) {
          table.full-width-mobile { width: 100% !important; }
          td.full-width-mobile { width: auto !important; }
        }</style></head><body><div><!--[if mso | IE]><table align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600" ><tr><td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;"><v:rect style="width:600px;" xmlns:v="urn:schemas-microsoft-com:vml" fill="true" stroke="false"><v:fill origin="0.5, 0" position="0.5, 0" src="https://images.unsplash.com/photo-1506862047911-9815cdcb77c2?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=229ddd4bbaee7a8702d2c5b67f006fe8&auto=format&fit=crop&w=1950&q=80" type="tile" /><v:textbox style="mso-fit-shape-to-text:true" inset="0,0,0,0"><![endif]--><div style="background:url(https://images.unsplash.com/photo-1506862047911-9815cdcb77c2?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=229ddd4bbaee7a8702d2c5b67f006fe8&auto=format&fit=crop&w=1950&q=80) top center / cover no-repeat;Margin:0px auto;max-width:600px;"><div style="line-height:0;font-size:0;"><table align="center" background="https://images.unsplash.com/photo-1506862047911-9815cdcb77c2?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=229ddd4bbaee7a8702d2c5b67f006fe8&auto=format&fit=crop&w=1950&q=80" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:url(https://images.unsplash.com/photo-1506862047911-9815cdcb77c2?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=229ddd4bbaee7a8702d2c5b67f006fe8&auto=format&fit=crop&w=1950&q=80) top center / cover no-repeat;width:100%;"><tbody><tr><td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;vertical-align:top;"><!--[if mso | IE]><table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td class="" style="vertical-align:top;width:600px;" ><![endif]--><div class="mj-column-px-600 outlook-group-fix" style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;"><table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%"><tr><td align="center" style="font-size:0px;padding:10px 25px;word-break:break-word;"><table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;"><tbody><tr><td style="width:162px;"><img height="auto" src="https://i.imgur.com/d13Pkud.png" style="border:0;display:block;outline:none;text-decoration:none;height:auto;width:100%;" width="162"></td></tr></tbody></table></td></tr><tr><td align="center" style="font-size:0px;padding:10px 25px;word-break:break-word;"><div style="font-family:Helvetica Neue;font-size:40px;line-height:1;text-align:center;color:#fff;">WEDNESDAY 10.3.18</div></td></tr></table></div><!--[if mso | IE]></td></tr></table><![endif]--></td></tr></tbody></table></div></div><!--[if mso | IE]></v:textbox></v:rect></td></tr></table><table align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600" ><tr><td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;"><![endif]--><div style="background:#f0f0f0;background-color:#f0f0f0;Margin:0px auto;max-width:600px;"><table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#f0f0f0;background-color:#f0f0f0;width:100%;"><tbody><tr><td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;vertical-align:top;"><!--[if mso | IE]><table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td class="" style="vertical-align:top;width:300px;" ><![endif]--><div class="mj-column-per-50 outlook-group-fix" style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;"><table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%"><tr><td align="center" style="font-size:0px;padding:10px 25px;word-break:break-word;"><div style="font-family:helvetica;font-size:20px;font-weight:bold;line-height:1;text-align:center;color:#AD343E;">ADS</div></td></tr><tr><td align="Center" style="font-size:0px;padding:10px 25px;word-break:break-word;"><div style="font-family:helvetica;font-size:13px;font-weight:bold;line-height:0px;text-align:Center;color:#000;">Bible Reading</div></td></tr><tr><td align="Center" style="font-size:0px;padding:10px 25px;word-break:break-word;"><div style="font-family:helvetica;font-size:13px;line-height:0px;text-align:Center;color:#000;">Genesis 1:1</div></td></tr><tr><td align="Center" style="font-size:0px;padding:10px 25px;word-break:break-word;"><div style="font-family:helvetica;font-size:13px;font-weight:bold;line-height:0px;text-align:Center;color:#000;">Memorization</div></td></tr><tr><td align="Center" style="font-size:0px;padding:10px 25px;word-break:break-word;"><div style="font-family:helvetica;font-size:13px;line-height:0px;text-align:Center;color:#000;">John 1:1</div></td></tr><tr><td align="center" vertical-align="middle" style="font-size:0px;padding:10px 25px;word-break:break-word;"><table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:separate;line-height:100%;"><tr><td align="center" bgcolor="#AD343E" role="presentation" style="border:none;border-radius:40px;cursor:auto;padding:10px 25px;" valign="middle"><p style="background:#AD343E;color:#ffffff;font-family:helvetica;font-size:12px;font-weight:normal;line-height:120%;Margin:0;text-decoration:none;text-transform:none;">SEE MORE PRAXIS</p></td></tr></table></td></tr></table></div><!--[if mso | IE]></td><td class="" style="vertical-align:top;width:300px;" ><![endif]--><div class="mj-column-per-50 outlook-group-fix" style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;"><table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%"><tr><td align="center" style="font-size:0px;padding:10px 25px;word-break:break-word;"><div style="font-family:helvetica;font-size:20px;font-weight:bold;line-height:1;text-align:center;color:#AD343E;">PRAXIS</div></td></tr><tr><td align="Center" style="font-size:0px;padding:10px 25px;word-break:break-word;"><div style="font-family:helvetica;font-size:13px;font-weight:bold;line-height:0px;text-align:Center;color:#000;">Bible Reading</div></td></tr><tr><td align="Center" style="font-size:0px;padding:10px 25px;word-break:break-word;"><div style="font-family:helvetica;font-size:13px;line-height:0px;text-align:Center;color:#000;">Genesis 1:1</div></td></tr><tr><td align="Center" style="font-size:0px;padding:10px 25px;word-break:break-word;"><div style="font-family:helvetica;font-size:13px;font-weight:bold;line-height:0px;text-align:Center;color:#000;">Memorization</div></td></tr><tr><td align="Center" style="font-size:0px;padding:10px 25px;word-break:break-word;"><div style="font-family:helvetica;font-size:13px;line-height:0px;text-align:Center;color:#000;">John 1:1</div></td></tr><tr><td align="center" vertical-align="middle" style="font-size:0px;padding:10px 25px;word-break:break-word;"><table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:separate;line-height:100%;"><tr><td align="center" bgcolor="#AD343E" role="presentation" style="border:none;border-radius:40px;cursor:auto;padding:10px 25px;" valign="middle"><p style="background:#AD343E;color:#ffffff;font-family:helvetica;font-size:12px;font-weight:normal;line-height:120%;Margin:0;text-decoration:none;text-transform:none;">SEE MORE PRAXIS</p></td></tr></table></td></tr></table></div><!--[if mso | IE]></td></tr></table><![endif]--></td></tr></tbody></table></div><!--[if mso | IE]></td></tr></table><table align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600" ><tr><td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;"><![endif]--><div style="Margin:0px auto;max-width:600px;"><table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;"><tbody><tr><td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;vertical-align:top;"><!--[if mso | IE]><table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td align="center" class="" style="" ><![endif]--><table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:separate;line-height:100%;"><tr><td align="center" bgcolor="white" role="presentation" style="border:none;border-radius:3px;cursor:auto;padding:10px 25px;" valign="middle"><a href="www.google.com" style="background:white;color:a0a0a0;font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:12px;font-weight:normal;line-height:120%;Margin:0;text-decoration:none;text-transform:none;" target="_blank">Unsubscribe</a></td></tr></table><!--[if mso | IE]></td></tr></table><![endif]--></td></tr></tbody></table></div><!--[if mso | IE]></td></tr></table><![endif]--></div></body></html>'''

    todaysPraxis = spreadsheet.getSpreadsheet()[spreadsheet.getTodayIndex()]
    todaysPraxis = {k:v for k, v in todaysPraxis.items() if v is not ''} # removes columns without a string
    adsPraxis = {k:v for k, v in todaysPraxis.items() if k[0:3] == 'ads'}
    praxisPraxis = {k:v for k, v in todaysPraxis.items() if k[0:6] == 'praxis'}

    sender = 'daily@praxtrain.com'

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Your Praxis for " + todaysPraxis['day']
    msg['From'] = 'DailyPrax <'+sender+'>'

    text =  '---ADS---\n'
    for k,v in adsPraxis.items():
        text += k.replace('_',' ')[4:] + ': ' + v.strip('*') + '\n'
    text += '--PRAXIS--\n'
    for k,v in praxisPraxis.items():
        text += k.replace('_',' ')[7:] + ': ' + v.strip('*') + '\n'

    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    msg.attach(part1)
    msg.attach(part2)

    for recipient in recipients:
      msg['To'] = recipient
      server.sendmail(sender, recipient, msg.as_string())
      print('Email sent to ' + recipient)

    server.quit()