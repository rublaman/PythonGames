import os
from twilio.rest import Client
from datetime import date, timedelta
import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
news_api_key = os.environ['NEWSAPI_API_KEY']
alphavantage_api_key = os.environ['ALPHAVANTAGE_API_KEY']


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def get_stock_price() -> dict:
    alphavantage_response = requests.get(
        f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={alphavantage_api_key}")
    data_alphavantage = alphavantage_response.json()
    return data_alphavantage


def get_fluctuation_stock(data_stock: dict) -> float:
    yesterday = date.today() - timedelta(days=1)
    before_yesterday = date.today() - timedelta(days=2)
    before_yesterday_str = before_yesterday.strftime("%Y-%m-%d")
    yesterday_str = yesterday.strftime("%Y-%m-%d")
    yesterday_close = data_stock["Time Series (Daily)"][yesterday_str]["4. close"]
    before_yesterday_close = data_stock["Time Series (Daily)"][before_yesterday_str]["4. close"]

    difference = yesterday_close - before_yesterday_close
    percentage = round(difference / before_yesterday_close * 100)
    if percentage >= 5 or percentage <= -5:
        return percentage
    else:
        return 0


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def get_last_three_news(fluctuation: int) -> list[dict]:
    list_news = []
    news_response = requests.get(f"https://newsapi.org/v2/top-headlines?q=tesla&apiKey={news_api_key}")
    data_news = news_response.json()
    for news in data_news["articles"][:3]:
        list_news.append({
            "fluctuation": fluctuation,
            "title": news["title"],
            "description": news["description"]
        })
    return list_news


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
def send_sms(news: dict):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+',
        body=f'{STOCK}: {news["fluctuation"]}\nHeadline: {news["title"]}\nBrief: {news["description"]}',
        to='+'
    )
    print(message.sid)


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


def main():
    stock_prices = get_stock_price()
    # fluctuation = get_fluctuation_stock(stock_prices)
    fluctuation = 5
    if fluctuation != 0:
        last_three_news = get_last_three_news(fluctuation)
        for news in last_three_news:
            send_sms(news)


main()
