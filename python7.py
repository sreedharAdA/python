# created by sreedhar
# 26/01/2024

# list
#
# mylist = [1, 2, 3, 4, 5, 6,]
# print(mylist)
# mylist1 = mylist
# print(mylist1)
# mylist1.append(14)
# print("the updated list1:", mylist1)
# print("the updated list:", mylist)
# mylist2 = list(mylist1)
# print(mylist2)
# mylist2.append(23)
# print("updated list:", mylist)
# print("updated list2:", mylist1)
# print("updated list3:", mylist2)

# set

# myset = {1, 2, 3, 4, 5}
# mylist1 = myset
# print(mylist1)
# print(myset)
# mylist1.add(10)
# print("updated:",mylist1)
# print("updated:",myset)
# mylist2 = list(mylist1)
# print(mylist2)
# myset.add(24)
# print(mylist2)
# print(myset)
#

# tuple
#
# tuple = (10, 20, 30, 40)
# mylist = tuple
# print(mylist)
# print(tuple)
# mylist1 = list(mylist)
# print(mylist1)
# print(dddmnd)
# mylist1 = (40, 55, 66, 77, 88,)
# print(mylist1)
# print(tuple)
#

# dictionary

# set = {"sreedhar" : "55","deva" : "90"}
# mylist = set
# print(set)
# print(mylist)
# mylist.update({"arun":"34"})
# mylist1 = dict(mylist)
# print(mylist1)
# print(mylist1)
# mylist1.update({"dev": "02"})
# print(mylist1)

# class father:
#     def fun(self):
#      print("gold")
#      print("amount")
# class son(father):
#     def fun(self):
#         print("a")
#         print("b")
#         print("c")
#         super().fun()
# son_obj=son()
# son_obj.fun()
# # Child_obj.fun1()
# class fatherclass:
#     def father_method(self):
#         print("")
# class sonclass(fatherclass):
#     def parent_method(self):
#         super().father_method()
#     def son_method(self):
#         print("")
#         super().father_method()
# son_obj=sonclass()
# son_obj.son_method()
#




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
# class sreedhar:
#     name ="abc"
#     Age = 23
#     DOB = "12-Jan-2000"
#     def _init_(self,name,Age,DOB):
#         self.name=name
#         self.Age=Age
#         self.DOB=DOB
#     def display(self):
#         pass
# obj=sreedhar()
# obj.display()
# class deva:
#     height="height"
#     age=23
#     def _init_(self,height,age):
#         self.height=height
#         self.age=age
#
#     def display(self):
#         pass
# obj=deva()
# obj.display()





