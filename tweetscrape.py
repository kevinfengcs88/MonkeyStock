import pandas as pd
import tweepy
import config

from keys.py import *

def auth():
    try:
        auth = tweepy.OAuthHandler(config.API_KEY, config.API_SECRET)
        auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_SECRET)
        api = tweepy.API(auth)
    except:
        print("Error")

    return api

def search_by_stock(api, date_since, date_until, stock):
    df = pd.DataFrame(columns=['text']) 
    tweets = tweepy.Cursor(api.search, q=stock, lang="it", wait_on_rate_limit=True,
                           since=date_since, until=date_until, tweet_mode='extended').items() 
    list_tweets = [tweet for tweet in tweets] 
         
    for tweet in list_tweets: 
        try: 
            text = tweet.retweeted_status.full_text 
        except AttributeError: 
            text = tweet.full_text 

        tweets = [text]

        df.loc[len(df)] = tweets 
          
    filename = 'tweets.csv'
    df.to_csv(filename) 

api = auth()
example_stock = "$GME"
start_date = "2022-03-30"
end_date = "2022-03-31"
search_by_stock(api, start_date, end_date, example_stock)