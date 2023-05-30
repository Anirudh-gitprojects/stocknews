STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
#REPLace Keys with environment vars.
api_key=GET_ENV
api_key2=GET_ENV
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
from twilio.rest import Client
twilio_sid=get_env(ENV_VAR)
twilio_auth=get_env(ENV_VAR)

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
import requests
from datetime import date, timedelta
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=TSLA&apikey=V8F1ML3AU3VAULVM'

url2="https://newsapi.org/v2/everything?q=Tesla&apiKey=a142dbd2ee7d47448553773bdc8f2e44"

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_params={"function": "TIME_SERIES_DAILY",
              "symbol": STOCK_NAME,
                "apikey": api_key,}
r = requests.get(url)
data = r.json()
yesterday = date.today() - timedelta(1)
day_before=date.today()-timedelta(2)
print(yesterday)
print(day_before)
print(data["Time Series (Daily)"])
yesterday_price=data["Time Series (Daily)"][f'{yesterday}']['4. close']
day_before_price=data["Time Series (Daily)"][f'{day_before}']['4. close']
print(yesterday_price)
print(day_before_price)
#TODO 2. - Get the day before yesterday's closing stock price

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
positive_diff=abs(float(yesterday_price)-float(day_before_price))
print(positive_diff)
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percentage=(positive_diff/float(yesterday_price))*100
print(diff_percentage)
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
new_params={
    "apiKey":api_key2,
    "q":COMPANY_NAME,
}
response2=requests.get('https://newsapi.org/v2/everything?q=Tesla&apiKey=a142dbd2ee7d47448553773bdc8f2e44')
response2.raise_for_status()
data_news=response2.json()["articles"]
print(data_news)
three_articles=data_news[:3]
new_article=[]
for article in three_articles:
    new_article.append(f"Title : {article['title']} \nDescription: {article['description']}")


#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio.



# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
from twilio.rest import Client

account_sid = env_var
auth_token = env_var
client = Client(account_sid, auth_token)

for article in new_article:
    message = client.messages.create(
    from_='your twilionum',
    body= article,
    to='mynum'
)

print(message.sid)
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

