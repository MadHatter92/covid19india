import requests
import json
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

data_list = []
active_list = []
date_list = []
annotation_list = []
color_list = []

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

url = 'https://api.covid19india.org/data.json'
response = requests.get(url)

data = json.loads(response.text)

data_list = data['cases_time_series']

for item in data_list:
    active_cases = int(item['totalconfirmed']) - int(item['totalrecovered']) - int(item['totaldeceased'])
    active_list.append(active_cases)
    date = item['date']
    date_list.append(date)
    if date == '25 March ':
        annotation_list.append('Lockdown 1 \n 25 March')
        color_list.append('red')
        current = active_cases
    elif date == '15 April ':
        percentage_change = "{:.0%}".format(active_cases/current - 1)
        annotation_list.append('Lockdown 2 \n 15 April \n Cases up by: '+percentage_change)
        print(current, active_cases)
        current = active_cases
        color_list.append('red')
    elif date == '04 May ':
        percentage_change = "{:.0%}".format(active_cases/current - 1)
        annotation_list.append('Lockdown 3 \n 04 May \n Cases up by: '+percentage_change)
        current = active_cases
        color_list.append('red')
    elif date == '18 May ':
        percentage_change = "{:.0%}".format(active_cases/current - 1)
        annotation_list.append('Lockdown 4 \n 18 May \n Cases up by: '+percentage_change)
        current = active_cases
        color_list.append('red')
    elif date == '01 June ':
        percentage_change = "{:.0%}".format(active_cases/current - 1)
        annotation_list.append('Unlock 1.0 \n 01 June \n Cases up by: '+percentage_change)
        current = active_cases
        color_list.append('black')
    elif date == '01 July ':
        percentage_change = "{:.0%}".format(active_cases/current - 1)
        annotation_list.append('Unlock 2.0 \n 01 July \n Cases up by: '+percentage_change)
        current = active_cases
        color_list.append('black')
    elif date == '01 August ':
        percentage_change = "{:.0%}".format(active_cases/current - 1)
        annotation_list.append('Unlock 3.0 \n 01 August \n Cases up by: '+percentage_change)
        current = active_cases
        color_list.append('black')
    elif date == '28 August ':
        percentage_change = "{:.0%}".format(active_cases/current - 1)
        annotation_list.append('Latest \n 28 August \n Cases up by: '+percentage_change)
        current = active_cases
        color_list.append('black')
    else:
        annotation_list.append('')
        color_list.append('')

x_axis = list(range(0, len(active_list)))

ax1.bar(x_axis[50:], active_list[50:], color='red', alpha=0.4)

plt.title('Number of Active Cases on the Day (Current: '+f'{active_list[-1]:,}'+')')

plt.ylabel('Active cases')
plt.xlabel('Days')

ax1.get_xaxis().set_major_formatter(
    mtick.FuncFormatter(lambda x, p: format(int(x), ',')))
ax1.get_yaxis().set_major_formatter(
    mtick.FuncFormatter(lambda x, p: format(int(x), ',')))

loc = mtick.MultipleLocator(base=20)
ax1.xaxis.set_major_locator(loc)

# print (date_list)

for item in active_list:
    annotation = annotation_list[active_list.index(item)]
    color = color_list[active_list.index(item)]
    ax1.annotate(annotation, (active_list.index(item), item+50000), ha='right', va='top',fontsize=9, color=color, bbox=dict(facecolor='grey', alpha=0.2, edgecolor='none', boxstyle='round,pad=0.2'))

plt.show()
