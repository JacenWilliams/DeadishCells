import numpy as np
import pygame as pg
import Cell
import Food
import DNA
from sklearn.neighbors import KDTree


class Game:
    def __init__(self, width, height, cell_count, food_count, food_spawn_interval, input_size, hidden_size,
                 output_size, crossover_rate, mutation_rate):
        self.width = width
        self.height = height
        self.initial_cell_count = cell_count
        self.initial_food_count = food_count
        self.food_spawn_interval = food_spawn_interval
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.friction = .01
        self.cells = []
        self.food = []
        self.vectors = []
        self.eaten_food = []
        self.dead_cells = []
        self.init_objects()
        self.kdtree = KDTree(self.vectors)
        pg.init()

    def init_objects(self):
        i = 0
        while i < self.initial_cell_count:
            cell = Cell.Cell(np.random.random() * self.width, np.random.random() * self.height, self.width,
                             self.height, self.friction, DNA.DNA(self.input_size, self.hidden_size, self.output_size,
                                                                 self.mutation_rate, self.crossover_rate))
            self.cells.append(cell)
            self.vectors.append([cell.position.x, cell.position.y])
            i += 1

        i = 0

        while i < self.initial_food_count:
            f = Food.Food(np.random.random() * self.width, np.random.random() * self.height)
            self.food.append(f)
            self.vectors.append([f.position.x, f.position.y])
            i += 1

    def update(self):
        num_cells = len(self.cells)
        num_food = len(self.food)
        neighbor_distances, neighbor_indexes = self.kdtree.query(self.vectors, k=5)

        for i, cell in enumerate(self.cells):
            input_list = [cell.position.x, cell.position.y, cell.velocity.x, cell.velocity.y, cell.health]

            for index in neighbor_indexes[i]:
                if index > num_cells:
                    input_list.append(1.0)
                    input_list.append(self.food[index - num_cells].position.x)
                    input_list.append(self.food[index - num_cells].position.y)
                else:
                    input_list.append(0.0)
                    input_list.append(self.cells[index].position.x)
                    input_list.append(self.cells[index].position.y)

            cell.update(input_list)
            collide = cell.collision(self.cells[neighbor_indexes[1]])

            if collide:
                # todo: food and cell collision logic
                pass

            if cell.health < 0:
                self.dead_cells.append((cell, i))
        # todo: removing dead stuff, adding new stuff, recalculating vectors/tree


    def draw(self):
        # todo: all the graphics stuff
        pass

    def get_terminate(self):
        if self.vectors < 5:
            return True
        else:
            return False

    def get_input(self, index):
        cell = self.cells[index]
        nearby = self.kdtree.query()



