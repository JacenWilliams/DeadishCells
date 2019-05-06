import Vector2D as v
import DNA
import math
import numpy as np


class Brain:
    def __init__(self, input_size, hidden_size, output_size, mutation_rate, crossover_rate):
        self.dna = DNA.DNA(input_size, hidden_size, output_size, mutation_rate, crossover_rate)

    def think(self, input_data):
        hidden_values = input_data.dot(self.dna.input_hidden_weights)
        hidden_activated = self.activation(hidden_values)
        output_values = hidden_activated.dot(self.dna.hidden_output_weights)
        output_vector = v.Vector2D(math.tanh(output_values[0]), math.tanh(output_values[1]))
        return output_vector

    def activation(self, input_data):
        # hyperbolic tangent function
        for i in range(len(input_data)):
            input_data[i] = math.tanh(input_data[i])

        return input_data

# test method
# brain = Brain(10, 20, 2, .001, .95)
# for i in range(50):
#     vec = brain.think(np.random.randn(1,10))
#     print(vec.x, vec.y)
