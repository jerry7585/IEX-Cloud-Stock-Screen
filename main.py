import numpy as np #numerical computing in python, based in c++ so it is faster
import pandas as pd #data science library for data manipulation and analysis
import requests #a popular http library for making http requests, typically through an api, very slow if we can use batch calls it is beter
import xlsxwriter #creating and manipulating excel files in python
import math #python mathematical functions

from my_secrets import IEX_CLOUD_API_TOKEN
#API Token is in a secrets.py file

print(IEX_CLOUD_API_TOKEN)