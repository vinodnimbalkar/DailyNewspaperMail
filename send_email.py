# import necessary packages
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.image import MIMEImage

import urllib.request, requests
from bs4 import BeautifulSoup
from datetime import date
import pandas as pd
import random

import os, shutil
import urllib.request
from datetime import date
import schedule as sh
from time import sleep
import time
from credentials import *

basedir = os.path.abspath(os.path.dirname(__file__))
d = date.today().strftime('%Y%m%d').lstrip("0").replace(" 0", " ")
# d = str(int(d)+1)
if not os.path.exists('./NewsPapers'):
    os.makedirs('./NewsPapers')

def dinVishesh():
    d = date.today().strftime('%d-%B').lstrip("0").replace(" 0", " ").lower()
    #specify the url of dinvishesh website
    janm = "http://www.dinvishesh.com/{}-janm/".format(d) #जन्म तारखे नुसार 
    ghatana = "http://www.dinvishesh.com/{}-ghatana/".format(d) #घटने नुसार 
    mrutyu = "http://www.dinvishesh.com/{}-mrutyu/".format(d) #मृत्यू नुसार
   
    #janm
    page_janm = urllib.request.urlopen(janm)
    soup = BeautifulSoup(page_janm, 'html.parser')
    vishesh_janm = soup.find('div', class_='td-post-content')
    data_janm = vishesh_janm.text
    #ghatana
    page_ghatana = urllib.request.urlopen(ghatana)
    soup = BeautifulSoup(page_ghatana, 'html.parser')
    vishesh_ghatana = soup.find('div', class_='td-post-content')
    data_ghatana = vishesh_ghatana.text
    #mrutyu
    page_mrutyu = urllib.request.urlopen(mrutyu)
    soup = BeautifulSoup(page_mrutyu, 'html.parser')
    vishesh_mrutyu = soup.find('div', class_='td-post-content')
    data_mrutyu = vishesh_mrutyu.text
    return data_janm, data_ghatana, data_mrutyu

def theHindu():
    print("Download Starting...")
    downloadUrl = url+d+"/Hindu.pdf"
    path = basedir+"/NewsPapers/Hindu.pdf"
    urllib.request.urlretrieve(downloadUrl, path)
    print("Download complete")

def indianExpress():
    print("Download Starting...")
    downloadUrl = url+d+"/Indian%20Express.pdf"
    path = basedir+"/NewsPapers/Indian%20Express.pdf"
    urllib.request.urlretrieve(downloadUrl, path)
    print("Download complete")

def lokmat(): 
    print("Download Starting...")  
    downloadUrl = url+d+"/Lokmat.pdf"
    path = basedir+"/NewsPapers/Lokmat.pdf"
    urllib.request.urlretrieve(downloadUrl, path)
    print("Download complete")

