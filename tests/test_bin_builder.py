# roulette/tests/test_bin_builder.py


import unittest
from roulette.outcome import Outcome
from roulette.wheel import Wheel
from roulette.bin_builder import BinBuilder
from roulette.roulettePayout import RoulettePayout


class BaseTestCaseBinBuilder(unittest.TestCase):

    def setUp(self):
        self.wheel = Wheel()
        self.bin_builder = BinBuilder()


class GenStraightTestCase(BaseTestCaseBinBuilder):

    def runTest(self):
        # call method to be tested
        self.bin_builder._gen_straight(self.wheel)

        # create some outcomes that should be there
        self.outcome1 = Outcome("Number 0", RoulettePayout.StraightBet)
        self.outcome2 = Outcome("Number 16", RoulettePayout.StraightBet)
        self.outcome3 = Outcome("Number 00", RoulettePayout.StraightBet)

        # check outcomes were created ok
        self.assertIn(self.outcome1, self.wheel.get(0))
        self.assertIn(self.outcome2, self.wheel.get(16))
        self.assertIn(self.outcome3, self.wheel.get(37))


class GenSplitTestCase(BaseTestCaseBinBuilder):

    def runTest(self):
        # call method to be tested
        self.bin_builder._gen_split(self.wheel)

        # create some outcomes that should be there
        self.outcome1 = Outcome("Split 1-2", RoulettePayout.SplitBet)
        self.outcome2 = Outcome("Split 5-8", RoulettePayout.SplitBet)
        self.outcome3 = Outcome("Split 35-36", RoulettePayout.SplitBet)

        # check outcomes were created ok
        self.assertIn(self.outcome1, self.wheel.get(1))
        self.assertIn(self.outcome1, self.wheel.get(2))

        self.assertIn(self.outcome2, self.wheel.get(5))
        self.assertIn(self.outcome2, self.wheel.get(8))

        self.assertIn(self.outcome3, self.wheel.get(35))
        self.assertIn(self.outcome3, self.wheel.get(36))


class GenStreetTestCase(BaseTestCaseBinBuilder):

    def runTest(self):
        # call method to be tested
        self.bin_builder._gen_street(self.wheel)

        # create some outcomes that should be there
        self.outcome1 = Outcome("Street 16-17-18", RoulettePayout.StreetBet)
        self.outcome2 = Outcome("Street 1-2-3", RoulettePayout.StreetBet)
        self.outcome3 = Outcome("Street 34-35-36", RoulettePayout.StreetBet)

        # check outcomes were created ok
        self.assertIn(self.outcome1, self.wheel.get(16))
        self.assertIn(self.outcome1, self.wheel.get(17))
        self.assertIn(self.outcome1, self.wheel.get(18))

        self.assertIn(self.outcome2, self.wheel.get(1))
        self.assertIn(self.outcome2, self.wheel.get(2))
        self.assertIn(self.outcome2, self.wheel.get(3))

        self.assertIn(self.outcome3, self.wheel.get(34))
        self.assertIn(self.outcome3, self.wheel.get(35))
        self.assertIn(self.outcome3, self.wheel.get(36))


class GenCornerTestCase(BaseTestCaseBinBuilder):

    def runTest(self):
        # call method to be tested
        self.bin_builder._gen_corner(self.wheel)

        # create some outcomes that should be there
        self.outcome1 = Outcome("Corner 1-2-4-5", RoulettePayout.CornerBet)
        self.outcome2 = Outcome("Corner 2-3-5-6", RoulettePayout.CornerBet)
        self.outcome3 = Outcome("Corner 32-33-35-36", RoulettePayout.CornerBet)

        # check outcomes were created ok
        self.assertIn(self.outcome1, self.wheel.get(1))
        self.assertIn(self.outcome1, self.wheel.get(2))
        self.assertIn(self.outcome1, self.wheel.get(4))
        self.assertIn(self.outcome1, self.wheel.get(5))

        self.assertIn(self.outcome2, self.wheel.get(2))
        self.assertIn(self.outcome2, self.wheel.get(3))
        self.assertIn(self.outcome2, self.wheel.get(5))
        self.assertIn(self.outcome2, self.wheel.get(6))

        self.assertIn(self.outcome3, self.wheel.get(32))
        self.assertIn(self.outcome3, self.wheel.get(33))
        self.assertIn(self.outcome3, self.wheel.get(35))
        self.assertIn(self.outcome3, self.wheel.get(36))


