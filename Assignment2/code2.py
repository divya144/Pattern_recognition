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
    #print(len(mean),len(new_mean[0]))
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
        new_mean=[[0,0,0] for i in range(len(clusters))]
        for i in range(len(clusters)):
            dimension=len(new_mean[i])
            for items in clusters[i]:
                for j in range(dimension):
                    new_mean[i][j]+=items[j]
            for j in range(dimension):
                new_mean[i][j]=new_mean[i][j]/len(clusters[i])
        print('iteration no.',repeat)
        converge=change(mean,new_mean)
        print(converge)
        if(converge==0):
            print('After',repeat,'iteration')
            break
        mean=new_mean
    return mean
def image_segmentation_pixels(img,vectorized,k):
    mean=sample(vectorized,k)
    print(mean)
    centre=centroids(vectorized,mean)
    print(centre)
    row,column,_=img.shape
    for r in range(row):
        for c in range(column):
            min=10000000.0
            index=-1
            for j in range(k):
                distance=find_distance(img[r][c],centre[j])
                if distance<min :
                    min=distance
                    index=j
            img[r][c]=centre[index]
    return img


#--------------------------------Using pixels only---------------------------------------#
if __name__ == "__main__":   
    img1=cv2.imread("original1.jpg")
    print('size of image',img1.shape)
    img=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
    Original=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
    print(img.shape)
    vectorized = img.reshape((-1,3))
    vectorized = np.float32(vectorized)
    k=15
    img=image_segmentation_pixels(img,vectorized,k)
    figure_size = 15
    plt.figure(figsize=(figure_size,figure_size))
    plt.subplot(1,2,1),plt.imshow(Original)
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(1,2,2),plt.imshow(img)
    plt.title('Segmented Image when K = %i' % k), plt.xticks([]), plt.yticks([])
    plt.show()





        
        
