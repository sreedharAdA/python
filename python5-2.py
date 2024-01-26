# created by sreedhar
# 25/01/2024

# single inhertance
class bank:
 def fun(self, accountnumber, ifc, bankname,balance):
     self.accountnumber = accountnumber
     self.ifc = ifc
     self.bankname = bankname
     self.balance = balance
     print("accountnumber:",accountnumber)
     print("ifc:",ifc)
     print("bankname:",bankname)
     print("balance:",balance)
     print("------------------")

class pbank(bank):
     def fun1(self,Gender,age):
         self.Gender = Gender
         self.age = age
         print("Gender:",Gender)
         print("age:",age)
obj= pbank()
obj.fun1("male","23")
obj.fun("12345678","000067","icic","2000")

# multilevel inhertance

class bank:
 def fun(self, accountnumber, ifc, bankname,balance):
     self.accountnumber = accountnumber
     self.ifc = ifc
     self.bankname = bankname
     self.balance = balance
     print("accountnumber:",accountnumber)
     print("ifc:",ifc)
     print("bankname:",bankname)
     print("balance:",balance)

class sreedharbank(bank):
     def fun1(self,Gender,age):
         self.Gender = Gender
         print("gender:",Gender)
         print("age:",age)

class devabank(sreedharbank,bank):
    def fun2(self,holdername,limit):
        self.holdername = holdername
        self.limit = limit
        print("holdername:",holdername)
        print("limit:",limit)
obj= devabank()
obj.fun2("sreedhar","500000")
obj.fun1("male","23")
obj.fun("12345678","000067","icic","2000")


# multiple inhertance

class sreedharbank:
    def fun1(self, Gender, age):
        self.Gender = Gender
        print("gender:", Gender)
        print("age:", age)


class devabank:
    def fun2(self, holdername, limit):
        self.holdername = holdername
        self.limit = limit
        print("holdername:", holdername)
        print("limit:", limit)

class arunbank(sreedharbank,devabank):
    def fun3(self,nationality,id):
        self.nationality = nationality
        self.id= id
        print("nationality:",nationality)
        print("id:",id)
        print("----------------------------------")
obj = arunbank()
obj.fun3("nationality","09876543221")
obj.fun2("sreedhar","500000")
obj.fun1("male","23")

# hybirde inhertance
class sreedharbank(bank):
     def fun1(self,Gender,age):
         self.Gender = Gender
         print("gender:",Gender)
         print("age:",age)

class devabank(sreedharbank,bank):
    def fun2(self,holdername,limit):
        self.holdername = holdername
        self.limit = limit
        print("holdername:",holdername)
        print("limit:",limit)

class sreedharbank:
    def fun1(self, Gender, age):
        self.Gender = Gender
        print("gender:", Gender)
        print("age:", age)


class devabank:
    def fun2(self, holdername, limit):
        self.holdername = holdername
        self.limit = limit
        print("holdername:", holdername)
        print("limit:", limit)

class arunbank(sreedharbank,devabank):
    def fun3(self,nationality,id):
        self.nationality = nationality
        self.id= id
        print("nationality:",nationality)
        print("id:",id)
        print("----------------------------------")
obj = arunbank()
obj.fun3("nationality","09876543221")
obj.fun2("sreedhar","500000")
obj.fun1("male","23")



