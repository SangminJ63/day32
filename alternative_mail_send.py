import smtplib
import ssl
from email.message import EmailMessage

msg = EmailMessage()
msg["From"] = "sangminj63@gmail.com"
my_password = "abcd9836()"
msg["To"] = "sangminj63@yahoo.com"
msg["Subject"] = "This is the Subject"
body = "This is the mail body."
msg.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP("smtp.gmail.com", port=587) as smtp:
    smtp.starttls(context=context)
    smtp.login(msg["From"], my_password)
    smtp.send_message(msg)

