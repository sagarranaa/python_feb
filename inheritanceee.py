""" Types of Inheritance in Python Programming
1). Single inheritance.
2). Multiple inheritances.
3). Multilevel inheritance.
"""

class A: #super class/parent class

    def features1(self):
        print("This is features1:")


class B(A):#sub class/child class
    def features2(self):
        print("This is features2:")

class C(B):# multi-level class
    def features3(self):
        print("This is feature3")
a=A()
a.features1()

b1=B()
c1=C()
c1.features1()
c1.features2()
c1.features3()


