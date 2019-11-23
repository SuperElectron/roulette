# roulette/tests/test_bin.py

import unittest
from roulette.outcome import Outcome
from roulette.bin import Bin
from roulette.roulettePayout import RoulettePayout


class TestBin(unittest.TestCase):

    def setUp(self):
        self.outcome_5 = Outcome("00-0-1-2-3", RoulettePayout.FiveBet)
        self.outcome_0 = Outcome("Number 0", RoulettePayout.StraightBet)
        self.outcome_00 = Outcome("Number 00", RoulettePayout.StraightBet)

        self.bin_0 = Bin(self.outcome_0, self.outcome_5)
        self.bin_00 = Bin(self.outcome_00, self.outcome_5)

        self.bin_add = Bin()

    def test_setup(self):
        """ verifying setUp variables for test_bin.py """
        pass

    def test_contain_outcome(self):
        self.assertIn(Outcome("Number 0", RoulettePayout.StraightBet),
                      self.bin_0)

    def test_not_contain_outcome(self):
        self.assertNotIn(Outcome("Number 00", RoulettePayout.StraightBet),
                         self.bin_0)

    def test_contain_all_outcomes(self):
        self.assertIn(Outcome("Number 0", RoulettePayout.StraightBet),
                      self.bin_0)
        self.assertIn(Outcome("00-0-1-2-3", 6), self.bin_0)

    def test_add(self):
        self.bin_add.add(self.outcome_0)
        self.bin_add.add(self.outcome_5)
        self.assertIn(self.outcome_0, self.bin_add)
        self.assertIn(self.outcome_5, self.bin_add)

    def test__str__(self):
        self.assertEqual(str(self.bin_0),
                         "00-0-1-2-3 (6:1), Number 0 (35:1)")


def main():
    unittest.main()


if __name__ == '__main__':
    main()
