#==============for loop review===============
#Loop over list of lists example 
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
#Write a for loop that goes through each sublist of house and prints out the x is y sqm,
#where x is the name of the room and y is the area of the room.

# Build a for loop from scratch
for h in house:
    name_of_room = h[0]
    name_of_area = h[1]
    print("the " + name_of_room + " is " + str(name_of_area) + " in sqm")

#=============WHILE LOOP REVIEW=============
# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0:
      offset = offset-1
    else : 
      offset = offset+1     
    print(offset)

#=========== loops for Dictionary and NumPy array ====
# Dictionary
# for key, val in my_dict.items() :
# NumPy array
# for val in np.nditer(my_array):

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for key, value in europe.items() :
    print ("the capital of " + key + " is " + value) 

#===== Loop over NumPy array==========
# Import numpy as np
import numpy as np

# For loop over np_height
# for x in np_height :
#     print(str(x) + " inches")

# # For loop over np_baseball
# for x in np.nditer(np_baseball) :  # 2D array
#     print(x)

#===== Loop over DataFrame ======
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for lab, row in cars.iterrows() :
    print (lab)
    print (row)

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Adapt for loop
for lab, row in cars.iterrows() :
    print(lab + ": " + str(row['cars_per_cap']))

#==============================
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows():
    cars.loc[lab, "COUNTRY"] = row["country"].upper()
# Print cars
print(cars)

#==============================
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Use .apply(str.upper)
for lab, row in cars.iterrows() :
    cars.loc[lab, "COUNTRY"] = row["country"].upper()

cars["COUNTRY"] = cars["country"].apply(str.upper)
print(cars)
