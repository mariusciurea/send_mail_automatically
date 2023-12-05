"""This is a simple script that receives the following information as input

    - e-mail sender
    - e-mail receiver
    - e-mail subject
    - e-mail body

    It finally sends an e-mail from e-mail sender address (gmail) to e-mail receiver address (any email
    service)
"""
import os
import ssl
import smtplib
from email.message import EmailMessage
from configparser import ConfigParser


def get_config_data():
    """Get the configuration data from environment variables
    """

    mail = os.environ.get('EMAIL')
    passwd = os.environ.get('PASSWORD')
    return mail, passwd


def send_mail(message: EmailMessage, mail_from, mail_to, password, attachment=None):
    """Send an e-mail message from a gmail account to any other type of e-mail service
    """

    # adding security
    c = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=c) as email_smtp:
            email_smtp.login(mail_from, password)
            email_smtp.sendmail(mail_from, mail_to, message.as_string())
    except smtplib.SMTPException as e:
        print(e)
    except Exception:
        SystemExit(2)


if __name__ == '__main__':
    # mail_sender = input('e-mail from: ')
    # mail_receiver = input('e-mail to: ')
    # subject = input('e-mail subject: ')
    # body = input('e-mail body: ')

    email, password = get_config_data()

    # Create an instance of EmailMessage()
    msg = EmailMessage()
    msg['From'] = email
    msg['To'] = 'ciurea.marius1@gmail.com'
    msg['Subject'] = 'test from python'
    msg.set_content('Body: test from my python script')

    # Get the password from config.ini file

    # send the e-mail
    send_mail(msg, email, 'ciurea.marius1@gmail.com', password)
