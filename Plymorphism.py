#Challenge:Create a base class Shape with a method area.
# Create two subclasses Rectangle and Circle that implement the area method.
# Demonstrate polymorphism by iterating over a list of shapes and calling their area methods.
import math
class Shape :

    def Area(self):
       pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Area(self):
        area=self.length*self.width
        return area
    def Volume(self,height):
        self.height=height
        vol=self.length*self.width*self.height
        return vol


class Circle(Shape) :
    def __init__(self,radius):
        self.radius = radius
        print("inside Circle shape")

    def Area(self):

        pii = math.pi
        area = pii*self.radius*self.radius
        return area

#when you are creating an obj,need to pass values for the init constructor variables specified
#neednt specify variables already initilaised again in method,access it through self.variable
#Any extra variables can be added in the method in the bracket
rect=Rectangle(1,2)
print(f'Rectangle area is {rect.Area()}')
circle=Circle(1)
print(f'area of circle is {circle.Area()}')

print(f'volume of rectangle is {rect.Volume(3)}')