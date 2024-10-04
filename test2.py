import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL for Tesla revenue data
url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
html_content = requests.get(url).text

# Parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Locate and extract the relevant table (you'll need to inspect the site)
table = soup.find_all('table')[1]  # Example table selection

# Extracting data
data = []
for row in table.find_all('tr')[1:]:
    cols = row.find_all('td')
    date = cols[0].text.strip()
    revenue = cols[1].text.strip()
    data.append([date, revenue])

# Convert to DataFrame
tesla_revenue_df = pd.DataFrame(data, columns=['Date', 'Revenue'])

# Display the first few rows
tesla_revenue_df.head()



