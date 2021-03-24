import requests as rq
from bs4 import BeautifulSoup
import pandas as pd
import re


source = rq.get("https://forecast.weather.gov/MapClick.php?lat=37.777120000000025&lon=-122.41963999999996#.YFspOK_0nIU").text

soup = BeautifulSoup(source, 'lxml')


article = soup.find(id="detailed-forecast-body")
article2 = soup.find(id='seven-day-forecast-list')
weather_week = []
days = []
temps = []

for item in article.find_all(class_='row row-odd row-forecast'):
    days.append(item.div.b.text)
    weather_week.append(item.text)

for temp in article2.find_all(class_='temp temp-high'):
    temps.append(temp.text)

weather_df = pd.DataFrame(weather_week, index=[days])
weather_df.rename(columns={0: 'WeatherDescription'}, inplace=True)
print(weather_df)
weather_df.to_csv('Weather_in_SF.csv', mode='a')



