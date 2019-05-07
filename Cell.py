import Vector2D as v
import Brain
import numpy as np


class Cell:
    def __init__(self, x, y, w, h, f, input_size, hidden_size, output_size, mutation_rate, crossover_rate):
        self.health = 1.0
        self.r = 20
        self.score = 0
        self.position = v.Vector2D(x, y)
        self.window_height = h
        self.window_width = w
        self.velocity = v.Vector2D(0, 0)
        self.acceleration = v.Vector2D(0, 0)
        self.friction = f
        self.brain = Brain.Brain(input_size, hidden_size, output_size, mutation_rate, crossover_rate)
        self.breed_cooldown = 50

    def update(self, input_data):

        self.velocity.scale(1 - self.friction)
        self.acceleration = (self.brain.think(np.array(input_data)))
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)
        self.breed_cooldown -= 1
        self.health -= .01
        self.wrap()

    def bounce(self):
        if self.position.x > self.window_width or self.position.x < 0:
            self.velocity.x = self.velocity.x * -1

        if self.position.y > self.window_height or self.position.y < 0:
            self.velocity.y = self.velocity.y * -1

    def wrap(self):
        if self.position.x > self.window_width:
            self.position.x = self.position.x % self.window_width

        if self.position.x < 0:
            self.position.x = self.window_width - self.position.x

        if self.position.y > self.window_height:
            self.position.y = self.position.y % self.window_height

        if self.position.y < 0:
            self.position.y = self.window_height - self.position.y

    def collision(self, other):
        if ((other.position.x - self.position.x) ** 2) + ((self.position.y - other.position.y) ** 2) \
                <= ((self.r + other.r) ** 2):
            return True
        else:
            return False

