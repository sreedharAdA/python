# created by sreedhar
# 22/02/2024
import os
# filepath="c://sreedhar/a/sree.txt"
# sreedhar=open(filepath,"r")
# data=sreedhar.read()
# print(data)
#
#
# # readline
# filepath="c://sreedhar/a/sree.txt"
# sreedhar=open(filepath,"r")
# data=sreedhar.readline()
# print(data)
#
# # readlines
# filepath="c://sreedhar/a/sree.txt"
# sreedhar=open(filepath,"r")
# sreedhar.seek(43)
# print(sreedhar.tell())
# data=sreedhar.readlines(20)
# print(data)

#
# write

filepath="c://sreedhar/a/sree.txt"
sreedhar=open(filepath,"w")
data=sreedhar.write("sreedhar is a good cricketer")
print(data)



# # write lines
# filepath="c://sreedhar/a/sree.txt"
# sreedhar=open(filepath,"w")
# data=sreedhar.writelines("sreedhar is a good cricketer")
# print(data)
# sreedhar.close()


# import os
# FilePath = "c://test/sreedhar.txt"
# sreedhar = open(FilePath, "r")
# MyData = sreedhar.read()
# print("the filepath is read:", MyData)

# # readline
#
# sreedhar = open(FilePath, "a+")
# sreedhar.seek(10)
# print(sreedhar.tell())
#
# MyData = sreedhar.readline(20)
# print("the filepath is readline:", MyData)
#
# # readlines
#
# sreedhar = open(FilePath, "r")
# # sreedhar.seek(0)
# sreedhar.tell()
# MyData = sreedhar.readlines()
# # print("the filepath is readlines:", MyData)
# #
# # write
# FilePath = "c://test/sreedhar1.txt"
# sreedhar = open(FilePath, "w+")
# MyData = "sreedhar is good crickete"
# sreedhar.write(MyData)
# sreedhar.close()
# #
#
# # write lines
# FilePath = "c://test/sreedhar1.txt"
# sreedhar = open(FilePath, "w+")
# MyData = "sreedhar is good cricketer"
# sreedhar.write(MyData)
#
strlist = ["sreedhar", "deva", "arun"]
sreedhar.writelines(str(strlist))
sreedhar.close()
