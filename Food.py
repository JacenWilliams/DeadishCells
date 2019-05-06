import Vector2D as v
import pygame as pg


class Food():
    def __init__(self, x, y):
        self.position = v.Vector2D(x, y)
        self.r = 5

