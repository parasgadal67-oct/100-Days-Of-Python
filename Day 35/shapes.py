# O.O.P POLYMORPHISM : Polymorphism means the same method name can behave differently depending on which object its called on.
# Using O.O.P polymorphism method creating the calculator which calculate the area of the given shapes.

from abc import ABC
class Shapes(ABC):
        pass
    
class Circle(Shapes):
    def __init__(self, radius):
          self.radius = radius
    
    def area(self):
        return 3.14 * self.radius **2    
    
class Square(Shapes):
    def __init__(self, side):
        self.side = side 
        
    def area(self):
        return self.side **2
    
class Rectangle(Shapes):
    def __init__(self, length, breadth):
              self.length = length
              self.breadth = breadth
        
    def area(self):
        return self.length * self.breadth 

class Triangle(Shapes):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area(self):
        return self.base * self.height
    
print("1 Circle")
print("2 Square")
print("3 Rectangle")
print("4 Triangle")

choice = input("Enter your choice(1-4): ")
if choice == "1":
    radius = float(input("Enter the radius: "))
    shape = Circle(radius)
elif choice == "2":
    side = float(input("Enter the side: "))
    shape = Square(side)
elif choice == "3":
    length = float(input("Enter the length: "))
    breadth = float(input("Enter the breadth: "))
    shape = Rectangle(length, breadth)
elif choice == "4":
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    shape = Triangle(base, height)    
else:
    print("Please enter the valid Shape !")
    
print(f"The area of {type(shape).__name__} is {shape.area()} cm²")