class A:
    def __init__(self): # contructor of A class
        print("This is constructor of A Class:")
    def feature1(self):
        print("this is features1")
class B(A):
    def __init__(self): # contructor of B class
        super().__init__() #accessing the contructors of A class
        print("This is constructor of B Class:")
    def feature2(self):
        print("This is features2")
a=A()
b=B()
b.feature2(),b.feature1()