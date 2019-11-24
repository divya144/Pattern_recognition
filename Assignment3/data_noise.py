import idx2numpy 
import numpy as np
import matplotlib.pyplot as plt
file_train='train-images-idx3-ubyte'
arr=idx2numpy.convert_from_file(file_train)
file_label='train-labels-idx1-ubyte'
label=idx2numpy.convert_from_file(file_label)
digit=[[] for i in range(10)]
for i in range(len(arr)):
    t=label[i]
    row,column=arr[i].shape
    level=0.5
    new=arr[i]+level*np.random.normal(10,10,(row,column))
    flatten=new.reshape(row*column,)
    digit[t].append(flatten)
for j in range(10):
    digit[j]=np.asarray(digit[j])
    print(len(digit[j])) 

for i in range(10):
    file=str(i)+'_noise.npy'
    np.save(file,digit[i])
plt.imshow(digit[3][0].reshape(28,28),cmap='gray')
plt.show()