import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker

df = pd.read_csv('../covid19india_data_parser/karnataka_fatalities_details_jul16_sep10_2.csv')
data = df['Age'].tolist()

female_cases = df.loc[df['Sex'].isin(['F'])]['Age'].tolist()
male_cases = df.loc[df['Sex'].isin(['M'])]['Age'].tolist()

bins = np.arange(-100, 100, 5) # fixed bin size

fig=plt.figure()

ax1=fig.add_subplot(311)
ax2=fig.add_subplot(312)
ax3=fig.add_subplot(313)

# plt.xlim([0, max(data)+5])

ax1.hist(data, bins=bins, color = "red", ec="red", alpha=0.2)
ax2.hist(male_cases, bins=bins, color = "red", ec="red", alpha=0.2)
ax3.hist(female_cases, bins=bins, color = "red", ec="red", alpha=0.2)

ax1.xaxis.set_ticks(np.arange(0, 100, 5))
ax2.xaxis.set_ticks(np.arange(0, 100, 5))
ax3.xaxis.set_ticks(np.arange(0, 100, 5))


plt.xlabel('Age')
plt.ylabel('Deceased Cases')
plt.title("Age Distribution of COVID-19 Deaths in Karnataka")

plt.show()

print(len(data))