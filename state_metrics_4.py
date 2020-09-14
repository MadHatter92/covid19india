import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker

df = pd.read_csv('../covid19india_data_parser/karnataka_fatalities_details_jul16_sep10_2.csv')
data = df['Age'].tolist()

df_no_comorbidity = df.loc[df['Comorbidities'].isin(['NONE++++'])]

cases_under_45 = df_no_comorbidity.loc[df_no_comorbidity['Age'] <= 45]
cases_45_to_60 = df_no_comorbidity.loc[(df_no_comorbidity['Age'] > 45) & (df_no_comorbidity['Age'] <= 60)]
cases_over_60 = df_no_comorbidity.loc[df_no_comorbidity['Age'] > 60]

bins = np.arange(-100, 100, 5) # fixed bin size

fig, ax = plt.subplots()
plt.xlim([0, max(data)+5])
ax.hist(data, bins=bins, color = "green", ec="green", alpha=0.2)

start, end = ax.get_xlim()
ax.xaxis.set_ticks(np.arange(start, end, 5))

plt.xlabel('Age')
plt.ylabel('Deceased Cases')
plt.title("Age Distribution of COVID-19 Deaths in Karnataka - No Comorbidities")
plt.annotate('Under 45 years: '+str(len(cases_under_45))+' cases, '+"{:.0%}".format(len(cases_under_45)/len(df_no_comorbidity))+' of total', xy = (10,100))
plt.annotate('45 to 60 years: '+str(len(cases_45_to_60))+' cases, '+"{:.0%}".format(len(cases_45_to_60)/len(df_no_comorbidity))+' of total', xy = (35,700))
plt.annotate('Over 60 years: '+str(len(cases_over_60))+' cases, '+"{:.0%}".format(len(cases_over_60)/len(df_no_comorbidity))+' of total', xy = (80,600))

plt.show()