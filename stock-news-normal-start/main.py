import requests
from datetime import datetime, timedelta
import smtplib

my_email = ""
gmail_app_password = ""

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY_STOCKS = ""
API_KEY_NEWS = ""

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
parameters_stock = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": API_KEY_STOCKS
}

response_stock = requests.get(url=STOCK_ENDPOINT, params=parameters_stock)
response_stock.raise_for_status()
stock_data = response_stock.json()

yesterday = datetime.now() - timedelta(days=1)
yesterday_str = yesterday.strftime("%Y-%m-%d")
# print(yesterday_str)

yesterday_close_price = float(stock_data["Time Series (Daily)"][yesterday_str]["4. close"])
# print(yesterday_close_price)

#TODO 2. - Get the day before yesterday's closing stock price

day_before_yesterday = datetime.now() - timedelta(days=2)
day_before_yesterday_str = day_before_yesterday.strftime("%Y-%m-%d")

day_before_yesterday_close_price = float(stock_data["Time Series (Daily)"][day_before_yesterday_str]["4. close"])
# print(day_before_yesterday_close_price)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

close_difference = abs(day_before_yesterday_close_price - yesterday_close_price)
# print(close_difference)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

percentage_difference = round(((yesterday_close_price - day_before_yesterday_close_price) / day_before_yesterday_close_price) * 100, 2)
# print(f"{percentage_difference}%")

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

if percentage_difference >= 5:
    print("Get News!!!")

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    news_parameters = {
        "q": COMPANY_NAME,
        "from": yesterday_str,
        "sortBy": "popularity",
        "apiKey": API_KEY_NEWS
    }

    response_news = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    response_news.raise_for_status()
    news_data = response_news.json()

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

    first_3_articles = news_data["articles"][:3]

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

    final_articles_list = [f"{article['title']}: {article['description']}" for article in first_3_articles]
    print(final_articles_list)


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 9. - Send each article as a separate message via Twilio. 

# from twilio.rest import Client
#
#     client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
#
#     for article in articles_list:
#         message = client.messages \
#             .create(
#                 body=article,
#                 from_='+1234567890',
#                 to=PHONE_NUMBER
#             )
#
#         print(message.status)

# TODO:10 Send notification to your email.
    for article in final_articles_list:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=gmail_app_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="",
                                msg=f"Subject:{STOCK_NAME}\n\n{article.encode('utf-8')}")
    connection.close()

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

