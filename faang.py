#!/usr/bin/env python3

# Problem 3: Script

# Shebang ref: https://realpython.com/python-shebang/

# Import necessary libraries
# Pandas for data manipulation: ref: https://pandas.pydata.org/
# yfinance for fetching stock data: ref: https://pypi.org/project/yfinance/
# Matplotlib for data visualization: ref: https://matplotlib.org/

import os
from datetime import datetime 
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates


def get_data(): 
    # List of tickers
        tickers = ['META', 'AAPL', 'AMZN', 'NFLX', 'GOOG']


        data = {}

        for ticker in tickers:
            stock = yf.Ticker(ticker)
            df = stock.history(period='5d', interval='1h')
            data[ticker] = df

# Combine all data into one DataFrame with a ticker column to ensure clear and easily readable 
        combined = pd.concat(data.values(), keys=data.keys(), names=['Ticker', 'Datetime'])

# Save and round to 2 decimal places
# Round function from w3schools - ref:https://www.w3schools.com/python/ref_func_round.asp
        price_cols = ['Open', 'High', 'Low', 'Close'] 
        combined[price_cols] = combined[price_cols].round(2)

# ensure output directory ists
        os.makedirs('data', exist_ok=True)

# timestamped filename
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        filename = f"data/{timestamp}.csv"


# Save the data and combine
        combined.to_csv(filename)
        print(f" Data saved to {filename}")
        return filename,combined
# Plotting function
def plot_data():
# Ensure plots directory exists
    os.makedirs('plots', exist_ok=True)
# Find the latest data file
    files = [f for f in os.listdir('data') if f.endswith('.csv')]
    if not files: print("No data files found in 'data' directory."); return
# Get the latest file based on filename sorting
    latest = sorted(files)[-1]
    filepath = os.path.join('data', latest)
# Read the data
    df = pd.read_csv(filepath, index_col=[0,1])
    df = df.reset_index()
    df.rename(columns={'level_0': 'Ticker', 'level_1': 'Datetime'}, inplace=True)

# Plot each ticker's closing prices
    plt.figure(figsize=(12, 8))    
    for ticker in df['Ticker'].unique(): 
            sub = df[df['Ticker'] == ticker]
            plt.plot(sub['Datetime'], sub['Close'], label=ticker)

# Customize the plot using Matplotlib
    plt.xlabel('Datetime')
    
    plt.ylabel('Closing Price (USD)')
    plt.title('FAANG Stock Prices - Last 5 Days (Hourly)')
    plt.legend()
    plt.grid(True)

# I ran into issue with datetime x-axis formatting, so I used Matplotlib's DateFormatter
# Matplotlib - ref:https://www.w3schools.com/python/matplotlib_plotting.asp
# DateFormatter ref:https://matplotlib.org/stable/api/dates_api.html
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.gcf().autofmt_xdate()
    
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    plot_filename = f"plots/FAANG_prices_{timestamp}.png"
    plt.savefig(plot_filename, dpi=200, bbox_inches='tight')
# Print the plot
    print(f"Plot saved to {plot_filename}")
# Main execution
if __name__ == "__main__":
    csv_file = get_data()
    plot_data()
    