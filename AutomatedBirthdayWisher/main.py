import os
import random
import smtplib
import pandas as pd
import datetime as dt
from configparser import ConfigParser

current_dir_password = os.path.dirname(__file__)
csv_path = os.path.join(current_dir_password, "birthdays.csv")
letter_path = os.path.join(current_dir_password, "letter_templates/")

date = dt.datetime.now()
month = date.month
day = date.day

df = pd.read_csv(csv_path)
filtered_df = df[(df["month"] == month) & (df["day"] == day)]


def get_random_path():
    files_txt = [archivo for archivo in os.listdir(letter_path) if archivo.endswith('.txt')]
    random_file_txt = random.choice(files_txt)
    random_file_path = os.path.join(current_dir_password, f"{letter_path}{random_file_txt}")

    return random_file_path


def send_email(name, path):
    config = ConfigParser()
    config.read("../config.cfg")
    email_user = config["email"]["account"]
    email_secret = config["email"]["secret"]

    with open(path, "r", encoding="utf-8") as data_file:
        file = data_file.read()
        file = file.replace("[NAME]", name)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email_user, password=email_secret)
        message = f"Subject:Happy Birthday!!\n\n{file}"
        connection.sendmail(
            from_addr=email_user,
            to_addrs="test@gmail.com",
            msg=message.encode("utf-8")
        )


if not filtered_df.empty:
    for index, row in filtered_df.iterrows():
        file_path = get_random_path()
        send_email(row["name"], file_path)











