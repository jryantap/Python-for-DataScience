import numpy as np

np.random.seed(123)
#set the list
tails = [0]

for x in range(10) : # do it 10 times
    coin = np.random.randint(0,2) # head or tails
    tails.append(tails[x] + coin) #set the element and show if it's head or tails

print(tails)

