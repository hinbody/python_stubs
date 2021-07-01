#!/usr/bin/env python3

import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content('email body here')

msg['Subject'] = 'subject here'
msg['From'] = ''
msg['To'] = ['']


try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.send_message(msg)
    print("success")
except smtplib.SMTPException:
    print("no success")
