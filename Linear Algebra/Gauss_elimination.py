from math import *
import numpy as np

'''
We need to solve Ax = b using Gauss Elimination
'''
def gaussElim(a, b):
    height = len(a)  # height, or number of equations
    for j in range(0, height-1):
        for i in range(height-1, j, -1):
            # gauss elimination equations
            product = a[i][j]/a[j][j]
            a[i] = a[i] - (product)*a[j]
            b[i] = b[i] - (product)*b[j]
    # a = upper triangular matrix
    # x through backsubstitution
    x = np.zeros((height, 1))
    x[height-1] = b[height-1]/a[height-1][height-1]
    for i in range(height-1, -1, -1):
        s = 0
        for j in range(height-1, i, -1):
            s = s + a[i][j]*x[j]
        x[i] = (b[i] - s)/a[i][i]
    return x


if __name__ == "__main__":
    # an example equation
    A = np.array([ 
    [-3.0, 2.0, 1.0],
    [2.0, -9.0, 4.0],
    [2.0, 8.0, -15.0]
    ])
    b = np.array([
        [-10.0],
        [0.0],
        [0.0]
    ])

    #Solve!
    solution = gaussElim(A,b)
    print('Solved equation = ', solution)

