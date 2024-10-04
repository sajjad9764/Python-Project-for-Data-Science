import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL for GameStop revenue data
url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
html_content = requests.get(url).text

# Parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Locate and extract the relevant table
table = soup.find_all('table')[1]

# Extracting data
data = []
for row in table.find_all('tr')[1:]:
    cols = row.find_all('td')
    date = cols[0].text.strip()
    revenue = cols[1].text.strip()
    data.append([date, revenue])

# Convert to DataFrame
gamestop_revenue_df = pd.DataFrame(data, columns=['Date', 'Revenue'])

# Display the first few rows
gamestop_revenue_df.head()


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