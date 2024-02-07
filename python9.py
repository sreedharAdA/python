# created by sreedhar
# 07/02/2024
# polymorphism
class sreedhar():
    def fun1(self,int):
        self.int = int
        print(int)
obj = sreedhar()
obj.fun1(12)

class sreedhar1():
    def fun1(self,str,str1):
        self.int = str
        self.str = str1
        print(str+str1)
obj = sreedhar1()
obj.fun1("sreedhar","sree")

class sreedhar2():
    def fun1(self,float,float1,float2):
        self.float = float
        self.float1= float1
        self.float= float2

        print(float,float1,float2)
obj = sreedhar2()
obj.fun1(12.5,34.4,23.5)

# multiple datatypes

class sreedhar():
    def fun1(self,int):
        self.int = int
        print(int)
obj = sreedhar()
obj.fun1(12)

class sreedhar1():
    def fun1(self,int,str1):
        self.int = int
        self.str = str1
        print(int+str1)
obj = sreedhar1()
obj.fun1("12","sree")

class sreedhar2():
    def fun1(self,float,str,complex):
        self.float = float
        self.float1= str
        self.float= complex
        print(float, str, complex)

    obj = sreedhar2()
    obj.fun1(12.5, sreedhar, 23.5j)


class sreedhar():
    def sree(self,a=None,b=None):
        print(a,b)
obj = sreedhar()
obj.sree()
obj.sree(10)
obj.sree(23,33)
