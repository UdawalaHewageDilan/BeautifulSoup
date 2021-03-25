import requests as rq
from bs4 import BeautifulSoup
import pandas as pd
import re
import datetime as dt


source = rq.get("https://forecast.weather.gov/MapClick.php?lat=37.777120000000025&lon=-122.41963999999996#.YFspOK_0nIU").text

soup = BeautifulSoup(source, 'lxml')


article = soup.find(id="detailed-forecast-body")
article2 = soup.find(id='seven-day-forecast-list')
weather_week = []
days = []
temps = []

# for item in article.find_all(class_='row row-odd row-forecast'):
#     days.append(item.div.b.text)
#     weather_week.append(item.text)

#for temp in \
print(article2)

forecast = article2.find(class_='tombstone-container')[4]
print(forecast)
# for period in article2.find_all(class_='period-name'):
#     print(period.text)
    # temperature = temp.split[4]
    # print(temperature)
    #temps.append(temp)


# for i in range(0, len(temps), 2):
#     if temps[i] != temps[-1]:
#         days.append(temps[i] + temps[i+1])
#     else:
#         days.append(temps[-1])
#
# print(days)
# week_dict = {}
# for day in days:
#     print(day)

    #week_dict[]

# fahrenheit to celsius
# lambda x : (x-32)*5/9

# pattern_temps = re.compile(r'(High|Low)\W\s\d+\s\S[F]')
# for day in days:
#     print(pattern_temps.findall(day))

# weather_df = pd.DataFrame(weather_week, index=[days])
# weather_df.rename(columns={0: 'WeatherDescription'}, inplace=True)
# print(weather_df)
# weather_df.to_csv('Weather_in_SF.csv', mode='a')



