import requests
import json
import matplotlib.pyplot as plt

cumulative_tested = []
daily_tested = []
Seven_DMA = []

url = 'https://api.covid19india.org/data.json'
response = requests.get(url)

data = json.loads(response.text)
testing_data = data.get('tested')

for item in testing_data:
	cumulative_tested.append(item.get('testspermillion').strip())

#Removing empty strings
cumulative_tested = list(filter(None, cumulative_tested))

index = 0
while index <= len(cumulative_tested)-2:
	daily_tested.append(int(cumulative_tested[index+1])-int(cumulative_tested[index]))
	index = index+1

focus = daily_tested

#7 day moving average calculation

end = len(focus)-1
begin = end-7
while begin >= 0:
	sliced = focus[begin:end]
	end = end-1
	begin = end-7
	Seven_DMA.append(int(sum(sliced)/7))

Seven_DMA.reverse()
print(Seven_DMA)

plt.plot(list(range(7,len(Seven_DMA)+7)), Seven_DMA, color = 'r', label = 'Seven Day Moving Average', linewidth = 5)
plt.bar(list(range(0,len(focus))), focus, color = 'r', alpha = 0.2, label = 'Incremental Tested Per Million')
plt.title('Incremental Samples Tested Per Million')
plt.xlabel('Days')
plt.legend(loc="upper left")
plt.show()	