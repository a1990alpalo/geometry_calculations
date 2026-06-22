class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


if __name__ == "__main__":
    rectangle = Rectangle(10, 5)

    print("Rectangle length:", rectangle.length)
    print("Rectangle width:", rectangle.width)
    print("Rectangle area:", rectangle.area())
    print("Rectangle perimeter:", rectangle.perimeter())