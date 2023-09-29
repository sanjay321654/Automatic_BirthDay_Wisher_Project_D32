from datetime import datetime
import pandas
import random
from smtplib import SMTP

my_email = "pythoncourse20102002@gmail.com"
my_password = "tenq ovqz kxvu wghm"

today = datetime.now()

today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
data_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in data_dict:
    birthday_person = data_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter:
        content = letter.read()
        new_content = content.replace("[NAME]", birthday_person["name"])

    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"],
                            msg=f"Subject: Happy Birthday!\n\n{new_content}")
