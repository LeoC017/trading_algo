import backtrader as bt
import yfinance as yf
import requests
import pandas as pd

api_key = '6JXLLU69O4A69AUK'

# Endpoint URL to fetch top N companies by market cap
endpoint = f"https://www.alphavantage.co/query?function=LISTING_STATUS&apikey={api_key}"

# Define the number of companies you want to track
num_companies = 100

# Make a GET request to the Alpha Vantage API
response = requests.get(endpoint)

if response.status_code == 200:
    # Read CSV data directly into a Pandas DataFrame
    data = pd.read_csv(response.text)
    
    # Extract top N companies from the DataFrame
    top_companies = data.head(num_companies)
    
    # Extract ticker symbols of top companies
    ticker_symbols = top_companies['symbol'].tolist()
    
    # Print each ticker symbol line by line
    for symbol in ticker_symbols:
        print(symbol)

##############################################################
    # data = response.json()
    
    # # Extract top N companies from the response
    # top_companies = data['data'][:num_companies]

    # # Extract ticker symbols of top companies
    # ticker_symbols = [company['symbol'] for company in top_companies]
    
    # Now you have a list of ticker symbols to observe
    # print(ticker_symbols)
else:
    print("Failed to fetch data")