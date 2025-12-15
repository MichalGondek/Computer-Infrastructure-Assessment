#!/usr/bin/env python3

# Problem 3: Script
# Create a Python script called faang.py in the root of your repository
# Copy the above functions into it and make it so that whenever someone at the terminal types ./faang.py
# The script runs, downloading the data and creating the plot.
# Note that this will require a shebang line and the script to be marked executable. Explain the steps you took in your notebook.

# Shebang reference: https://realpython.com/python-shebang/

#!/usr/bin/env python3
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

# combine all data into one DataFrame with a ticker column to ensure clear and easily readable 
        combined = pd.concat(data.values(), keys=data.keys(), names=['Ticker', 'Datetime'])

# Save and round to 2 decimal places
# Round function from w3schools - https://www.w3schools.com/python/ref_func_round.asp
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

def plot_data():

    os.makedirs('plots', exist_ok=True)

    files = [f for f in os.listdir('data') if f.endswith('.csv')]
    if not files: print("No data files found in 'data' directory."); return

    latest = sorted(files)[-1]
    filepath = os.path.join('data', latest)

    df = pd.read_csv(filepath, index_col=[0,1])
    df = df.reset_index()
    df.rename(columns={'level_0': 'Ticker', 'level_1': 'Datetime'}, inplace=True)

    plt.figure(figsize=(12, 8))

    for ticker in df['Ticker'].unique(): 
            sub = df[df['Ticker'] == ticker]
            plt.plot(sub['Datetime'], sub['Close'], label=ticker)


    plt.xlabel('Datetime')
    plt.ylabel('Closing Price (USD)')
    plt.title('FAANG Stock Prices - Last 5 Days (Hourly)')
    plt.legend()
    plt.grid(True)

# I ran into issue with datetime x-axis formatting, so I used Matplotlib's DateFormatter
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.gcf().autofmt_xdate()
    
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    plot_filename = f"plots/FAANG_prices_{timestamp}.png"
    plt.savefig(plot_filename, dpi=200, bbox_inches='tight')

    print(f"Plot saved to {plot_filename}")

if __name__ == "__main__":
    csv_file = get_data()
    plot_data()
    