import requests
import json
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib import style
import pandas as pd
from matplotlib import style

style.use('seaborn-whitegrid')

fig = plt.figure(figsize=(16, 8), dpi=120)
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
	latest = state_data.get(list(state_data)[-50])
	confirmed_1.append(latest.get('total').get('confirmed')/latest.get('total').get('tested'))
	deceased_1.append(latest.get('total').get('deceased')/latest.get('total').get('confirmed'))
	tested_1.append(latest.get('total').get('tested')/pop)

df = pd.DataFrame(({'State':state_list, 'Beginning': deceased_1, 'End': deceased_2}))
ordered_df = df.sort_values(by = 'End')

my_range=range(1,len(df.index)+1)

print(ordered_df)

plt.hlines(y = my_range, xmin=ordered_df['Beginning'], xmax = ordered_df['End'], color = 'maroon', alpha = 0.4)
plt.scatter(ordered_df['Beginning'], my_range, color = 'red', alpha = 0.3, label = '50 Days Ago')
plt.scatter(ordered_df['End'], my_range, color = 'red', alpha = 1, label = 'Today')
plt.legend(loc='lower right', frameon=True)

plt.yticks(my_range, ordered_df['State'])

# for x_coord,y_coord, z_coord, state_name in zip(x,y,z,state_list):
# 	plt.annotate(state_name + " " + "{:.1%}".format(z_coord), xy = (x_coord, y_coord), horizontalalignment='center', verticalalignment='center')

plt.xlabel('Percentage tested out of total population')
plt.title('COVID-19 Statewise Progress: Test Penetration')

for y, Beginning, End in zip(my_range, ordered_df['Beginning'], ordered_df['End']):
	plt.annotate("{:.1%}".format(Beginning), (Beginning, y), ha='left',size=8, color = 'grey')
	plt.annotate("{:.1%}".format(End), (End, y), ha='right',size=9,)

ax1.xaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))

plt.show()