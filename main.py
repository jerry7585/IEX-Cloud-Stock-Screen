import numpy as np #numerical computing in python, based in c++ so it is faster
import pandas as pd #data science library for data manipulation and analysis
import math #python mathematical functions
import tkinter as tk #python simple gui

from tkinter import simpledialog, Tk, Label
from flask import Flask
from PIL import Image, ImageTk, ImageSequence
from my_secrets import IEX_CLOUD_API_TOKEN #API Token is in a secrets.py file
from api_methods import fetch_stock_data #method from other file to perform GET request

#method to get the ticker from user input, simple gui
def get_ticker():
    ticker = simpledialog.askstring("Input", "Enter the stock ticker:")
    
    if ticker:
        fetch_stock_data(ticker.upper())

ticker = "AAPL"

fetch_stock_data(ticker)
