import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

data = []
for row in table.find_all('tr')[1:]:  # Skipping the header row
        cols = row.find_all('td')
        if len(cols) >= 2:  # Ensure there are enough columns in the row
            date = cols[0].text.strip()
            revenue = cols[1].text.strip().re


gamestop_data = yf.Ticker("GME").history(period="max")
gamestop_revenue_df = pd.DataFrame(data, columns=['Date', 'Revenue'])

# Create a figure
fig = go.Figure()

# Add GameStop stock price trace
fig.add_trace(go.Scatter(x=gamestop_data.index, y=gamestop_data['Close'], mode='lines', name='GameStop Stock Price'))

# Add GameStop revenue trace
fig.add_trace(go.Scatter(x=gamestop_revenue_df['Date'], y=gamestop_revenue_df['Revenue'], mode='lines', name='GameStop Revenue'))

# Update the layout
fig.update_layout(title="GameStop Stock Price and Revenue", xaxis_title="Date", yaxis_title="USD")
fig.show()
