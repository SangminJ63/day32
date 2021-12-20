import smtplib, ssl
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()

with open("quotes.txt") as data_file:
    quotes = data_file.readlines()

daily_quote = random.choice(quotes)

my_email = "sangminj63@yahoo.com"
my_password = "hyetfyysewpaxkgq"

context = ssl.create_default_context()
if weekday == 0:
    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
        connection.starttls(context=context)
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="sangminj63@gmail.com", msg=f"Subject:Today's Quote\n\n{daily_quote}")
        connection.close()
else:
    pass


