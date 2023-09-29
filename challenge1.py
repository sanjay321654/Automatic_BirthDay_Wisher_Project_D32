from datetime import datetime
from smtplib import SMTP
import random

my_email = "pythoncourse20102002@gmail.com"
my_password = "tenq ovqz kxvu wghm"

now = datetime.now()

with open("quotes.txt") as quotes:
    list_quotes = quotes.readlines()
    random_quotes = random.choice(list_quotes)

day_of_week = now.weekday()
if day_of_week == 0:
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="sanjay20102002@yahoo.com",
                            msg=f"Subject: Monday Motivation\n\n{random_quotes}")
