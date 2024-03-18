import numpy as np #numerical computing in python, based in c++ so it is faster
import pandas as pd #data science library for data manipulation and analysis
import pandasgui as pg
import math #python mathematical functions
import tkinter as tk

from tkinter import Text,Scrollbar, simpledialog
from my_secrets import IEX_CLOUD_API_TOKEN #API Token is in a secrets.py file
from api_methods import fetch_stock_data #method from other file to perform GET request
from api_methods import quote_dictionary, fundamentals_dictionary

#make market cap easier to read
def format_market_cap(market_cap):
    if market_cap >= 10**12:
        return f'{market_cap / 10**12:.2f}T'
    elif market_cap >= 10**9:
        return f'{market_cap / 10**9:.2f}B'
    else:
        return market_cap


stocks = ['MSFT', 'AAPL', 'NVDA', 'AMZN', 'GOOGL', 'META', 'TSLA', 'LLY', 'V', 'AVGO']


my_columns = [
    "Company", 
    "Ticker", 
    "Last Price", 
    "Market Cap", 
    "PE Ratio", 
    "52 week high", 
    "52 week low", 
    "YTD Change",
    "Revenue",
    "Revenue Growth",
    "Profit Margin",
    "Total Cash Flow",
    "Long Term Debt"
]

final_dataframe = pd.DataFrame(columns=my_columns)
pd.set_option('display.max_colwidth', 30)

for stock in stocks:
    fetch_stock_data(stock)
    
    new_data = pd.Series([
        quote_dictionary.get('companyName'), 
        quote_dictionary.get('symbol'), 
        quote_dictionary.get('latestPrice'), 
        quote_dictionary.get('marketCap'), 
        quote_dictionary.get('peRatio'), 
        quote_dictionary.get('week52High'), 
        quote_dictionary.get('week52Low'), 
        quote_dictionary.get('ytdChange'),
        fundamentals_dictionary.get('revenue'),
        fundamentals_dictionary.get('pricePerEarningsPerRevenueYoyDeltaPercent'),
        fundamentals_dictionary.get('profitGrossPerRevenue'),
        fundamentals_dictionary.get('totalCashFlow'),
        fundamentals_dictionary.get('liabilitiesNonCurrentDebt')
    ], index=my_columns)
    
    final_dataframe = pd.concat([final_dataframe, new_data.to_frame().T], ignore_index=True)
    
final_dataframe['Market Cap'] = final_dataframe['Market Cap'].apply(format_market_cap)
final_dataframe['Revenue'] = final_dataframe['Revenue'].apply(format_market_cap)
final_dataframe['Total Cash Flow'] = final_dataframe['Total Cash Flow'].apply(format_market_cap)
final_dataframe['Long Term Debt'] = final_dataframe['Long Term Debt'].apply(format_market_cap)

gui_quote = pg.show(final_dataframe)
