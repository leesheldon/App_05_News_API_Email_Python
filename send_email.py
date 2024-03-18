import smtplib
import ssl
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "lhanco@gmail.com"
    password = os.getenv("Python_App_Send_Email")

    receiver = "lhanco@gmail.com"
    context = ssl.create_default_context()

    msg = MIMEMultipart('alternative')
    msg['From'] = username
    msg['To'] = receiver
    msg['Subject'] = "Subject: Today's news" + "\n"

    html_part = MIMEText(message, 'html')
    msg.attach(html_part)

    msg_str = msg.as_string()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, msg_str)

















































