from math import *
import numpy as np
import time
import matplotlib.pyplot as plt


def iterationCmpltCallbackFunc(currentval): # if you want to do something after each iteration completes
    global dist
    dist = np.append(dist, [dist[-1]  + currentval])


def func(t, v):
    ''' 
    Solve for dy/dt = func(x,y) here y = v, x = t
    '''
    global dist
    m = 68.1
    cd = 1.5
    L = 30
    g = 9.81
    k = 40
    gamma = 8
    if dist[-1] <= L:
        return g - np.sign(v)*cd*(v**2)/m
    else:
        return g - np.sign(v)*cd*(v**2)/m - (k/m)*(dist[-1] - L) - (gamma/m)*v



def rungeKuttaFourODE(x, foo, y0, h, iterationCallback):
    y = np.zeros(x.size)
    y[0] = y0
    for i in range(1, x.size):
        k1 = h*foo(x[i-1], y[i-1])
        k2 = h*foo(x[i-1] + 0.5*h, y[i-1] + 0.5*k1)
        k3 = h*foo(x[i-1] + 0.5*h, y[i-1] + 0.5*k2)
        k4 = h*foo(x[i-1] + h, y[i-1] + k3)
        y[i] = y[i-1] + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
        iterationCallback(y[i]*h)
    return x, y


if __name__ == "__main__":
    '''
    Let us solve the terminal velocity equation!
    '''


    dist = np.array([0])
    legend = []
    h = 1
    x = np.arange(0.0, 50.0, h)
    y = np.zeros(x.size)
    
    timeStart = time.time()
    x, y = rungeKuttaFourODE(x, func, y0 = 0, h = h, iterationCallback = iterationCmpltCallbackFunc)
    
    print("RungeKutta METHOD: ",time.time() - timeStart,' s' )
    legend.append('Runge Kutta')
    plt.figure(1)
    plt.plot(x,dist)
    plt.xlabel('Time (s)')
    plt.ylabel('Displacement (m)')
    plt.title('Displacement vs Time')
    plt.legend(legend)
    
    
    plt.figure(2)
    plt.plot(x,y,'b-')
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (m/s)')
    plt.title('Velocity vs Time')
    plt.legend(legend)
    
    plt.show()
