import requests as rq
from bs4 import BeautifulSoup
import csv

source = rq.get("https://forecast.weather.gov/MapClick.php?lat=37.777120000000025&lon=-122.41963999999996#.YFspOK_0nIU").text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('test.csv', 'w')
csv_wrtr = csv.writer(csv_file)
csv_wrtr.writerow(['Period', 'Temperature', 'Description'])

for temp in soup.find_all(class_='tombstone-container'):
    print(temp.text.split())
    period = temp.text.split()[0]
    desc = temp.text.split()[1]
    temperature_fahr = temp.text.split()[-2]
    print(temperature_fahr)
    temperature_cel = round(((float(temperature_fahr)-32)*(5/9)), 2)
    csv_wrtr.writerow([period, temperature_cel, desc])
#
csv_file.close()
