import numpy as np
array1=np.array([1,2,3])
array2=np.array([4,5,6])
array3=np.vstack((array1,array2))
print(array3)
print()
print()



# 2D
array1=np.array([[1],[2],[3]])
array2=np.array([[4],[5],[6]])
array3=np.vstack((array1,array2))
print(array3)
print()
print()

# 3D
array1=np.array([[[1],[2],[3]]])
array2=np.array([[[4],[5],[6]]])
array3=np.vstack((array1,array2))
print(array3)
print()
print()