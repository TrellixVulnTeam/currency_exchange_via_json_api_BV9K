import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from GMAIL_PWD import GMAIL_PWD
from request_customizable import string_for_each_currency


subject = 'Daily Exchange {}'.format(datetime.now().strftime("%Y-%m-%d %H:%M"))
fromMessage = 'marius.tao@gmail.com'
toMessage = 'marius.a.nicolae@outlook.com'
text = string_for_each_currency

BODY = '\r\n'.join(['To: %s' % toMessage,
                    'From: %s' % fromMessage,
                    'Subject: %s' % subject,
                    '', text])

server = smtplib.SMTP('smtp.gmail.com', port=587)
server.ehlo()
server.starttls()
server.ehlo()
server.login('marius.tao@gmail.com', GMAIL_PWD)

try:
    server.sendmail(fromMessage, [toMessage], BODY)
    print('email sent')
except:
    print('error sending mail')

server.quit()
