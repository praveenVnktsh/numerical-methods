from math import *

def fx(x):
    '''
    Returns the function that needs to be evaluated
    '''
    return x
def computeTrapInt(points, funcToIntegrate):
    integral = 0
    for i in range(1,len(points)):
        integral += (funcToIntegrate(points[i][1]) + funcToIntegrate(points[i-1][1]))*(points[i][0] - points[i-1][0])/2
    return integral



if __name__ == "__main__":
    pts = [(0.0,0.002),(0.02, 0.00135),(0.04, 0.00134),(0.05, 0.0016),(0.06,0.00158),(0.07,0.00142),(0.1,0.002)]
    integral = computeTrapInt(pts, fx)
    print('Integral =  ',)



