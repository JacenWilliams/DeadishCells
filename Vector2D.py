import math


class Vector2D():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y

    def subtract(self, other):
        self.x = self.x - other.x
        self.y = self.y - other.y

    def scale(self, n):
        self.x = self.x * n
        self.y = self.y * n

    def distance(self, other):
        return math.sqrt(((other.x - self.x) ** 2) + ((other.y - self.y) ** 2))

