# ---------------------------------------------------------------------------
# Author: Jacen Williams
# Assignment: Final Project
# Class: Machine Learning
# Due Data: 5/7/19
# ---------------------------------------------------------------------------
import Game
import math
import pygame as pg


# simulation variables
initial_generations = 70

# physics variables
width = 1600
height = 900
initial_cell_count = 20
initial_food_count = 200
food_spawn_rate = 0
max_generation_lifespan = 1000

# genetic algorithm variables
crossover_rate = 1
mutation_rate = .001

# neural network variables
num_inputs = 20
num_hidden_neurons = 10
num_outputs = 2


# init
pg.init()
game = Game.Game(width, height, initial_cell_count, initial_food_count, food_spawn_rate, num_inputs,
                 num_hidden_neurons, num_outputs, crossover_rate, mutation_rate)


lifespans = []

# prerender loop
generation = 0
while generation < initial_generations:
    print("Generation: ", generation)
    counter = 0
    while counter < max_generation_lifespan and not game.get_terminate():
        game.update()
        # game.draw()
        counter += 1
    generation += 1
    lifespans.append([game.lifespans])
    game.reinitialize()
# render loop
print(lifespans)

screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()
terminate = False
while True:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            print(game.lifespans)
            quit()
    if not terminate:
        screen.fill((255, 255, 255))
        game.update()
        print("Cells: ", len(game.cells), " Food: ", len(game.food))
        terminate = game.get_terminate()
        for cell in game.cells:
            pg.draw.circle(screen, (0, 255, 0), [math.floor(cell.position.x), math.floor(cell.position.y)], cell.r)
        for food in game.food:
            pg.draw.circle(screen, (0, 155, 0), [math.floor(food.position.x), math.floor(food.position.y)], food.r)
        pg.display.flip()


