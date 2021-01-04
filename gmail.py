'''
Created on 2020/12/29

@author: hellomyzn
'''


# -*- coding: utf-8 -*-

import smtplib, ssl, os, csv

from dotenv import load_dotenv
from email.mime.text import MIMEText

# set up student list
students_list   = "test.txt"

# Input .env file 
load_dotenv("./.env")
gmail_account   = os.environ['GMAIL']
gmail_password  = os.environ['PASSWORD']

# Input emmail sentence from text.txt
with open('text.csv', 'r') as csv_file:
    temp = {}
    reader = csv.DictReader(csv_file)
    for row in reader:
        temp[row['Key']] = row['Value']
subject         = temp["SUBJECT"]
body            = temp['BODY']


# set up on list
def set_up_mail(ga: str, gp: str, mt: str, subject: str, body: str) -> list:

    mail_setting = {}
    mail_setting["gmail_account"]   = ga
    mail_setting["gmail_password"]  = gp
    mail_setting["mail_to"]         = mt
    mail_setting["subject"]         = subject
    mail_setting["body"]            = body
    return mail_setting


# sending email
def send_email(mail_setting: list):

    msg             = MIMEText(mail_setting["body"], "html")
    msg["Subject"]  = mail_setting["subject"]
    msg["To"]       = mail_setting["mail_to"]
    msg["From"]     = mail_setting["gmail_account"]
    server          = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context())

    server.login(mail_setting["gmail_account"], mail_setting["gmail_password"])
    server.send_message(msg)
    print("ok.")




if __name__ == "__main__":
    with open(students_list, "r") as f:
        while True:
            # Read each line
            mail_to = f.readline()
            if not mail_to:
                print("### Finish all ###")
                break

            print("###############################\n")
            print("Start: ", mail_to)

            # set up and send email
            mail_setting = set_up_mail(gmail_account, gmail_password, mail_to, subject, body)
            send_email(mail_setting)
            print("Sent: ", mail_to)
            print("###############################")


    send_email(mail_setting)
