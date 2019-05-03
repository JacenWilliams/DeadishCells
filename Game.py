import sklearn as sk
import numpy as np
from sklearn.neighbors import KDTree


class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # self.objects = self.init_objects()
        # self.coords = self.init_coords()
        # self.kdtree = KDTree(self.coords)

    def init_objects(self):
        pass

    def init_coords(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def get_terminate(self):
        pass


game = Game(1, 2)
print(game)

