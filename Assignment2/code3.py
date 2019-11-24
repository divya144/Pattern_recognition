import numpy as np
import matplotlib.pyplot as plt
import math
import sys
import random
from random import sample
import cv2

def find_distance(A,mean):
    ans=0.0
    for i in range(len(A)):
        ans+=math.pow(A[i]-mean[i],2)
    return math.sqrt(ans)

def change(mean,new_mean):
    difference=0
    for i in range(len(mean)):
        for j in range(len(mean[i])):
            difference=difference+math.pow(mean[i][j]-new_mean[i][j],2)
    return math.sqrt(difference) 

def centroids(A,mean):
    for repeat in range(10):
        clusters = [[] for i in range(len(mean))]
        for i in range(len(A)):
            min=10000000.0
            index=-1
            for j in range(len(mean)):
                distance=find_distance(A[i],mean[j])
                if distance < min :
                    min=distance
                    index=j
                clusters[index].append(A[i])
        new_mean=[[0,0,0,0,0] for i in range(len(clusters))]
        for i in range(len(clusters)):
            dimension=len(new_mean[i])
            for items in clusters[i]:
                for j in range(dimension):
                    new_mean[i][j]+=items[j]
            for j in range(dimension):
                new_mean[i][j]=new_mean[i][j]/len(clusters[i])
        print('-------------iteration no.',repeat,'-------')
        converge=change(mean,new_mean)
        print(converge)
        if(converge==0):
            print('After',repeat,'iteration')
            break
        mean=new_mean
    return mean
def image_segmentation_pixels_position(img,A,k):
    mean=sample(A,k)
    print('initial mean',mean)
    centre=centroids(A,mean)
    print('final centroids',centre)
    row,column,_=img.shape
    t=0
    for i in range(row):
        for j in range(column):
            min=100000000.0
            index=-1
            for c in range(k):
                distance=find_distance(A[t],centre[c])
                if distance<min:
                    min=distance
                    index=c
            t+=1
            img[i][j]=centre[index][2:5]
    # lt.imshow(img)
    # plt.show()p
    return img



if __name__ == "__main__":
    img2=cv2.imread("original1.jpg")
    img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
    figure_size = 15
    plt.figure(figsize=(figure_size,figure_size))
    plt.subplot(1,2,1),plt.imshow(img2)
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    row,column,_=img2.shape
    A=[]
    for r in range(row):
        for c in range(column):
            R=img2[r][c][0]
            G=img2[r][c][1]
            B=img2[r][c][2]
            A.append([r,c,R,G,B])
    k=15
    A=np.float32(A)
    img3=image_segmentation_pixels_position(img2,A,k)
    plt.subplot(1,2,2),plt.imshow(img3)
    plt.title('Segmented Image when K = %i' % k), plt.xticks([]), plt.yticks([])
    plt.show()




        
        
