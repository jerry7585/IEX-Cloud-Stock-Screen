import requests #a popular http library for making http requests, typically through an api, very slow if we can use batch calls it is better
import xlsxwriter #creating and manipulating excel files in python
from my_secrets import IEX_CLOUD_API_TOKEN
#main method to call the API and perform a GET request

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

workbook = xlsxwriter.Workbook('stock_parameters.xlsx')

def fetch_stock_data(ticker):
    
    #endpoint to retrieve the data using the API
    endpoint = f'{base_url}/{ticker}?token={IEX_CLOUD_API_TOKEN}'

    #sandbox endpoint
    sandbox_endpoint = f'{sandbox_base_url}/{ticker}/quote?token={IEX_CLOUD_API_TOKEN}' 

    #send a GET request to the API endpoint
    response = requests.get(endpoint)

    #Check if successful, code is 200 when success
    if response.status_code == 200:
        worksheet = workbook.add_worksheet()
        worksheet.write('A1', 'Parameter')
        worksheet.write('B1', 'Value')
                
        # Extract the stock quote data from the response JSON
        stock_data = response.json()[0]

        # Print the stock quote data
        row = 1
        for k,v in stock_data.items():
            if k in key_parameters:
                worksheet.write(row,0,k)
                worksheet.write(row,1,v)
                row += 1
            
        workbook.close()
    else:
        #Print an error message
        print(f"Failed to fetch stock quote for {ticker}. Status code: ", response.status_code)