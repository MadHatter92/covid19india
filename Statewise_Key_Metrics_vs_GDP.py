import requests
import json
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from datetime import date
from matplotlib import style


fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

x,y,z,s, color = [], [], [], [], []

state_list = ['AP', 'AS', 'BR', 'CT', 'DL', 'GJ', 'HP', 'HR', 'JH', 'JK', 'KA', 'KL', 'MP', 'OR', 'PB', 'RJ', 'TG', 'TN', 'UP', 'UT', 'WB', 'MH']
state_pop = [49577103, 31205576, 104099452, 25545198, 16787941, 60439692, 6864602, 25351462, 32988134, 12267032, 61095297, 33406061, 72626809, 41974219, 27743338, 68548437, 35003674, 72147030, 199812341, 10086292, 91276115, 112374333]
state_gdp_ppp_usd = [8261, 4485, 2395, 5294, 19974, 10789, 9792, 12904, 4154, 5021, 11524, 11153, 4973, 5200, 8470, 6044, 11174, 10587, 3635, 10860, 5983, 10477]

url = 'https://api.covid19india.org/v3/timeseries.json'
response = requests.get(url)
data = json.loads(response.text)

for state, pop, gdp in zip(state_list, state_pop, state_gdp_ppp_usd):
	state_data = data.get(state)
	latest = state_data.get(list(state_data)[-1])
	z.append(latest.get('total').get('deceased')/latest.get('total').get('confirmed'))
	y.append(gdp)
	x_value = latest.get('total').get('tested')/pop
	x.append(x_value)
	if x_value > 0.01:
		color.append('green')
	elif x_value>0.005:
		color.append('grey')
	else: color.append('red')

ax1.scatter(x,y,s = [50000*i for i in z], c=color, alpha=0.6, edgecolors=color, linewidth=2)

for x_coord,y_coord, state_name in zip(x,y,state_list):
	plt.annotate(state_name, xy = (x_coord, y_coord), horizontalalignment='center', verticalalignment='center')


# ax1.get_xaxis().set_major_formatter(
#     mtick.FuncFormatter(lambda x, p: format(int(x), ',')))
ax1.get_yaxis().set_major_formatter(
    mtick.FuncFormatter(lambda x, p: format(int(x), ',')))

plt.xlabel('Percentage of population tested', fontweight = 'bold')
plt.ylabel('State GDP in USD (PPP)', fontweight = 'bold')
plt.title('Statewise metrics vs state GDP: '+str(date.today()), fontweight = 'bold')
plt.figtext(0.55, 0.12, "Percentage figures inside the circles denote mortality, shown by size of the circle", style = 'italic', fontweight = 'bold')

axes = plt.gca()
axes.set_xlim([0,0.026])
ax1.xaxis.set_major_formatter(mtick.PercentFormatter(xmax = 1))

plt.show()