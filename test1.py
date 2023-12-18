import pandas as pd
import matplotlib.pyplot as plt

# Get historical price data (replace this with your data source)
# For example, using Pandas' data reader with Yahoo Finance
# Make sure to adjust the parameters according to your requirements
data = pd.read_csv('TSLA.csv')

# Calculate moving averages
data['SMA_50'] = data['Close'].rolling(window=50).mean()
data['SMA_200'] = data['Close'].rolling(window=200).mean()

# Generate buy/sell signals based on crossover
data['Signal'] = 0
data.loc[data['SMA_50'] > data['SMA_200'], 'Signal'] = 1  # Buy signal
data.loc[data['SMA_50'] < data['SMA_200'], 'Signal'] = -1  # Sell signal

# Visualize the strategy
plt.figure(figsize=(10, 6))
plt.plot(data['Close'], label='Price')
plt.plot(data['SMA_50'], label='SMA 50')
plt.plot(data['SMA_200'], label='SMA 200')
plt.plot(data[data['Signal'] == 1]['Close'], marker='^', markersize=10, color='g', label='Buy Signal')
plt.plot(data[data['Signal'] == -1]['Close'], marker='v', markersize=10, color='r', label='Sell Signal')
plt.legend()
plt.show()
