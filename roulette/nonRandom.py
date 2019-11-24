# roulette/roulette/nonRandom.py


import random


class NonRandom(random.Random):

    def __init__(self):
        self.value = None

    def set_seed(self, value):
        self.seed(value)
