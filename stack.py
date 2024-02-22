# created by sreedhar
# 22/02/2024


# 1D as a axis=0 don't 2,3,4
import numpy as np
sreedhar=np.array([1,2,3])
sreedhar1=np.array([4,5,6])
print(sreedhar)
print(sreedhar1)
# sreedhar2=[np.random.randn(1, 3) for _ in range(10)]
sreedhar2=np.stack(sreedhar,axis=0).shape
print(sreedhar2)
print()


# 2D as axis=1 don't work=3,4
sreedhar=np.array([[1,2,3]])
sreedhar1=np.array([[4,5,6]])
print(sreedhar)
print(sreedhar1)
sreedhar2=np.stack(sreedhar,axis=1).shape
print(sreedhar2)

# 3D axis=2
sreedhar=np.array([[[1,2,3]]])
sreedhar1=np.array([[[4,5,6]]])
print(sreedhar)
print(sreedhar1)
sreedhar2=np.stack(sreedhar,axis=2).shape
print(sreedhar2)


# 4D axis=3
sreedhar=np.array([[[[1,2,3]]]])
sreedhar1=np.array([[[[4,5,6]]]])
print(sreedhar)
print(sreedhar1)
sreedhar2=np.stack(sreedhar,axis=3).shape
print(sreedhar2)
