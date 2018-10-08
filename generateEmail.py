
def generateHTML(todaysPraxis, adsPraxis, praxisPraxis, unsubURL):
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
        }</style></head><body><div><!--[if mso | IE]><table align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600" ><tr><td style="line-height:18px;font-size:0px;mso-line-height-rule:exactly;"><v:rect style="width:600px;" xmlns:v="urn:schemas-microsoft-com:vml" fill="true" stroke="false"><v:fill origin="0.5, 0" position="0.5, 0" src='''
    
    imgSrc = 'https://i.imgur.com/MzMwMAJ.jpg'
    
    html += imgSrc
    html += '''type="tile" /><v:textbox style="mso-fit-shape-to-text:true" inset="0,0,0,0"><![endif]--><div style="background:url('''
    html += imgSrc
    html += ''') top center / cover no-repeat;Margin:0px auto;max-width:600px;"><div style="line-height:0;font-size:0;"><table align="center" background="'''
    html += imgSrc
    html += ''' border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:url('''
    html += imgSrc
    html += ''') top center / cover no-repeat;width:100%;"><tbody><tr><td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;vertical-align:top;"><!--[if mso | IE]><table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td class="" style="vertical-align:top;width:600px;" ><![endif]--><div class="mj-column-px-600 outlook-group-fix" style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;"><table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%"><tr><td align="center" style="font-size:0px;padding:10px 25px;word-break:break-word;"><table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;"><tbody><tr><td style="width:162px;"><img height="auto" src="''' 
    
    logoSrc = 'https://image.ibb.co/eBt9EK/praxlogo.png'
    html += logoSrc
    html += '''" style="border:0;display:block;outline:none;text-decoration:none;height:auto;width:100%;" width="162"></td></tr></tbody></table></td></tr><tr><td align="center" style="font-size:0px;padding:10px 25px;word-break:break-word;"><div style="font-family:Helvetica Neue;font-size:40px;line-height:1;text-align:center;color:#fff;">'''
    html += todaysPraxis['day'] + ' · ' + todaysPraxis['date'].replace('/','.')
    
    html += '''</div></td></tr></table></div><!--[if mso | IE]></td></tr></table><![endif]--></td></tr></tbody></table></div></div><!--[if mso | IE]></v:textbox></v:rect></td></tr></table><table align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600" ><tr><td style="line-height:18px;font-size:0px;mso-line-height-rule:exactly;"><![endif]--><div style="background:#f0f0f0;background-color:#f0f0f0;Margin:0px auto;max-width:600px;"><table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#f0f0f0;background-color:#f0f0f0;width:100%;"><tbody><tr><td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;vertical-align:top;"><!--[if mso | IE]><table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td class="" style="vertical-align:top;width:300px;" ><![endif]--><div class="mj-column-per-50 outlook-group-fix" style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;"><table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%"><tr><td align="center" style="font-size:0px;padding:10px 25px;word-break:break-word;"><div style="font-family:helvetica;font-size:20px;font-weight:bold;line-height:1;text-align:center;color:#AD343E;">ADS</div></td></tr>'''
    for k,v in adsPraxis.items():
        html += '''<tr><td align="Center" style="font-size:0px;padding:10px 25px;word-break:break-word;"><div style="font-family:helvetica;font-size:13px;font-weight:bold;line-height:18px;text-align:Center;color:#000;">'''
        html += k.replace('_', ' ').strip('ads ').title()
        html += '''</div></td></tr><tr><td align="Center" style="font-size:0px;padding:10px 25px;word-break:break-word;"><div style="font-family:helvetica;font-size:13px;line-height:18px;text-align:Center;color:#000;">'''
        html += '<br>'.join(v.split(', ')).replace('*', '')
        html += '''</div></td></tr>'''

    # See more praxis button and praxis section header
    html += '''<tr><td align="center" vertical-align="middle" style="font-size:0px;padding:10px 25px;word-break:break-word;"><table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:separate;line-height:100%;"><tr><td align="center" bgcolor="#AD343E" role="presentation" style="border:none;border-radius:40px;cursor:auto;padding:10px 25px;" valign="middle"> <a href="praxtrain.com" style="background:#AD343E;color:#ffffff;font-family:helvetica;font-size:12px;font-weight:normal;line-height:120%;Margin:0;text-decoration:none;text-transform:none;" target="_blank">SEE MORE PRAXIS</a> </td></tr></table></td></tr></table></div><!--[if mso | IE]></td><td class="" style="vertical-align:top;width:300px;" ><![endif]--><div class="mj-column-per-50 outlook-group-fix" style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;"><table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%"><tr><td align="center" style="font-size:0px;padding:10px 25px;word-break:break-word;"><div style="font-family:helvetica;font-size:20px;font-weight:bold;line-height:1;text-align:center;color:#AD343E;">PRAXIS</div></td></tr>'''

    for k, v in praxisPraxis.items():
        html +='''<tr><td align="Center" style="font-size:0px;padding:10px 25px;word-break:break-word;"><div style="font-family:helvetica;font-size:13px;font-weight:bold;line-height:18px;text-align:Center;color:#000;">'''
        html += k.replace('_', ' ').strip('praxis ').title()
        html +='''</div></td></tr><tr><td align="Center" style="font-size:0px;padding:10px 25px;word-break:break-word;"><div style="font-family:helvetica;font-size:13px;line-height:18px;text-align:Center;color:#000;">'''
        html += '<br>'.join(v.split(', ')).replace('*', '')
        html +='''</div></td></tr>'''

    # See more praxis button
    html += '''<tr><td align="Center" style="font-size:0px;padding:10px 25px;word-break:break-word;"><div style="font-family:helvetica;font-size:13px;font-weight:bold;line-height:18px;text-align:Center;color:#000;">Memorization</div></td></tr><tr><td align="Center" style="font-size:0px;padding:10px 25px;word-break:break-word;"><div style="font-family:helvetica;font-size:13px;line-height:18px;text-align:Center;color:#000;">John 1:1</div></td></tr><tr><td align="center" vertical-align="middle" style="font-size:0px;padding:10px 25px;word-break:break-word;"><table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:separate;line-height:100%;"><tr><td align="center" bgcolor="#AD343E" role="presentation" style="border:none;border-radius:40px;cursor:auto;padding:10px 25px;" valign="middle"><a href="praxtrain.com" style="background:#AD343E;color:#ffffff;font-family:helvetica;font-size:12px;font-weight:normal;line-height:120%;Margin:0;text-decoration:none;text-transform:none;" target="_blank">SEE MORE PRAXIS</a></td></tr></table></td></tr></table></div><!--[if mso | IE]></td></tr></table><![endif]--></td></tr></tbody></table></div><!--[if mso | IE]></td></tr></table><table align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600" ><tr><td style="line-height:18px;font-size:0px;mso-line-height-rule:exactly;"><![endif]--><div style="Margin:0px auto;max-width:600px;"><table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;"><tbody><tr><td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;vertical-align:top;"><!--[if mso | IE]><table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td align="center" class="" style="" ><![endif]--><table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:separate;line-height:100%;"><tr><td align="center" bgcolor="white" role="presentation" style="border:none;border-radius:3px;cursor:auto;padding:10px 25px;" valign="middle"><a href="'''
    html += unsubURL
    html += '''" style="background:white;color:#a0a0a0;font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:12px;font-weight:normal;line-height:120%;Margin:0;text-decoration:none;text-transform:none;" target="_blank">Unsubscribe</a></td></tr></table><!--[if mso | IE]></td></tr></table><![endif]--></td></tr></tbody></table></div><!--[if mso | IE]></td></tr></table><![endif]--></div></body></html>'''
    
    return html

