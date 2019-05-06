import numpy as np


class DNA:
    def __init__(self, input_size, hidden_size, output_size, mutation_rate, crossover_rate):
        self.input_hidden_weights = np.random.randn(input_size, hidden_size)
        self.hidden_output_weights = np.random.randn(hidden_size, output_size)
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate

    def crossover(self, parent1, parent2):
        for i, weight in enumerate(self.input_hidden_weights):
            # print(i)
            seed = np.random.random()
            if seed < self.crossover_rate:
                seed = np.random.randn()
                if seed < 0:
                    self.input_hidden_weights[i] = parent1.input_hidden_weights[i]
                else:
                    self.input_hidden_weights[i] = parent2.input_hidden_weights[i]

            seed = np.random.random()
            if seed < self.mutation_rate:
                self.input_hidden_weights[i] = np.random.randn()

        for i, weight in enumerate(self.hidden_output_weights):
            seed = np.random.random()
            if seed < self.crossover_rate:
                seed = np.random.randn()
                if seed < 0:
                    self.hidden_output_weights[i] = parent1.hidden_output_weights[i]
                else:
                    self.hidden_output_weights[i] = parent2.hidden_output_weights[i]

            seed = np.random.random()
            if seed < self.mutation_rate:
                self.hidden_output_weights[i] = np.random.randn()


# test method
# dna = DNA(10, 20, 2, .001, .95)
# dna2 = DNA(10, 20, 2, .001, .95)
# dna3 = DNA(10, 20, 2, .001, .95)
#
# dna3.crossover(dna, dna2)
# print("dna1")
# print(dna.input_hidden_weights)
# print(dna.hidden_output_weights)
# print()
# print("dna2")
# print(dna2.input_hidden_weights)
# print(dna2.hidden_output_weights)
# print()
# print("dna3")
# print(dna3.input_hidden_weights)
# print(dna3.hidden_output_weights)
# print()
#
# print(np.allclose(dna.input_hidden_weights, dna3.input_hidden_weights))
