import numpy as np
import matplotlib.pyplot as plt
import math
import sys
import random
from random import sample

# random.seed(120)
def read_file(file,A):
    f=open(file,"r")
    for line in f:
        num1,num2=line.split()
        A.append([float(num1),float(num2)])
    return A
#finds distance between a point and mean
def find_distance(A,mean):
    ans=0.0
    for i in range(len(A)):
        ans+=math.pow(A[i]-mean[i],2)
    return math.sqrt(ans)
#plots whole list of features with initial mean
def plot_color(A, color,mean):
    for i in range(len(A)):
        plt.plot(A[i][0],A[i][1],color,markersize = 6 )
    plot_mean(mean)
    plt.show()
#plot clusters with new mean
def plot_clusters(clusters,mean):
    colors=['yo','mo','co']
    for i in range(len(clusters)):
        for j in range(len(clusters[i])):
            plt.plot(clusters[i][j][0],clusters[i][j][1],colors[i],markersize = 6)
    plot_mean(mean)
    plt.show()
#plot means
def plot_mean(mean):
    colors=['ro','bo','go']
    for i in range(len(mean)):
        plt.plot(mean[i][0],mean[i][1],colors[i],markersize=8)
 
def change(mean,new_mean):
    difference=0
    for i in range(len(mean)):
        for j in range(len(mean[i])):
            difference=difference+math.pow(mean[i][j]-new_mean[i][j],2)
    return math.sqrt(difference) 
def centroids(A,mean):
    for repeat in range(100):
        clusters = [[] for i in range(len(mean))]
        for i in range(len(A)):
            min=10000
            index=-1
            for j in range(len(mean)):
                distance=find_distance(A[i],mean[j])
                if distance < min :
                    min=distance
                    index=j
                clusters[index].append(A[i])

        new_mean=[[0,0] for i in range(len(clusters))]
        for i in range(len(clusters)):
            for items in clusters[i]:
                new_mean[i][0]+=items[0]
                new_mean[i][1]+=items[1]
            new_mean[i][0]=new_mean[i][0]/len(clusters[i])
            new_mean[i][1]=new_mean[i][1]/len(clusters[i])
        # plot_clusters(clusters,mean)
        converge=change(mean,new_mean)
        print(converge)
        if(converge==0):
            print('After',repeat,'iteration')
            break
        mean=new_mean
    plot_clusters(clusters,mean)
    return mean

if __name__ == "__main__":
    A=[]  #1500 x 2
    A=read_file("Data1/Class1.txt",A)
    A=read_file("Data1/Class2.txt",A)
    A=read_file("Data1/Class3.txt",A)
    k=3
    mean=sample(A,k)
    plot_color(A,'ko',mean)
    centre=centroids(A,mean)
    print(centre)

