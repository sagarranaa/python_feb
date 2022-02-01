# class Computer:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def type(self):
#         print(self.name,self.age)
# c1=Computer('sagar',21)
# # c2=Computer()
# print(c1.type())
# # print(c2.age=22)

##Practise more

class A:
    def __init__(self): #constructor or initilizers
        self.x=2
        self.y=1
    def compare(self,other):
        if self.x==other.x:
            return True
        else:
            return False
com1=A()
com1.x=5
com2=A()
if com1.compare(com2):
    print("they are equal")
else:
    print("Not equal")
print(com1.x)
print(com2.x)