import smtplib

from configparser import  ConfigParser


config = ConfigParser()
config.read("../config.cfg")
email_user = config["email"]["account"]
email_secret = config["email"]["secret"]


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=email_user, password=email_secret)
    connection.sendmail(
        from_addr=email_user,
        to_addrs="rubenblancomanzano@gmail.com",
        msg="Subject:Hi!!\n\nThis is the body of the mail"
    )
