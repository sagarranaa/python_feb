""" Type of methods
    1.instance methodd
    2.class method
    3.static method
1.Instacne Method:
    1.accessor method
    2.mutator method
some basic knowledge

*-1.Class variable:-A class variable is nothing but a constructor.a class variable is also called as static variable
*-2.Accessor(Getters):-if you want to fetch the value from an instance variable .we call them accessor
*-3.Mutator(setters):-if you want to modify the value.we call them mutators """

class Student:

    some_college="Viva college"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self): # methods
        return self.m1+self.m2+self.m3/3

    def Get_value(self): #Accessor method(Getters)
        return self.m1
    def Set_value(self,x): #Mutators(setters)
        self.m1=x

    @classmethod
    def info(self): # class method
        return self.some_college

    @staticmethod # if we want to extera modification .go with static method
    def info_class():
        print("This is static method")

s1=Student(2,2,2)
# setting the value of m1 using setter method
s1.Set_value(4)
# print(s1.Set_value())
print(s1.info())
print(s1.avg(),s1.some_college)
print(s1.Get_value())
Student.info_class()