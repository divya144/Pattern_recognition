import idx2numpy 
import numpy as np

file_train='train-images.idx3-ubyte'
arr=idx2numpy.convert_from_file(file_train)
file_label='train-labels.idx1-ubyte'
label=idx2numpy.convert_from_file(file_label)

#noisy_img = img + np.random.normal(mean, std, img.shape)

digit=[[] for i in range(10)]
for i in range(len(arr)):
    t=label[i]
    row,column=arr[i].shape
    flatten=arr[i].reshape(row*column,)
    digit[t].append(flatten)

for j in range(10):
    digit[j]=np.asarray(digit[j])
    print(len(digit[j])) 

for i in range(10):
    file=str(i)+'.npy'
    np.save(file,digit[i])
