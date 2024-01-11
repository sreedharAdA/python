# sreedhar
# 10/01/2024
import os
FilePath = "c://test/sreedhar.txt"
sreedhar = open(FilePath, "r")
MyData = sreedhar.read()
print("the filepath is read:", MyData)

# readline

sreedhar = open(FilePath, "a+")
# sreedhar.seek(0)
print(sreedhar.tell())

MyData = sreedhar.readline(20)
print("the filepath is readline:", MyData)

# readlines

sreedhar = open(FilePath, "r")
# sreedhar.seek(0)
sreedhar.tell()
MyData = sreedhar.readlines()
print("the filepath is readlines:", MyData)

# write
FilePath = "c://test/sreedhar1.txt"
sreedhar = open(FilePath, "w+")
MyData = "sreedhar is good crickete"
sreedhar.write(MyData)
sreedhar.close()


# write lines
FilePath = "c://test/sreedhar1.txt"
sreedhar = open(FilePath, "w+")
MyData = "sreedhar is good crickete"
sreedhar.write(MyData)

strlist = ["sreedhar", "deva", "arun"]
sreedhar.writelines(str(strlist))
sreedhar.close()



