#Assignment 8 - Data Visualization
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#Create the array/dataset
CityAH = ([33,37,44,56,67,75,79,78,71,60,50,38])
CityAL = ([19,22,28,38,47,57,62,60,53,42,35,24])
CA = ([33,37,44,56,67,75,79,78,71,60,50,38],
      [19,22,28,38,47,57,62,60,53,42,35,24])
#Create the line plots for city A's highs and lows
fig=plt.figure();ax=fig.add_subplot(1,1,1)
ax.plot(CityAH,'ro--', label='High')
ax.plot(CityAL,'bo--', label='Low')
ax.set_title('Annual Temperature Variation - City A')
plt.xlabel('Month')
plt.ylabel('Temp.')
plt.xticks(np.arange(12), (['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug',
           'Sep','Oct','Nov','Dec']),rotation=60)
plt.legend()
#Create bar plots for city A's highs and lows
fig, ax2=plt.subplots()
index=np.arange(12)
bar_width = 0.35
opacity = 0.8

r1=plt.bar(index,CityAH,bar_width,
           alpha=opacity,
           color='r',
           label='High')
r2=plt.bar(index+bar_width,CityAL,bar_width,
           alpha=opacity,
           color='b',
           label='Low')

plt.xlabel('Month')
plt.ylabel('Temp.')
plt.title('Annual Temperature Variation - City A')
plt.xticks(index + bar_width, (['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug',
           'Sep','Oct','Nov','Dec']),rotation=60)
plt.legend()
plt.tight_layout()
plt.show()

#Draw a scatter plot to show the correlation between the two cities’ monthly high temperatures and the correlation between their monthly low temperatures
CityBH = ([54,59,67,76,83,91,93,94,84,75,63,55])
CityBL = ([26,30,37,46,56,65,69,67,59,48,36,28])
plt.scatter(CityAH,CityBH, label='Highs', color='g', s=20, marker="o")
plt.scatter(CityAL,CityBL, label='Lows', color='c', s=20, marker="o")
plt.xlabel('City A High/Low')
plt.ylabel('City B High/Low')
plt.title('Correlation between City A and B High and Low Temps')
plt.legend()
plt.show()