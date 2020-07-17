import requests
import json
import matplotlib.pyplot as plt
from matplotlib import rcParams
import matplotlib.ticker as mtick
import pandas as pd

plt.rcParams['font.family'] = 'SFNS Display'
# plt.rcParams['font.family'] = 'Roboto Slab'
# plt.rcParams['font.family'] = 'Noto Sans'

no_of_days = 30

fig = plt.figure(dpi=120)
ax1 = fig.add_subplot(1,1,1)

state_list = ['AP', 'AS', 'BR', 'CT', 'DL', 'GJ', 'HP', 'HR', 'JH', 'JK', 'KA', 'KL', 'MP', 'OR', 'PB', 'RJ', 'TG', 'TN', 'UP', 'UT', 'WB', 'MH']
state_pop = [49577103, 31205576, 104099452, 25545198, 16787941, 60439692, 6864602, 25351462, 32988134, 12267032, 61095297, 33406061, 72626809, 41974219, 27743338, 68548437, 35003674, 72147030, 199812341, 10086292, 91276115, 112374333]

url = 'https://api.covid19india.org/v3/timeseries.json'
response = requests.get(url)
data = json.loads(response.text)

confirmed_1, deceased_1, tested_1 = [], [], []
confirmed_2, deceased_2, tested_2 = [], [], []

for state, pop in zip(state_list, state_pop):
	state_data = data.get(state)
	latest = state_data.get(list(state_data)[-1])
	confirmed_2.append(latest.get('total').get('confirmed')/latest.get('total').get('tested'))
	deceased_2.append(latest.get('total').get('deceased')/latest.get('total').get('confirmed'))
	tested_2.append(latest.get('total').get('tested')/pop)

for state, pop in zip(state_list, state_pop):
	state_data = data.get(state)
	latest = state_data.get(list(state_data)[-no_of_days])
	confirmed_1.append(latest.get('total').get('confirmed')/latest.get('total').get('tested'))
	deceased_1.append(latest.get('total').get('deceased')/latest.get('total').get('confirmed'))
	tested_1.append(latest.get('total').get('tested')/pop)

color = ['green' if end-beginning <= 0.0 else 'red' for end, beginning in zip(tested_1, tested_2)]

df = pd.DataFrame(({'State':state_list, 'Beginning': tested_1, 'End': tested_2, 'Color':color}))
ordered_df = df.sort_values(by = 'End')

my_range=range(1,len(df.index)+1)

print(ordered_df)

plt.hlines(y = my_range, xmin=ordered_df['Beginning'], xmax = ordered_df['End'], color = ordered_df['Color'], alpha = 0.4)
plt.scatter(ordered_df['Beginning'], my_range, color = 'grey', alpha = 0.3, label = str(no_of_days)+' Days Ago')
plt.scatter(ordered_df['End'], my_range, color = ordered_df['Color'], alpha = 1, label = 'Today')
plt.legend(loc='lower right', frameon=True)

plt.yticks(my_range, ordered_df['State'], weight = 'bold')

# for x_coord,y_coord, z_coord, state_name in zip(x,y,z,state_list):
# 	plt.annotate(state_name + " " + "{:.1%}".format(z_coord), xy = (x_coord, y_coord), horizontalalignment='center', verticalalignment='center')

plt.xlabel('Percentage of population tested')
plt.title('COVID-19 Statewise Progress: Testing penetration')

for y, Beginning, End in zip(my_range, ordered_df['Beginning'], ordered_df['End']):
	plt.annotate("{:.1%}".format(Beginning), (Beginning, y), ha='right',size=8, color = 'grey')
	plt.annotate("{:.1%}".format(End), (End, y), ha='left',size=9, weight = 'bold')

ax1.xaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))
ax1.grid(which='major', alpha = 0.3, axis = 'y')

plt.figtext(0.98, 0.01, "Pranshumaan Singh \n github.com/MadHatter92", ha="right", fontsize=7)
plt.show()