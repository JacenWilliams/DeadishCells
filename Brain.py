import Vector2D as v
import DNA


class Brain:
    def __init__(self, input_size, hidden_size, output_size, mutation_rate, crossover_rate):
        self.dna = DNA.DNA(input_size, hidden_size, output_size, mutation_rate, crossover_rate)

    def think(self, input_data):
        # todo: matrix math for feedforward
        pass
