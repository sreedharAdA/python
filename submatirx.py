import numpy as np
sreedhar= np.array([[1,2,3],[4,5,6],[7,8,9]])
matirx= np.array(sreedhar)
print(matirx)
print("--------------------------------")
# sub matirx and slicing

result=matirx[ : , : ]
print(result)
print("--------------------------------")

result=matirx[0:3, 0:3]
print(result)
print("--------------------------------")

result=matirx[0:2, 0:2]
print(result)
print("--------------------------------")

result=matirx[0:1, 0:1]
print(result)
print("--------------------------------")

result=matirx[0:1, 0:3]
print(result)
print("--------------------------------")

arr = np.array([20,40,60,80,100,120,140,160,180,200])
print(arr)
print(arr.size)
print(arr.shape)
print(arr.ndim)
print()
print(arr.reshape(2,5))
print()
arr = np.array([20,40,60,80,100,120,140,160,180])
print(arr)
print(arr.size)
print(arr.shape)
print(arr.ndim)
print()
print(arr.reshape(3,3))
print()
print()
arr = np.array([20,40,60,80,100,120,140,160,180,200])
print(arr)
print(arr.size)
print(arr.shape)
print(arr.ndim)
print()
print(arr.resize(6))