def newspaperMail():
    print("Sending Mail in Progress...")
    subject = 'The Hindu Newspaper'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = ", ".join(email_send)
    msg['Subject'] = subject

    birth, event, death = dinVishesh()

    #Read Image
    with open('images/h1.gif', 'rb') as h1Img:
        headerImg = MIMEImage(h1Img.read())
    with open('images/left.gif', 'rb') as lImg:
        leftImg = MIMEImage(lImg.read())
    with open('images/right.gif', 'rb') as rImg:
        rightImg = MIMEImage(rImg.read())

    # Define the image's ID as referenced above
    headerImg.add_header('Content-ID', '<image1>')
    msg.attach(headerImg)
    leftImg.add_header('Content-ID', '<left>')
    msg.attach(leftImg)
    rightImg.add_header('Content-ID', '<right>')
    msg.attach(rightImg)

    # body = 'आजचा दिनविशेष जन्म तारखे नुसार '+birth+'\nघटने नुसार '+event+'\nमृत्यू नुसार '+death
    body = f""" <body style="margin: 0; padding: 0;">
	<table border="0" cellpadding="0" cellspacing="0" width="100%">	
		<tr>
			<td style="padding: 10px 0 30px 0;">
				<table align="center" border="0" cellpadding="0" cellspacing="0" width="600" style="border: 1px solid #cccccc; border-collapse: collapse;">
					<tr>
						<td align="center" bgcolor="#70bbd9" style="padding: 40px 0 30px 0; color: #153643; font-size: 28px; font-weight: bold; font-family: Arial, sans-serif;">
							<img src="cid:image1" alt="Creating Email Magic" width="300" height="230" style="display: block;" />
						</td>
					</tr>
					<tr>
						<td bgcolor="#ffffff" style="padding: 40px 30px 40px 30px;">
							<table border="0" cellpadding="0" cellspacing="0" width="100%">
								<tr>
									<td style="color: #153643; font-family: Arial, sans-serif; font-size: 24px;">
										<b>आजचा दिनविशेष जन्म तारखे नुसार</b>
									</td>
								</tr>
								<tr>
									<td style="padding: 20px 0 30px 0; color: #153643; font-family: Arial, sans-serif; font-size: 16px; line-height: 20px;">
                                    {birth}
									</td>
								</tr>
								<tr>
									<td>
										<table border="0" cellpadding="0" cellspacing="0" width="100%">
											<tr>
												<td width="260" valign="top">
													<table border="0" cellpadding="0" cellspacing="0" width="100%">
														<tr>
															<td>
																<img src="cid:left" alt="" width="100%" height="140" style="display: block;" /><br>
                                                                <b>आजचा दिनविशेष घटने नुसार</b>
															</td>
														</tr>
														<tr>
															<td style="padding: 25px 0 0 0; color: #153643; font-family: Arial, sans-serif; font-size: 16px; line-height: 20px;">
																{event}
															</td>
														</tr>
													</table>
												</td>
												<td style="font-size: 0; line-height: 0;" width="20">
													&nbsp;
												</td>
												<td width="260" valign="top">
													<table border="0" cellpadding="0" cellspacing="0" width="100%">
														<tr>
															<td>
																<img src="cid:right" alt="" width="100%" height="140" style="display: block;" /><br>
                                                                <b>आजचा दिनविशेष मृत्यू नुसार</b>
															</td>
														</tr>
														<tr>
															<td style="padding: 25px 0 0 0; color: #153643; font-family: Arial, sans-serif; font-size: 16px; line-height: 20px;">
																{death}
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</table>
									</td>
								</tr>
							</table>
						</td>
					</tr>
					<tr>
						<td bgcolor="#ee4c50" style="padding: 30px 30px 30px 30px;">
							<table border="0" cellpadding="0" cellspacing="0" width="100%">
								<tr>
									<td style="color: #ffffff; font-family: Arial, sans-serif; font-size: 14px;" width="75%">
										&reg; Vinod Nimbalkar 2018<br/>
										You are receiving this because you are friend of Vinod Nimbalkar
									</td>
								</tr>
							</table>
						</td>
					</tr>
				</table>
			</td>
		</tr>
	</table>
</body>
"""

    msg.attach(MIMEText(body,'html'))

    filename= ['NewsPapers/Hindu.pdf']
    for f in filename:
        attachment = open(f,'rb')

        part = MIMEBase('application','octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',"attachment; filename= "+f)

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

def deleteNewsPaper():
    path = basedir+"/NewsPapers"
    if os.path.isdir(path):
        shutil.rmtree(path)
        print("News Paper Deleted")

if __name__ == "__main__":
    sh.every().day.at("08:05").do(theHindu)
    # sh.every().day.at("08:00").do(indianExpress)
    # sh.every().day.at("08:02").do(lokmat)
    sh.every().day.at("08:08").do(newspaperMail)
    sh.every().day.at("08:12").do(deleteNewsPaper)
    while True:
        sh.run_pending()
        time.sleep(1)