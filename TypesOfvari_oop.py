#Type of variable in oops
 # Namespace is an area where you create and store object/variable
 #    1.Class Namespace
 #    2.Object/Instance namespace

class Car:
    wheel=4
    color='white' # class namespace
    def __init__(self):
        self.mil=10
        self.company="BMW" #instance namespace
    def compare(self,other):
        if c1.wheel==other.wheel:
            return True
        else:
            return False
c1=Car()
c2=Car()
c2.wheel=8
if c1.compare(c2):
    print("equal")
else:
    print("Not Equal")
print(c1.wheel,c2.wheel)
