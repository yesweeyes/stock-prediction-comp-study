import yfinance as yf

# Define stock ticker and date range
ticker = "AAPL"  # example: Apple Inc.
start_date = "2010-01-01"
end_date = "2023-01-01"

# Download data
stock_data = yf.download(ticker, start=start_date, end=end_date)

# Save to CSV
stock_data.to_csv("AAPL_stock_data.csv")
