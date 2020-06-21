import requests
import json
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

# Possible metrics: 'confirmed', 'deceased', 'recovered', 'tested'
metric = 'recovered'

state_list = ['MH', 'DL', 'GJ', 'UP', 'TN']

url = 'https://api.covid19india.org/v3/timeseries.json'
response = requests.get(url)
data = json.loads(response.text)

for state in state_list:
	data_series = []
	Seven_DMA = []
	cumulative_confirmed_list = []
	daily_deceased_list = []
	state_data = data.get(state)
	for key in state_data.keys():
		try:
			cumulative_confirmed = state_data[key].get('total').get('confirmed')
			daily_deceased = state_data[key].get('total').get('deceased')
		except:
			pass
		cumulative_confirmed_list.append(cumulative_confirmed)
		daily_deceased_list.append(daily_deceased)
	for (conf, dece) in zip(cumulative_confirmed_list, daily_deceased_list):
		try:
			data_series.append(dece/conf)
		except:
			pass	
	# try:
	# 	data_series.remove(1409) #Removes outlier deaths from Maharashtra
	# except:
	# 	pass

	focus = data_series

	#7 day moving average calculation

	# end = len(focus)-1
	# begin = end-7
	# while begin >= 0:
	# 	sliced = focus[begin:end]
	# 	end = end-1
	# 	begin = end-7
	# 	Seven_DMA.append(int(sum(sliced)/7))

	# Seven_DMA.reverse()
	ax1.plot(list(range(0,len(focus))), focus, label = state, linewidth = 3)

plt.xlabel('Days Since First Death Recorded')
ax1.legend(loc="upper left")
plt.title('Statewise mortality data (Cumulative deaths divided by cumulative confirmed cases )')
ax1.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))
plt.show()