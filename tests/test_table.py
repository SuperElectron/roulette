# roulette/tests/test_bin.py


import unittest
from roulette.table import Table, InvalidBet
from roulette.bet import Bet
from roulette.outcome import Outcome
from roulette.roulettePayout import RoulettePayout


class TableTestCase(unittest.TestCase):

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

    def test_isValid(self):

        # check valid bets
        self.assertTrue(self.table.isValid(self.bet_5))
        self.assertTrue(self.table.isValid(self.bet_0))

        # check invalid bet
        self.assertFalse(self.table.isValid(self.bet_0_big))

    def test_placeBet(self):

        # place valid bet
        self.table.placeBet(self.bet_5)

        # check is in bets list
        self.assertIn(self.bet_5, self.table.bets)

        # attempt to place invalid bet
        self.assertRaises(InvalidBet, self.table.placeBet, self.bet_0_big)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
