import alpaca_trade_api as tradeapi

BASE_URL = "https://paper-api.alpaca.markets"
ALPACA_API_KEY = 'PK79TSBSO0EWBBBU55OE'
ALPACA_SECRET_KEY = #SECRET KEY NOT FOR YOU!!!!

api = tradeapi.REST(key_id=ALPACA_API_KEY, secret_key=ALPACA_SECRET_KEY, 
                    base_url=BASE_URL, api_version='v2')

def buyStocks(stocks):
    for stock in stocks:
        api.submit_order(stock,5,'buy','market','gtc')

print(api.list_positions())