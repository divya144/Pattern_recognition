# Pattern_recognition
Contains code of assignments of CS669 course

# Assignment-2
a) For the dataset of Assignment 1, perform classification using k-means clustering for the non-linearly seperable cases 

b) Perform k-means clustering based segmentation of the given images,

i) When using only pixel colour values as features

II) When using both pixel colour and location values as features

(in both cases, display the segmentation output as a colour image, with different colours assigned pixels belonging to different clusters, and same colours assigned to pixels belonging to the same cluster)

# Assignment-3
Dataset: MNIST digit dataset: http://yann.lecun.com/exdb/mnist/

Problem statement

a) Given a set of images of any single digit from the above dataset, compute a covariance matrix and the Eigen vector basis using the vectorized representation of these images. Project each image onto this PCA space using i) all Eigen vectors ii) Selected Eigen vectors with different values of energy thresholds (computed using the top k Eigen values). Reconstruct the original images using the projected data obtained in the cases above and comment on the quality of reconstruction based for different cases.  

b) Now add up to 20% noise to the images, and perform the same experiment as above. Comment on the tradeoff between denoising and reconstruction quality for different cases of no. of principal components.

# Assignment-4

Assignment 4: Perceptron

In the data set used for problem 1, for linearly separable classes

a) Perform classification using a two class perceptron

b) Perform classification using a multiclass perception

In both cases, 1) show the decision regions, 2) Plot the convergence curves 

# Assignment-5

Classify and Compare the following methods on a dataset from the link provided in assignment 1, 

The dataset should be chosen as follows:
non-seperable, more than two classes, requiring atleast 3 Gaussians in case of GMM


a) GMM (choose the dataset which requires at least 3 Gaussians in the mixture)

b) Parzen window (with a window of your choice)

c) Multiclass perceptron (Decide the criteria to stop, if the data is not seperable)
