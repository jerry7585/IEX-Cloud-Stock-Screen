import requests #a popular http library for making http requests, typically through an api, very slow if we can use batch calls it is better
import xlsxwriter #creating and manipulating excel files in python

from my_secrets import IEX_CLOUD_API_TOKEN

#base URL for the IEX Cloud API, global variable, never changes
base_url = 'https://api.iex.cloud/v1/data/core/quote'

#sandbox api for free
sandbox_base_url = 'https://sandbox.iexapis.com/stable/stock'

key_parameters = {
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
}

dictionary = {}

def fetch_stock_data(ticker):
    
    #endpoint to retrieve the data using the API
    endpoint = f'{base_url}/{ticker}?token={IEX_CLOUD_API_TOKEN}'

    #sandbox endpoint
    sandbox_endpoint = f'{sandbox_base_url}/{ticker}/quote?token={IEX_CLOUD_API_TOKEN}' 

    #send a GET request to the API endpoint
    response = requests.get(endpoint)

    #Check if successful, code is 200 when success
    if response.status_code == 200:
                
        # Extract the stock quote data from the response JSON
        data = response.json()[0]

        #parse it into a dictionary
        for k,v in data.items():
            dictionary[k] = v
             
    else:
        #Print an error message
        print(f"Failed to fetch stock quote for {ticker}. Status code: ", response.status_code)