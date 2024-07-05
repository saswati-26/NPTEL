'''
in a file there is a set of 10000 bits numbers in the form of 0's and 1's. your task is to change the o's to 1's for a randomly generated value that is 1
'''

import random

def evolve(x):
    ind = random.randint(0, len(x)-1)
    p = random.randint(1,100)
    if (p == 1):
        if (x[ind] == '0'):
            x[ind] = 1
        else:
            x[ind] = '0'

with open("file27.txt" , 'r+') as myfile:
    x = myfile.read()
    x = list(x)
for i in range (0, 10000):
    evolve(x)
print(x)
myfile.close()