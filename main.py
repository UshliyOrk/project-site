# !/usr/bin/env python3
import cgi
import smtplib
from email.mime.text import MIMEText


class sender:
    def __init__(self):
        self.smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        self.smtpObj.starttls()
        self.log = "Polpilgun@gmail.com"
        self.password = "hjwgksmgrkvdrnam"
        self.receiver = "pavelpilgun9@gmail.com"
        self.smtpObj.login(self.log, self.password)


    def send(self, message, subj):
        msg = MIMEText(message)
        msg["Subject"] = subj
        self.smtpObj.sendmail(self.log, self.receiver, msg.as_string())
        self.smtpObj.quit()


form = cgi.FieldStorage()
name = form.getfirst("name", "не задано")
comment = form.getfirst("comment", "не задано")

send = sender()
send.send(comment, name)
