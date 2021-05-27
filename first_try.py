import numpy as np
import pprint as pp
import random

def generateLab(size):
    a = [[0 for i in range(size)]for x in range(size)]

    for i in range(size):
        for x in range(size):
            if i < size-1 and x<size-1:
                if a[i-1][x-1]==1 and a[i+1][x+1]==1:
                    a[i][x]=0
            else:
                a[i][x] = random.randint(0, 1)
    return a

pp.pprint(generateLab(5))