class GenLineTestCase(BaseTestCaseBinBuilder):

    def runTest(self):
        # call method to be tested
        self.bin_builder._gen_line(self.wheel)

        # create some outcomes that should be there
        self.outcome1 = Outcome("Line 1-2-3-4-5-6", RoulettePayout.LineBet)
        self.outcome2 = Outcome(
            "Line 31-32-33-34-35-36", RoulettePayout.LineBet)
        self.outcome3 = Outcome(
            "Line 10-11-12-13-14-15", RoulettePayout.LineBet)

        # check outcomes were created ok
        self.assertIn(self.outcome1, self.wheel.get(1))
        self.assertIn(self.outcome1, self.wheel.get(2))
        self.assertIn(self.outcome1, self.wheel.get(3))
        self.assertIn(self.outcome1, self.wheel.get(4))
        self.assertIn(self.outcome1, self.wheel.get(5))
        self.assertIn(self.outcome1, self.wheel.get(6))

        self.assertIn(self.outcome2, self.wheel.get(31))
        self.assertIn(self.outcome2, self.wheel.get(34))
        self.assertIn(self.outcome2, self.wheel.get(36))

        self.assertIn(self.outcome3, self.wheel.get(11))
        self.assertIn(self.outcome3, self.wheel.get(13))
        self.assertIn(self.outcome3, self.wheel.get(14))


class GenDozenTestCase(BaseTestCaseBinBuilder):

    def runTest(self):
        # call method to be tested
        self.bin_builder._gen_dozen(self.wheel)

        # create some outcomes that should be there
        self.outcome1 = Outcome("Dozen 1", RoulettePayout.DozenBet)
        self.outcome2 = Outcome("Dozen 2", RoulettePayout.DozenBet)
        self.outcome3 = Outcome("Dozen 3", RoulettePayout.DozenBet)

        # check outcomes were created ok
        self.assertIn(self.outcome1, self.wheel.get(1))
        self.assertIn(self.outcome1, self.wheel.get(7))
        self.assertIn(self.outcome1, self.wheel.get(12))

        self.assertIn(self.outcome2, self.wheel.get(15))
        self.assertIn(self.outcome2, self.wheel.get(16))
        self.assertIn(self.outcome2, self.wheel.get(18))

        self.assertIn(self.outcome3, self.wheel.get(25))
        self.assertIn(self.outcome3, self.wheel.get(30))
        self.assertIn(self.outcome3, self.wheel.get(36))


class GenColumnTestCase(BaseTestCaseBinBuilder):

    def runTest(self):
        # call method to be tested
        self.bin_builder._gen_column(self.wheel)

        # create some outcomes that should be there
        self.outcome1 = Outcome("Column 1", RoulettePayout.ColumnBet)
        self.outcome2 = Outcome("Column 2", RoulettePayout.ColumnBet)
        self.outcome3 = Outcome("Column 3", RoulettePayout.ColumnBet)

        # check outcomes were created ok
        self.assertIn(self.outcome1, self.wheel.get(1))
        self.assertIn(self.outcome1, self.wheel.get(4))
        self.assertIn(self.outcome1, self.wheel.get(7))

        self.assertIn(self.outcome2, self.wheel.get(11))
        self.assertIn(self.outcome2, self.wheel.get(14))
        self.assertIn(self.outcome2, self.wheel.get(20))

        self.assertIn(self.outcome3, self.wheel.get(24))
        self.assertIn(self.outcome3, self.wheel.get(30))
        self.assertIn(self.outcome3, self.wheel.get(36))


class GenEvenTestCase(BaseTestCaseBinBuilder):

    def runTest(self):
        # call method to be tested
        self.bin_builder._gen_even(self.wheel)

        # create some outcomes that should be there
        self.outcome1 = Outcome("Red", RoulettePayout.EvenBet)
        self.outcome2 = Outcome("Odd", RoulettePayout.EvenBet)
        self.outcome3 = Outcome("High", RoulettePayout.EvenBet)

        # check outcomes were created ok
        self.assertIn(self.outcome1, self.wheel.get(3))
        self.assertIn(self.outcome1, self.wheel.get(23))
        self.assertIn(self.outcome1, self.wheel.get(34))

        self.assertIn(self.outcome2, self.wheel.get(1))
        self.assertIn(self.outcome2, self.wheel.get(17))
        self.assertIn(self.outcome2, self.wheel.get(35))

        self.assertIn(self.outcome3, self.wheel.get(19))
        self.assertIn(self.outcome3, self.wheel.get(31))
        self.assertIn(self.outcome3, self.wheel.get(36))


class GenFiveTestCase(BaseTestCaseBinBuilder):

    def runTest(self):
        # call method to be tested
        self.bin_builder._gen_five(self.wheel)

        # create some outcomes that should be there
        self.outcome1 = Outcome("00-0-1-2-3", RoulettePayout.FiveBet)

        # check outcomes were created ok
        self.assertIn(self.outcome1, self.wheel.get(0))
        self.assertIn(self.outcome1, self.wheel.get(37))
        self.assertIn(self.outcome1, self.wheel.get(1))
        self.assertIn(self.outcome1, self.wheel.get(2))
        self.assertIn(self.outcome1, self.wheel.get(3))


def main(void):
    unittest.main()


if __name__ == '__main__':
    main()
