# created by sreedhar
# 24/01/2024


# class account:
#  def account(self, accountnumber, ifc, bankname,balance):
#      self.accountnumber = accountnumber
#      self.ifc = ifc
#      self.bankname = bankname
#      self.balance = balance
#  def display(self):
#     print("accountnumber:",self.accountnumber)
#     print("ifc:", self.ifc)
#     print("bankname:", self.bankname)
#     print("balance:", self.balance)
# obj=account()
# obj.display()


#Single inheritance
class sreedhar:
    def fun(self):
        print("This is parent class")
class deva(sreedhar):
    def fun1(self):
        print("This is child class")
obj=deva()
obj.fun1()
obj.fun()
print("-----------")
#Multiulevel inheritance
class khajanna:
    def fun1(self):
        print("This is parent class")
class sreedhar(khajanna):
    def fun2(self):
        print("This is child class")
class Grandchild(sreedhar):
    def fun3(self):
        print("this is grandchild class")
obj=Grandchild()
obj.fun3()
obj.fun2()
obj.fun1()
print("--------")
#Multiple inheritance
class Father:
    def fun1(self):
        print("This is father class")
class mother:
    def fun2(self):
        print("this is mother class")
class sreedhar(khajanna,mother):
    def fun3(self):
        print("This is sreedhar class")
obj=sreedhar()
obj.fun3()
obj.fun2()
obj.fun1()
print("--------")
#Hybrid inheritance
class white:
    def fun1(self):
        print("this is white class")
class sai(white):
    def fun2(self):
        print("This is sai")
class ramesh(white):
    def fun3(self):
        print("This is ramesh")
class Student(sai,ramesh):
    def fun4(self):
        print("This is sreedhar class")
obj=Student()
obj.fun4()
obj.fun3()
obj.fun2()
obj.fun1()





