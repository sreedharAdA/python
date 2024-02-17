# created by sreedhar
# 17/02/2024
# zero dimension
import numpy as np
# sreedhar=np.array([1,2,3])
# print(sreedhar)
# print(sreedhar[1])
# print(sreedhar.shape)
# print("......................")
#
# # Two dimension
# sreedhar1 = np.array([[1,2,3],[4,5,6]])
# print(sreedhar1)
# print(sreedhar1.shape)
# print(sreedhar1[1][2])
#
# sreedhar2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(sreedhar2)
# print(sreedhar2.shape)
# print(sreedhar2[2][2])
# print("-----------------")
#
#
# # three dimension
# sreedhar3 = np.array([[[1,2,3],[7,8,9],[4,5,6]]])
# print(sreedhar3)
# print(sreedhar3.shape)
# print(sreedhar3[1][1])

# # array in sliceing
# sreedhar4 = np.array([[1,2,3],[5,6,7],[7,8,9]])
# print(sreedhar4)
# print(sreedhar4[0:1,2])
# print(sreedhar4[1:3,1:1])


#
# # add array
#
# sreedhar5= np.array([1,2,3])
# sreedhar6= np.array([4,5,6])
# print(sreedhar5)
# print(sreedhar6)
# resultarray= sreedhar5+sreedhar6
# print(resultarray)

#
# # multipleing array
# sreedhar5= np.array([1,2,3])
# sreedhar6= np.array([4,5,6])
# print(sreedhar5)
# print(sreedhar6)
# resultarray= sreedhar6*sreedhar5
# print(resultarray)
# print("------------")
# # matrix's multiple array
#
# sreedhar7= np.array([1,2,3])
# sreedhar8= np.array([1,2,2])
# print(sreedhar7)
# print(sreedhar8)
# result=sreedhar7@sreedhar8
# print(result)
# print("--------------")
#
# sreedhar7= np.array([[1,2,3],[4,5,6],[7,8,9]])
# sreedhar8= np.array([1,2,])
# print(sreedhar7)
# print(sreedhar8)
# result=sreedhar7@sreedhar8
# print(result)

#
# sreedhar7= np.array([[1,2,3],[4,5,6],[7,8,9]])
# sreedhar8= np.array([[1,2],[3,4]])
# print(sreedhar7)
# print(sreedhar8)
# result=sreedhar7@sreedhar8
# print(result)

# sreedhar7= np.array([[[1,2,3],[4,5,6],[7,8,9]]])
# sreedhar8= np.array([[[1,2],[3,4],[6,7]]])
# print(sreedhar7)
# print(sreedhar8)
# result=sreedhar7@sreedhar8
# print(result)

# print(result)

sreedhar7= np.array([[[1,2],[4,5]]])
sreedhar8= np.array([[[1,2],[3,4]]])
print(sreedhar7)
print(sreedhar8)
result=sreedhar7@sreedhar8
print(result)

