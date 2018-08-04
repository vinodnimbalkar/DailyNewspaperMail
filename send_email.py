# import necessary packages
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

import os, shutil
import urllib.request
from datetime import date
import schedule as sh
from time import sleep
import time
from credentials import *

basedir = os.path.abspath(os.path.dirname(__file__)) #current directory
d = date.today().strftime('%Y%m%d').lstrip("0").replace(" 0", " ") #date in yyyymmdd format

def theHindu():
    os.mkdir("Hindu")
    downloadUrl = url+d+"/Hindu.pdf"
    path = basedir+"/Hindu/Hindu.pdf"
    urllib.request.urlretrieve(downloadUrl, path)
    print("Download complete")

def lokmat():
    os.mkdir("Lokmat")    
    downloadUrl = url+d+"/Lokmat.pdf"
    path = basedir+"/Lokmat/Lokmat.pdf"
    urllib.request.urlretrieve(downloadUrl, path)
    print("Download complete")

def newpaperMail():
    subject = 'The Hindu Newspaper'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = ", ".join(email_send)
    msg['Subject'] = subject

    body = 'Hi there, sending this email from Python!'
    msg.attach(MIMEText(body,'plain'))

    filename='Hindu/Hindu.pdf'
    attachment  =open(filename,'rb')

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)

    msg.attach(part)
    text = msg.as_string()
    try:
        server = smtplib.SMTP('smtp.mail.yahoo.com',587)
        server.starttls()
        server.login(email_user,email_password)

        server.sendmail(email_user,email_send,text)
        server.quit()
        print("Mail successfully send")
    except smtplib.SMTPException:
         print("Error: unable to send email")

def deleteHindu():
    path = basedir+"/Hindu"
    if os.path.isdir(path):
        shutil.rmtree(path)
        print("The Hindu folder and pdf Deleted")

def deleteLokmat():
    path = basedir+"/Lokmat"
    if os.path.isdir(path):
        shutil.rmtree(path)
        print("Lokmat folder Deleted")

if __name__ == "__main__":
    sh.every().day.at("08:00").do(theHindu)
    sh.every().day.at("08:10").do(newpaperMail)
    sh.every().day.at("08:20").do(deleteHindu)
    while True:
        sh.run_pending()
        time.sleep(1)