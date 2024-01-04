import smtplib
import time
from configparser import ConfigParser

import requests
from datetime import datetime

MY_LAT = 40.4165
MY_LONG = -3.70256


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5):
        return True
    else:
        return False

def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunrise or time_now <= sunset:
        return True
    else:
        return False


while True:

    if is_iss_overhead() and is_night():
        config = ConfigParser()
        config.read("../config.cfg")
        email_user = config["email"]["account"]
        email_secret = config["email"]["secret"]

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email_user, password=email_secret)
            message = f"Subject:Check the sky!!\n\nISS is crossing your night sky!"
            connection.sendmail(
                from_addr=email_user,
                to_addrs="test@gmail.com",
                msg=message.encode("utf-8")
            )
    else:
        print("ISS is not crossing your location")
    time.sleep(60)

