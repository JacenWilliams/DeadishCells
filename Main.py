# ---------------------------------------------------------------------------
# Author: Jacen Williams
# Assignment: Final Project
# Class: Machine Learning
# Due Data: 5/7/19
# ---------------------------------------------------------------------------
import Game


# simulation variables
initial_time = 0 #seconds of runtime before graphical simulation

# physics variables
width = 900
height = 600
initial_cell_count = 200
initial_food_count = 200
food_spawn_interval = 10

# genetic algorithm variables
crossover_rate = 1
mutation_rate = .001

# neural network variables
num_inputs = 20
num_hidden_neurons = 10
num_outputs = 2

# init game
game = Game.Game(width, height, initial_cell_count, initial_food_count, food_spawn_interval)

# prerender loop
counter = 0

while counter < initial_time * 60:
    game.update()
    game.draw()
    counter = counter + 1

# render loop
terminate = False

while not terminate:
    game.update()
    game.draw()
    counter = counter + 1
    terminate = game.get_terminate()




