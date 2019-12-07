import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

def predict(W1,W2,W3,x): 
    Z=np.zeros(len(x))
    for i in range(len(x)):
        calc1=W1[0]+W1[1]*x[i][0]+W1[2]*x[i][1]
        calc2=W2[0]+W2[1]*x[i][0]+W2[2]*x[i][1]
        calc3=W3[0]+W3[1]*x[i][0]+W3[2]*x[i][1]
        if(calc1>calc2 and calc1>calc3):
            Z[i]=1
        elif (calc2>calc1 and calc2>calc3):
            Z[i]=2
        else:
            Z[i]=3
    return Z


def plot_decision_boundry(X,Y,W1,W2,W3):
    h = 0.02
    x_min, x_max = X[:,0].min() - 100*h, X[:,0].max() + 100*h
    y_min, y_max = X[:,1].min() - 100*h, X[:,1].max() + 100*h
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),np.arange(y_min, y_max, h))
    Z = predict(W1,W2,W3,np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    print("size of z",Z.shape)
    # c = ('#ff0000', '#ffff00', '#0000FF', '0.6', 'c', 'm')
    plt.figure(figsize=(8,8))
    plt.contourf(xx, yy, Z,alpha=0.25)
    plt.contour(xx, yy, Z, colors='k', linewidths=0.5)
    plt.scatter(X[:,0], X[:,1], c=Y)   
    

