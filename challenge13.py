class Shape:
    def __init__(self):
        pass

    def what_am_i(self):
        return "I am shape"
    
class Square(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return self.width * 2 + self.height * 2

    def change_size(self, width):
        self.width += width


class Rectangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3

class Horse:
    def __init__(self, name, rider):
        self.name = name
        self.rider = rider

class Rider:
    def __init__(self, name):
        self.name = name



rectangle = Rectangle(20, 50, 60)
print(rectangle.what_am_i())
#print(rectangle.calculate_perimeter())

square = Square(20, 50)
print(square.what_am_i())
#print(square.calculate_perimeter())

#square.change_size(10)
#print(square.calculate_perimeter())

#square.change_size(-30)
#print(square.calculate_perimeter())

rider = Rider("イスカンダル")

horse = Horse("サンデーサイレンス", rider)
print(horse.rider.name)
