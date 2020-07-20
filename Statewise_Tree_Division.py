import requests
import json
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import squarify
import matplotlib

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

x,y,z,s, color = [], [], [], [], []

state_list = ['AP', 'AS', 'BR', 'CT', 'DL', 'GJ', 'HP', 'HR', 'JH', 'JK', 'KA', 'KL', 'MP', 'OR', 'PB', 'RJ', 'TG', 'TN', 'UP', 'UT', 'WB', 'MH']
state_pop = [49577103, 31205576, 104099452, 25545198, 16787941, 60439692, 6864602, 25351462, 32988134, 12267032, 61095297, 33406061, 72626809, 41974219, 27743338, 68548437, 35003674, 72147030, 199812341, 10086292, 91276115, 112374333]
state_gdp_ppp_usd = [8261, 4485, 2395, 5294, 19974, 10789, 9792, 12904, 4154, 5021, 11524, 11153, 4973, 5200, 8470, 6044, 11174, 10587, 3635, 10860, 5983, 10477]

url = 'https://api.covid19india.org/v3/timeseries.json'
response = requests.get(url)
data = json.loads(response.text)

country_data = data.get('TT')
latest_country_data_point = country_data.get(list(country_data)[-1])
total_confirmed_cases = latest_country_data_point.get('total').get('confirmed')
total_deceased_cases = latest_country_data_point.get('total').get('deceased') 

for state, pop, gdp in zip(state_list, state_pop, state_gdp_ppp_usd):
	state_data = data.get(state)
	latest = state_data.get(list(state_data)[-1])
	y.append(latest.get('total').get('confirmed')/total_confirmed_cases)
	z.append(gdp)
	x_value = latest.get('total').get('deceased')/total_deceased_cases
	x.append(x_value)


squarify.plot(sizes=z, label=state_list, alpha=.7 )
plt.axis('off')
plt.show() 

# ax1.scatter(x,y,s = [x/10 for x in z], c=z, cmap="Reds", alpha=0.6, edgecolors="Black", linewidth=1)

# for x_coord,y_coord, state_name in zip(x,y,state_list):
# 	plt.annotate(state_name, xy = (x_coord, y_coord), horizontalalignment='center', verticalalignment='center')

# plt.xlabel('Share of deceased', fontweight = 'bold')
# plt.ylabel('Share of confirmed cases', fontweight = 'bold')
# plt.title('State share in confirmed cases vs share in deceased: '+str(date.today()), fontweight = 'bold')
# plt.figtext(0.7, 0.12, "Size of the circle indicates per capita GDP (PPP)", style = 'italic', fontweight = 'bold')

# axes = plt.gca()
# # axes.set_xlim([0,0.026])
# ax1.xaxis.set_major_formatter(mtick.PercentFormatter(xmax = 1))
# ax1.yaxis.set_major_formatter(mtick.PercentFormatter(xmax = 1))

plt.show()