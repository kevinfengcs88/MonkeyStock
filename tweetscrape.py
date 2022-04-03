import pandas as pd
import tweepy

#from keys.py import *

# keys go here

def auth():
    try:
        auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        api = tweepy.API(auth)
    except:
        print("Error")
        return

    print("here")
    return api

def search_by_stock(api, stock):
    df = pd.DataFrame(columns=['text']) 
    tweets = tweepy.Cursor(api.search_tweets, q=stock, lang="en", result_type="mixed", count = 100).items() 
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
    print(df)

api = auth()
example_stock = "$GME"
start_date = "2022-03-30"
end_date = "2022-03-31"
search_by_stock(api, start_date, end_date, example_stock)