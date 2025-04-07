#Filtering pandas DataFrames
import pandas as pd 
import numpy as np
from io import StringIO

brics = pd.read_csv("brics.csv", index_col=0)
#to make sure it prints correctly
print(brics)

###We want the country with over 8 million km^2 ###

# 1. select the area column
brics["area"]
#or 
#brics.loc[:, "area"]
#or
#brics.iloc[:, 2]

# 2. compare the area column
is_huge = brics["area"] > 8 

# 3. Use the result to select the countries
print(brics[is_huge])

# 4. do it in one line, check the column "area"
print(brics[brics.loc[:, "area"]>8])

###================================
# Import cars data
import pandas as pd
import numpy as np

cars = pd.read_csv('cars.csv', index_col = 0)
# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars["cars_per_cap"]

many_cars = cpc > 500
car_maniac = cars[many_cars]

# Print car_maniac
print(car_maniac)

#one line
print(cars[cars["cars_per_cap"] > 500])  #same output.
#OR
print(cars[cars.loc[ :, "cars_per_cap"] > 500])