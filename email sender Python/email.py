from email.message import EmailMessage

import ssl
import smtplib

email_sender = """Write you email here"""
email_password ="""Write the password that google gave you from appp password"""

email_receiver ="divor88998@devswp.com"

subject = "Dont forget to code"
body = """
When you start coding, dont forget to get a coffee
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em[' subject'] = subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL( 'smtp.gmail.com' , 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())


