import yfinance as yf

# Download GameStop stock data
gamestop = yf.Ticker("GME")
gamestop_data = gamestop.history(period="max")

# Display the first few rows of the dataset
gamestop_data.head()
