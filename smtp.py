#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
import config

class EmailBySmtp (object):
	
    def __init__(self, c):
        self.smtp_server = config.smtp["server"]
        self.login = config.smtp["login"]
        self.password = config.smtp["password"]

        self.From = config.smtp["From"]
        self.to = config.smtp["to"]
        self.subject = c["subject"]

        self.message = MIMEText(c["message"], 'html')
        self.message['From'] = self.From
        self.message['To'] = self.to
        self.message['Subject'] = self.subject

        self.server = smtplib.SMTP(self.smtp_server)
        self.server.starttls()
        self.server.login(self.login, self.password)

    def send(self ):
        self.server.sendmail(self.From, [self.to], self.message.as_string())
        self.server.quit()


if __name__ == '__main__':
    EmailBySmtp({
        'subject': 'Error 303',
        'message': '<h2>Error URL</h2>',
    }).send()

