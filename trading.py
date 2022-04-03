import alpaca_trade_api as tradeapi

BASE_URL = "https://paper-api.alpaca.markets"
#*keys here not for you

api = tradeapi.REST(key_id=ALPACA_API_KEY, secret_key=ALPACA_SECRET_KEY, 
                    base_url=BASE_URL, api_version='v2')

def buyStocks(stocks):
    for stock in stocks:
        api.submit_order(stock,5,'buy','market','gtc')

print(api.list_positions())