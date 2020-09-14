import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker

df = pd.read_csv('../covid19india_data_parser/karnataka_fatalities_details_jul16_sep10_2.csv')
data = df['Age'].tolist()

bins = np.arange(-100, 100, 5) # fixed bin size

fig, ax = plt.subplots()
plt.xlim([0, max(data)+5])
ax.hist(data, bins=bins, color = "red", ec="red", alpha=0.2)

start, end = ax.get_xlim()
ax.xaxis.set_ticks(np.arange(start, end, 5))

plt.xlabel('Age')
plt.ylabel('Deceased Cases')
plt.title("Age Distribution of COVID-19 Deaths in Karnataka")

plt.show()

# print(df)