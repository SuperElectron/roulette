# roulette/tests/test_bin.py


import unittest
from roulette.table import Table, InvalidBet
from roulette.bet import Bet
from roulette.outcome import Outcome
from roulette.roulettePayout import RoulettePayout


class TableTestCase(unittest.TestCase):
    """Test Table class methods."""

    def setUp(self):

        # create table
        self.table = Table()
        self.table.limit = 1000

        # create outcomes
        self.outcome_5 = Outcome("00-0-1-2-3", RoulettePayout.FiveBet)
        self.outcome_0 = Outcome("Number 0", RoulettePayout.StraightBet)

        # create bets
        self.bet_5 = Bet(100, self.outcome_5)
        self.bet_0 = Bet(100, self.outcome_0)
        self.bet_0_big = Bet(1100, self.outcome_0)

    def test_is_valid(self):
        """Test is_valid method."""

        # check valid bets
        self.assertTrue(self.table.is_valid(self.bet_5))
        self.assertTrue(self.table.is_valid(self.bet_0))

        # check invalid bet
        self.assertFalse(self.table.is_valid(self.bet_0_big))

    def test_place_bet(self):
        """Test place_bet method."""

        # place valid bet
        self.table.place_bet(self.bet_5)

        # check is in bets list
        self.assertIn(self.bet_5, self.table.bets)

        # attempt to place invalid bet
        self.assertRaises(InvalidBet, self.table.place_bet, self.bet_0_big)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
