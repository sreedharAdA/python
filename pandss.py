#  created by sreedhar
#  06/03/2024

# series
import numpy as np
import pandas as pd
# arr=[1,5,3,8,11]
# s=pd.Series(data=arr)
# print(s)
# print()
#
#
# # labels
# labels=["a","b","c","d","f"]
# sa=pd.Series(data=arr,index=labels)
# print()
#
# # array
# arr=[1,2,3,4]
# sa1=np.array(arr)
# print(sa1)
# print()
#
# labels=["a","b","c","d"]
# sa=pd.Series(data=arr,index=labels)
# # converting arr into series
# sa2=pd.Series(arr,labels)
# print(sa2)
# print()
# print()
#
#
# # converting dictionarty to series
#
# data1={'sreedhar':24,'deva':23,'arun':22,'pavan':25}
# sa3=pd.Series(data1)
# print(sa3)
# print()
# print()
#
# # series can hold vatriy object type
# ss=pd.Series(data=labels)
# print(ss)
# print()
# print()

saa1=pd.Series([1,2,3,4], index= ['sreedhar' , 'deva' , 'arun' , 'pavan'])
saa2=pd.Series([1,2,3,4], index= ['pavan' , 'arun' , 'deva' , 'sreedhar'])

print(saa1)
print()
print(saa2)


#
# saa1['sreedhar']
# print(saa1)

# saa1.values
saa3=saa1+saa2
print(saa3)

