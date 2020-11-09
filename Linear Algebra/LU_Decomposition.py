import numpy as np
from math import *

def ludecomp(a):
    height = len(a)  # height, or number of equations
    L = np.zeros((height, height))
    U = np.zeros((height, height))
    for i in range(height):
        L[i][i] = 1
    for j in range(0, height-1):
        for i in range(j+1, height):
            product = a[i][j]/a[j][j]
            L[i][j] = product
            a[i] = a[i] - (product)*a[j]
    return (a, L)  # Returns Upper and lower triangular matrices

def forwardSubstitution(L, m):# For any general lower triangular matrix with non identity diagonal.
    height = len(L)
    x = np.zeros((height, 1))
    x[0] = float(m[0]/L[height-1][height-1])
    for i in range(1, height):
        s = 0
        for j in range(0, i):
            s = s + L[i][j]*x[j]
        x[i] = (m[i] - s)/L[i][i]
    return x

def backwardSubstitution(U, y):  # For any general upper triangular matrix
    height = len(U)
    x = np.zeros((height, 1))
    x[height-1] = y[height-1]/U[height-1][height-1]
    for i in range(height-1, -1, -1):
        s = 0
        for j in range(height-1, i, -1):
            s = s + U[i][j]*x[j]
        x[i] = (y[i] - s)/U[i][i]
    return x



if __name__ == "__main__":
    # An example question
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
    
    U, L = ludecomp(A) # Decompose A into U and L 
    y = forwardSubstitution(L, b) # Find y from L and b
    x = backwardSubstitution(U, y) # Find x from U and y    
    print("SOLUTION:", x)
