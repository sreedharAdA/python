# cerated by sreedhar
# 07/06/2024

import numpy as np
import pandas as pd
arr=pd.Series(np.arange(10,16,1),index=["a","b","c","d","e","f"])
print(arr)
C=arr["c"]
print(C)
print()

a=arr["c":"f"]=500
print(a)
print()

b=arr[::-3]
print(b)
print()

d=arr['a':'f':2]
print(d)
print()

aa=arr[::3]
print(aa)
print()
print()

sreedhar=pd.Series(["sreedhar","deva","arun","pavan"])
print(sreedhar)
print()

sss=sreedhar["sreedhar":"arun"]
print(sss)




s=pd.name="sreedhar"
print(s)


data1={
    'a' : 1,'b':2,'c':3,
}
print(data1)
sa0=pd.Series(data=data1,index=['a','b','c'])
print(sa0)

#

sa9=pd.Series(data=data1,index=['a','b','c','d'])
print(sa9)
print()


# name in Series
stuname=pd.Series([22,23,23,24,25],name="stuage")
print(stuname)
print()

# index name
stuage=stuname.index.name="sreedhar"
print(stuage)


# adding two values
arr1=pd.Series([1,2,3,4,5])
arr2=pd.Series([6,7,8,9,])
wherevalue=0
arr3=(arr1+arr2)
print(arr3)

# value

print()
# size
sa2=pd.Series([1,2,3,4]).size
print(sa2)
print()

# methods
sa3=pd.Series({'sreedhar':24,'deva':23,'arun':45,'pavan':60},name="age")
print("the max age is:",sa3.max())
print()
print("the min age is:",sa3.min())
print()
print("the head  is:",sa3.head())
print()
print("the tail is:",sa3.tail())
print("the count is:",sa3.count())
