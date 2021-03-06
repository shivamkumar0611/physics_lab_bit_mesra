import matplotlib.pyplot as plt
import numpy as np
print("WELCOME_TO_BIT_MESRA_PHYSICS_LAB")
print("Created by SHIVAM KUMAR ECE K19 batch")
n = int(input("Enter number of elements : "))  
X = list(map(float,input("\nEnter the x-co ordinates : ").strip().split())) 
Y = list(map(float,input("\nEnter the y-co ordinates: ").strip().split()))
if (len(X)!=n or len(Y)!=n):
    print("Some Data is Missing...")
    print('Please check again.. ')
else :
    mean_x = np.mean(X)
    mean_y = np.mean(Y)
    m = len(X)
    numer = 0
    denom = 0
    for i in range(m):
        numer +=(X[i] - mean_x) * (Y[i] - mean_y)
        denom +=(X[i] - mean_x) **2
    b1 = numer / denom
    b0 = mean_y - (b1 * mean_x)
    max_x = np.max(X) + 100
    min_x = np.min(X) - 100
    x = np.linspace(min_x, max_x, 1000)
    y = b0 + b1 * x
    plt.plot(x, y, label='Regression Line')
    plt.scatter(X, Y, label='Scatter plot')
    s1=str(input("Enter the title: "))
    plt.title(s1.upper(), color='r')
    x2=str(input("Enter the name of X-axis: "))
    plt.xlabel(x2,fontsize=12 ,color='b')
    y2=str(input("Enter the name of Y-axis: "))
    plt.ylabel(y2,fontsize=12 , color='b')
    plt.legend()
    plt.grid()
    plt.show()
