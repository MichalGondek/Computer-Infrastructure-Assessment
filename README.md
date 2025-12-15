# Computer-Infrastructure-Assessment
# Author Michal Gondek

# FAANG Stock Dtat Automation Project

## Overview
This project automates the collection, visulaisation and scheduling of hourly stock price data for five FAANG companies
This repository was set up as part of the Computer Infrasctucture assessment and demonstrates scripting, auotmation and workflow organisation
- Facebook (META)
- Apple (APPL)
- Amazon (AMZN)
- Netflix (NFLX)
- Google (GOOG)

Using Python the project:
- Downlaods the most recet five dats of hourly stock data
- Saved the data in a structured format
- Generates a combined price plot
- Automatically runs a Github Action on a schdule every Saturday at 9:00 UTC

## Use of this Project
- Demonstraters practical use of finicnial API yfinance
- Shows correct handling of file automation and timestamping
- Uses Matplotlib for data visualisation
- Implements continuous automation with GitHub Actions