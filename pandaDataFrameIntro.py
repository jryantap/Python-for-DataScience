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

