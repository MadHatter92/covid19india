import requests
import json
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from datetime import date
from matplotlib import style
import time
import matplotlib.animation as animation
matplotlib.use("Agg")

number_of_days = 31
global day
day =  -number_of_days

fig = plt.figure(figsize=(16, 8), dpi=120)
ax1 = fig.add_subplot(1,1,1)

state_list = ['AP', 'AS', 'BR', 'CT', 'DL', 'GJ', 'HP', 'HR', 'JH', 'JK', 'KA', 'KL', 'MP', 'OR', 'PB', 'RJ', 'TG', 'TN', 'UP', 'UT', 'WB', 'MH']
state_pop = [49577103, 31205576, 104099452, 25545198, 16787941, 60439692, 6864602, 25351462, 32988134, 12267032, 61095297, 33406061, 72626809, 41974219, 27743338, 68548437, 35003674, 72147030, 199812341, 10086292, 91276115, 112374333]

url = 'https://api.covid19india.org/v3/timeseries.json'
response = requests.get(url)
data = json.loads(response.text)

def animate(i):
	global day
	if day <= -1:
		x,y,z,s, color = [], [], [], [], []
		ax1.clear()	
		for state, pop in zip(state_list, state_pop):
			state_data = data.get(state)
			latest = state_data.get(list(state_data)[day])
			x.append(latest.get('total').get('confirmed')/latest.get('total').get('tested'))
			y.append(latest.get('total').get('deceased')/latest.get('total').get('confirmed'))
			z_value = latest.get('total').get('tested')/pop
			z.append(latest.get('total').get('tested')/pop)
			if z_value > 0.01:
				color.append('green')
			elif z_value>0.005:
				color.append('grey')
			else: color.append('red')

		ax1.scatter(x,y,s = [100000*x for x in z], c=color, alpha=0.6, edgecolors=color, linewidth=2)

		for x_coord,y_coord, z_coord, state_name in zip(x,y,z,state_list):
			plt.annotate(state_name + " " + "{:.1%}".format(z_coord), xy = (x_coord, y_coord), horizontalalignment='center', verticalalignment='center')

		plt.xlabel('Percentage confirmed out of total tested', fontweight = 'bold')
		plt.ylabel('Percentage deceased out of total confirmed', fontweight = 'bold')
		plt.title('COVID-19 statewise metrics ' + str(-day) + ' days ago', fontweight = 'bold')
		plt.figtext(0.38, .12, "Percentage figures inside the circles denote percentage of population that has been tested, shown by size of the circle", style = 'italic', fontweight = 'regular')

		axes = plt.gca()
		axes.set_xlim([0,0.18])
		axes.set_ylim([0,0.065])
		ax1.yaxis.set_major_formatter(mtick.PercentFormatter())
		ax1.xaxis.set_major_formatter(mtick.PercentFormatter())

	else:
		exit()

def daycalc(i):
	animate(i)
	global day
	day = day + 1

ani = animation.FuncAnimation(fig, daycalc, interval = 1000*0.5)
plt.show()

mywriter = animation.FFMpegWriter(fps=1, extra_args=['-vcodec', 'libx264'])
ani.save('myanimation.mp4',writer=mywriter)

