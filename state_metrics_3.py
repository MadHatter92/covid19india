import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker

df = pd.read_csv('../covid19india_data_parser/Kerala_fatalities_Jan_Sep13.csv')
data = df['Age'].tolist()

cases_under_45 = df.loc[df['Age'] <= 45]
cases_45_to_60 = df.loc[(df['Age'] > 45) & (df['Age'] <= 60)]
cases_over_60 = df.loc[df['Age'] > 60]

bins = np.arange(-100, 100, 5) # fixed bin size

fig, ax = plt.subplots()
plt.xlim([0, max(data)+5])
ax.hist(data, bins=bins, color = "red", ec="red", alpha=0.2)

start, end = ax.get_xlim()
ax.xaxis.set_ticks(np.arange(start, end, 5))

plt.xlabel('Age')
plt.ylabel('Deceased Cases')
plt.title("Age Distribution of COVID-19 Deaths in Odisha")
plt.annotate('Under 45 years: '+str(len(cases_under_45))+' cases, '+"{:.0%}".format(len(cases_under_45)/len(data))+' of total', xy = (10,10))
plt.annotate('45 to 60 years: '+str(len(cases_45_to_60))+' cases, '+"{:.0%}".format(len(cases_45_to_60)/len(data))+' of total', xy = (35,70))
plt.annotate('Over 60 years: '+str(len(cases_over_60))+' cases, '+"{:.0%}".format(len(cases_over_60)/len(data))+' of total', xy = (80,60))

plt.show()