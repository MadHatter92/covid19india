import requests
import json
import matplotlib.pyplot as plt

dates = []
dailyconfirmed = []
dailydeceased = []
dailyrecovered = []
Seven_DMA = []

url = 'https://api.covid19india.org/data.json'
response = requests.get(url)

data = json.loads(response.text)
cases_time_series = data.get('cases_time_series')

for item in cases_time_series:
	dates.append(item.get('date'))
	dailyconfirmed.append(int(item.get('dailyconfirmed')))
	dailyrecovered.append(int(item.get('dailyrecovered')))
	dailydeceased.append(int(item.get('dailydeceased')))

focus = dailydeceased

# Removing the outlier

focus.remove(2004)

#7 day moving average calculation

end = len(focus)-1
begin = end-7
while begin >= 0:
	sliced = focus[begin:end]
	end = end-1
	begin = end-7
	Seven_DMA.append(int(sum(sliced)/7))

Seven_DMA.reverse()

plt.bar(list(range(0,len(focus))), focus, color = 'r', alpha = 0.2, label = 'Daily Deceased')
plt.plot(list(range(7,len(Seven_DMA)+7)), Seven_DMA, color = 'r', label = 'Seven Day Moving Average', linewidth = 5)
plt.figtext(0.13, .8, "Note: Outlier count of 2004 deceased on 17 June 2020 has been removed from the data")
plt.title('Daily Deceased')
plt.legend(loc="upper left")
plt.xlabel('Days')
plt.show()