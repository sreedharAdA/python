'''
created by sreedhar
21/02/2024
'''

import numpy as np
array1 = np.array([[12,31,41],[21,22,23],[31,32,33]])
print(array1)
print("number of dimensions:",array1.ndim)
print("size of the array1:",array1.size)
print("shape of the array1:",array1.shape)
print("type of a array1:",array1.dtype)
print("item of size in array1",array1.itemsize)
print()
# methods of a array
# reshape in 1D array
array2=np.array([1,2,3,4,5,6,7,8,9,0])
print(array2)
print("resize of array2:\n",array2.reshape(5,2))

# converting 1D to 3D array
array3=np.array([1,2,3,4,5,6,7,8])
print("1D to 3D array:\n",array3.reshape(2,2,2))

array3=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print("1D to 3D array:\n",array3.reshape(3,2,2))

# Reshape row-wise and column-wise
array3=np.array([1,2,3,4,5,6,7,8,9,0,])
print("reshape row-wise in array:\n",array3.reshape(5,2))
Array = np.array([0, 1, 2, 3, 4, 5, 6, 7])
reshapedArray = np.reshape(Array, (2, 4), 'F')
print(reshapedArray)
print()
# flatarray
sreedhar=np.array([[1,2,3],[4,5,6],[7,8,9]])
resultarray=np.reshape(sreedhar,-1)
print(resultarray)



# transpose method()

sreedhar1= np.array([[1,2,3],[4,5,6],[7,8,9]])
resultarray1=np.transpose(sreedhar1)
print(resultarray1)

# axies transpose method()

# sreedhar2= np.array([[[1,2,3],[4,5,6],[7,8,9]]])
# resultarray1=np.transpose(sreedhar2(2,0,1))
# print(resultarray1)

originalArray = np.array([[[0, 1], [2, 3]], [[4, 5], [6, 7]]])
print('When axes are (2, 0, 1):')
transposedArray = np.transpose(originalArray, (2, 0, 1))
print(transposedArray)
print('When axes are (0, 2, 1):')
transposedArray = np.transpose(originalArray, (0, 2, 1))
print(transposedArray)


# append method()
sreedhar21=np.array([1,2,3])
sreedhar22=np.array([4,5,6])
sreedhar23=np.append(sreedhar21,sreedhar22)
print(sreedhar23)


# append axies 0
s=np.array([[1,2],[3,4]])
a=np.array([[5,6],[7,8]])

# # append axis concatemate
# a=np.array([1,2,3])
# b=np.array([[4,5,6],[7,8,9]])
# c=np.array((a, b))
# print(c)


# sort
sree1=np.array([10,2,3,6,7,-1])
sree2=np.sort(sree1)
print(sree2)

sree3=np.array(['apple','cat','bell'])
sree4=np.array(sree3)
print(sree4)


# tolist
array=np.array([[1,2,3],[4,5,6]])
sree5=array.tolist()
print(sree5,type(sree5))


# split

arr=np.array([1,2,3,4])
sub=np.split(arr,2)
print(sub)


#  concatenate

arr1 =np.array([[1,2,3],[4,5,6]])
arr2=np.array([[4,5,6],[7,8,9]])
arr3=np.concatenate((arr1,arr2))
print(arr3)


