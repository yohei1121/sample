#チェレンジ14章

class Square:

    square_list = []

    def __init__(self, width):
        self.width = width
        self.square_list.append(self)

    def __repr__(self):
        return "{} by {} by {} by {}".format(
            self.width,
            self.width,
            self.width,
            self.width
            )

def check_same(x, y):
    return x is y
        

square1 = Square(10)
print(square1)
square2 = Square(20)
print(square2)
print(Square.square_list)

print(check_same(square1, square1))
print(check_same(square2, square2))
print(check_same(square1, square2))