def generateText(todaysPraxis, adsPraxis, praxisPraxis, unsubURL):
    text = 'Praxis for ' + todaysPraxis['day'] + ' · ' + todaysPraxis['date'].replace('/','.') + '\n\n---ADS---\n'
    for k,v in adsPraxis.items():
        text += k.replace('_', ' ').strip('ads ').title()
        text += '\n'
        text += '\n'.join(v.split(', ')).replace('*', '')
    text += '\n\n --PRAXIS--\n'
    for k,v in praxisPraxis.items():
        text += k.replace('_', ' ').strip('praxis ').title()
        text += '\n'
        text += '\n'.join(v.split(', ')).replace('*', '')
    text += '\n'

    text += 'To unsubscribe, follow the link below.\n'
    text += unsubURL
    return text

def generateConfHTML(url):
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
        <![endif]--><style type="text/css">@media only screen and (min-width:480px) {
        .mj-column-px-600 { width:600px !important; max-width: 600px; }
.mj-column-per-100 { width:100% !important; max-width: 100%; }
      }</style><style type="text/css">@media only screen and (max-width:480px) {
      table.full-width-mobile { width: 100% !important; }
      td.full-width-mobile { width: auto !important; }
    }</style></head><body><div><!--[if mso | IE]><table align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600" ><tr><td style="line-height:18px;font-size:0px;mso-line-height-rule:exactly;"><v:rect style="width:600px;" xmlns:v="urn:schemas-microsoft-com:vml" fill="true" stroke="false"><v:fill origin="0.5, 0" position="0.5, 0" src="https://images.unsplash.com/photo-1506862047911-9815cdcb77c2?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=229ddd4bbaee7a8702d2c5b67f006fe8&auto=format&fit=crop&w=1950&q=80" type="tile" /><v:textbox style="mso-fit-shape-to-text:true" inset="0,0,0,0"><![endif]--><div style="background:url(https://images.unsplash.com/photo-1506862047911-9815cdcb77c2?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=229ddd4bbaee7a8702d2c5b67f006fe8&auto=format&fit=crop&w=1950&q=80) top center / cover no-repeat;Margin:0px auto;max-width:600px;"><div style="line-height:0;font-size:0;"><table align="center" background="https://images.unsplash.com/photo-1506862047911-9815cdcb77c2?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=229ddd4bbaee7a8702d2c5b67f006fe8&auto=format&fit=crop&w=1950&q=80" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:url(https://images.unsplash.com/photo-1506862047911-9815cdcb77c2?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=229ddd4bbaee7a8702d2c5b67f006fe8&auto=format&fit=crop&w=1950&q=80) top center / cover no-repeat;width:100%;"><tbody><tr><td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;vertical-align:top;"><!--[if mso | IE]><table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td class="" style="vertical-align:top;width:600px;" ><![endif]--><div class="mj-column-px-600 outlook-group-fix" style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;"><table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%"><tr><td align="center" style="font-size:0px;padding:10px 25px;word-break:break-word;"><table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;"><tbody><tr><td style="width:162px;"><img height="auto" src="https://image.ibb.co/eBt9EK/praxlogo.png" style="border:0;display:block;outline:none;text-decoration:none;height:auto;width:100%;" width="162"></td></tr></tbody></table></td></tr><tr><td align="center" style="font-size:0px;padding:10px 25px;word-break:break-word;"><div style="font-family:Helvetica Neue;font-size:40px;line-height:1;text-align:center;color:transparent;">.</div></td></tr></table></div><!--[if mso | IE]></td></tr></table><![endif]--></td></tr></tbody></table></div></div><!--[if mso | IE]></v:textbox></v:rect></td></tr></table><table align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600" ><tr><td style="line-height:18px;font-size:0px;mso-line-height-rule:exactly;"><![endif]--><div style="background:#f0f0f0;background-color:#f0f0f0;Margin:0px auto;max-width:600px;"><table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#f0f0f0;background-color:#f0f0f0;width:100%;"><tbody><tr><td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;vertical-align:top;"><!--[if mso | IE]><table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td class="" style="vertical-align:top;width:600px;" ><![endif]--><div class="mj-column-per-100 outlook-group-fix" style="font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;"><table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%"><tr><td align="center" style="font-size:0px;padding:10px 25px;word-break:break-word;"><div style="font-family:helvetica;font-size:20px;font-weight:bold;line-height:1;text-align:center;color:#AD343E;">Subscribe to Praxtrain</div></td></tr><tr><td align="Center" style="font-size:0px;padding:10px 25px;word-break:break-word;"><div style="font-family:helvetica;font-size:13px;line-height:18px;text-align:Center;color:#000;">Click the link below to confirm your email.</div></td></tr><tr><td align="center" vertical-align="middle" style="font-size:0px;padding:10px 25px;word-break:break-word;"><table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:separate;line-height:100%;"><tr><td align="center" bgcolor="#AD343E" role="presentation" style="border:none;border-radius:40px;cursor:auto;padding:10px 25px;" valign="middle"><a href="'''
    html += url
    html += '''" style="background:#AD343E;color:#ffffff;font-family:helvetica;font-size:12px;font-weight:normal;line-height:120%;Margin:0;text-decoration:none;text-transform:none;" target="_blank">Confirm Subscription</a></td></tr></table></td></tr></table></div><!--[if mso | IE]></td></tr></table><![endif]--></td></tr></tbody></table></div><!--[if mso | IE]></td></tr></table><![endif]--></div></body></html>'''
    return html

def generateConfText(url):
    text = 'Click the url below to confirm your email:\n'
    text += url + '\n\nPraxTrain\n'
    return text
