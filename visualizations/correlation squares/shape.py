from abc import ABC,abstractclassmethod
from math import radians, sqrt, tan, pi, sqrt

class Shape(ABC):
    "Super Class"
    @abstractclassmethod
    def area(self): pass
    @abstractclassmethod
    def perimeter(self): pass
    @abstractclassmethod
    def config(self): 
        return [self.perimeter(), int(self.area())]

class Regular(Shape):
    def __init__(self, x, n) -> None:
        """
        x = length of side
        n = count of edge
        """
        self.x = x
        self.n = n

    def area(self):
        return ((self.x**2)*self.n) / (4*tan(radians(180)/self.n))

    def perimeter(self):
        return (self.x * self.n)

    def config(self):
        return [(self.perimeter()), (self.area())]

class Circle(Shape):
    def __init__(self, r) -> None:
        self.r = r
    
    def area(self):
        return pi*self.r**2
    
    def perimeter(self):
        return 2*pi*self.r

    def config(self):
        return [(self.perimeter()), (self.area())]

# class Diagonal(Shape):
#     def __init__(self, diag, n) -> None:
#         self.diag = diag
#         self.n = n
    
#     def area(self):
#         x = sqrt(((self.diag/2)**2)-((self.n/2)**2))
#         return (x*self.n**2)/2
    
#     def perimeter(self):
#         return 2*pi*self.r

#     def config(self):
#         return [(self.perimeter()), (self.area())]

