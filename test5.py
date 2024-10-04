import yfinance as yf
import pandas as pd

# Download Tesla stock data using yfinance
tesla_data = yf.Ticker("TSLA")
tesla_revenue_df = tesla_data.history(period="max")

# Example of Tesla revenue DataFrame (you should already have this)
tesla_revenue_df.head()

import plotly.graph_objects as go

# Create a figure
fig = go.Figure()

# Add Tesla stock price trace
fig.add_trace(go.Scatter(x=tesla_data.index, y=tesla_data['Close'], mode='lines', name='Tesla Stock Price'))

# Add Tesla revenue trace
fig.add_trace(go.Scatter(x=tesla_revenue_df['Date'], y=tesla_revenue_df['Revenue'], mode='lines', name='Tesla Revenue'))

# Update the layout
fig.update_layout(title="Tesla Stock Price and Revenue", xaxis_title="Date", yaxis_title="USD")
fig.show()
