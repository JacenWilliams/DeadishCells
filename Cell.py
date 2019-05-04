import Vector2D as v
import Brain


class Cell():
    def __init__(self, x, y, w, h, f, dna):
        self.health = 1.0
        self.r = 20

        self.position = v.Vector2D(x, y)
        self.window_height = h
        self.window_width = w
        self.velocity = v.Vector2D(0, 0)
        self.acceleration = v.Vector2D(0, 0)
        self.friction = f
        self.brain = Brain.Brain(dna)

    def update(self, input_data):
        self.bounce()
        self.velocity.scale(1 - self.friction)
        self.acceleration.add(self.brain.think(input_data))
        self.velocity.add(self.acceleration)
        self.position.add(self.velocity)

    def bounce(self):
        if self.position.x > self.window_width or self.position.x < 0:
            self.velocity.x = self.velocity.x * -1

        if self.position.y > self.window_height or self.position.y < 0:
            self.velocity.y = self.velocity.y * -1

    def collision(self, other):
        if self.position.distance(other.position) < self.r + other.r:
            return True
        else:
            return False
