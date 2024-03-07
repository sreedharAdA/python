import numpy as np
import pandas as pd
# arr=[1,5,3,8,11]
#
# s=pd.Series(data=arr)
# sa=s[3]
# print(s)
# print(sa)
# print()
#
# sa1=s[1:3]
# print(sa1)
# print()
# print()
#
#
# sa2=s[1+3]
# print(sa2)
# print()
#
# sa3=s[2-2]
# print(sa3)

# s=pd.name="sreedhar"
# print(s)


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

# ssa=pd.Series([1,2,3])
# ssa.dtypes('int64')

# s = pd.Series([1, 2, 3])
# s.dtypes
# dtype('int64')

# sss=pd.Series([1,2,3]).values
# array([1,2,3])
# print(array)

#
# m= pd.Series(['Ant', 'Bear', 'Cow'])
# print(m)
# m.size()