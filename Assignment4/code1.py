import numpy as np
import matplotlib.pyplot as plt

def read_file(A,file):
    f=open(file,"r")
    for line in f:
        num1,num2=line.split()
        A.append([float(num1),float(num2)])
    return A
def cal(X,W):
    output=W[0]*X[0]+W[1]*X[1]+W[2]*X[2]
    if output>=0:
        return 1
    else:
        return -1
def train(A,Y):
    samples,features=A.shape
    A = np.hstack((np.ones((samples,1)), A))
    W = np.random.rand(features+1).reshape((-1,1))
    misclassified=True
    iter=0
    convergence=[]
    while misclassified!=False:
        misclassified=False
        iter=iter+1
        error=0
        # print(iter)
        for index,x in enumerate(A):
            out=cal(x,W)
            # print(out)
            if out!=Y[index]:
                misclassified=True
                error=error+1
                W=W+(Y[index]*x.reshape((-1,1)))
        convergence.append(error)
        if(iter==10000):
            break
    print("NUmber of iteration: ",iter)
    return W,convergence
def predict(W,x):
    print(x.shape)
    Z=np.zeros(len(x))
    for i in range(len(x)):
        cal=W[0]+W[1]*x[i][0]+W[2]*x[i][1]
        if(cal>=0):
            Z[i]=1
        else:
            Z[i]=-1
    return Z
def plot_decision_boundry(X,Y,w):
    h = 0.02
    cmap='Paired_r'
    x_min, x_max = X[:,0].min() - 100*h, X[:,0].max() + 100*h
    y_min, y_max = X[:,1].min() - 100*h, X[:,1].max() + 100*h
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),np.arange(y_min, y_max, h))
    Z = predict(w,np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    print("size of z",Z.shape)
    plt.figure(figsize=(8,8))
    c = ('r','y','m')
    # plt.contourf(xx, yy, Z, cmap=cmap, alpha=1)
    plt.contourf(xx, yy, Z, alpha=0.25)
    plt.contour(xx, yy, Z, colors='k', linewidths=0.5)
    plt.scatter(X[:,0], X[:,1], c=Y)
    plt.legend       

def plot_convergence(convergence):
    iteration=[]
    for i in range(len(convergence)):
        iteration.append(i)
    plt.plot(iteration,convergence)
    plt.show()







