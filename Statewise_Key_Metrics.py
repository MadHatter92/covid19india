import requests
import json
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from datetime import date

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
x,y,z,s = [], [], [], []

state_list = ['AP', 'AS', 'BR', 'CH', 'CT', 'DL', 'GJ', 'HP', 'HR', 'JH', 'JK', 'KA', 'KL', 'MP', 'OR', 'PB', 'RJ', 'TG', 'TN', 'UP', 'UT', 'WB']

url = 'https://api.covid19india.org/v3/timeseries.json'
response = requests.get(url)
data = json.loads(response.text)

for state in state_list:
	state_data = data.get(state)
	latest = state_data.get(list(state_data)[-1])
	x.append(latest.get('total').get('tested'))
	z.append(latest.get('total').get('deceased')/latest.get('total').get('confirmed'))
	y.append(latest.get('total').get('confirmed'))

ax1.scatter(x,y,s = [100000*x for x in z], c=z, cmap="Reds", alpha=0.6, edgecolors="maroon", linewidth=2)

for x_coord,y_coord, z_coord, state_name in zip(x,y,z,state_list):
	plt.annotate(state_name + " " + "{:.1%}".format(z_coord), xy = (x_coord, y_coord), horizontalalignment='center', verticalalignment='center')

ax1.get_xaxis().set_major_formatter(
    mtick.FuncFormatter(lambda x, p: format(int(x), ',')))
ax1.get_yaxis().set_major_formatter(
    mtick.FuncFormatter(lambda x, p: format(int(x), ',')))

plt.xlabel('Total cases tested', fontweight = 'bold')
plt.ylabel('Total confirmed cases', fontweight = 'bold')
plt.title('Statewise metrics (exc. Maharashtra): '+str(date.today()), fontweight = 'bold')
plt.figtext(0.53, .12, "Percentage figures inside the circles denote mortality, depicted by the size of the circle", style = 'italic', fontweight = 'bold')

plt.show()