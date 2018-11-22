#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests, json

months = {'01':'January','02':'February', '03':'March','04':'April',
			'05':'May','06':'June','07':'July','08':'August','09':'September',
			'10':'October','11':'November','12':'December'}

years = list(range(2011,2019))


for year in years:
	for month in months:
		print(month)
		url = "https://api-ak.wunderground.com/api/d8585d80376a429e/"
		url += "history_" + str(year) + month + "01" + str(year) + month + "31/lang:EN/units:english/"
		url += "bestfct:1/v:2.0/q/KBTR.json"
		try:
			page = requests.get(url)
			data = page.json()
			print("For " + str(months[month]) + "/" + str(year))
			for day in data['history']['days']:
				weather = []
				weather.append(str(day['summary']['date']['year'])  
								+ '-' + str(day['summary']['date']['month']).zfill(2)
								+ '-' + str(day['summary']['date']['day']).zfill(2))
				weather.append(str(day['summary']['min_temperature']))
				weather.append(str(day['summary']['max_temperature']))
				weather.append(str(day['summary']['temperature']))
				weather.append(str(day['summary']['min_dewpoint']))
				weather.append(str(day['summary']['max_dewpoint']))
				weather.append(str(day['summary']['dewpoint']))
				weather.append(str(day['summary']['min_humidity']))
				weather.append(str(day['summary']['max_humidity']))
				weather.append(str(day['summary']['min_pressure']))
				weather.append(str(day['summary']['max_pressure']))
				weather.append(str(day['summary']['pressure']))
				weather.append(str(day['summary']['min_visibility']))
				weather.append(str(day['summary']['max_visibility']))
				weather.append(str(day['summary']['visibility']))
				weather.append(str(day['summary']['min_wind_speed']))
				weather.append(str(day['summary']['max_wind_speed']))
				weather.append(str(day['summary']['wind_speed']))
				weather.append(str(day['summary']['fog']))
				weather.append(str(day['summary']['rain']))
				weather.append(str(day['summary']['thunder']))
				weather.append(str(day['summary']['precip']))

				# save the data
				row = ",".join(weather)
				with open("weather_data.csv", "a+") as f:
					f.write(row)
					f.write("\n")			
		except:
			print("error")
			pass
