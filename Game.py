import numpy as np
import Cell
import Food
import math
import heapq
from sklearn.neighbors import KDTree


class Game:
    def __init__(self, width, height, cell_count, food_count, food_spawn_rate, input_size, hidden_size,
                 output_size, crossover_rate, mutation_rate):
        self.width = width
        self.height = height
        self.initial_cell_count = cell_count
        self.initial_food_count = food_count
        self.food_spawn_rate = food_spawn_rate
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.friction = .1
        self.cells = []
        self.food = []
        self.vectors = []
        self.eaten_food = []
        self.dead_cells = []
        self.new_food = []
        self.new_cells = []
        self.init_objects()
        self.kdtree = KDTree([[0,0], [0,0]])
        self.breed_cooldown = 100
        self.breed_penalty = 0.1
        self.lifespans = []
        self.counter = 0
        self.max_queue_list = []
        self.elite_count = 2

    def init_objects(self):
        i = 0
        while i < self.initial_cell_count:
            cell = Cell.Cell(np.random.random() * self.width, np.random.random() * self.height, self.width,
                             self.height, self.friction, self.input_size, self.hidden_size, self.output_size,
                             self.mutation_rate, self.crossover_rate)
            self.cells.append(cell)
            i += 1

        i = 0

        while i < self.initial_food_count:
            f = Food.Food(np.random.random() * self.width, np.random.random() * self.height)
            self.food.append(f)
            i += 1

    def update(self):
        self.recalculate_vectors()
        self.kdtree = KDTree(self.vectors)
        neighbor_distances, neighbor_indexes = self.kdtree.query(self.vectors, k=6)
        neighbor_indexes = neighbor_indexes[:, 1:]
        num_cells = len(self.cells)
        # self.food_spawn_rate = math.ceil(len(self.cells) / 30)

        for i, cell in enumerate(self.cells):
            input_list = [cell.position.x, cell.position.y, cell.velocity.x, cell.velocity.y, cell.health]

            for index in neighbor_indexes[i]:
                if index > num_cells - 1:
                    input_list.append(1.0)
                    input_list.append(self.food[index - num_cells].position.x)
                    input_list.append(self.food[index - num_cells].position.y)
                else:
                    input_list.append(0.0)
                    input_list.append(self.cells[index].position.x)
                    input_list.append(self.cells[index].position.y)

            cell.update(input_list)
            nearest_index = neighbor_indexes[i][1]
            if nearest_index < len(self.cells):
                nearest = self.cells[nearest_index]

            else:
                nearest = self.food[nearest_index - num_cells]
            collide = cell.collision(nearest)

            if collide:
                if isinstance(nearest, Food.Food):
                    cell.health += 0.1
                    cell.score += 1
                    self.eaten_food.append([nearest, nearest_index - num_cells])
                elif cell.breed_cooldown < 0 and nearest.breed_cooldown < 0:
                    self.breed_cells(cell, nearest)
                    cell.score += 2
                    nearest.score += 2

            if cell.health < 0:
                self.dead_cells.append([cell, i])

        for i in range(self.food_spawn_rate):
            food = Food.Food(np.random.random() * self.width, np.random.random() * self.height)
            self.new_food.append(food)

        self.remove_dead_objects()
        self.add_new_objects()
        self.counter += 1

    def get_terminate(self):
        if len(self.cells) < 1:
            return True
        else:
            return False

    def breed_cells(self, x, y):
        child = Cell.Cell(np.random.random() * self.width, np.random.random() * self.height, self.width,
                          self.height, self.friction, self.input_size, self.hidden_size, self.output_size,
                          self.mutation_rate, self.crossover_rate)
        child.brain.dna.crossover(x.brain.dna, y.brain.dna)
        self.new_cells.append(child)
        x.breed_cooldown = self.breed_cooldown
        y.breed_cooldown = self.breed_cooldown

    def remove_dead_objects(self):
        cells_hold = self.cells[:]
        food_hold = self.food[:]
        food_to_del = []
        cells_to_del = []
        for i, cell_tuple in enumerate(self.dead_cells[:]):
            cells_to_del.append(cell_tuple[1])
            self.lifespans.append(self.counter)
            if isinstance(cell_tuple[0], Cell.Cell):
                self.max_queue_list.append(cell_tuple[0])

        for i in sorted(cells_to_del, reverse=True):
            del cells_hold[i]

        self.dead_cells = []
        self.cells = cells_hold

        for i, food in enumerate(self.eaten_food[:]):
            food_to_del.append(food[1])
        for i in sorted(set(food_to_del), reverse=True):
            del food_hold[i]

        self.eaten_food = []
        self.food = food_hold

    def add_new_objects(self):
        for cell in self.new_cells[:]:
            self.cells.append(cell)
            self.new_cells.remove(cell)

        for food in self.new_food[:]:
            self.food.append(food)
            self.new_food.remove(food)

    def recalculate_vectors(self):
        self.vectors = []
        for cell in self.cells:
            self.vectors.append([cell.position.x, cell.position.y])

        for food in self.food:
            self.vectors.append([food.position.x, food.position.y])

    def reinitialize(self):
        for cell in self.cells:
            self.max_queue_list.append(cell)

        print(self.max_queue_list)
        self.max_queue_list.sort(key=lambda x: x.score, reverse=True)

        elite = self.max_queue_list[:5]
        self.cells = elite
        self.food = []

        i = len(self.cells)
        while i < self.initial_cell_count:
            cell = Cell.Cell(np.random.random() * self.width, np.random.random() * self.height, self.width,
                             self.height, self.friction, self.input_size, self.hidden_size, self.output_size,
                             self.mutation_rate, self.crossover_rate)
            self.cells.append(cell)
            i += 1

        i = 0

        while i < self.initial_food_count:
            f = Food.Food(np.random.random() * self.width, np.random.random() * self.height)
            self.food.append(f)
            i += 1






