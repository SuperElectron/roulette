# roulette/tests/test_wheel.py


import unittest
from roulette.outcome import Outcome
from roulette.wheel import Wheel
from roulette.nonRandom import NonRandom
from roulette.bin_builder import BinBuilder
from roulette.roulettePayout import RoulettePayout


class WheelConstructionTestCase(unittest.TestCase):

    def setUp(self):

        # create outcomes
        self.outcome_5 = Outcome("00-0-1-2-3", 6)
        self.outcome_0 = Outcome("0", 35)
        self.outcome_00 = Outcome("00", 35)

        # create wheel and bin builder
        self.wheel = Wheel()
        self.bin_builder = BinBuilder()

    def test_add_outcome(self):

        # Bin 0 outcomes
        self.wheel.add_outcome(0, self.outcome_0)
        self.wheel.add_outcome(0, self.outcome_5)

        # Bin 00 outcomes
        self.wheel.add_outcome(37, self.outcome_00)
        self.wheel.add_outcome(37, self.outcome_5)

        # assert Bin 0 outcomes
        self.assertIn(self.outcome_0, self.wheel.get(0))
        self.assertIn(self.outcome_5, self.wheel.get(0))

        # assert Bin 00 outcomes
        self.assertIn(self.outcome_00, self.wheel.get(37))
        self.assertIn(self.outcome_5, self.wheel.get(37))

    def test_bin_building(self):

        # build bins for the wheel
        self.bin_builder.buildBins(self.wheel)

        sample_bin1 = [Outcome("Street 1-2-3", RoulettePayout.StreetBet),
                       Outcome("Number 1", RoulettePayout.StraightBet),
                       Outcome("Line 1-2-3-4-5-6", RoulettePayout.LineBet),
                       Outcome("Low", RoulettePayout.EvenBet),
                       Outcome("Odd", RoulettePayout.EvenBet),
                       Outcome("Red", RoulettePayout.EvenBet),
                       Outcome("Corner 1-2-4-5", RoulettePayout.CornerBet),
                       Outcome("Dozen 1", RoulettePayout.DozenBet),
                       Outcome("Column 1", RoulettePayout.ColumnBet),
                       Outcome("Split 1-2", RoulettePayout.SplitBet),
                       Outcome("Split 1-4", RoulettePayout.SplitBet),
                       Outcome("00-0-1-2-3", RoulettePayout.FiveBet)
                       ]

        sample_bin2 = [Outcome("Number 00", RoulettePayout.StraightBet),
                       Outcome("00-0-1-2-3", RoulettePayout.FiveBet)]

        # check number of outcomes to be equal
        self.assertEqual(len(sample_bin1), len(self.wheel.get(1)))
        self.assertEqual(len(sample_bin2), len(self.wheel.get(37)))

        # check outcomes to be in the bin 1
        for outcome in sample_bin1:
            self.assertIn(outcome, self.wheel.get(1))

        # check outcomes to be in the bin 00
        for outcome in sample_bin2:
            self.assertIn(outcome, self.wheel.get(37))

    def test_outcome_mapping(self):

        # add outcomes to wheel
        self.wheel.add_outcome(0, self.outcome_0)
        self.wheel.add_outcome(37, self.outcome_00)
        self.wheel.add_outcome(3, self.outcome_5)

        # check that they are mapped
        self.assertEqual(self.wheel.getOutcome(self.outcome_0.getName()),
                         self.outcome_0)
        self.assertEqual(self.wheel.getOutcome(self.outcome_00.getName()),
                         self.outcome_00)
        self.assertEqual(self.wheel.getOutcome(self.outcome_5.getName()),
                         self.outcome_5)


class WheelAndNonRandomNumberTestCase(unittest.TestCase):
    """Test Wheel instance spinning results.

    Based on a non random number generator with a seed and a fixed sequence of
    results."""

    def setUp(self):

        # create NonRandom instance with seed
        non_random = NonRandom()
        non_random.setSeed(1)

        # create wheel with NonRandom instance
        self.wheel = Wheel(non_random)

    def test_next(self):
        # self.assertEqual(self.wheel.next(), self.wheel.get(5))
        # self.assertEqual(self.wheel.next(), self.wheel.get(32))
        # self.assertEqual(self.wheel.next(), self.wheel.get(29))
        # self.assertEqual(self.wheel.next(), self.wheel.get(9))
        # self.assertEqual(self.wheel.next(), self.wheel.get(18))
        # self.assertEqual(self.wheel.next(), self.wheel.get(17))
        pass


def main(void):
    unittest.main()


if __name__ == '__main__':
    main()
