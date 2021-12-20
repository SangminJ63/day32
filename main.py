import datetime as dt
import pandas as pd
import random
import smtplib, ssl

now = dt.datetime.now()
today = (now.month, now.day)

my_email = "sangminj63@yahoo.com"
my_password = "hyetfyysewpaxkgq"

birthdays = pd.read_csv("birthdays.csv")
birthdays_dict = {(row["month"], row["day"]): row for (index, row) in birthdays.iterrows()}

if today in birthdays_dict:
    with open(f"letter_templates\letter_{random.randint(1,3)}.txt") as letter:
        mail_body = letter.read()
        mail_body = mail_body.replace("[NAME]", birthdays_dict[today]["name"])
    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=birthdays_dict[today]["email"], msg=f"Subject:Happy Birthday!\n\n{mail_body}")
