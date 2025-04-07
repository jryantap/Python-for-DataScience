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
