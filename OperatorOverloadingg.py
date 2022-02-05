# Python Program to perform addition
# of two complex numbers using binary
# + operator overloading.

# class complex:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     # adding two objects
#     def __add__(self, other):
#         return self.a + other.a, self.b + other.b
#
#
# Ob1 = complex(1, 2)
# Ob2 = complex(2, 3)
# Ob3 = Ob1 + Ob2
# print(Ob3)
# # Equal operator in python
#
#
# # Python program to overload equality
# # and less than operators
#
# class A:
#     def __init__(self, a):
#         self.a = a
#
#     def __lt__(self, other):
#         if (self.a < other.a):
#             return "ob1 is lessthan ob2"
#         else:
#             return "ob2 is less than ob1"
#
#     def __eq__(self, other):
#         if (self.a == other.a):
#             return "Both are equal"
#         else:
#             return "Not equal"
#
#
# ob1 = A(2)
# ob2 = A(3)
# print(ob1 < ob2)
#
# ob3 = A(4)
# ob4 = A(4)
# print(ob3 == ob4)

# divied method

class Student:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __truediv__(self,other):
        x=self.x/other.x
        y=self.y/other.y
        s3=Student(x,y)

        return s3

s1=Student(2,2)
s2=Student(4,3)
s3=s1/s2
print(s3.x)


