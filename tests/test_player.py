# roulette/tests/test_bin.py


import unittest
from roulette.player import Martingale, SevenReds
from roulette.table import Table
from roulette.bet import Bet
from roulette.wheel import Wheel
from roulette.game import Game
from roulette.nonRandom import NonRandom


class PlayerBaseTestCase(unittest.TestCase):

    def _getOutcome(self, outcome_name):
        """Query a constructed wheel for getting outcome."""

        # create Whell
        wheel = Wheel()

        return wheel.getOutcome(outcome_name)


class MartingaleTestCase(PlayerBaseTestCase):

    def setUp(self):

        # create player
        self.table = Table()
        self.player = Martingale(self.table)
        self.player.setStake(1000)

        # create bets to test them
        self.bet1 = Bet(1, self._getOutcome("Black"))
        self.bet2 = Bet(2, self._getOutcome("Black"))
        self.bet3 = Bet(4, self._getOutcome("Black"))

        # create NonRandom instance with seed
        non_random = NonRandom()
        non_random.setSeed(1)

        # create game
        self.wheel = Wheel(non_random)
        self.game = Game(self.wheel, self.table)

    def test_placeBets(self):

        # first round
        self.player.placeBets()
        self.assertIn(self.bet1, self.player.getTable())
        self.player.lose(self.bet1)
        self.assertTrue(self.player.getTable().isEmpty())

        # second round
        self.player.placeBets()
        self.assertIn(self.bet2, self.player.getTable())
        self.player.lose(self.bet2)
        self.assertTrue(self.player.getTable().isEmpty())

        # third round
        self.player.placeBets()
        self.assertIn(self.bet3, self.player.getTable())
        self.assertNotIn(self.bet1, self.player.getTable())
        self.assertNotIn(self.bet2, self.player.getTable())
        self.player.win(self.bet3)
        self.assertTrue(self.player.getTable().isEmpty())

        # fourth round
        self.player.placeBets()
        self.assertIn(self.bet1, self.player.getTable())
        self.player.lose(self.bet1)
        self.assertTrue(self.player.getTable().isEmpty())

    def test_stake(self):

        # first round: red - bet 1
        self.game.cycle(self.player)
        self.assertEqual(self.player.getStake(), 1001)

        # first round: red - bet 2
        self.game.cycle(self.player)
        self.assertEqual(self.player.getStake(), 1000)

        # first round: black - bet 4
        self.game.cycle(self.player)
        self.assertEqual(self.player.getStake(), 1002)

        # first round: red - bet 1
        self.game.cycle(self.player)
        self.assertEqual(self.player.getStake(), 1001)

        # first round: red - bet 2
        self.game.cycle(self.player)
        self.assertEqual(self.player.getStake(), 999)

        # first round: black - bet 4
        self.game.cycle(self.player)
        self.assertEqual(self.player.getStake(), 1003)


class SevenRedsTestCase(PlayerBaseTestCase):

    def setUp(self):

        # create player
        self.table = Table()
        self.player = SevenReds(self.table)
        self.player.setStake(1000)

        # create bets to test them
        self.bet1 = Bet(1, self._getOutcome("Black"))
        self.bet2 = Bet(2, self._getOutcome("Black"))
        self.bet3 = Bet(4, self._getOutcome("Black"))

        # create NonRandom instance with seed
        non_random = NonRandom()
        non_random.setSeed(1)

        # create game
        self.wheel = Wheel(non_random)
        self.game = Game(self.wheel, self.table)

    def test_red_count(self):

        # first round: red - no bet (6 red to go)
        self.game.cycle(self.player)
        self.assertEqual(self.player.getStake(), 1000)
        self.assertEqual(self.player.red_count, 7)

        # first round: red - no bet (5 red to go)
        self.game.cycle(self.player)
        self.assertEqual(self.player.getStake(), 1000)
        self.assertEqual(self.player.red_count, 6)

        # first round: black - no bet (7 red to go)
        self.game.cycle(self.player)
        self.assertEqual(self.player.getStake(), 1000)
        self.assertEqual(self.player.red_count, 7)

    def _getOutcome(self, outcome_name):

        # create Whell
        wheel = Wheel()

        return wheel.getOutcome(outcome_name)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
