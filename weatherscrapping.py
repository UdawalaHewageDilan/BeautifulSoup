import requests as rq
from bs4 import BeautifulSoup
import pandas as pd


source = rq.get("https://forecast.weather.gov/MapClick.php?lat=37.777120000000025&lon=-122.41963999999996#.YFspOK_0nIU").text

soup = BeautifulSoup(source, 'lxml')
#print(soup.prettify())

today = soup.find()
print(today)



