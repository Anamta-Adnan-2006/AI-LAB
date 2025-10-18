import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)
    def perimeter(self):
        return 2 * math.pi * self.radius
try:
    r = float(input("Enter the radius of the circle: "))
    circle1 = Circle(r)
 print("Area of the circle:", round(circle1.area(), 2))
    print("Perimeter of the circle:", round(circle1.perimeter(), 2))
except ValueError:
    print("Please enter a valid number for radius.")
