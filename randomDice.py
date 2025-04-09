# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(123)

# Generate and print random float
r = np.random.rand()
print(r)

#======dice roll======#
# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1,7) 

# if dice is 1 or 2, go one step down
# if dice is 3, 4 or 5, go one step up
# else, throw the dice again, the number of dice is the number of steps you go up. 
if dice <= 2 :
    step = step - 1
elif dice <=5 :
    step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)

