# roulette/tests/test_bet.py


import unittest
from roulette.outcome import Outcome
from roulette.roulettePayout import RoulettePayout
from roulette.bet import Bet


class BetTestCase(unittest.TestCase):
    def setUp(self):
        self.outcome_5 = Outcome("00-0-1-2-3", RoulettePayout.FiveBet)
        self.outcome_0 = Outcome("Number 0", RoulettePayout.StraightBet)
        self.bet_5 = Bet(1000, self.outcome_5)
        self.bet_0 = Bet(1000, self.outcome_0)

    def test_winAmount(self):
        self.assertEqual(self.bet_5.winAmount(), 1000 + 1000 * 6)
        self.assertEqual(self.bet_0.winAmount(), 1000 + 1000 * 35)

    def test_getAmount(self):
        self.assertEqual(self.bet_5, "1000 on 00-0-1-2-3 (6:1)")


def main(void):
    unittest.main()


if __name__ == '__main__':
    main()
