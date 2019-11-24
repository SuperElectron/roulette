# roulette/tests/test_bin.py


import unittest
from roulette.player import Martingale, SevenReds
from roulette.table import Table
from roulette.bet import Bet
from roulette.wheel import Wheel
from roulette.game import Game
from roulette.nonRandom import NonRandom


class PlayerBaseTestCase(unittest.TestCase):

    # AUXILIAR METHODS
    def _get_outcome(self, outcome_name):
        """Query a constructed wheel for getting outcome."""

        # create Whell
        wheel = Wheel()

        return wheel.get_outcome(outcome_name)


class MartingaleTestCase(PlayerBaseTestCase):
    """Test Martingale Player subclass."""

    def setUp(self):

        # create player
        self.table = Table()
        self.player = Martingale(self.table)
        self.player.set_stake(1000)

        # create bets to test them
        self.bet1 = Bet(1, self._get_outcome("Black"))
        self.bet2 = Bet(2, self._get_outcome("Black"))
        self.bet3 = Bet(4, self._get_outcome("Black"))

        # create NonRandom instance with seed
        nr = NonRandom()
        nr.set_seed(1)

        # create game
        self.wheel = Wheel(nr)
        self.game = Game(self.wheel, self.table)

    # PUBLIC
    def test_place_bets(self):
        """Test Martingale place bets method."""

        # first round
        self.player.place_bets()
        self.assertIn(self.bet1, self.player.get_table())
        self.player.lose(self.bet1)
        self.assertTrue(self.player.get_table().is_empty())

        # second round
        self.player.place_bets()
        self.assertIn(self.bet2, self.player.get_table())
        self.player.lose(self.bet2)
        self.assertTrue(self.player.get_table().is_empty())

        # third round
        self.player.place_bets()
        self.assertIn(self.bet3, self.player.get_table())
        self.assertNotIn(self.bet1, self.player.get_table())
        self.assertNotIn(self.bet2, self.player.get_table())
        self.player.win(self.bet3)
        self.assertTrue(self.player.get_table().is_empty())

        # fourth round
        self.player.place_bets()
        self.assertIn(self.bet1, self.player.get_table())
        self.player.lose(self.bet1)
        self.assertTrue(self.player.get_table().is_empty())

    def test_stake(self):
        """Play some cycles of Martingale game checking stake evolution."""

        # first round: red - bet 1
        self.game.cycle(self.player)
        self.assertEqual(self.player.get_stake(), 1001)

        # first round: red - bet 2
        self.game.cycle(self.player)
        self.assertEqual(self.player.get_stake(), 1000)

        # first round: black - bet 4
        self.game.cycle(self.player)
        self.assertEqual(self.player.get_stake(), 1002)

        # first round: red - bet 1
        self.game.cycle(self.player)
        self.assertEqual(self.player.get_stake(), 1001)

        # first round: red - bet 2
        self.game.cycle(self.player)
        self.assertEqual(self.player.get_stake(), 999)

        # first round: black - bet 4
        self.game.cycle(self.player)
        self.assertEqual(self.player.get_stake(), 1003)


class SevenRedsTestCase(PlayerBaseTestCase):
    """Test SevenReds Player subclass."""

    def setUp(self):

        # create player
        self.table = Table()
        self.player = SevenReds(self.table)
        self.player.set_stake(1000)

        # create bets to test them
        self.bet1 = Bet(1, self._get_outcome("Black"))
        self.bet2 = Bet(2, self._get_outcome("Black"))
        self.bet3 = Bet(4, self._get_outcome("Black"))

        # create NonRandom instance with seed
        nr = NonRandom()
        nr.set_seed(1)

        # create game
        self.wheel = Wheel(nr)
        self.game = Game(self.wheel, self.table)

    def test_red_count(self):
        """Play some cycles of Martingale game checking stake evolution."""

        # first round: red - no bet (6 red to go)
        self.game.cycle(self.player)
        self.assertEqual(self.player.get_stake(), 1000)
        self.assertEqual(self.player.red_count, 7)

        # first round: red - no bet (5 red to go)
        self.game.cycle(self.player)
        self.assertEqual(self.player.get_stake(), 1000)
        self.assertEqual(self.player.red_count, 6)

        # first round: black - no bet (7 red to go)
        self.game.cycle(self.player)
        self.assertEqual(self.player.get_stake(), 1000)
        self.assertEqual(self.player.red_count, 7)

    # AUXILIAR METHODS
    def _get_outcome(self, outcome_name):
        """Query a constructed wheel for getting outcome."""

        # create Whell
        wheel = Wheel()

        return wheel.get_outcome(outcome_name)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
