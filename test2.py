# backtrader Simple Moving Average Crossover

# 6JXLLU69O4A69AUK
# alpha vantage api key

from datetime import datetime
import backtrader as bt
import yfinance as yf
import requests
import pandas as pd

# Create a subclass of Strategy to define the indicators and logic

class SmaCross(bt.Strategy):
    # list of parameters which are configurable for the strategy
    params = dict(
        pfast=10,  # period for the fast moving average
        pslow=30   # period for the slow moving average
    )

    def __init__(self):
        sma1 = bt.ind.SMA(period=self.p.pfast)  # fast moving average
        sma2 = bt.ind.SMA(period=self.p.pslow)  # slow moving average
        self.crossover = bt.ind.CrossOver(sma1, sma2)  # crossover signal

    def next(self):
        if not self.position:  # not in the market
            if self.crossover > 0:  # if fast crosses slow to the upside
                self.buy()  # enter long

        elif self.crossover < 0:  # in the market & cross to the downside
            self.close()  # close long position


cerebro = bt.Cerebro()  # create a "Cerebro" engine instance

# Create a data feed
#data = bt.feeds.YahooFinanceData(dataname='TSLA',
#                                 fromdate=datetime(2021, 1, 1),
#                                 todate=datetime(2022, 12, 31))

# Fetch data using yfinance
data = yf.download('TSLA', start='2022-12-12', end='2023-12-12')

# Convert data to Pandas DataFrame
data = bt.feeds.PandasData(dataname=data)


# api_key = '6JXLLU69O4A69AUK'

# # Endpoint URL to fetch top N companies by market cap
# endpoint = "https://www.alphavantage.co/query?function=LISTING_STATUS&apikey={api_key}"

# # Define the number of companies you want to track
# num_companies = 100

# # Make a GET request to the Alpha Vantage API
# response = requests.get(endpoint)

# if response.status_code == 200:
#     data = response.json()
    
#     # Extract top N companies from the response
#     top_companies = data['data'][:num_companies]

#     # Extract ticker symbols of top companies
#     ticker_symbols = [company['symbol'] for company in top_companies]
    
#     # Now you have a list of ticker symbols to observe
#     print(ticker_symbols)
# else:
#     print("Failed to fetch data")


# cerebro.adddata(data)  # Add the data feed

# cerebro.addstrategy(SmaCross)  # Add the trading strategy
# cerebro.run()  # run it all
# cerebro.plot()  # and plot it with a single command


