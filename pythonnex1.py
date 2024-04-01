# created by sreedhar
# 01/04/2024


# array indexing

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[0])


arr = np.array([1, 2, 3, 4])

print(arr[1])


arr = np.array([1, 2, 3, 4])

print(arr[2] + arr[3])



arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1])

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('5th element on 2nd row: ', arr[1, 4])


arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])




arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1])

# slicing

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])



arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[4:])



arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[:4])


arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[-3:-1])


arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2])



arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[::2])


arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])


arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 2])


arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 1:4])


arr = np.array([1, 2, 3, 4])

print(arr.dtype)


arr = np.array(['apple', 'banana', 'cherry'])

print(arr.dtype)



arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)


arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)



arr = np.array(['a', '2', '3'], dtype='i')



arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)



arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype(int)

print(newarr)
print(newarr.dtype)



arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)




