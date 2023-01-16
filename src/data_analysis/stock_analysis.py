# Raw Package
import numpy as np
import pandas as pd

#Data Source
import yfinance as yf

google = yf.Ticker("GOOGL") 
# #shares out standing 
print(google.shares) 
print("--------------------------")
print(google.get_shares_full())

#earnings 
print("--------------------------")
print(google.earnings)
print("--------------------------")
print(google.quarterly_earnings)

#dividends
print("--------------------------")
print(google.dividends)

#income statement
print("--------------------------")
print(google.income_stmt)

#balance sheet
print("--------------------------")
print(google.balance_sheet.to_string())

#cash_flow
print("--------------------------")
print(google.cash_flow.to_string())