import smtplib, ssl

my_email = "sangminj63@yahoo.com"
my_password = "hyetfyysewpaxkgq"

context = ssl.create_default_context()
with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
    connection.starttls(context=context)
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs="sangminj63@gmail.com", msg="Subject:Hello\n\nThis is the way.")
    connection.close()
