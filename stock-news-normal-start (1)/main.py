import requests
from datetime import datetime
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
today = datetime.today()
open_time = today.replace(day=7, hour=5, minute=0, second=0, microsecond=0)
close_time = today.replace(day=7, hour=20, minute=0, second=0, microsecond=0)
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_ENDPOINT_API = "1BF9SYLGKME2PXNB"
NEWS_ENDPOINT_API = "25c0f2993bd74b3ba30a441945ff967c"
NEWS_API_PARAMS = {
    "apikey": NEWS_ENDPOINT_API,
    "q": COMPANY_NAME,
    "from": str(open_time),
    "to": str(today)
}
STOCK_API_PARAMS = {
    "apikey": STOCK_ENDPOINT_API,
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK_NAME,
    "interval": "60min"
}
    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
r = requests.get(STOCK_ENDPOINT, params=STOCK_API_PARAMS)
r.raise_for_status()
intraday_data = r.json()
hourly_data = intraday_data["Time Series (60min)"]
open = float(hourly_data[str(open_time)]["1. open"])
close = float(hourly_data[str(close_time)]["4. close"])
high_prices = []
low_prices = []
for key in hourly_data:
    high_prices.append(hourly_data[key]["2. high"])
    low_prices.append(hourly_data[key]["3. low"])
high = max(high_prices)
low = min(low_prices)
percen_change = (abs(open - close)*100)/open
print(open, high, low, close, percen_change)
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
n = requests.get(NEWS_ENDPOINT, params=NEWS_API_PARAMS)
n. raise_for_status()
news = n.json()
articles = news["articles"][:3]
for n in articles:
    print(n["title"])
    print(n["content"])
#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

