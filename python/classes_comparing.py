class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return self.x + other.x and self.y + other.y


point = Point(20, 20)
other = Point(2, 4)
# print(point == other)
print(point + other)
