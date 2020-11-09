import numpy as np
from math import *


def isConverged(a, b):
    netError = [False, False, False, False]
    for i in range(len(a)):
        if(abs((a[i] - b[i])) / a[i] < 1/(10**10)):
            netError[i] = True
    return not all(netError)


def gaussSeidel(a, b):
    height = len(a)
    x = np.array([
        [1.0],
        [1.0],
        [1.0],
        [1.0]
    ])
    prevx = x.copy()
    prevx[2] = 3 #just to change the initial error from being zero
    j = 0
    while isConverged(x, prevx):
        prevx = x.copy()
        j = j + 1
        for i in range(height):
            x[i] = (b[i] - np.matmul(a[i],x) + x[i]*a[i][i])/a[i][i]
    return (x, 'No of iterations = ' + str(j))




if __name__ == "__main__":
        
    a = np.array([
        [-4, 1, 0, 1],
        [1, -4, 1, 0],
        [0, 1, -4, 1],
        [1, 0, 1, -4],
    ])

    b = np.array([
        [-275],
        [-75],
        [-25],
        [-225]
    ])
    print(gaussSeidel(a, b))
