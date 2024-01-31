# created by sreedhar
# 30/01/2024
class father:
    def fun(self):
     print("gold")
     print("amount")
class son(father):
    def fun(self):
        print("a")
        print("b")
        print("c")
        super().fun()
class grandson:
    def fun(self):
        print("d")
        print("e")
        print("f")
obj = grandson()
obj.fun()
class fatherclass:
    def father(self):
        print("")
class sonclass(father):
    def son(self):
        print("")
class grandsonclass(son,father):
    def father(self):
        super().father()
    def son(self):
        print("")
        super().father()
    def garndson(self):
        print("")
        super().father()
obj=grandsonclass()
obj.fun()





# son_obj.father_method()
# Interface
class sreedhar:
    name ="abc"
    Age = 23
    DOB = "12-Jan-2000"
    def _init_(self,name,Age,DOB):
        self.name=name
        self.Age=Age
        self.DOB=DOB
    def display(self):
        pass
obj=sreedhar()
obj.display()
class deva:
    height="height"
    age=23
    def _init_(self,height,age):
        self.height=height
        self.age=age

    def display(self):
        pass
obj=deva()
obj.display()

class arun:
    def _init_(self,na,A,D):
        self.name=na
        self.Age=A
        self.DOB=D
    def display(self):
        print("sreedhar")
obj=arun()
obj.display()
obj=deva()
obj.display()
obj=sreedhar()
obj.display()


