import requests
import json
import matplotlib.pyplot as plt

dates = []
totalconfirmed = []
dailydeceased = []
dailyrecovered = []
Seven_DMA = []

url = 'https://api.covid19india.org/data.json'
response = requests.get(url)

data = json.loads(response.text)
cases_time_series = data.get('cases_time_series')

for item in cases_time_series:
	dates.append(item.get('date'))
	totalconfirmed.append(int(item.get('totalconfirmed')))
	dailyrecovered.append(int(item.get('totalrecovered')))
	dailydeceased.append(int(item.get('totaldeceased')))

focus = [(confirmed - recovered - deceased) for confirmed, recovered, deceased in zip(totalconfirmed, dailyrecovered, dailydeceased)]
focus = [focus[i+1] - focus[i] for i in list(range(len(focus)-1))]

print(focus)

#7 day moving average calculation

end = len(focus)-1
begin = end-7
while begin >= 0:
	sliced = focus[begin:end]
	end = end-1
	begin = end-7
	Seven_DMA.append(int(sum(sliced)/7))

Seven_DMA.reverse()

plt.bar(list(range(0,len(focus))), focus, color = 'r', alpha = 0.2, label = 'Daily Active Cases')
plt.plot(list(range(7,len(Seven_DMA)+7)), Seven_DMA, color = 'r', label = 'Seven Day Moving Average', linewidth = 5)
plt.title('Daily Increase in Active Cases')
plt.legend(loc="upper left")
plt.xlabel('Days')
plt.show()