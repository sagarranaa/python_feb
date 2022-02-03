#class inside a class(inner class)`1
class Student:

    def __init__(self,name,roll):
        self.Name=name
        self.roll=roll
        self.lap=self.laptop() ## creating the object to access the inner class

    def show(self):
        print(self.Name,self.roll)
        self.lap.show()

    class laptop:

        def __init__(self):
            self.brand="Hp"
            self.cpu='i7'
            self.ram=12

        def show(self):
            print(self.brand,self.cpu,self.ram) #to show the inside class show function we need to define it outside of the class
s1=Student('Rana',10)
# print(s1.Name,s1.roll)
s1.show()
s1.show()