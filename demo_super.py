# demo super() in python

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
    def described(self):
        print(f'It is color {self.color} and {self.is_filled}')

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
    def described(self):
        super().described()
        print(f'Circle area is {3.14 * self.radius * self.radius:.2f} cm^2')

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width
    def described(self):
        super().described()
        print(f'Square area is {self.width * self.width:.2f} cm^2')

class Triagle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height
    def described(self):
        super().described()
        print(f'Triagle area is {(self.width * self.height)/2} cm^2')

if __name__ == '__main__':

    circle = Circle('red', True, 10)
    square = Square('blue', False, 15)
    triagle = Triagle('green', True, 4, 5)

    print(f'Circle color {circle.color}, is filled {circle.is_filled} & radius about {circle.radius} cm')
    circle.described()
    print()
    print(f'Square color {square.color}, is filled {square.is_filled} & width about {square.width} cm')
    square.described()
    print()
    print(f'Triagle color {triagle.color}, is filled {triagle.is_filled}, radius about {triagle.width} cm & height {triagle.height} cm')
    triagle.described()
    print()
# EOF    
