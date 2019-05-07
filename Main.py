# ---------------------------------------------------------------------------
# Author: Jacen Williams
# Assignment: Final Project
# Class: Machine Learning
# Due Data: 5/7/19
# ---------------------------------------------------------------------------
import Game
import math
import pygame as pg
import numpy as np
import matplotlib.pyplot as plt


# simulation variables
initial_generations = 50

# physics variables
width = 1600
height = 900
initial_cell_count = 200
initial_food_count = 200
food_spawn_rate = 1
max_generation_lifespan = 1000
mean_lifespans = []
lifespans = []
scores = []
mean_scores = []
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
    lifespans.append([game.get_lifespans()])
    mean_lifespans.append(np.mean(game.get_lifespans()))
    scores.append([game.get_scores()])
    mean_scores.append([np.mean(game.get_scores())])
    game.reinitialize()
# render loop
print(lifespans)
print(mean_scores)

lifespan_plt_x = []
lifespan_plt_y = []
score_plt_x = []
score_plt_y = []

for i, mean in enumerate(mean_scores):
    score_plt_x.append(i)
    score_plt_y.append(mean)

plt.plot(score_plt_x, score_plt_y)
# plt.show()


screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()
terminate = False
image_num = 0
while True:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            # print(game.lifespans)
            quit()
    if not terminate:
        screen.fill((255, 255, 255))
        game.update()
        # print("Cells: ", len(game.cells), " Food: ", len(game.food))
        terminate = game.get_terminate()
        for cell in game.cells:
            pg.draw.circle(screen, (0, 255, 0), [math.floor(cell.position.x), math.floor(cell.position.y)], cell.r)
        for food in game.food:
            pg.draw.circle(screen, (0, 155, 0), [math.floor(food.position.x), math.floor(food.position.y)], food.r)
        pg.display.flip()

        str_num = "000" + str(image_num)
        file_name = "image" + str_num[-4:] + ".png"
        pg.image.save(screen, file_name)
        image_num += 1


