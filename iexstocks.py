import requests

URL = "https://cloud.iexapis.com/"

#r = requests.get('https://cloud.iexapis.com/ref-data/iex/symbols')

token = 'pk_62e14354ce4f41b5bbb10e69f666afb1'
#https://cloud.iexapis.com/stable/tops?token=YOUR_TOKEN_HERE&symbols=aapl

#r = requests.get('https://cloud.iexapis.com/stable/tops?token={}&symbols=aapl'.format(token))

#print(r)
#print(r.content)

#HTTPS request
r = requests.get('https://cloud.iexapis.com/stable/ref-data/iex/symbols?token={}'.format(token))

#Get the names of all the stocks in the list
stockNames = []
for stock in r.json():
    stockNames.append(stock['symbol'])
#print(stockNames)

import random
def chooseStocks():
    chosenStocks = random.sample(stockNames, 5)
    #print(chosenStocks)
chooseStocks()

