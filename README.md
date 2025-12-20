# Computer-Infrastructure-Assessment
# Author Michal Gondek

# FAANG Stock Data Automation Project

## Overview
This project automates the collection, visualization and scheduling of hourly stock price data for five FAANG companies
This repository was set up as part of the Computer Infrastructure assessment and demonstrates scripting, auotmation and workflow organisation
- Facebook (META)
- Apple (APPL)
- Amazon (AMZN)
- Netflix (NFLX)
- Google (GOOG)

## Using Python this project:
- Downloads the most recent five dats of hourly stock data
- Saved the data in a structured format
- Generates a combined price plot
- Automatically runs a Github Action on a schedule every Saturday at 9:00 UTC

## Use of this Project
- Demonstrates practical use of financial API yfinance
- Shows correct handling of file automation and timestamping
- Uses Matplotlib for data visualisation
- Implements continuous automation with GitHub Actions

## Problem 1 - Data Collection
In problem 1 I used yfinance package to:
- Download hourly stock data for previous 5 days
- Cover all five stocks listed in brief
- Combine data into single Pandas DataFrame
- Round price values to two decimal places
- Save the tile to data/ directory

## Problem 2 - Plotting Data
In problem 2 I used Function plot_data/matplotlib to:
- Load the most recent CSV file from the data directory
- Plot the close price for each of the 5 stocks on a single chart
- I included axis labels, legend, grid and clear datetime formatting for easy readability 
- Saved the plot to plots/ directory

## Problem 3 - Script
In problem 3 I wrote a script called faang.py to:
- Run get_data and plot_data functions including shebang line to execute directly from the terminal
- This script downloads the latest stock data
- Saves it to the data folder
- Generates and saves a plot to the plots folder

## Problem 4 - Automation
In problem 4 I wrote a automation script in github actions workflow to:
- Run workflow every Saturday at 9:00am UTC
- Use workflow_dispatch to manually test workflow
- Use the latest Ubuntu runner
- Install Python 3.12
- Execute the faang.py script automatically 

# Advise on how to run locally
To run this code in its designed manner:
- Clone the repository 
- Pip install yfinance pandas matplotlib
- Run script

# Conclusion
This project provided me with practical experience in building an end to end automated data pipeline using Python.
Through using financial data with the yfinance library, structuring and sorting datesets using Pandas and creating clear visualizations using Matplotlib
I strengthened my understanding of data handling and analysis workflows.
Using GitHub Actions reinforced key concepts in scripting, scheduling and continuous automation.
Overall the project improved my confidence in working with real world data and deploying automated solutions using modern development tools.