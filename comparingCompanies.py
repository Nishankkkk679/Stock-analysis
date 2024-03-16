import yfinance as yf

# Get the stock data for two companies
stock1 = yf.download('AAPL', start='2020-01-01', end='2022-12-31')
stock2 = yf.download('GOOG', start='2020-01-01', end='2022-12-31')

# Calculate the returns for the two stocks
returns1 = stock1['Close'].pct_change()
returns2 = stock2['Close'].pct_change()

# Calculate the correlation between the returns
correlation = returns1.corr(returns2)

# Print the correlation
print(correlation)
