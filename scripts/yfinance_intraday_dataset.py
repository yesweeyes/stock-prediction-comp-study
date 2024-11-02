import yfinance as yf
import pandas as pd

# Define the stock ticker and data interval
ticker = "AAPL"
interval = "15m"  # Switching to a 15-minute interval
period = "1mo"    # Keeps the data range to the last 30 days

# Download the data
try:
    data = yf.download(ticker, period=period, interval=interval)
    
    # Check if data is retrieved successfully
    if not data.empty:
        # Save the data to a CSV file
        data.to_csv("AAPL_30days_15min_data.csv")
        print("Downloaded Data Sample:")
        print(data.head())
    else:
        print("No data found for the specified period and interval.")

except Exception as e:
    print("Error downloading data:", e)
