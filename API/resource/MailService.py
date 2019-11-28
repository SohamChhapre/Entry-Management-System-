import smtplib,ssl
import base64
import os
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import time

EMAIL_ADDRESS="email"
EMAIL_PASSWORD="password"
def create_mail(sender,receiver,subject,body,*args):
    msg = MIMEMultipart()
    msg['Subject']=subject
    msg['From']=sender
    msg['To']=receiver
    msg.attach(MIMEText(body ,'plain'))
   
    return msg

def SendMail(body,subject,Emaillist):
    # context = ssl.create_default_context()
    # with smtplib.SMTP('smtp.gmail.com',587) as server:
    #     # server.ehlo()
    #     server.starttls()
    #     server.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    s = smtplib.SMTP('smtp-gmail.com',587)
    s.starttls()
    s.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
       
    
    for email in Emaillist:

            msg=create_mail(EMAIL_ADDRESS,email,subject,body)
            s.send_message(msg)    
    
    # creates SMTP session 
    # s = smtplib.SMTP('smtp.gmail.com', 587) 
    
    # # start TLS for security 
    # s.starttls() 
    
    # # Authentication 
    # s.login(EMAIL_ADDRESS, EMAIL_PASSWORD) 
    
    # # message to be sent 
    # message = "Message_you_need_to_send"
    
    # # sending the mail 
    # s.sendmail(EMAIL_ADDRESS, Emaillist[0], message) 
    
    # # terminating the session 
    # s.quit()   

def send_email(message,receiver):
    server = smtplib.SMTP ('smtp.gmail.com', 587)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    server.sendmail(EMAIL_ADDRESS, receiver, message)
    server.quit()

    

def send_email_at(send_time,message,sender):
    time.sleep(send_time.timestamp() - time.time())
    send_email(message,sender)
    print('email sent')   