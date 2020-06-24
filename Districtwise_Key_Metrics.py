import requests
import json
import matplotlib.pyplot as plt
import random

data_list = []
district_list = []
active_list = []
deceased_list = []
top_districts = []

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

url = 'https://api.covid19india.org/state_district_wise.json'
response = requests.get(url)

data = json.loads(response.text)

for key in data.keys():
	data_list.append(data[key])

for item in data_list:
	district_data = [item.get('districtData') for item in data_list]

for data_dict in district_data:
	for key, value in data_dict.items():
		district_list.append(key)
		active_list.append(value.get('active'))
		deceased_list.append(value.get('deceased'))

data_dict_list = [{'district': district_name, 'active': active_cases, 'deceased': deceased_cases} for district_name, active_cases, deceased_cases in zip(district_list, active_list, deceased_list)]

for item in data_dict_list:
	if item.get('district') not in ['Unassigned', 'Unknown']:
		if item.get('active') > 500:
			top_districts.append(item)

	else:
		pass

ax1.scatter([item.get('active') for item in top_districts],[item.get('deceased') for item in top_districts], s = 50, alpha = 0.6, edgecolors="black", linewidth=1)
for x_coord,y_coord, district_name in zip([item.get('active') for item in top_districts],[item.get('deceased') for item in top_districts], [item.get('district') for item in top_districts]):
	plt.annotate(district_name, xy = (x_coord, y_coord+10), horizontalalignment='center', verticalalignment='top')	

plt.title('District wise active cases and deaths')

plt.xlabel('Active cases')
plt.ylabel('Deaths')

plt.show()
