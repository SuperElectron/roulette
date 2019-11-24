# roulette/tests/test_game.py


import unittest
from roulette.wheel import Wheel
from roulette.table import Table
from roulette.player import Passenger57
from roulette.game import Game
from roulette.nonRandom import NonRandom


class GameTestCase(unittest.TestCase):
    """
    Test Game class for running a complete game cycle.

    Uses a nonRandom() number generator and a stub Player to predict wheel
    results and stake evolution based on a fixed sequence of winning bins.
    """

    def setUp(self):

        # create NonRandom instance with seed
        non_random = NonRandom()
        non_random.setSeed(1)

        # create game
        self.wheel = Wheel(non_random)
        self.table = Table()
        self.game = Game(self.wheel, self.table)

        # create player
        self.player = Passenger57(self.table)
        self.player.setStake(1000)

    def test_cycle(self):

        self.game.cycle(self.player)
        self.assertEqual(self.player.getStake(), 1100)

        self.game.cycle(self.player)
        self.assertEqual(self.player.getStake(), 1000)

        self.game.cycle(self.player)
        self.assertEqual(self.player.getStake(), 1100)

        self.game.cycle(self.player)
        self.assertEqual(self.player.getStake(), 1000)

        self.game.cycle(self.player)
        self.assertEqual(self.player.getStake(), 900)

        self.game.cycle(self.player)
        self.assertEqual(self.player.getStake(), 1000)

    def test_cycle_depleted_stake(self):

        # reduce stake so player loses all and cannot bet again
        self.player.setStake(300)

        self.game.cycle(self.player)
        self.assertEqual(self.player.getStake(), 400)

        self.game.cycle(self.player)
        self.assertEqual(self.player.getStake(), 300)

        self.game.cycle(self.player)
        self.assertEqual(self.player.getStake(), 400)

        self.game.cycle(self.player)
        self.assertEqual(self.player.getStake(), 300)

        self.game.cycle(self.player)
        self.assertEqual(self.player.getStake(), 200)

        self.game.cycle(self.player)
        self.assertEqual(self.player.getStake(), 300)

        self.assertTrue(self.game.cycle(self.player))
        self.assertTrue(self.player.playing())


def main(void):
    unittest.main()


if __name__ == '__main__':
    main()
