import numpy as np #numerical computing in python, based in c++ so it is faster
import pandas as pd #data science library for data manipulation and analysis
import math #python mathematical functions
import tkinter as tk

from tkinter import Text,Scrollbar, simpledialog
from my_secrets import IEX_CLOUD_API_TOKEN #API Token is in a secrets.py file
from api_methods import fetch_stock_data #method from other file to perform GET request
from api_methods import dictionary

#method to get the ticker from user input, simple gui
def get_ticker():
    ticker = simpledialog.askstring("Input", "Enter the stock ticker:")
    
    if ticker:
        fetch_stock_data(ticker.upper())

ticker = "AAPL"
stocks = ['MSFT', 'AAPL', 'NVDA', 'AMZN', 'GOOGL', 'META', 'TSLA', 'LLY', 'V', 'AVGO']

my_columns = [
    "companyName", 
    "symbol", 
    "latestPrice", 
    "latestVolume", 
    "marketCap", 
    "peRatio", 
    "week52High", 
    "week52Low", 
    "change", 
    "changePercent", 
    "open", 
    "high", 
    "low", 
    "close", 
    "volume", 
    "ytdChange"
]


#fetch_stock_data(ticker)
final_dataframe = pd.DataFrame(columns=my_columns)

for stock in stocks:
    fetch_stock_data(stock)
    
    new_data = pd.Series([
        dictionary.get('companyName'), 
        dictionary.get('symbol'), 
        dictionary.get('latestPrice'), 
        dictionary.get('latestVolume'), 
        dictionary.get('marketCap'), 
        dictionary.get('peRatio'), 
        dictionary.get('week52High'), 
        dictionary.get('week52Low'), 
        dictionary.get('change'), 
        dictionary.get('changePercent'), 
        dictionary.get('open'), 
        dictionary.get('high'), 
        dictionary.get('low'), 
        dictionary.get('close'), 
        dictionary.get('volume'), 
        dictionary.get('ytdChange')
    ], index=my_columns)
    
    final_dataframe = pd.concat([final_dataframe, new_data.to_frame().T], ignore_index=True)
    
print(final_dataframe)