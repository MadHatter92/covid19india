import requests
import json
import matplotlib.pyplot as plt

data_list = []
Seven_DMA = []
metric = 'deceased'
state = 'GJ'
focus = []

url = 'https://api.covid19india.org/v3/timeseries.json'
response = requests.get(url)

data = json.loads(response.text)
state_data = data.get(state)

for key in state_data.keys():
	data_list.append(state_data[key].get('delta'))

focus = [0 if item == None else item.get(metric) for item in data_list]
focus = [0 if item == None else item for item in focus]

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

plt.bar(list(range(0,len(focus))), focus, color = 'r', alpha = 0.2, label = 'Daily ' + metric)
plt.plot(list(range(7,len(Seven_DMA)+7)), Seven_DMA, color = 'r', label = 'Seven Day Moving Average', linewidth = 5)
plt.title('Daily ' + metric + ': ' + state)
plt.legend(loc="upper left")
plt.xlabel('Days')
plt.show()