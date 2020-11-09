from math import *

def massFlowMultiplier():
    return 9


def computeSimpsonThreeIntegral(points, coeffMultiplerFunc):
    #1/3 rule
    integral = 0
    for i in range(1,len(points),2):
        integral += coeffMultiplerFunc()*((points[i+1][0] - points[i-1][0])/6)*(points[i-1][1] + 4*points[i][1] + points[i+1][1])
    return integral

def computeSimpsonEightIntegral(points, coeffMultiplerFunc):
    #3/8 rule
    integral = 0
    for i in range(0,len(points)-1,3):
        integral += coeffMultiplerFunc()*((points[i+3][0] - points[i][0])*3/24)*(points[i][1] + 3*points[i+1][1] + 3*points[i+2][1]+ points[i+3][1])
    return integral



if __name__ == "__main__":
    
    pts1 = [(0, 10), (10, 35), (20, 55), (30, 58)]
    pts2 = [(30, 58), (35, 62), (40, 66), (45, 70), (50, 78)]

    int2 = computeSimpsonThreeIntegral(pts2,massFlowMultiplier)
    int1 = computeSimpsonEightIntegral(pts1,massFlowMultiplier)
    print("TOTAL INTEGRAL:", int1+int2)