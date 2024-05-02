from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'example@gmail.com'
email_password = 'app password'

email_receiver = 'example2@gmail.com'

subject = "Don't forget to subscribe"

body = """
When you watch a video, please hit subscribe.
love u~
"""

em = EmailMessage()
em['from'] = email_sender
em['to'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

