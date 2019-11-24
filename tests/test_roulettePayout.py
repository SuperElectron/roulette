# roulette/tests/test_roulettePayout.py


import unittest
from roulette.roulettePayout import RoulettePayout


class RoulettePayoutTestCase(unittest.TestCase):
    """Test Table class methods."""

    def setUp(self):
        self.straightBet = 35
        self.splitBet = 17
        self.streetBet = 11
        self.dozenBet = 11
        self.cornerBet = 8
        self.fiveBet = 6
        self.lineBet = 5
        self.columnBet = 2
        self.evenBet = 1

    def test_attributes(self):
        """Test attributes from RoulettePayout Class. """

        self.assertTrue(RoulettePayout.StraightBet, self.straightBet)
        self.assertTrue(RoulettePayout.SplitBet, self.splitBet)
        self.assertTrue(RoulettePayout.StreetBet, self.streetBet)
        self.assertTrue(RoulettePayout.DozenBet, self.dozenBet)
        self.assertTrue(RoulettePayout.CornerBet, self.cornerBet)
        self.assertTrue(RoulettePayout.FiveBet, self.fiveBet)
        self.assertTrue(RoulettePayout.LineBet, self.lineBet)
        self.assertTrue(RoulettePayout.ColumnBet, self.columnBet)
        self.assertTrue(RoulettePayout.EvenBet, self.evenBet)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
