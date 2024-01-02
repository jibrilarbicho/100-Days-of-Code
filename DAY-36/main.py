from cgi import print_arguments
import requests
from twilio.rest import Client
import os

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "9XI6UFJPCKTDNC3V"
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
NEWS_API = "5e48832105ba49a5ade3843776a785e7"
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
datalist = [value for (key, value) in data.items()]
# print(datalist)
yestrday = datalist[0]
yestrday_close_price = yestrday["4. close"]
print(yestrday_close_price)
day_before_yestday_data = datalist[1]
day_before_yestday_data_closing_price = day_before_yestday_data["4. close"]
print(day_before_yestday_data_closing_price)
difference = abs(
    float(yestrday_close_price) - float(day_before_yestday_data_closing_price)
)
print(difference)
diff_percent = (difference / float(yestrday_close_price)) * 100
print(diff_percent)

if diff_percent > 1:
    news_params = {"apikey": NEWS_API, "qInTitle": COMPANY_NAME}

    newResponse = requests.get("https://newsapi.org/v2/everything", params=news_params)
    articles = newResponse.json()["articles"]
print(articles)
three_articles = articles[:3]


formatted_articles = [
    f"Headline: {article['title']},\nBrief: {article['description']}"
    for article in three_articles
]
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
client = Client(account_sid, auth_token)
for articless in formatted_articles:
    message = client.messages.create(
        body=articless,
        from_="+16174311282",
        to="+251 93 404 4223",
    )

print(message.sid)
