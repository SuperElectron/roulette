# roulette/tests/test_outcome.py

import unittest
from roulette.outcome import Outcome


class TestOutcome(unittest.TestCase):

    def setUp(self):
        self.outcome1 = Outcome(name="red", odds=17)
        self.outcome2 = Outcome("red", 17)
        self.outcome3 = Outcome("first-12", 2)
        self.outcome4 = Outcome("split-bet", 19)

    def test_setup(self):
        """ verifying setUp variables for test_outcome.py """
        self.assertEqual(self.outcome1, self.outcome2)
        self.assertNotEqual(self.outcome1, self.outcome3)
        self.assertEqual(self.outcome1.getName(), self.outcome2.getName())

    def test___eq__(self):
        self.assertTrue(self.outcome1.__eq__(self.outcome2))
        self.assertFalse(self.outcome1.__eq__(self.outcome3))

    def test___ne__(self):
        self.assertTrue(self.outcome1.__ne__(self.outcome3))
        self.assertFalse(self.outcome1.__ne__(self.outcome1))

    def test___str__(self):
        self.assertEqual(str(self.outcome1), "red (17:1)")
        self.assertEqual(self.outcome1.__str__(), "red (17:1)")

    def test___repr__(self):
        self.assertEqual(self.outcome1.__repr__(), "red (17:1)")

    def test_winAmount(self):
        self.assertEqual(self.outcome1.winAmount(10), 170)

    def test_hash(self):
        self.assertEqual(hash(self.outcome1), hash(self.outcome2))
        self.assertNotEqual(hash(self.outcome1), hash(self.outcome3))


def main():
    unittest.main()


if __name__ == '__main__':
    main()
