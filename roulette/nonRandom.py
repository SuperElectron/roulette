# roulette/roulette/nonRandom.py


import random


class NonRandom(random.Random):
    """ NonRandom generator for testing to set value and seed. """

    def __init__(self):
        self.value = None

    def setSeed(self, value):
        self.seed(value)
