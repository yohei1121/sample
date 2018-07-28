import math

class Apple:

    def __init__(self, color, price, sugar_content, producing_area):
        self.color = color
        self.price = price
        self.sugar_content = sugar_content
        self.producing_area = producing_area
        print("Create Apple!")

class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return self.r ** 2 * math.pi

class Triangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height / 2

apple1 = Apple("red", 300, 12, "青森")

circle = Circle(3)
print(circle.area())
circle2 = Circle(6)
print(circle2.area())


triangle = Triangle(4, 40)
print(triangle.area())
