import random
import smtplib
import datetime as dt
import os
from configparser import ConfigParser

current_dir_password = os.path.dirname(__file__)
file_path = os.path.join(current_dir_password, "quotes.txt")

config = ConfigParser()
config.read("../config.cfg")
email_user = config["email"]["account"]
email_secret = config["email"]["secret"]

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    with open(file_path, "r", encoding="utf-8") as data_file:
        lines = data_file.readlines()
        phrase = random.choice(lines)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email_user, password=email_secret)
        message = f"Subject:Phrase of the day!\n\n{phrase}"
        connection.sendmail(
            from_addr=email_user,
            to_addrs="test@gmail.com",
            msg=message.encode("utf-8")
        )
