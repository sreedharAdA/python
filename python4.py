# created by  sreedhar
# 23/01/2024
# class & object
# class Mobile:
#  def __init__(self, brand,battery, ram, price):
#      self.brand = brand
#      self.battery = battery
#      self.ram = ram
#      self.price = price
#  def display(self):
#     print("brand:",self.brand)
#     print("battery:", self.battery)
#     print("ram:", self.ram)
#     print("price:", self.price)
# obj=Mobile("vivo","5000mh","8gb","30000")
# obj.display()
#
# # single class & multiple object
#
# class Mobile:
#  def __init__(self, brand,battery, ram, price):
#      self.brand = brand
#      self.battery = battery
#      self.ram = ram
#      self.price = price
#  def display(self):
#     print("brand:",self.brand)
#     print("battery:", self.battery)
#     print("ram:", self.ram)
#     print("price:", self.price)
#     print("-------------------------")
# obj=Mobile("vivo","5000mh","8gb","30000")
# obj.display()
#
# obj1=Mobile("apple","4000mh","8gb","90000")
# obj1.display()
#

class Mobile:
 def __init__(self, brand,battery, ram, price):
     self.brand = brand
     self.battery = battery
     self.ram = ram
     self.price = price
 def __init__(self,sreedhar,arun,deva):
     self.sreedhar = sreedhar
     self.arun = arun
     self.deva = deva
 def __init__(self,room,office,cafe,bar):
     self.room = room
     self.office = office
     self.cafe = cafe
     self.bar = bar
 def display(self):
     print("apple","5000mh","8","200")
 def display(self):
     print("sreedhar","arun","deva")
 def display(self):
     print("room","office","cafe","bar")
obj=Mobile("apple","5000mh","8","200")
obj.display()


