# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {"country": names, "drives_right": dr, "cars_per_cap": cpc}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars, just row labels as index for now to make sure parse is ok. 
print(cars) 

# Specify the row labels this time
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RUS', 'MOR', 'EG']
cars.index = row_labels

# Printer cars again, this time with the row labels
print (cars)

# OR do the following
# import pandas as pd
# Import the cars.csv data: cars
# cars = pd.read_csv("cars.csv")
# # Print out cars
# print (cars)

##### loc and iloc ####
##### I mostly used loc ####

import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
print(cars)

# Print out drives_right column as Series ##
print(cars.loc[:, 'drives_right'])
# Print out drives_right column as DataFrame
print(cars.loc[:, 'drives_right'])

# Print out cars_per_cap and drives_right as DataFrame ##
print(cars.loc[:, ['cars_per_cap','drives_right']])