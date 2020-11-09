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


def heunsODE(t, foo, y0,h, iterationCallback):
    v = np.zeros(t.size)
    v[0] = y0
    for i in range(1, t.size):
        y_i = v[i-1] + h*foo(t[i-1],v[i-1])
        v[i] = v[i-1] + (foo(t[i-1],v[i-1]) + foo(t[i],y_i))*(h/2.0)
        iterationCallback(v[i]*h)
    return t, v


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
    x, y = heunsODE(x, func, y0 = 0, h = h, iterationCallback = iterationCmpltCallbackFunc)
    
    print("HEUNS METHOD: ",time.time() - timeStart,' s' )
    legend.append('HEUNS')
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
