import requests
import json
import matplotlib.pyplot as plt

cumulative_tested_per_million = []
Seven_DMA = []
focus = []

url = 'https://api.covid19india.org/data.json'
response = requests.get(url)

data = json.loads(response.text)
testing_data = data.get('tested')

for item in testing_data:
	cumulative_tested_per_million.append(item.get('testspermillion').strip())

#Removing empty strings
cumulative_tested_per_million = list(filter(None, cumulative_tested_per_million))

for item in cumulative_tested_per_million:
	focus.append(int(item)) 

#7 day moving average calculation

end = len(focus)-1
begin = end-7
while begin >= 0:
	sliced = focus[begin:end]
	end = end-1
	begin = end-7
	Seven_DMA.append(int(sum(sliced)/7))

Seven_DMA.reverse()

plt.bar(list(range(0,len(focus))), focus, color = 'r', alpha = 0.2, label = 'Cumulative Tested Per Million')
plt.plot(list(range(7,len(Seven_DMA)+7)), Seven_DMA, color = 'r', label = 'Seven Day Moving Average', linewidth = 5)
plt.title('Cumulative Tests Per Million')
plt.xlabel('Days')
plt.legend(loc="upper left")
plt.show()