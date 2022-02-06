from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def noofsites(self):
        pass
class Triangle(Polygon):
    def noofsites(self):
    #overriding abstract method
        print("Have 3 sides")
class Pentagon(Polygon):
    def noofsites(self):
        print("Have 5 sides")
class Hexagon(Polygon):
    def noofsites(self):
        print("Have 6 Sides ")
class Quadilateral(Polygon):
    def noofsites(self):
        print("Have 4 sides")
#Drive code
R=Triangle()
R.noofsites()

k=Quadilateral()
k.noofsites()

R=Pentagon()
R.noofsites()

k=Hexagon()
k.noofsites()
