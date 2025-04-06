import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#load the data 
#from io import StringIO
#data_str = 

# read
data = pd.read_csv("population_data.csv")

# Map continents to colors
continent_colors = {
    'Asia': 'red',
    'Europe': 'green',
    'Africa': 'blue',
    'Americas': 'yellow',
    'Oceania': 'cyan'
}

gdp_cap = data['gdp_cap']
life_exp = data['life_exp']
pop = data['population']
col = data['cont'].map(continent_colors)

# Scatter plot the "/200000" is to make the bubble smaller for China and India since they bigger numbers
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) / 200000, c = col, alpha = 0.8)


# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Additional customizations
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

# Add axis limits to fix display
plt.xlim(200, 100000)
plt.ylim(30, 90)

# Add country labels at actual coordinates
india = data[data['country'] == 'India']
china = data[data['country'] == 'China']
plt.text(india['gdp_cap'].values[0], india['life_exp'].values[0], 'India')
plt.text(china['gdp_cap'].values[0], china['life_exp'].values[0], 'China')

# Add grid() call
plt.grid(True)


# Show the plot
plt.show()