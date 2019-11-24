# roulette/tests/test_simulator.py


import unittest
from roulette.player import Martingale
from roulette.table import Table
from roulette.wheel import Wheel
from roulette.nonRandom import NonRandom
from roulette.game import Game
from roulette.simulator import Simulator


class SimulatorTestCase(unittest.TestCase):

    def setUp(self):

        # create NonRandom instance with seed
        non_random = NonRandom()
        non_random.setSeed(1)

        # create game and player
        wheel = Wheel(non_random)
        table = Table()
        game = Game(wheel, table)
        player = Martingale(table)

        # assign default values to prevent future changes on them
        player.BASE_AMOUNT = 1
        player.BASE_BET = "Black"

        # create simulator instance
        self.simulator = Simulator(game, player)
        self.simulator.SAMPLES = 3

    def test_session(self):

        sample = self.simulator.session()
        max_value = max(sample)
        final_value = sample[-1]
        duration = len(sample)

        # check values derived from non-random generator
        self.assertEqual(max_value, 125)
        self.assertEqual(final_value, 62)
        self.assertEqual(duration, 54)

    def test_gather(self):

        # execute all sessions
        self.simulator.gather()

        # check gathered stats
        self.assertEqual(self.simulator.maximum, [125, 204, 224])
        self.assertEqual(self.simulator.final, [62, 77, 223])
        self.assertEqual(self.simulator.durations, [54, 221, 250])


def main():
    unittest.main()


if __name__ == '__main__':
    main()
